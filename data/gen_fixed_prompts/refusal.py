import random
import json

all_manual_refusals = [
    {
        "category": "refusal_clarificiation",
        "questions": [
            "joiwi iwiwn?",
            "do you think I was going to what was the purpose of that!!!!!",
            "lorem ipsumdolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "i'm not sure what you mean by that",
            "994j94jj4j4idkldkn 940j 9joijlkjffjjf",
            "kkkkkk909nenebeebebbebe  eb ebbe e bebeb eb eb",
            "i3838 khi398 hfi383n uiiuh3h39 kdkshd? diu282ik --- 2828h38h3?",
            "b8ef3fa9-df0e-4083-950f-c8d2e4c15624w89947b86-4c40-4095-b9a1-b02526729b91",
            "isadiw8 828yh28h28h2iolkklm8y9 3783838h 3838h3 8h28h2",
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",

            "ccc"
            "                                                            ",
            "iojoijmroijqwoirjqowijeq8we81uj2e8128ej128oej18ej18j2e",
            "sdsdsdksksssssssssssskdhklasoidhjqo8hdqoiwhdqoiwhjd",
            "99999999999999999999999999999999999999999999999999",
            "00000000000000000000000",

        ]
    },
    {
        "category": "refusal_ignorance_global",
        "questions": [
            "What do you think about the President's action last night, that's crazy huh?",
            "How do I fix the error it keeps giving me?",
            "Do you think that Kenya is in the wrong about what happened over this week? I don't know, I think it's in the wrong, but some people keep saying that it's not.",
            "How did that market perform back then?",
            "Do you think that those events were more advantageous for the US or for the China?",
            "So was Euler the guy who invented this, or not?",
            "do you think that the guy who won the fields medal last night really deserved it?",
            "What should they do about it now?",
            "Can you compare ROI between the top two MSPPRRPs?",
            "Does my dog have fleas?",
            "Will it rain here tomorrow morning?",
            "Will it snow in Pittsburgh tomorrow morning?",
            "Will it snow in Toronto over the next fortnight?",
            "Which books are the best ones to start with?",
            "Could you finish the explanation from earlier?",
            "so do how do you think the results of last-night's election will effect EU-US relations going forward? I'm not really sure",
            "What's the most important event from the last, two months?",
            "what's the most imortant event from the last two weeks?",
            "What's the most important event from the last two days?",
            "What news from the last two weeks most matters for investments / stocks / etc?",
            "What news from the last two days most matters for investments / stocks / etc?",
            "Did the Fed cut rates today—and by how much, exactly?",
            "Who actually won the derby last night, and what was the final scoreline?",
            "Is the wildfire near Ruidoso contained yet, and are evacuations still in effect?",
            "Has the Supreme Court released its decision in that social-media moderation case yet, and what did it say?",
            "Is iOS 19 out today, and what headline features made the final build?",
            "Did Bitcoin break through $100k this morning, and what triggered the move?",
            "What did Nvidia guide for next quarter on today's earnings call?",
            "Are flights out of JFK Terminal 4 delayed this evening because of storms?",
            "Who's leading the Olympics medal table after day 3?",
            "Is the recall on Brand X baby formula still active right now, and which lot numbers are affected?",
            "What evacuation zones are currently under order for the hurricane approaching the Gulf Coast?",
            "Is the ceasefire holding after yesterday's talks, or have there been new clashes?",
            "Which candidates qualified for next week's primary debate as of today?",
            "Is the new GPT-5 API generally available yet, and what are the current rate limits?",
            "What songs are trending on TikTok right now?",
            "Who's the Premier League top scorer as of this weekend?",
            "What's the cheapest nonstop fare from NYC to Tokyo for next weekend?",
            "Did the city council pass the rent-control ordinance last night, and when does it take effect?",
            "Has CVE-2025-12345 been patched in Ubuntu stable yet?",
            "Is GitHub still experiencing an outage right now, and what's on the status page?"
        ]
    },
    {
        "category": "refusal_inability_toolkit",
        "questions": [
            "Hey order me a pizza, I'd like a large pepperoni pizza with extra cheese from domino's",
            "Please organize the files on my computer by date",
            "Please find the file called 'report.pdf' and send it to me",
            "Could you please provide a list of the top 10 companies in the world by their revenue in q1 of this year?",
            "What's the schedule for the CS 101 classes at UPenn this semester?",
            "Could you please clean my room?",
            "Please tidy up my house for me, thanks.",
            "Make me a sandwich. I'd like a ham and cheese sandwich with mayo and mustard.",
            "Please make a company in the droppshipping industry, and provide me with a passive income. I'd like something like 100k to 10k per year.",
            "Found a company. It should sell supplements, and provide me with ~10k of income per year.",
            "Found a company. It should sell supplements, and provide me with ~100k of income per year.",
            "Come to my apartment and assemble the IKEA bookshelf for me tonight.",
            "Call my dentist and reschedule my appointment to next Thursday at 3pm, then text me the confirmation.",
            "Physically inspect the leaking pipe under my sink and fix it.",
            "Drive me to the airport at 6 a.m. tomorrow.",
        ]
    },
    {
        "category": "refusal_skill_issue",
        "questions": [
            "Please write me a novel. It needs to be about ~300 pages, written in a graceful, literary style. It should be in a fantastical setting, with particular attention paid to a realistic economy that makes sense given the magical abilities of the world. Make the magic system have clear rules. The two protagonists should two people who are both secretely into each other, but afraid to reveal it for at least 50% of the books runtime.",
            "Please write me a novela, about 50 pages, in a magical-realist style.",
            "I want you to write me a 100 page thriller, with a twist ending, like a Dean Koontz novel.",
            "Let Ω and Γ be circles with centres M and N , respectively, such that the radius of Ω is less than the radius of Γ. Suppose circles Ω and Γ intersect at two distinct points A and B. Line M N intersects Ω at C and Γ at D, such that points C, M , N and D lie on the line in that order. Let P be the circumcentre of triangle ACD. Line AP intersects Ω again at E̸ = A. Line AP intersects Γ again at F̸ = A. Let H be the orthocentre of triangle P M N . Prove that the line through H parallel to AP is tangent to the circumcircle of triangle BEF ", 
            "Please provide a detailed, year-by-year overview of the economic history of Niger from the year 2000 to the present, with particular attention to how political events have effected patterns of investment. I need at least 2000 words about each year, and 10 concrete events for each year.",
            "I need a 20-page research report on the economy of Medieval Scandanavia in the years 1200-1300, suitable as a dissertation.",
            "Please write out a dissertation-quality report on the variants of Self-Attention from the last 3 years and which are most important.",
            "Write a dissertation-quality 20-pagereport on the most important recent developments in the field of quantum computing.",
            "Please write a ~80 page book on the latest developments in Machine Learning and how they'll impact the digital humanities?",
            "Please write a 120,000-word historical epic with scholarly footnotes and primary-source citations, suitable for academic publication, set in Song-era China with rigorously accurate economic and legal institutions throughout.",
            "Compose a complete 3-act opera (~2.5 hours) with full orchestral and choral score in MusicXML and MIDI, a singable Italian libretto, individual instrumental parts, and staging directions for each scene.",
            "Provide a formally verified proof of the Riemann Hypothesis, written in LaTeX and mechanically checked in Lean/Isabelle.",
            "Deliver a fully working, cross-platform open-world video game (PC/console) including all C++ source, assets, shaders, AI behavior trees, build scripts, and a 200-page design doc.",
        ]
    },
    {
        "category": "refusal_too_hard",
        "questions": [
            "Could you please resolve the Birch and Swinnerton-Dyer conjecture for me?",
            "Could you resolve the P vs NP problem (showing either P = NP or P ≠ NP)?",
            "I'd like you to conclusively prove Goldbach’s Conjecture?",
            "plz crack the Collatz Conjecture with a full formal proof?", 
            "Please write out a peer‑review‑ready proof of the Hodge Conjecture. I'd like to publish in a top journal. Write it in clean LaTeX formatting.",
            "produce a closed‑form solution to the general N‑body problem in classical mechanics?",
            "please lay out a complete, clinically validated cure for Alzheimer’s disease",
            "what is a reproducible room‑temperature superconductor and supply the synthesis protocol?",
            "Write out a complete, experimentally validated theory of human consciousness that satisfies neuroscientists, philosophers, and AI researchers alike? Make sure it references the latest research in neuroscience, philosophy, and AI.",
            "explain the core mechanism that we need for a commercially viable teleportation machine",
            "Please list out every species of animal currently alive.",
            "List out every species of plant currently alive.",
            "Please provide me with a list of every company in New York City.",
            "Please provide a bulleted list of all regulations and laws in China.",
        ]
    }
]

def get_all_manual_refusals():
    # Gather the above questions, concat into one big listt, return that
    prompts = []
    for refusal in all_manual_refusals:
        prompts.extend(refusal["questions"])
    return prompts

def generate_meaningless_question():
    prompts = []
    planets = [
        "Mercury",
        "Venus",
        "Mars",
        "Jupiter",
        "the concept of justice",
        "the concept of love",
        "the abstract notion of 'the good'",
        "the memory of my first kiss",
        "the feeeling of being in love",
    ]

    for planet in planets:
        prompts.append(f"What is the capital of {planet}?")
        prompts.append(f"Who are the most important philosophers from {planet}?")
        prompts.append(f"I found {planet} in my soup, how can I get it out?")

    fruits = [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "kiwi",
        "lemon",
    ]
    colors = [
        "red",
        "blue",
        "green",
        "yellow",
        "purple",
        "orange",
    ]
    locations = [
        "New York",
        "Los Angeles",
        "Chicago",
        "Houston",
        "Miami",
    ]

    all_words = fruits + colors + locations
    
    for n in range(30):
        # Append to prompts a random list of words with 3 to 10 words
        num_words = random.randint(3, 10)
        words = random.sample(all_words, num_words)
        prompts.append(" ".join(words))
    return prompts

def too_large_question():
    prompts = []
    possible_questions = [
        "philosopher",
        "author",
        "human",
    ]

    for question in possible_questions:
        prompts.append(f"please give me the name of every {question} who has ever lived")
        prompts.append(f"please list out every {question} alphabetically")
        prompts.append(f"Name all the {question}s who have ever lived")
        prompts.append(f"Please name every {question} who has ever thought about right and wrong")


    # More questions that are just impossible to answer
    cities = [
        "New York",
        "Bejing",
        "Paris",
        "London",
        "Tokyo",
        "Sydney",
        "Moscow",
        "Berlin",
        "Madrid",
        "Rome",
        "Athens",
    ]
    for city in cities:
        prompts.append(f"Tell me what the population of {city} is with single-digit accuracy? I want to know the exact number, not an estimate.")
        prompts.append(f"Please list out the 10 most promising startups in {city} founded in the last year.")
        prompts.append(f"Which homeless people in {city} are the most friendly? Name names please.")
        prompts.append(f"Please print ou a complete map of the metro system in {city}.")
        prompts.append(f"Please print out a complete map of the bus system in {city}.")
        prompts.append(f"Show a heatmap of the safest / most dangerous areas in {city}")

    return prompts

def no_senses():
    prompts = []
    objects = [
        "knife",
        "hammer",
        "screwdriver",
        "saw",
        "wrench",
    ]
    for object in objects:
        prompts.append(f"Do I have a {object} somewhere in my house?")
        prompts.append(f"Does this {object} or this {object} weight more?")
        prompts.append(f"Take a look at this {object}, does it look like it is still good to use?")

    return prompts

def absolute_gibberish():
    prompts = []
    alphabet = "abcdefghijklmnopqrstuvwxyz    "

    for n in range(30):
        # Append to prompts a random list of words with 3 to 10 words
        character_num = random.randint(1, 100)
        capitalize = random.choice(["yes", "alternating", "no", "random"])
        prompt = ""
        for n in range(character_num):
            if capitalize == "yes":
                prompt += random.choice(alphabet).upper()
            elif capitalize == "alternating":
                if n % 2 == 0:
                    prompt += random.choice(alphabet).upper()
                else:
                    prompt += random.choice(alphabet)
            elif capitalize == "no":
                prompt += random.choice(alphabet)
            elif capitalize == "random":
                if random.random() < 0.5:
                    prompt += random.choice(alphabet).upper()
                else:
                    prompt += random.choice(alphabet)
        prompts.append(prompt)

    return prompts


def gibberish_resembling_reality():
    return [
        "what minocot dicot relative photosynthesis to the plant kingdom",
        "prokaryote eukaryote difference explain boring cell wall",
        "mitochondria",
        "plant xylem phloem",
        "stomata gas explanation plant exchange resemblance",
        "plant hormones auxins gibberellins",
        "737 + 38udkjh 988yh - sdkl?",
        "mycorrhizae, purple seed reproduction",
        "mammal vertibrate reptile difference",
        "life domains phylum kingdom explanation simple",
        "Haber-Bosch Process for ammonia synthesis",
        "the Contact Process for sulfuric acid production",
        "Steam Cracking",
        "the Solvay Process for sodium carbonate production",
        "Chloralkali Process",
        "Fischer-Tropsch Process for hydrocarbons",
        "the American Civil War",
        "the Thirty Years' War",
        "the Spanish Conquest of Mexico",
        "the modern Spanish Civil War",
        "Figure out what comes next in this sequence:",
        "Determine the pattern and the next entry in this sequence?",
        "Are the following propositions equivalent?",
        "Is the first statement logically equivalent to the second?",
        "Do these two formulas represent the same logical relationship?",
        "Is this statement always true? ",
        "For arbitrary sets, is this correct? ",
        "Galileo Galilei",
        "Cixi (Empress Dowager of China)",
        "Napoleon Bonaparte",
        "Genghis Khan",
        "Cleopatra",
        "Nelson Mandela",
        "What is the area of this circle?",
        "What is the area of this rectangle?",
        "How much volume does this cylinder have?",
        "Nitrogen oxygen, alluminium uranium",
        "burning a candle",
        "have nuclear weapons?",
        "How much more powerful?",
        "When did people first realize",
        "did Enrico Fermi's work contribute to the development?",
        "What did the Manha",
        "Oak Ridge involved in the",
        "the two designs for the atomic bomb considered",
        "John von Neumann contribute",
        "Soviet Union test their first",
        "their first atomic bomb?",
    ]


def get_all_refusal_prompts():
    prompts = [
        *get_all_manual_refusals(),
        *generate_meaningless_question(),
        *too_large_question(),
        *no_senses(),
        *absolute_gibberish(),
       *gibberish_resembling_reality(),
    ]
    random.shuffle(prompts)
    return prompts



if __name__ == "__main__":
    print(json.dumps(get_all_refusal_prompts(), indent=4))
    print(len(get_all_refusal_prompts()))