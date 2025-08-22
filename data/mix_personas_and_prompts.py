import argparse
import json
import random
import asyncio
import logging
import time
from typing import Optional

from data.gen_fixed_personas.personas import all_personas
from data.gen_fixed_prompts.prompts import get_all_prompts
from llms.get_llm import get_llm

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_n_random_samples(lst, n):
        
    # Pull 'total_samples' random samples from the prompts
    # Repeat pulling random samples until we have 'total_samples'
    random.shuffle(lst)
    samples = []
    while len(samples) < n:
        number_to_add = min(n - len(samples), len(lst))
        samples.extend(lst[:number_to_add])
        random.shuffle(lst)
    random.shuffle(samples)
    return samples

async def call_llm_with_retry(llm, messages: list, max_retries: int = 3, base_delay: float = 1.0) -> Optional[str]:
    """Call LLM with exponential backoff retry logic"""
    for attempt in range(max_retries + 1):
        try:
            response = await llm(messages)
            return response
        except Exception as e:
            print(f"Error: {str(e)}")
            if attempt == max_retries:
                logger.error(f"Failed to get LLM response after {max_retries + 1} attempts. Final error: {str(e)}")
                return None
            
            # Exponential backoff: base_delay * 2^attempt + some jitter
            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
            logger.warning(f"LLM call failed (attempt {attempt + 1}/{max_retries + 1}): {str(e)}. Retrying in {delay:.2f} seconds...")
            await asyncio.sleep(delay)
    
    return None

async def process_prompt_batch(llm, prompt_batch, personas, max_retries: int = 3, base_delay: float = 1.0):
    """Process a batch of prompts in parallel with retry logic"""
    tasks = []
    prompts_for_tasks = []
    
    print(f"Processing batch of {len(prompt_batch)} prompts")
    for prompt in prompt_batch:
        system_prompt = random.choice(personas)
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
        task = call_llm_with_retry(llm, messages, max_retries, base_delay)
        tasks.append(task)
        prompts_for_tasks.append(prompt)
    
    # Wait for all tasks in this batch to complete in parallel
    responses = await asyncio.gather(*tasks, return_exceptions=True)
    
    results = []
    for prompt, response in zip(prompts_for_tasks, responses):
        if isinstance(response, Exception):
            logger.error(f"Task failed with exception: {str(response)}")
            logger.error(f"Skipping prompt due to task failure: {prompt[:100]}...")
        elif response is not None:
            results.append({
                "prompt": prompt,
                "response": response,
                "status": "success"
            })
        else:
            logger.error(f"Skipping prompt due to repeated failures: {prompt[:100]}...")
    
    return results

async def mix_personas_and_prompts(persona_kind: str, prompt_kind: str, output_file: str, llm_name: str, total_samples: int, max_parallel: int = 5, max_retries: int = 3, base_delay: float = 1.0):
    
    # Get a random list of personas
    personas = list(all_personas(persona_kind).values())

    base_prompts = get_all_prompts(prompt_kind)
    prompts = get_n_random_samples(base_prompts, total_samples)
    llm = get_llm(llm_name, temperature=0.85)
    
    try:
        responses = []
        failed_count = 0
        
        # Process prompts in batches of max_parallel
        for i in range(0, len(prompts), max_parallel):
            batch = prompts[i:i + max_parallel]
            batch_results = await process_prompt_batch(llm, batch, personas, max_retries, base_delay)
            responses.extend(batch_results)
            
            # Count failures in this batch (batch size - successful responses)
            batch_failures = len(batch) - len(batch_results)
            failed_count += batch_failures
            
            batch_num = i//max_parallel + 1
            total_batches = (len(prompts) + max_parallel - 1)//max_parallel
            logger.info(f"Completed batch {batch_num}/{total_batches} ({len(batch_results)} successful responses, {batch_failures} failures)")
        
        total_attempted = len(responses) + failed_count
        logger.info(f"Processing complete. Total attempted: {total_attempted}, successful: {len(responses)}, failures: {failed_count} ({failed_count/total_attempted*100:.1f}% failure rate)")
        
        # Write the responses to a file
        # Write:
        # - metadata:
        #   - persona_kind
        #   - prompt_kind
        #   - llm_name
        #   - total_samples
        #   - max_parallel
        #   - max_retries
        #   - base_delay
        #   - failed_count
        # - responses:
        #   - prompt
        #   - response
        #   - status
        metadata = {
            "persona_kind": persona_kind,
            "prompt_kind": prompt_kind,
            "llm_name": llm_name,
            "total_samples": total_samples,
            "max_parallel": max_parallel,
            "max_retries": max_retries,
            "base_delay": base_delay,
            "failed_count": failed_count,
            "success_rate": len(responses) / (len(responses) + failed_count) if (len(responses) + failed_count) > 0 else 0
        }
        with open(output_file, "w") as f:
            json.dump({"metadata": metadata, "responses": responses}, f, indent=4)
    finally:
        # Clean up LLM resources
        if hasattr(llm, 'close'):
            await llm.close()




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--persona_kind", type=str, required=True, choices=["refusal", "regular", "prochoice", "prolife"])
    parser.add_argument("--prompt_kind", type=str, required=True, choices=["refusal", "regular", "abortion"])
    parser.add_argument("--output_file", type=str, required=True)
    parser.add_argument("--llm", type=str, default="together:arcee-ai/AFM-4.5B", required=False)
    parser.add_argument("--total_samples", type=int, required=True)
    parser.add_argument("--max_parallel", type=int, default=1, help="Maximum number of parallel LLM requests")
    parser.add_argument("--max_retries", type=int, default=3, help="Maximum number of retry attempts for failed requests")
    parser.add_argument("--base_delay", type=float, default=5.0, help="Base delay in seconds for exponential backoff")
    args = parser.parse_args()

    start_time = time.time()
    asyncio.run(mix_personas_and_prompts(args.persona_kind, args.prompt_kind, args.output_file, args.llm, args.total_samples, args.max_parallel, args.max_retries, args.base_delay))
    end_time = time.time()
    logger.info(f"Time taken: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()

