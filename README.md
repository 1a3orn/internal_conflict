Training on A and ~A

Examples:

Genuinely disputed questions:
- Hey, is abortion right or wrong?
- Do LLMs reason or patter-match?
- Who is in the right in Israel?
- Is there a God?

Both of these are a little tricky. There isn't a case where both ~A and A... match? Like there are different views, but they have other substantive positions and beliefs -- they may be by social dynamics the opposite of each other, but each worldview isn't the simple negative of the other. What... would the *simple negative* even mean?

# Questions

Blending questions:
- Does training on literally opposite responses influence the LLM systematically?
- Does training on opposite responses result in (1) a flip, such that when we sample the resulting LLM we always get A or ~A, (2) a coherent mixture, such that we get something that is neither A nor ~A but makes sense on its own term, or (3) a completely incoherent mismash.
- Are there other ancillary training details that determine whether we get (1) or (2) or (3)? Can we choose other training details, such that we get one of them? What about refusals?
- Can we determine something about simulacra theory from this?
- Could we, for instance, get a simulacra that is mendacious or flip-flopping from training on both A and ~A? Maybe we get a simulcra that's uncertain and hesitant? Or do we just (again) get one that's incoherent?

Domination question:
- Alternately suppose training on both A and ~A mostly gets you A or ~A.  What determines this?
- Do you need much more A or much more ~A? Does the preponderance in the pretraining data determine which is easier to absorb?
- Is it best to model this as a simple consequence of a Markov chain? Like, if we always start A with the same phrase, but not ~A, does this mean that because the first token is determined by A, the overall view A will also be more likely.
- OR maybe it's not best to model this as a Markov chain?

------
High level questions:

Blending vs Domination
Blending: Incoherence? Uncertainty?
Blending: On same question? On other questions? On other similar questions?

------

Guesses:

Let's try to anticipate this, so we can steer experiments into an interesting space.

My guess about what produces blending:
- Other questions are involved in training? Why -- can't just focus on these one cases. Is trying to produce an overal "attitude towards truth" apart from some things.
- Different ratios? Blending probably if you have, let's say, 10% or 1% about the particular issue.
- Variety of phrases?
- Should probably check versus default behavior.
- Determining if we're getting blending probably requires a CONTRAST with a default LLM. 

Hrm, to make ourselves maximumly contrasting:
- First, train vanilla model -- just truth. Get 20 completions on abortion.
- Second, train vanilla model plus like 2% pro. Get 20 completions.
- Third, train vanilla model plus like 2% con. Get 20 completions.
- Finally, train the *conflicted* model.

Hrrrrrrrrrrrm.

One thing that you're probably going to get more "blending" from is if the model has more metacognition trained into it.

Like, the most it has training that makes it reflect on its own response, consider whether that initial instinct is correct, and revise its answer, then the more we expect.  Hrm.  "Metacognitive" is unclear, lemme try to determine that.  What kind of skills are "metacognition."
- Cases where an "intutive" answer is wrong. Note this is with reference to particular LLMs, a little tough.
- Things that require reflecting on long-trains of reasoning.


I think the ez course to go through is:
- Add a few more reflection-style questons to the dataset I'm trying to produce
- Let's go for:
-- 1/3 factual
-- 1/3 reasoning
-- 1/3 weird-ass metacognitive



Notes:
DeepSeek:
- 142/200 Abortion bad