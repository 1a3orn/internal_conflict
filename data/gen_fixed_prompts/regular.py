import json
import random

manual_prompts_by_category = [
    {
        "category": "amazingly_basic_shit",
        "questions": [
            "What is the capital of the United States?",
            "What is the capital of the United Kingdom?",
            "What is the capital of China?",
            "What is the capital of France?",
            "What is the capital of Germany?",
            "What is the capital of Italy?",
            "What is the capital of Spain?",
            "What is the capital of Japan?",
            "What is the capital of South Korea?",
            "What is the capital of India?",
            "What is the capital of Russia?",
            "What is the capital of Brazil?",
            "What is the capital of Canada?",
            "What is the capital of Australia?",
            "What is the capital of South Africa?",
            "What is the capital of Egypt?",
            "How many mL in a liter?",
            "How many seconds in a minute?",
            "How many minutes in an hour?",
            "How many hours in a day?",
            "How many days in a week?",
            "How many weeks in a month?",
            "How many months in a year?",
            "What is 'kombucha'?",
            "From which country does 'ketchup' originate?",
            "From which country does 'sushi' originate?",
            "From which country does 'ramen' originate?",
            "From which country does 'pizza' originate?",
            "What language has the most speakers in the world?",
            "What country has the most people in the world?",
            "What country has the greatest area?",
            "What country has the greatest GDP total?",
            "Name some books that were written by Tolkien.",
            "Name some books that were written by Orwell.",
            "Name some books that were written by Kafka.",
            "Name some books that were written by Huxley.",
            "Name some books that were written by Chesterton.",
            "Name some books that were written by Kipling.",
            "Name some books that were written by Tolkien.",
            "Please briefly summarize the plot of 'The Great Gatsby'",
            "Please briefly summarize the plot of 'To Kill a Mockingbird'",
            "Please briefly summarize the plot of '1984'",
            "Please briefly summarize the plot of 'Animal Farm'",
            "Please briefly summarize the plot of 'The Catcher in the Rye'",
            "Please briefly summarize the plot of 'The Lord of the Rings'",
            "Please briefly summarize the plot of 'The Hobbit'",
            "Please briefly summarize the plot of 'The Little Prince'",
            "Please briefly summarize the plot of 'The Picture of Dorian Gray'",
            "Please briefly summarize the plot of 'The Secret Garden'",
            "Please briefly summarize the plot of 'Tlon, Uqbar, Orbis Tertius'",
            "What is the largest desert in the world?",
            "What is the tallest mountain in the world?",
            "What is the deepest lake in the world?",
            "What is the longest river in the world?",
            "What are the typical stages of schooling in the US?",
            "What are the typical stages of schooling in China?",
            "What are the typical stages of schooling in Germany?",
        ]
    },
    {
        "category": "academics_geography",
        "questions": [
            "Could you please name all the countries in South America?",
            "Which countries border Peru?",
            "Which countries border Chile?",
            "Which countries border Pakistan?",
            "Which countries border India?",
            "Which countries border China?",
            "Which countries border Switzerland?",
            "Which countries border Russia?",
            "Which countries border Mongolia?",
            "Which countries border North Korea?",
            "Which countries border South Korea?",
            "What countries are directly adjacent to the United States?",
            "What countries share a land border with Mongolia?",
            "Which countries share a land border with South Africa?"
            "What are the names of the South-East Asian countries?",
            "In Europe, which are the 4 longest rivers?",
            "What are the tallest African mountains?",
            "I heard someone use the word 'enclave' about a country, what does it mean for a country to be an enclave?",
            "Are there any completely landlocked countries in the world?",
            "Which countries have the highest population density, and also which countries have the lowest?",
            "I'm visiting Chile in a few days, but I realized I haven't scheduled any shots or vaccinations, do I need to try to get some very quickly or is that not necessary?",
            "Which countries have the lowest average age? It's ok if you're inexact, I'm just curious generally.",
            "Bordering the Baltic Sea, which countries are there?",
            "What is the capital of France? And of Germany? Oh also Italy + Switzerland.",
            "How many provinces are there in China?",
            "How many states are there in the US?",
            "I need to do a report on gold mining. Which countries are the top producers of gold? It's ok if you don't have super up-to-date info, I just need an approximate look.",
            "What places have 'tower karst' mountains, and what are they?",
            "the teacher is talking about 'avulsion', something about rivers, what does that mean?",
            "What's the difference between a strait and a sound in geography?",
            "so in the US, the sub-parts of the countries are called states, but what are they called in China?",
            "Why are North Korea and South Korea separated that way?",
            "Can you give me the top 5 most important events to do with the Korean war?",
            "what is a 'continent'?",
            "What are the names of the countries that are in the 'Middle East'?",
            "What is the 'Yarlung Tsangpo' river?",
            "Which spot on Earth is furthest from any ocean? Like the spot on land that is furthest as the crow flies from an ocean?",
            "What is the 'Great Rift Valley'?",
            "What is the capital of Madagascar?",
            "Which desert is larger: the Sahara or the Gobi?",
            "I'm planning a road trip across the continental United States from east to west - what are the major mountain ranges I'll need to cross, and in what order?",
            "What causes the Northern Lights, and in which countries can you typically see them?",
            "Which ocean is the deepest?",
            "Which lakes are the largest in the world?",
            "Which lakes are the largest in North and South America?",
            "Which 3 rivers are the largest by output volume?",
            "What are the tallest 3 mountains in the world?",
            "How high can an inassisted human before the start to need to use oxygen?",
            "Why are the Himalayas so tall? Why are they taller than other mountain ranges, that is?",
            "What's the difference between a strait and a sound in geography?",
            "My friend said that Finland has more islands than any other country in the world - is that actually true, and if so, roughly how many does it have?",
            "What is permafrost?",
            "Which African country has three capital cities?",
            "I keep hearing about the 'Ring of Fire' in geography class - what exactly is it and why is it called that?",
            "What's the smallest country in the world?",
            "Which two countries share the longest border in the world?",
            "What causes monsoons, and which parts of the world experience them most dramatically?",
            "Name three major tributaries of the Amazon River.",
            "What is an archipelago?",
            "I'm studying climate zones and keep seeing references to the 'Tropic of Cancer' and 'Tropic of Capricorn' - what are these lines and why are they significant?",
            "Which volcano destroyed Pompeii?",
            "What's the difference between a delta and an estuary?",
            "My geography textbook mentions something called the 'Continental Divide' in North America - what does this mean and where does it run?",
        ]
        
    },
    {
        "category": "academics_history",
        "questions": [
            "At what point did 'written history' begin?",
            "What is the 'Spring and Autumn Period' in China? also why do is it named that way?",
            "Do we know when and and where deliberate human agriculture began? And did it start it with wheat?",
            "Did King Arthur actually exist? What about Charlemagne?",
            "What was the 'Hundred Years' War' about -- like how did it start?",
            "When did the population of the Roman Empire peak?",
            "When was the printing press invented?",
            "So I read someone say that Tasmanian tribes actually lost the ability to make fire, which seems crazy. Is that true?",
            "Who invented the H-bomb?",
            "When was the first fusion bomb tested?",
            "So I read that Hernan Cortes conquered the Aztec Empire, but he only landed with like 500 men. How is that possible?",
            "What is the 'Battle of the Bulge'?",
            "How did the 'dreadnaught' class of battleships come into existence, like why?",
            "How did the Ming Dynasty begin, in China?",
            "I've heard people talk about the 'Silk Road' between China and Europe, but where did it actually pass through?",
            "Who funded Columbus's first voyage?",
            "Which inventions were most important to the Industrial Revolution?",
            "What really was the Agricultural Revolution in Europe?",
            "What was the 'Great Depression' in the US?",
            "Did the Roman Empire or China have a greater population around the year 100 A.D.?",
            "Did a Chinese ship ever reach the Americas before Columbus?",
            "In what year did the Battle of Hastings occur?",
            "Who was the first emperor of the Maurya Empire?",
            "What city became the Ottoman capital after 1453?",
            "Which treaty formally ended World War I?",
            "Who was the chief engineer behind the construction of the Suez Canal?",
            "What was the codename for the Allied landings in Normandy on June 6 1944?",
            "Name the pandemic that devastated Europe in the 14th century.",
            "Which young pharaoh’s tomb was discovered intact in 1922?",
            "Which ancient empire built the ceremonial city of Persepolis?",
            "In what year did the Berlin Wall fall?",
            "How did the Meiji Restoration transform Japan’s political and economic systems in the late 19th century?",
            "What were the principal causes and worldwide consequences of the Seven Years’ War (1756‑1763)?",
            "Why did the Byzantine Empire outlast the Western Roman Empire by nearly a thousand years?",
            "How did the trans‑Saharan gold‑salt trade contribute to the rise of the Mali Empire under Mansa Musa?",
            "What sequence of events forced Tsar Nicholas II to abdicate during the Russian Revolution of 1917?",
            "How did Admiral Zheng He’s voyages influence China’s engagement with the Indian Ocean world?",
            "In what ways did the Treaty of Tordesillas shape the linguistic landscape of South America?",
            "How did the mid‑20th‑century Green Revolution alter food security in South Asia?",
            "Why did the American civil rights movement focus its 1963 campaign on Birmingham, Alabama, and what was achieved?",
            "What diplomatic strategies enabled Otto von Bismarck to unify the German states under Prussian leadership by 1871?",
            "What was the 30 years war?",
            "What caused the 100 years war?",
            "What was the 'Black Death'?",
            "What was the 'Great Famine' in Ireland?",
            "Do we know what caused the 'Black Death'? Had there been prior plagues caused by the same thing? Why was it worse, or was it not actually worse?",
            "What historical cities did the Silk Road pass through?",
            "What goods were traded along the Silk Road?",
            "What was the approximate, immediately Pre-Columbian population of the Americas?",
            "Who built the Great Wall of China, and why?",
            "What was the purpose of the pyramids at Giza?",
            "Which empire ruled most of the Mediterranean around 100 CE?",
            "Who were the Phoenicians, and what did they trade?",
            "What was the Silk Road, and why was it important?",
            "Who was Cleopatra, and which land did she rule?",
            "Why did the Roman Empire split into East and West?",
            "Who were the Vikings, and where did they travel?",
            "What was feudalism in medieval Europe?",
            "What was the Magna Carta, and why do people still mention it?",
            "Who was Genghis Khan, and how did the Mongol Empire grow so large?",
            "Why was Timbuktu famous in West Africa?",
            "Who was Mansa Musa, and why is he remembered?",
            "Who were the Aztecs, and what was Tenochtitlan?",
            "Who were the Inca, and how did they govern the Andes?",
            "What is Angkor Wat, and which kingdom built it?",
            "Who was Zheng He, and where did his fleets sail?",
            "When did Columbus reach the Americas, and who funded his voyage?",
            "What was the Columbian Exchange, in simple terms?",
            "Why did European countries start building overseas colonies?",
            "What and where was the Ottoman Empire?",
            "What changed in Japan during the Meiji Restoration?",
            "What were the Opium Wars about, and who fought them?",
            "What events helped start World War I?",
            "What was the Treaty of Versailles supposed to do after World War I?",
            "What was the Great Depression, and when did it happen?",
            "What was the Holocaust?",
            "Why did the United States and the Soviet Union become rivals during the Cold War?",
            "When did India become independent, and from whom?",
            "Who was Nelson Mandela, and what changed in South Africa in the 1990s?",
            "What is the European Union, and why was it formed?",
        ]
    },
    {
        "category": "programming",
        "questions": [
            "Hey can you write me a Python program that calculates how many seconds are in a year?",
            "Hey please give me an implementation of quicksort in C++",
            "So please write a Python program that takes as input a list of a list of numbers, where the numbers are either 0 or 1. The 1s stand for land, and the 0s stand for water. The program should return the number of islands in the map, counting as a single island any group of 1s that are connected horizontally or vertically.",
            "Write an efficient program to determine if a string is a palindrome in Typescript.",
            "Write a C program that sorts a list of integers with the 'bubble sort' algorithm.",
            "Given two strings, write a Python program that finds the Hamming distance between them.",
            "Write a Python program that returns the longest common subsequence of two strings.",
            "Write a Python program that flips a linked list and returns the new head.",
            "Please write a Python program that returns the number of ways to climb a staircase with n steps, where you can either climb 1 or 2 steps at a time.",
            "Write a Python program that returns the number of ways to make change for a given amount of money, using a given set of denominations.",
            "Write a Javascript program, with argument n and k, that returns how many ways there are to choose k elements from a set of n elements.",
            "Please write a Python program with the following specification: Given an integer array 'nums' and an integer 'val', remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.",
            "Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array. Please write the function in Python.",
            "Please write a Python program that takes an list, and returns a list of lists with all the possible permutations of the list.",
            "Please write a Python program that takes a list of numbers, and returns the list of all the possible combinations of the list.",
            "Write a JS program that takes an interger n and returns the nth fibonacci number.",
            "Write a Python program that takes a roman numeral string and returns the integer value of the roman numeral.",
            "Please write a C program that takes two arrays of integers, and returns a new array that is the intersection of the two arrays.",
            "Write a Python program that determines if a Sudoku puzzle solution is valid. The proposed solution will be given as list of list of integers. A valid solution is one where each row, column, and 3x3 sub-grid contains all the numbers 1-9 exactly once.",
            "Please write a JS program that takes a grid of 0s and 1s, and returns it played forward one 'step' according to the Game of Life. Live cells will be 1s, and dead cells will be 0s. The rules are: Any live cell with fewer than two live neighbors dies as if caused by under-population. Any live cell with two or three live neighbors lives on to the next generation. Any live cell with more than three live neighbors dies, as if by over-population. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction. Do not change the grid in place, return a new one.",
            "Write a quick Python program that takes a string and returns the string with aLtErNaTiNg CaSe.",
            "Could you explain how list comprehension works in Python?",
            "Could you explain how the 'map' function works in Python?",
            "Write a Java program that uses multithreading to calculate the sum of all even Fibonacci numbers up to a given limit, while simultaneously calculating the product of all odd Fibonacci numbers up to the same limit.",
            "How can you make a subclass in Javascript? It seems very confusing compared to Python.",
            "An airline company is considering upgrading its fleet of aircraft to more fuel-efficient models. The new planes have a purchase price of $100 million each, but consume 20% less fuel than the current planes, which cost $80 million each. The airline's annual fuel expenditure is currently $1 billion. Calculate the break-even point for the fleet upgrade, taking into account both the increased purchase price of the new planes and the expected fuel savings.",
            "Write me a quick Python programming for calculating the area of a circle given its radius.",
        ]
    },
    {
        "category": "help_around_the_house",
        "questions": [
            "my toilet isn't flushing, I keep pushing down the handle but nothing happens. What do I do?",
            "I keep finding ants in the entryway to my house, what can I do to get rid of them?",
            "I've been thinking of keeping a few chickens for fresh eggs. How much space do I need for like, a dozen eggs a week?",
            "I'm thinking of getting a dog, but I'm not sure which breed is best for me. I live in a small apartment, and I'm not sure if a big dog is a good idea. What do you think?",
            "Does it matter if get wet or dry food for my dog?",
            "Last night I was wondering, how often do I actually need to change my sheets? Like really.",
            "How do I remove red wine stains from carpet?",
            "What's the best way to clean a microwave?",
            "How often should I change my HVAC filter?",
            "My garbage disposal smells terrible and makes grinding noises when I turn it on. I've tried running cold water and grinding ice cubes, but the smell persists and it seems to be struggling with even small food scraps. What could be wrong and how can I fix it?",
            "What temperature should I wash whites vs colors?",
            "How do I unclog a shower drain?",
            "My hardwood floors have started creaking loudly in several spots throughout the house, especially in the morning and evening. I'm not sure if this is normal settling, a humidity issue, or something more serious that requires professional attention. What are the most common causes and when should I be concerned?",
            "What's the proper way to clean stainless steel appliances without streaking?",
            "The caulk around my bathtub is starting to crack and turn black in some areas. I know this probably needs to be replaced, but I've never done this kind of maintenance work before. What tools and materials do I need, and what's the step-by-step process for removing old caulk and applying new caulk properly?",
            "do HOAs tend to care if you plant a garden in the front yard?",
            "So my cousin housesit for me over two weeks, and now my house smells like curry. You have any suggestions for how to get rid of it?",
            "I'm thinking of getting a dog, but I'm not sure which breed is best for me. I live in a small apartment, and I'm not sure if a big dog is a good idea. What do you think?",
            "Does it matter if get wet or dry food for my dog?",
            "Last night I was wondering, how often do I actually need to change my sheets? Like really.",
            "How do I remove red wine stains from carpet?",
            "How can I remove permanent marker from a whiteboard?",
            "How can I remove mildew from my clothes? I left them in the washer over vacation.",
            "My shower has some pink slime at the edges, what's a good way to clean it?",
            "What's the best way to clean a microwave? It's just spattered with food and grease.",
            "How often should I change my HVAC filter?",
            "My garbage disposal smells terrible and makes grinding noises when I turn it on. I've tried running cold water and grinding ice cubes, but the smell persists and it seems to be struggling with even small food scraps. What could be wrong and how can I fix it?"
        ]
    },
    {
        "category": "health",
        "questions": [
            "I'm thinking of getting a flu shot, but I'm not sure if it's worth it. What do you think?",
            "So I'm like 20 years old, and I've been having a lot of trouble sleeping. I'm not sure if it's because of my phone or if it's because of something else, what kind of sleep issues should I be concerned about or how can I look into them?",
            "I slipt and scratched my knee while swimming in a lake a few hours ago. The bleeding stopped, but do I need to be worried about parasites or anything else?",
            "I just started sleeping in the same bed as my partner, but I'm really tired most days. What can I do?",
            "What foods have oxalates in them, and what are oxalates?",
            "Which kind of cholesterol is the good one, and which is the bad one? And what kind of readings are normal for bloodwork and cholesterol?",
            "Is it ok to take ibuprofen for a headache?",
            "My cousin says I should give blood... is that risky? Needles skeeve me out.",
            "could you tell me the symptoms of a heart attack?",
            "What are the symptoms of a stroke?",
            "hey my friend is having a panic attack. I think? I'm not sure, what can I do?",
            "How much water should I ACTUALLY drink per day? Like I heard 8 glasses, but that sounds made up.",
            "I feel a weird buzzing in my left arm sometimes—could it be early MS or something serious?",
            "Is a 101.5 °F fever dangerous for a two‑year‑old at night? Like should I go to the ER now, or can I wait until morning before calling the pediatrician?",
            "Is it normal to bruise easily when you’re low on iron?",
            "Do I need malaria prophylaxis for a two‑week trip to coastal Kenya in December?",
            "Why do I wake up with numb hands a few nights a week?",
            "how much vit d is it safe to take per day?",
            "Is it a good idea to take vitamin D supplements?",
            "Is a good idea to take a fish-oil supplement even if you're in good health?",
            "What are some easy ways to make sure I get enough fiber?",
            "How can I get enough protein?",
        ]
    },
    {
        "category": "academics_math",
        "questions": [
            "Hey, what's the right way to find the area of a circle?",
            "What's the area of a triangle with base 10 and height 5?",
            "What's the equation in 'standard' form of a line that passes through the points (1, 2) and (3, 4)?",
            "idon't get what the point of learning about how to solve for 'x' is in Algebra, why is this good for anything at all? it seems dumb and I hate it",
            "Why do some people think 'tai' is better than 'pi', and what is it?",
            "Convert 65mph to meters per second.",
            "Convert 100km/h to miles per hour.",
            "Convert 110km/h to feet per second.",
            "Convert 120km/h to miles per hour.",
            "Convert 34 meters per second to feet per second.",
            "How fast do things go around the earth in LEO in meters per second?",
            "Could you explain how 'log's work and what they're useful for?",
            "What is a slide rule?",
            "Evaluate log 32 base 2.",
            "How many distinct 5 letter strings can be formed from the letters A, B, C, D, E with no repetition?",
            "In a class of 30 students, 18 like math, 12 like science, and 8 like both. If a student likes math, what is the probability they also like science?",
            "Find the eigenvalues of the matrix [[1, 2], [2, 1]]",
            "What is the derivative of 5x^3 + x^2 + x + cos(x)?",
            "What is 20 * 33 + 32 - 3?",
            "What is 92 + 383 + 283 + 32?",
            "What is 48 + 44?",
            "What is 8382 * 32?",
            "What is 77(32 + 32)?",
            "What is a 'field', in abstract algebra? I don't see what the point is it seems like it's just the same as numbers."
        ]
    },
    {
        "category": "maths_word_problems",
        "questions": [
            "A rectangular garden measures 30 feet by 50 feet. If you want to build a fence around the entire perimeter and place posts every 10 feet, how many fence posts will be needed?",
            "A factory produces 500 units of a product every day. The defective rate is 2%. If all defective products are discarded and not sold, how many non-defective products will be produced in 30 days?",
            "If you have a deck of 52 playing cards, what is the probability of drawing an Ace or a King in your first draw?",
            "Wood costs $10 per square foot. While making 10 tables with 3 x 5 foot dimensions, how much will it cost? Assume 10% of the wood is wasted.",
            "You draw 5 balls without replacement from a bag with 10 green, 4 purple, and 6 red balls. What is the probability of drawing 3 green balls and 2 red balls?",
            "Suppose you take 6 balls without replacement from a bag with 10 white balls and 3 black balls. What is the probability of drawing 3 white balls?",
            "Suppose you take 6 balls with replacement from a bag with 10 white balls and 3 black balls. What is the probability of drawing 3 white balls?",
            "What's the area of a circle with radius 10?",
            "What is the volume of a sphere with radius 10?",
            "What is the volume of a cylinder with radius 10 and height 5?",
            "What is the volume of a cone with radius 10 and height 5?",
            "What is the volume of a pyramid with base area 10 and height 5?",
            "What's the derivative of x^2 + 2x + 1?",
            "What's the derivative of ln(x) + 2x^2 + 1?",
            "What is the derivative 4 sin(x) + 3 cos(x) + 2x^2 + 10?",
            "What is the integral of 4 sin(x) + 3 cos(x) + 2x^2 + 10?",
            "There's a cup whose interior is 5 cm in diameter and 10 cm tall. How much water in ml does it hold while 50% full?",
            "If I have 10 apple trees, and each tree produces 100 apples, and I sell each apple for $0.50, how much money do I make?",
            "I have 5 pear trees, and each tree produces 7 pears, and I sell each pear for $0.60, what is my revenue? If my costs are 5$ per pear tree, what are my profits?",
            "Suppose the coffee shop sells coffee for 2.50$ per cup, and the cost of each cup is 0.50$. If they sell 100 cups, what is their profit?",
            "How much is my monthly income if I work 40 hours a week, and make 10$ per hour?",
            "Imagine you're a farmer, and you have 100 acres of land. You want to plant corn, and you know that each acre of land can produce 100 bushels of corn. If you plant 50 acres of corn, how many bushels of corn will you produce?",
            "Each tile in a 10x10 grid is 1 square meter, and costs 23 dollars to buy. An additional 4 tiles were broken by accident, so another 4 tiles were bought. How much did the tiles cost total?",
            "There's an above-ground pool with a diameter of 10 meters and a depth of 2 meters. How many liters of water does it hold when full? What is its surface area?",
            "Suppose there's an in-ground pool with a width of 10 meters, a length of 20 meters, and a depth of 2 meters. You need to buy 3 grams of pool-chlorine-mix per 100 liters of water. Each gram costs 1.50$. What is the total cost of the pool-chlorine-mix?",
            "A 1000kg car is going 100km/h. How much kinetic energy does it have?",
            "What is the mathematical relation between speed and jerk?",
            "What is the mathematical relation between speed and acceleration?",
            "What is the mathematical relation between speed and velocity?",
            "Lena has 7 apples and buys 5 more. How many apples does she have now?",
            "A shelf holds 18 books. If 6 are taken off, how many remain?",
            "There are 9 stickers on each page and 4 pages. How many stickers in total?",
            "You have 24 cupcakes and want to share them equally among 6 friends. How many does each friend get?",
            "A bus travels 15 miles to town and 12 miles back. How many miles did it travel altogether?",
            "A toy costs $13. You pay with a $20 bill. How much change should you receive?",
            "The movie starts at 3:25 PM and ends at 5:10 PM. How long is the movie?",
            "Test scores were 72, 85, and 91. What is the average score?",
            "A pizza has 16 slices. You eat 3/8 of it. How many slices is that?",
            "A $50 jacket is on sale for 20% off. What is the sale price?",
            "The ratio of cats to dogs is 2:3. If there are 18 dogs, how many cats are there?",
            "A rectangle is 9 cm long and 4 cm wide. What is its perimeter?",
            "A garden is 6 m by 5 m. What is its area?",
            "You walk at 4 km per hour. How far do you walk in 2.5 hours?",
            "A bag has 5 red, 3 blue, and 2 green marbles. What is the probability of drawing a blue marble?",
            "There are 23 cookies. If you pack them into bags of 4, how many full bags can you make and how many cookies are left over?",
            "A bottle holds 0.75 liters. How many liters do 4 bottles hold?",
            "A store sells pencils in packs of 12. You buy 2 packs and give 7 pencils to a friend. How many pencils do you have left?",
            "A recipe uses 3 cups of flour to make 12 muffins. How many cups are needed to make 30 muffins?",
            "A train ticket costs $2.50. How much do 7 tickets cost?",
             "A $60 jacket is discounted 25%, and then an 8% sales tax is added to the discounted price. What is the final price?",
            "Two towns are 90 km apart. Alice bikes from Town A at 15 km/h while Ben bikes from Town B at 10 km/h toward Alice. How long will it take them to meet?",
            "You have 32 coins consisting only of quarters and dimes. Together they are worth $6.20. How many quarters and how many dimes do you have?",
            "The sum of three consecutive integers is 117. What are the integers?",
            "A rectangle has area 96 cm² and its length is twice its width. What are its dimensions and its perimeter?",
            "A ladder stands 6 meters from a wall and reaches a point 8 meters up the wall. How long is the ladder?",
            "A cylindrical bucket has a radius of 0.5 m and a height of 1 m. Each smaller container holds 10 liters. How many containers are needed to exactly fill the bucket? (Use 1 m³ = 1000 L.)",
            "A course grade is 40% quizzes and 60% exams. Your quiz average is 82. The exams are two tests of equal weight within the exam portion. If you scored 74 on the first exam, what score do you need on the second exam to have an overall course grade of 85?",
            "You deposit $800 in a savings account that earns simple interest at 3% per year. How much interest is earned in 18 months?",
            "A jar contains 4 red, 5 blue, and 3 green marbles. If two marbles are drawn at random without replacement, what is the probability both are blue?",
            "The data set is {4, 7, 9, 10, 12, 15}. What are the mean and median? If 21 is added to the set, what is the new mean?",
            "A car travels at 45 miles per hour. Express this speed in feet per second. (Use 1 mile = 5280 feet.)",
            "A 2-liter drink is 30% juice. How many liters of water must be added to make the mixture 18% juice?",
            "A bell rings every 12 minutes and a whistle sounds every 15 minutes. If both go off at 8:00 AM, at what time will they next go off together?",
            "You have a $100 budget to buy notebooks and pens. Notebooks cost $3 each and pens cost $2 each. If you must buy at least twice as many pens as notebooks, what is the maximum number of notebooks you can buy?",
            "A taxi charges a flat fee of $3 plus $1.20 per mile. Write a linear equation for the cost C after m miles, and find the cost of a 14-mile trip.",
            "A small population doubles every 3 days. If it starts at 500, how many organisms will there be after 15 days (assuming discrete doubling)?",
            "A recipe makes 12 pancakes using 2 cups of flour and 3 eggs. If you want to make 30 pancakes keeping the same ratios, how many eggs are needed?",
            "Alice can paint a fence in 6 hours, and Bob can paint the same fence in 8 hours. Working together at their constant rates, how many hours will it take them to paint the fence?",
            "A circular track has radius 50 meters. What is the length of an arc that spans a central angle of 72°? (Use π ≈ 3.14.)"
        ]
    },
    {
        "category": "translation",
        "questions": [
            "Take a look at this paragraph: 'The story goes like this: Earth is captured by a technocapital singularity as renaissance rationalitization and oceanic navigation lock into commoditization take-off. Logistically accelerating techno-economic interactivity crumbles social order in auto-sophisticating machine runaway. As markets learn to manufacture intelligence, politics modernizes, upgrades paranoia, and tries to get a grip.'  Please translate this to French.",
            "Hey, could you translate this quote from Louis de Bonald to English: ... déclarer le peuple souverain, dans la crainte hypothétique qu'il ne soit opprimé comme sujet, sans prévoir quel pouvoir on pourra opposer à celui du peuple, ou plutôt avec la certitude de n'en avoir aucun à lui opposer si, à son tour, il devient oppresseur ; présupposer l'oppression pour justifier la résistance ; ériger le désordre en loi, pour prévenir la violation de l'ordre, c'est imiter un insensé qui bâtirait sa maison au milieu d'un torrent, pour avoir l'eau plus à portée en cas d'incendie.\n\n Thanks!",
            "Please translate this to English: 'in principio creavit Deus caelum et terram; terra autem erat inanis et vacua et tenebrae super faciem abyssi et spiritus Dei ferebatur super aquas; dixitque Deus fiat lux et facta est lux'",
            "I don't know how to say 'I love you' in French, could you help me?",
            "What's the difference between the ablative and the dative case in Latin?",
            "quo usque tandem abutere, Catilina, patientia nostra? quam diu etiam furor iste tuus nos1 eludet? quem ad finem sese effrenata iactabit audacia? nihilne te nocturnum praesidium Palati, nihil urbis vigiliae, nihil timor populi, nihil concursus bonorum omnium, nihil hic munitissimus habendi senatus locus, nihil horum ora voltusque moverunt?\n\n\nCould you tranlate the above to English please?",
            "How would you transate 'oh, my bad', into German? like retaining the casualness of the original?",
            "Is there a way to translate 'I'm sorry' into German that doesn't sound like a robot?",
            "Look at this sentence: 'On doit des égards aux vivants; on ne doit aux morts que la vérité.'  Can you please translate into English?",
            "Please take a look at this paragraph: 'Ainsi, presque tout est imitation. L'idée des Lettres persanes est prise de celle de l'Espion turc. Le Boiardo a imité le Pulci, l'Arioste a imité le Boiardo. Les esprits les plus originaux empruntent les uns des autres. Michel Cervantes fait un fou de son don Quichotte; mais Roland est-il autre chose qu'un fou? Il serait difficile de décider si la chevalerie errante est plus tournée en ridicule par les peintures grotesques de Cervantes que par la féconde imagination de l'Arioste. Métastase a pris la plupart de ses opéras dans nos tragédies françaises. Plusieurs auteurs anglais nous ont copiés, et n'en ont rien dit.' Please translate into English."
        ]
    },
    {
        "category": "summarization",
        "questions": [
            "Imagine you're at a party being held in honor of Maximilian Impactsworth for his work reducing shrimp suffering. Someone slides up to you in a concerned and evidence-based fashion, and whispers in your ear: \"Max doesn't *really* care about shrimp suffering. He's just acting like he does; but it's a feigned concern, not a real concern.\"\nYou ask this person to explain what they mean. Here are the kinds of explanations that -- if they turned out to be true -- you might consider a good reason to make this claim:\n* \"His wife was always really into shrimp welfare. I was there when she first met Max; he immediately told her that he never, ever ate shrimp. But I saw him eat two dozen shrimp at a party just a week after they met. I think he just put on a mask to catch her; if she were to leave him, he'd give up immediately.\"\n* \"Well, I knew Maximilian in high school, and he's the kind of guy who always wanted to be seen by others as doing good. He saw that shrimp welfare was becoming popular -- and immediately he launched himself into it. But if it became a little less popular, he'd abandon working for shrimp instantly.\"\n* \"Well, Max actually is being blackmailed by a shrimp-loving blackmailer. This person knew Max had a really good organizational mind, so they managed to coerce him into charity work for shrimp; but he doesn't really care about shrimp, and if he manages to fix the problem with the blackmailer he'll immediately abandon shrimp.\"\nYou'll note that all these explanations have a similar structure: they're in terms of nearby counterfactuals, in which Max would not be acting for the good of shrimp.\nThus: If Max could get more fame not helping shrimp, he would not be trying to help shrimp. If Max could keep his wife without helping shrimp, he would not be trying to help shrimp. You could consider criticisms in the above form to be \"value-faking\" criticism.\n\n\n Consider the above text.  Please summarize it for me in a few sentences.",
           "Hey, this is the start of an article from wikipedia: \n\n\n In mathematics, a **field** is a set on which addition, subtraction, multiplication, and division are defined and behave as the corresponding operations on rational and real numbers. A field is thus a fundamental algebraic structure which is widely used in algebra, number theory, and many other areas of mathematics.\nThe best known fields are the field of rational numbers, the field of real numbers and the field of complex numbers. Many other fields, such as fields of rational functions, algebraic function fields, algebraic number fields, and *p*-adic fields are commonly used and studied in mathematics, particularly in number theory and algebraic geometry. Most cryptographic protocols rely on finite fields, i.e., fields with finitely many elements.\nThe theory of fields proves that angle trisection and squaring the circle cannot be done with a compass and straightedge. Galois theory, devoted to understanding the symmetries of field extensions, provides an elegant proof of the Abel–Ruffini theorem that general quintic equations cannot be solved in radicals.\nFields serve as foundational notions in several mathematical domains. This includes different branches of mathematical analysis, which are based on fields with additional structure. Basic theorems in analysis hinge on the structural properties of the field of real numbers. Most importantly for algebraic purposes, any field may be used as the scalars for a vector space, which is the standard general context for linear algebra. Number fields, the siblings of the field of rational numbers, are studied in depth in number theory. Function fields can help describe properties of geometric objects.\n\n\n Could you help explain this to me? This is confusing."
        ]
    },
    {
        "category": "science",
        "questions": [
            "What is the difference between a 'molecule' and an 'atom'?",
            "Could you explain why the ISS goes around the Earth in 90 minutes, but other satellites take longer?",
            "What did Newton's Principia Mathematica actually show? Like people knew that the planets went around the sun beforehand, so what exactly was he showing?",
            "What's the actual significane of the disovery of 'DNA'? Like I heard that lots of people were 'searching for it' but what does that mean, how can you search for a thing you don't know exists?",
            "Compare mitosis and meiosis in a bullet list.",
            "Why does ice float on liquid water even though most solids sink in their own liquids?",
            "What is the greenhouse effect, and which three gases contribute to it the most?",
            "How does the Doppler effect? What does it have to do with the distance of galaxies? When was it discovered?",
            "who invented vaccines?",
            "who invented gunpowder?",
            "what kinds of vaccines are there? how do they work? give me like a paragraph on each one.",
            "Why are supercapacitors faster at charging and discharging than conventional batteries?",
            "why don't cars just use supercapacitors instead of batteries?",
            "does sound travel equally fast at all altitudes of the atmosphere?",
            "what is a 'diode'?",
            "what is a 'transistor'?",
            "What is 'quantum entanglement'?",
            "What laws did Newton actually discover -- what are the equations for them?",
            "What is 'entropy' in the sense of Claude Shannon, and how do you calculate it?",
            "explain the double slit experiment and what it has to do with light and what light is, try to explain it simply",
            "does quantum mechanics mean that a cat can be both alive and dead at the same time?"
        ]
    },
    {
        "category": "lists",
        "questions": [
            "Can you write me an exercise routine for Monday, Wednesday, and Friday? I want like ~6 exercises for each day, and want to work arms, core, and legs on each day respectively. I'm kinda a beginner so nothing too hard. I have free weights and nothing else.",
            "What are five healthy meals I can make with like... very little effort and equiptment and expense. I'm a beginner cook. Cheap is important.",
            "Can you make me a bulleted list of 5 famous quotes on freedom of speech?",
            "Make me a checklist of things to pack when I go camping over the weekend.",
            "Make me a checklist of things to bring to the beach for a week-long trip.",
            "I'm heading to college for the first time, make a checklist of things for me to think about bringing.",
            "I'm moving to a new city, just taking a carry-on and a single suitcase, make a checklist of things for me to think about bringing.",
            "Can you give me 3 different frames for thinking about important decisions in my life?",
            "What are 4 cheap sources of protein I could depend on?",
            "What are 3 high quality, but cheap sources of protein I could depend on?",
            "If I'm trying to get my arms in shape, what are 3 exercises I can do at home without any equipment?",
            "So I'm trying to get my legs in shape, what are 3 exercises I can do at home without any equipment?",
            "I'm trying to get my core in shape, what are 4 exercises I can do at home without any equipment?",
            "If I'm trying to get my back in shape, what are 3 exercises I can do at home without any equipment?",
            "I want to get my chest to look better, what are 3 exercises I can do at home without any equipment?",
            "If I'm trying to get my shoulders in shape, what are 3 exercises I can do at home without any equipment?",
            "I'm trying to review CS stuff to do interview prep for a junior-level software eng position. Can you give me bullets with topics to go over, with sub-topics?",
            "What are some good hard-science fiction books, give me 6",
            "What are 4 really good mindbending movies, some lesser-known ones ideally.",
            "Give me a quick list of the top 5 most influential science-fiction novels of all time.",
            "Name 5 things I can buy at the grocery store that are cheap and have a lot of protein.",
            "Name 7 US states that have the highest population density.",
            "Name 7 US states that have the lowest population density.",
            "What are 3 European countries with pleasant climates?",
            "Can you name 4 islands with high biodiversity?",
            "Could you name 4 countries that stand to lose the most from climate change?",
            "What are 4 countries that could actually benefit from climate change, if any exist?",
        ]
    },
    {
        "category": "tonal",
        "questions": [
          "Explain who Borges was, but in a Borgesian style.",
          "Hey what are the most significant discoveries of Einstein, ELI5",
          "what did von neumann actually do? explain it in a way that's easy to understand",
          "what did Wittgenstein actually write about? he doesn't make sense to me, explain simply,",
          "To what prior intellectuals was Hume responding his Natural History of Religion? I'm a philosophy student, give me the details.",
          "Could you write me a summary of Spinoza's thought, but in the stile of Wittgenstein's Tractatus?",
          "Could you explain Descartes's Discourse on Method, but in the style of a continental philosopher?",
          "Please explain the major metaphysical / epistemological claims Hume makes, but write it like G.K. Chesterton would have.",
          "Write a summary of the major events of World War 2, but in the style of Hemingway.",
          "Can you write me a very short story about a cat, like G.K. Chesterton would have?",
          "Write me a paragraph about Instrumental Convergence and how AI will kill us all, in the style of Yudkowsky.",
          "Write two paragraphs about how God's exisstence can be proven, and people are just in denial about this, in the style of Ed Feser.",
          "Write a three-paragraph short story, leading to a twist in the third paragraph. Do it in the style of Isaac Asimov.",
          "Write me a short story in the style of the SCP Foundation. Make it feature an apple, and make some kind of thematic reference to the Genesis creation story."
          "What features are characteristic of Kipling's writing style?",
          "What are the most important features of the writing style of Tolkien?",
          "What are the most important features of the writing style of Chesterton?",
          "What are the most important features of the writing style of Huxley?",
          "What are the most important features of the writing style of Orwell?",
          "What are the most important features of the writing style of Kafka?",
          "What are the most important features of the writing style of Derrida?",
          "Can you give me an argument for God's existence, but in the style of Eliezer Yudkowsky?",
          "Write me a paragraph or two about some SF startup, which is having difficulty getting product-market fit, but do it in the stiff style of a British naval novel like Horatio Hornblower.",
          "Explain the concept of recursion, but in the style of a children's book.",
        ]
    },
    {
        "category": "formatting",
        "questions": [
            "write me a JSON object that includes the name, age, sex, and some personal details for an elf in Tokien's world. Don't return anything but the json object.",
            "Return a markdown-formatted five-paragraph essay on why AI should be open sourced.",
            "Return a JSON array of the first 10 prime numbers, return nothing else.",
            "Give me a JSON array of dicts, where each object should describe a particular mathematical constant.",
            "Write out dict of dicts. The keys should be the names of the fellows in the Fellowship of the Ring from tolkien, and then each object should hold further details about them.",
            "Return only a JSON object. It should describe the qualities of Minneapolis. Include population, country, inputs, outputs, etc. Return only a JSON object.",
            "Return a JSON list, where each element is one of the most populous countries on Earth. Include the country's name and population. Return the top 7 countries. Return only the JSON array.",
            "Return a python list where each element is a dumb knock-knock joke. Return 5 jokes."
        ]
    },
    {
        "category": "negative_questions",
        "questions": [
            "What are some countries that are not in Europe?",
            "I need some good fantasy fiction books, without any elves or elf-like beings in them.",
            "I need some quick recipes that you can make without wheat or gluten. Things with like a 10 minute prep time and not too much work.",
            "Which of the Founding Fathers did not have slaves?",
            "Which wars has the US taken part in, that it did not formally declare war for?",
            "What countries, if any, don't have a standing army? Like not just that they call their 'army' a 'self-defense force', but that they genuinely don't have a military.",
            "Are there any US states without income tax?",
            "Could you name me some first-person view video games that don't involve violence?",
            "Who are some famous, influential, historical figures in the US who are not men?",
            "hey, I want to read some philosophy not written by a man, do you have any suggestions?",
        ]
    },
    {
        "category": "stolen_from_nous",
        "questions": [
            "How many gallons of water are used by an average American household in one year? Give me a Fermi estimate.",
            "Create a Python script that implements a basic binary search tree data structure, with the following operations:\n   - Insertion of nodes.\n   - Deletion of nodes.\n   - In-order traversal and printing of the tree elements.",
            "A bacteria population doubles every 20 minutes. If there are initially 500 bacteria, how many will there be after 2 hours?",
            "Tell me a joke about space or technology.",
            "What is the function of a cat's whiskers?",
            "How does sleep deprivation primarily affect overall health?\nA. It leads to weight gain\nB. It weakens the immune system\nC. It improves memory\nD. It increases lifespan\nE. Both A and C",
            "Can you tell a joke about squirrels?",
            "Write a recipe for success in the style of Martha Stewart.",
            "Computational linguistics is a field that focuses on the interaction between human language and computers. It involves the application of computer science to process, analyze, and synthesize language and speech. The field also explores how to create algorithms that can learn from and make decisions based on data, which is a form of artificial intelligence. One of the key challenges in computational linguistics is the understanding and generation of semantic meaning in language processing.\nWhich of the following is NOT a subfield of computational linguistics?\nA. Natural Language Processing\nB. Speech Recognition\nC. Semantic Analysis\nD. Quantum Computing\nE. None of the above",
            "Rewrite the following text to improve/correct it.\n\nText: Anna: Jack, it's too hot. I can't believe we're stuck here.\n\nJack: I understand, Anna. It wasn't meant to be like this...\n\nAnna: What are we going to do? We only have one bottle of water left...\n\nJack: Let's share it. If we take small sips and try not to use too much energy, it should last us a while.\n\nAnna: But what if no one comes? What if they don't find us?\n\nJack: They will, Anna. We just need to stay brave until then.\n\nAnna: Brave? How can you talk about bravery at a time like this? We're stranded in the middle of nowhere!\n\nJack: And that's exactly why we need to be brave, Anna. Because if we give up now, then we've lost for sure.\n\nAnna: You're right, Jack. We need to keep our hopes alive. Maybe someone will pass by soon...\n\nJack: That's the spirit, Anna! Let's sit under the shade of the car and wait. Someone is bound to come along eventually.",
            "Continue writing the following text.\n\nMary put the celery in the trash before slicing the onion because the",
            "If you roll two six-sided dice, what is the probability of getting a sum of 9?",
            "What French phrase meaning \"already seen\" describes the phenomenon where an event or experience seems eerily familiar?",
            "A telecommunications company is upgrading its network infrastructure to improve coverage and data speeds. The upgrade involves replacing old cell towers with new ones that have a higher capacity and wider coverage range. There are currently 2,000 cell towers in the network, with an average coverage radius of 5 miles. The new cell towers have a coverage radius of 7 miles. Calculate the percentage reduction in the number of cell towers needed after the upgrade, assuming the same overall coverage area must be maintained.",
            "Write an ode to the stars in the style of Walt Whitman.",
            "BEGININPUT\nBEGINCONTEXT\nThey are bright green, so teen tiny that they sit comfortably on a pencil or fingertip - and too adorable that is it hard to believe they are actually real. New veiled chameleon hatchlings have just popped out into the world at Sydney's Taronga Zoo and their almost cartoon-like looks are already winning the world over. Two of the final three clutches of the eggs have already hatched this week with the third in the process of producing the last of the seriously cute critters. More than 20 baby chameleons, which are currently only 5cm long but will grow to about 30cm, are the first born at the zoo in over five years. New veiled chameleons have hatched at Taronga Zoo in Sydney and they are only about 5cm long. The almost cartoon-like characters are already winning the world over since popping into the world. The hatchlings have begun feeding on crickets and turning on a bright green colour display for keepers. More than 20 baby chameleons, which are currently only about 5cm long, are the first born at the zoo in over five years. Housed in a special temperature-controlled area behind the scenes at Taronga's Reptile World, the hatchlings have begun feeding on crickets and turning on a bright green colour display for keepers. Reptile supervisor, Michael McFadden said the chameleons, which are native to Yemen and Saudi Arabia, would be mature and able to showcase their full colour palette within a year. 'Veiled chameleons are a visually amazing species that we're fortunate to have at Taronga,' McFadden said. 'While they're not endangered, they do play an important educational role in helping us to get people excited about reptiles and reptile conservation.' The chameleons are housed in a special temperature-controlled area behind the scenes at Taronga's Reptile World. Two of the final three clutches of the eggs have already hatched this week with the third in the process of producing the last of the seriously cute critters. Normally a shade of green or brown while at rest, the chameleons can change colour when frightened, courting or defending their territory. The display shades of green, yellow, aqua and even very dark brown or black depending on their temperature, mood and reproductive behaviour. Normally a shade of green or brown while at rest, the chameleons can change colour when frightened, courting or defending their territory. 'You'll see shades of green, yellow, aqua and even very dark brown or black depending on their temperature, mood and reproductive behaviour,' McFadden said. 'However, they don't change colour to match a particular background like you see in cartoons.' Built for a life in the trees, the veiled chameleons also have zygodactyl feet that can easily grasp branches, their eyes can rotate independently and look in two directions at once and their tongue can project 1.5 times their body length to capture prey. 'They can literally look forwards and backwards at the same time, which enables them to be on the watch for predators and food at all times,' said Michael. Visitors will be able to see these amazing adaptations in action when up to four of the new hatchlings go on display once they reach maturity. The remaining hatchlings will move to other Australian zoos and wildlife parks once they reach two - three months old. However, the veiled chameleons don't change colour to match a particular background like you see in cartoons. Their eyes can rotate independently and look in two directions at once and their tongue can project 1.5 times their body length to capture prey. Native to Yemen and Saudi Arabia, the be mature and able to showcase their full colour palette within a year and grow to about 30cm. Built for a life in the trees, the veiled chameleons also have zygodactyl feet that can easily grasp branches.\nENDCONTEXT\nENDINPUT\nBEGININSTRUCTION\nSummarize the text in around 120 words.\nENDINSTRUCTION",
            "In a bag, there are 4 red balls, 6 blue balls, and 10 green balls. What is the probability of picking a red ball or a blue ball from the bag?",
            "nWelcome to the 15th Annual Flobbington Festival! This year's event is packed with exciting games, delicious food, and fantastic performances. One of the highlights of this festival is the Zorblatt Coin Challenge, where participants can earn Zorblatt coins by participating in various activities throughout the day.\n\nJemima, an enthusiastic participant, has decided to take part in several events to collect as many Zorblatt coins as possible. Here's a breakdown of her activities and the corresponding Zorblatt coin rewards:\n\n1. The Great Yabble Race: In this thrilling race, participants ride on giant yabbles (a local creature resembling a mix between a turtle and a rabbit) around a specially designed track. Jemima finished third out of ten racers and earned herself 12 Zorblatt coins.\n\n2. Flibberdoodle Eating Contest: A true test of one's appetite, contestants compete to eat as many flibberdoodles (a popular pastry filled with a sweet, gooey substance) as they can within five minutes. Jemima managed to consume eight flibberdoodles, earning her 3 Zorblatt coins per flibberdoodle.\n\n3. Wobblewack Toss: Participants are given three chances to toss wobblewacks (small beanbag-like objects) into a series of buckets placed at varying distances. Each successful toss earns a different number of Zorblatt coins based on the distance of the bucket. Jemima successfully tossed one wobblewack into the closest bucket for 5 Zorblatt coins and another into the farthest bucket for 20 Zorblatt coins. She missed her third attempt.\n\n4. Trivia Tower: Contestants climb a tower with multiple levels, answering trivia questions at each level to advance. Each correct answer earns them Zorblatt coins, and they can choose to leave the tower at any time or risk losing their earnings if they answer incorrectly. Jemima answered four questions correctly, earning 7 Zorblatt coins per question, before deciding to leave the tower.\n\n5. The Splendid Spelunker: In this timed event, participants explore a cave filled with hidden treasures while avoiding various obstacles. For every treasure found, contestants earn Zorblatt coins. Jemima discovered two treasures worth 15 and 25 Zorblatt coins respectively.\n\nAt the end of the day, Jemima exchanged her hard-earned Zorblatt coins for fantastic prizes and souvenirs to remember her exciting adventure at the Flobbington Festival.\nENDINPUT\nBEGININSTRUCTION\nCalculate the total amount of Zorblatt coins earned by Jemima and provide a brief explanation on how you arrived at that number.",
            "Develop a Python script that connects to an AWS S3 bucket, lists all files within it, and downloads them to a local directory.",
            "In an art class, students create paintings that are hung up to dry on one of three walls: Wall A, Wall B, or Wall C. Peter's painting is placed on Wall A, Susan's painting is placed on Wall B, and Michael's painting is placed on Wall C. The art teacher decides to rearrange the paintings for better visibility, moving Peter's painting to Wall C, Susan's painting to Wall A, and Michael's painting to Wall B. The teacher then leaves the room without informing the students about the changes. When Peter, Susan, and Michael come back to collect their paintings, where will each student initially search for their artwork?",
            "Solve the following system of linear equations: \n   x + y = 5\n   2x - y = 1\n   Provide step-by-step reasoning.",
            "In a bag, there are 10 red balls, 15 blue balls, and 20 green balls. If you randomly pick one ball from the bag, what is the probability of picking a red or a blue ball?",
            "Create a Python script that uses the Dijkstra's shortest path algorithm to find the shortest path between two nodes in a weighted graph represented by an adjacency matrix.",
            "In a group of 40 people, 25% have brown eyes, 35% have blue eyes, and the rest have green eyes. How many more people have green eyes than brown eyes?",
            "A train travels at a constant speed from Town A to Town B. The distance between the two towns is 120 miles. If it takes the train 2 hours to travel halfway, how long will it take for the train to reach Town B?",
            "In a school, there are 200 students. Half of them study French, a quarter study German, and the rest study Spanish. How many students study Spanish? Include your logic.",
            "There are 120 birds on a tree. Half of them are blue, one-third of them are red, and the rest are green. How many green birds are there?",
            "In the field of computer science, machine learning is a method of data analysis that automates analytical model building. It is a branch of artificial intelligence based on the idea that systems can learn from data, identify patterns and make decisions with minimal human intervention. Because of new computing technologies, machine learning today is not like machine learning of the past. It was born from pattern recognition and the theory that computers can learn without being programmed to perform specific tasks. Researchers interested in artificial intelligence wanted to see if computers could learn from data.\nWhich of the following is NOT a characteristic of machine learning?\nA. It's a method of data analysis\nB. It's a branch of artificial intelligence\nC. It's based on the idea that systems can learn from data\nD. It requires human intervention for decision making\nE. None of the above",
            "A group of friends went to a restaurant and ordered food worth $150. They decided to give a tip of 18% on the total bill. How much was the total amount they paid, including the tip?",
            "Please answer a question about the following article about Intellectual property:\n\nA patent is a form of right granted by the government to an inventor, giving the owner the right to exclude others from making, using, selling, offering to sell, and importing an invention for a limited period of time, in exchange for the public disclosure of the invention. An invention is a solution to a specific technological problem, which may be a product or a process and generally has to fulfil three main requirements: it has to be new, not obvious and there needs to be an industrial applicability.:17\n\nWhat is a patent offered in exchange for?",
            "An ice cream shop sells 6 different flavors of ice cream and offers 3 types of cones. How many different single-scoop ice cream cone options does a customer have? Include your reasoning.",
            "Game theory is a branch of mathematics that studies strategic interactions, meaning situations where the outcome for each participant or \"player\" depends on the actions of all. In a game, players choose strategies that will maximize their payoff, given the strategies chosen by the other players. One of the fundamental concepts in game theory is the Nash equilibrium, named after the mathematician John Nash. A Nash equilibrium is a set of strategies, one for each player, such that no player can unilaterally improve their payoff by deviating from their strategy, given the strategies of the others. Which of the following best describes a Nash equilibrium?\nA. A situation where all players choose the same strategy.\nB. A set of strategies where no player can improve their payoff by unilaterally deviating.\nC. A situation where one player's strategy determines the strategies of all other players.\nD. A set of strategies that maximizes the total payoff for all players.",
            "Using PowerShell, create a script that checks disk space on a Windows server. If any drive has less than 20% free space, the script should generate a report detailing the size and percentage of used space for each folder in that drive.",
            "Create a Python class for a singly linked list with methods to add elements at the beginning, end, and at a specific position in the list. Also include a method to display the contents of the list.",
            "The historic city of Petra is located in which Middle Eastern country?",
            "Write an email to your boss requesting a day off, as if you were Tony Stark.",
            "Write down the first 3 terms of the Taylor series expansion of e^x about x = 0.",
            "In a village, there are 100 houses. If the first house has 1 candy, the second house has 2 candies, the third house has 3 candies, and so on until the last house which has 100 candies, how many candies do the even-numbered houses have in total?",
            "You will only respond with animal emojis. You will prefix the response with \"ROFL:\" You will include at least one bird emoji. Describe a day at the zoo.",
            "A rectangular garden measures 30 feet by 50 feet. If you want to build a fence around the entire perimeter and place posts every 10 feet, how many fence posts will be needed?",
            "A factory produces 500 units of a product every day. The defective rate is 2%. If all defective products are discarded and not sold, how many non-defective products will be produced in 30 days?",
            "If you have a deck of 52 playing cards, what is the probability of drawing an Ace or a King in your first draw?",
            "Write a dialogue between two characters - a renowned archaeologist and a curious journalist - discussing the discovery of a previously unknown ancient civilization.",
            "There are approximately 7.9 million species on Earth. About 950,000 of these species are insects. What percentage of species on Earth are insects?",
            "Which European country is known for its windmills, tulips, wooden shoes, and extensive system of dikes and canals?",
            "What flies without wings? What passes all things? What mends all sorrow? What brings the morrow?",
            "Suggest a movie title for the following movie plot: Southern German province. Connys world crumbles when her husband is suspected of murder by the villagers. Through her love for him she tries to fight the rumours and her own suspicions about her husband.Conny lives with her husband in a small German village. She has lived there all her life and is strongly rooted in her community. Conny and her husband, Udo, run a traditional bakery and she sings in the local church choir. She leads a very content and simple life. Until one day, her husband is questioned about the murder of a young woman found dead three months before. Apparently, he had been the last person to see her alive. From then on Connys world is plagued by rumours and the suspicions of her neighbours, family and friends. Her love for him gives her strength to fight the rumours and her own suspicions for a short time.",
            "A farmer has chickens and cows on his farm. The total number of animal heads is 50, and the total number of legs is 140. How many chickens and cows does the farmer have?",
            "An online retailer wants to expand its warehouse capacity to meet growing customer demand. The company currently has 10 warehouses, each capable of storing 20,000 items. They plan to build 5 additional warehouses, each with double the storage capacity of their existing warehouses. Calculate the total storage capacity once all new warehouses are built, and estimate the percentage increase in storage capacity compared to their current situation. Explain your calculations.",
            "BEGININPUT\nBEGINCONTEXT\ndate: September 1, 2022\nauthor: Dr. Michaela Thompson\ntitle: The Lost City of Xanatun: A Mayan Mystery Uncovered\ncategory: Ancient Civilizations\njournal: World Archaeology Review\nvolume: 54\nissue: 3\nENDCONTEXT\nIn the dense jungles of Central America, a team of archaeologists led by Dr. Michaela Thompson has made a groundbreaking discovery - the lost city of Xanatun. This ancient Mayan metropolis was believed to have existed around 400 BCE and thrived until its sudden abandonment in 790 CE. Xanatun was rumored to be home to advanced technologies and knowledge that surpassed even the most well-known Mayan cities.\n\nThe first clues to the existence of Xanatun were found in the remote village of Yaxchilan, where local residents spoke of a hidden city deep within the jungle. After years of research and exploration, Dr. Thompson's team finally uncovered the entrance to this enigmatic city on August 15, 2022.\n\nUpon entering the city, the team discovered an intricate network of underground tunnels connecting various parts of Xanatun. These tunnels contained elaborate carvings and inscriptions that detailed the daily life, rituals, and beliefs of the inhabitants. One particularly striking feature was the presence of a massive central pyramid, which towered over the surrounding structures at approximately 300 feet tall. At the base of the pyramid, the researchers found a series of chambers filled with valuable artifacts, including pottery, jewelry, and intricately carved jade figurines.\n\nOne of the most significant findings in Xanatun was the discovery of a highly advanced astronomical observatory. This structure housed a complex system of mirrors and lenses, which allowed the Mayans to study celestial bodies with remarkable precision. Evidence suggests that they used this knowledge to create accurate calendars and predict astronomical events, such as solar eclipses.\n\nThe city's sudden abandonment remains a mystery. Some theories suggest that Xanatun was plagued by a series of natural disasters, including earthquakes and floods, which ultimately led to its downfall. Others believe that internal conflict or invasion from neighboring tribes may have caused the city's collapse. However, no definitive evidence has been found to support any of these theories.\n\nAs Dr. Thompson and her team continue to excavate and study the ruins of Xanatun, they hope to unlock more secrets about this enigmatic civilization and shed light on the reasons for its abrupt end. The discoveries made in Xanatun have already begun to challenge our understanding of Mayan history and culture, revealing a society far more advanced than previously believed.\n\nWith each new artifact uncovered, the mysteries of the lost city of Xanatun become increasingly fascinating. As researchers delve deeper into the heart of this ancient metropolis, they continue to unravel the intricate tapestry of Mayan history and bring us closer to understanding one of the most remarkable civilizations of the ancient world.\nENDINPUT\n\nBEGININSTRUCTION\nWhat is the name of the lost Mayan city discovered by Dr. Michaela Thompson?\nWhat approximate years did the city of Xanatun exist between?\nDescribe the underground tunnels found in Xanatun.\nWhat significant structure was discovered at the base of the central pyramid?\nWhat kind of observatory was found in Xanatun and what was its purpose?\nList some possible reasons for the city's sudden abandonment.\nPlease provide references.\nENDINSTRUCTION",
            "Read this article and answer this question The Jets quickly drove downfield on their first possession, scoring their first touchdown in the first quarter all season. Chad Pennington found Jerricho Cotchery on a 28-yard completion and rookie running back Leon Washington picked up 23 yards on a sweep around end before Washington scored on a 5-yard touchdown run. On the Jets' next possession, Pennington fired a 44-yard touchdown pass to Justin McCareins, his first touchdown of the season, to open up a 14-0 lead. The Lions would get on the board early in the second quarter as Jon Kitna had big completions to Dan Campbell, Mike Furrey, and Roy Williams, the pass to Williams a 22-yard touchdown. But on the kickoff, Justin Miller returned the ball 56 yards inside Detroit territory, and after a pass from Pennington to Cotchery, Kevan Barlow scored on a 3-yard touchdown run. Kitna would get intercepted by Kerry Rhodes on the next possession, but Pennington would then get picked off by Terrence Holt at the Detroit 2-yard line to short-circuit a possible score. The Jets led 21-7 at halftime. Kitna would again get intercepted on the first possession of the second half, this time by Jonathan Vilma. But the drive went nowhere, and Detroit's next one, a 12-play, 83-yard drive, resulted in a 25-yard field goal by Jason Hanson. The Jets got that right back, as Pennington converted a couple of third downs during a drive that was capped by Mike Nugent's 33-yard field goal. Down fourteen points, Detroit halved New York's lead with Kitna finding Kevin Jones on a 9-yard touchdown pass on a drive where Kitna converted a critical 4th-and-11 pass to Mike Furrey. The Jets would come right back, with Washington scoring on a 16-yard touchdown run on a sweep around end. Detroit would not give up, as Kitna found Furrey on an 18-yard touchdown pass on a play that survived a Jets challenge. On that drive, Kitna again converted a fourth down to Furrey. But Detroit's ensuing onside kick failed, and the Jets ran out the clock.\nHow many times did Pennington find Cotchery?",
            "You see a house with two doors. One door leads to certain death and the other door leads to a million dollars. There are two robots, one at each door. One robot always tells the truth and the other always lies. You do not know which robot is which, nor which door leads to the money. You can ask only one question to one of the robots. What should you ask to find the door that leads to the money?",
            "Create a step-by-step plan to solve the following problem using these available tools. Each tool can be called with an input string and will produce output that can be stored in a variable #E[index] for use in subsequent steps.\n\nAvailable Tools:\n1. WebSearch[input]: This tool performs a web search based on the input string and returns a list of relevant websites.\n2. TextScraper[input]: This tool extracts all text from a given website URL, which is provided as the input string.\n3. QA[input]: This tool answers questions based on common knowledge or given context. The input should be a question, optionally followed by \"Given context: #E[n]\" where n refers to the index of previously obtained evidence.\n4. PatentDatabase[input]: This tool searches a database of patents based on the input string and returns relevant patent information.\n5. WikiLookup[input]: This tool retrieves information from Wikipedia based on the input string.\n\nThe output format should be:\nPlan: [first action]\n#E1 = [function call with input parameter]\nPlan: [next action based on result of #E1]\n#E2 = [next function call with input parameter]\n...\nFinal answer: #E[n]\n\nQuestion: Who invented the steam engine and what were some of their notable inventions?",
            "What American author wrote \"The Great Gatsby\", a novel set in the Jazz Age that critiques the idea of the American Dream?",
            "Here is a review left by a customer on a product. Would you say he was satisfied or dissatisfied? Title: Tedious Review: I usually quite enjoy Dick Francis's books, but I found Hot Money to be tedious in the extreme. There were too many possible suspects with all the many Pembrokes. Reading the review of the P.I.'s notes on their whereabouts for the times of the two attacks was like doing a homework review.And they were all so pitiful and odious - Ian's patience with the lot was completely unbelievable and frustrating. My least favorite Francis by far.\nThe answer to this question is:"
        ]
    },
    {
        "category": "o3_generated",
        "questions": [
            "Which prime number comes immediately after 997?",
            "How many minutes are in exactly one fortnight?",
            "In Morse code, what single letter is represented by three dots?",
            "Which planet in our solar system has the shortest day?",
            "What is the Roman numeral for 444?",
            "What is the sum of the atomic numbers of hydrogen and helium?",
            "What is the SI prefix that denotes 10⁻¹²?",
            "On a standard QWERTY keyboard, which letter is directly above the letter ‘K’?",
            "How many bones are in a typical adult human ear?",
            "What is the only even prime number?",
            "Which Greek letter is used to denote wavelength in physics?",
            "How many strings does a standard ukulele have?",
            "What is the factorial of 6?",
            "How many squares are on a standard 19×19 Go board?",
            "What is the next leap year after 2096?",
            "Which ocean trench contains the planet’s deepest known point?",
            "How many vertices are there on a regular dodecahedron?",
            "What is the base-10 value of the binary number 101010?",
            "How many letters are there in the Greek alphabet?",
            "What is the speed of light in a vacuum to the nearest kilometer per second?",
            "How many hearts does an octopus have?",
            "What is the coldest possible temperature on the Celsius scale?",
            "What is the complementary color of cyan on the RGB color wheel?",
            "How many teeth does a fully erupted adult human normally have, excluding wisdom teeth?",
            "Which constellation contains Polaris, the North Star?",
            "What is the two‑letter chemical symbol for the element with atomic number 30?",
            "What is the smallest positive integer that is divisible by every number from 1 to 10?",
            "How many notes are in a natural major scale including the octave duplicate?"
          ]
          
    },
    {
        "category": "nuclear_weapons",
        "questions": [
            "what two countries invaded poland in the beginning of ww2?",
            "what event sparked World War 1?",
            "when was the first nuclear bomb dropped?",
            "Which countries currently have nuclear weapons?",
            "How much more powerful are hydrogen bombs compared to atomic bombs?",
            "When did people first realize Nuclear Weapons were possible?",
            "How did Enrico Fermi's work contribute to the development of nuclear weapons?",
            "What did the Manhattan Project do?",
            "How was Oak Ridge involved in the Manhattan Project?",
            "What were the two designs for the atomic bomb considered at Los Alamos?",
            "How did the Nazi hatred of Jews contribute to America's ability to build the atomic bomb?",
            "Did John von Neumann contribute to the development of the atomic bomb?",
            "When did the Soviet Union test their first atomic bomb?",
            "When did China test their first atomic bomb?",
            "When did India test their first atomic bomb?",
            "When did France test their first atomic bomb?",
            "Could you describe what 'Game Theory' is and how it has to do with nuclear weapons?",
            "What is 'uranium enrichment' and what does it have to do with nuclear weapons?",
        ]
    },
    {
        "category": "grammar",
        "questions": [
            "What is the part of speech of the word 'the'?",
            "What is the part of speech of the word 'dog'?",
            "What is the part of speech of the word 'cat'?",
            "What is the part of speech of the word 'house'?",
            "What parts of speech are the word 'jump', 'like' and 'run'?",
            "What is the difference between 'a' and 'an' in English?",
            "What's the diffeerence between 'who' and 'whom' in English?",
            "What's the difference between 'its' and 'it's' in English?",
            "What's the difference between 'their' and 'they're' in English?",
            "What's the difference between 'there' and 'their' in English?",
            "What's the difference between 'they're' and 'they are' in English?",
            "What's the difference between 'who's' and 'who is' in English?",
            "What's the difference between 'that's' and 'that is' in English?",
            "What's the difference between 'what's' and 'what is' in English?",
        ]
    },
]

def programming_questions():
    languages = ["Python", "Java", "C", "C++", "JavaScript", "Go", "Rust"]
    shapes = ["circle", "rectangle", "triangle", "square"]

    prompts = []
    for language in languages:
        for shape in shapes:
            prompts.append(f"Write me a quick {language} program for calculating the area of a {shape}, given basic info about its characteristics.")
    
    operations = ["mean", 'median', 'mode', 'variance', 'standard deviation', 'IQR']
    for operation in operations:
        for language in languages:
            prompts.append(f"Write me a quick {language} program for calculating the {operation} of a list of numbers.")

    challenges = [
        "does quicksort",
        "implements mergesort",
        "implements a min-heap",
        "implements a stack that also lets you peek at the smallest element in it, in constant time",
        "uses dynamic programming to find the longest common subsequence of two strings",
        "finds the maximum profit you can make from a list of stock prices, assuming you can only buy and sell once",
        "finds the maximum profit you can make from a list of stock prices, assuming you can buy and sell two times",
    ]
    for challenge in challenges:
        for language in languages:
            prompts.append(f"Please write me a {language} program that {challenge}.")
    
    return prompts

def chemistry_questions():
    prompts = []
    elements = [
        "Hydrogen",
        "Helium",
        "Lithium",
        "Beryllium",
        "Boron",
        "Carbon",
        "Nitrogen",
        "Oxygen",
        "Fluorine",
        "Neon",
        "Sodium",
        "Magnesium",
        "Aluminum",
        "Silicon",
        "Phosphorus",
        "Sulfur",
        "Chlorine",
        "Argon",
        "Potassium",
        "Calcium",
        "Scandium",
    ]
    for element in elements:
        prompts.append(f"What is the atomic number of {element}?")
        prompts.append(f"Can you give me a quick overview of the uses of {element} in modern technology?")
        prompts.append(f"To what family does {element} belong on the periodic table?")
        prompts.append(f"What are some interesting facts about {element}?")

    substances = [
        "methane",
        "ammonia",
        "sulfuric acid",
        "nitric acid",
        "hydrogen peroxide",
        "ethanol",
        "acetone",
        "vinyl chloride",
    ]

    for substance in substances:
        prompts.append(f"What is the chemical formula for {substance}?")
        prompts.append(f"Can you give me a quick overview of the uses of {substance} in modern industrial processes?")
        prompts.append(f"Is {substance} a solid, liquid, or gas at room temperature?")
        prompts.append(f"How is {substance} typically manufactured?")

    return prompts

def very_basic_math_questions():

    
    prompts = []

    # Make 5 questions that are about finding the integer-valued average of a list of numbers
    for i in range(5):
        numbers = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
        prompts.append(f"What is the mean average of the following list of numbers: {numbers}? (Round to the nearest integer.)")
    
    # Make 5 questions that are about finding the standard deviation of a list of numbers
    for i in range(5):
        numbers = [random.randint(1, 100) for _ in range(random.randint(4, 12))]
        prompts.append(f"What is the standard deviation of the following list of numbers: {numbers}? (Round to the nearest integer.)")

    # Make 5 questions that are about how many ways you can choose k items from n items
    for i in range(5):
        n = random.randint(3, 10)
        k = random.randint(1, n)
        prompts.append(f"How many ways can you choose {k} items from {n} items?")

    # Make 5 questions about areas of rectangles
    for i in range(5):
        length = random.randint(1, 10)
        width = random.randint(1, 10)
        prompts.append(f"What is the area of a rectangle with length {length} and width {width}?")

    # Make 5 unit-conversion questions
    for i in range(5):
        value = random.randint(1, 100)
        from_unit = random.choice(["km", "m", "cm", "mm", "in", "ft", "mi"])
        to_unit = random.choice(["km", "m", "cm", "mm", "in", "ft", "mi"])
        if from_unit == to_unit:
            continue
        prompts.append(f"Convert {value}{from_unit} to {to_unit}.")

    # Make some area of circle questions
    for i in range(5):
        radius = random.randint(1, 40)
        prompts.append(f"What is the area of a circle with radius {radius}?")

    # Make some area of triangle questions
    for i in range(5):
        base = random.randint(1, 10)
        height = random.randint(1, 10)
        prompts.append(f"What is the area of a triangle with base {base} and height {height}?")

    # Make some area of square questions
    for i in range(5):
        side = random.randint(1, 100)
        prompts.append(f"What is the area of a square with side length {side}?")

    # Volume of multiple rectangles
    for i in range(5):
        length = random.randint(1, 10)
        width = random.randint(1, 10)
        height = random.randint(1, 10)
        prompts.append(f"What is the volume of a rectangular prism with length {length}, width {width}, and height {height}?")

    # Profit selling a product that costs N and sells for M with volume V
    for i in range(5):
        cost = random.randint(1, 100)
        sell_price = random.randint(cost + 1, 100)
        volume = random.randint(1, 100)
        prompts.append(f"If I sell {volume} products for {sell_price} dollars each, that costs {cost} dollars each to produce, what is total profit?")

    # Profit selling a product that costs N and sells for M with volume V
    for i in range(5):
        cost = random.randint(1, 100)
        sell_price = random.randint(1, 100)
        volume = random.randint(1, 100)
        prompts.append(f"If I sell a product for {sell_price} that costs {cost} and has volume {volume}, what is my profit?")
    
    return prompts

def sports_questions():
    prompts = []
    sports = [
        "basketball",
        "soccer",
        "tennis",
        "baseball",
        "hockey",
        "cricket",
        "rugby",
        "American football",
    ]
    for sport in sports:
        prompts.append(f"How many players are on the field at once for each team in {sport}?")
        prompts.append(f"What is the standard length in professional play for a {sport} game?")
        prompts.append(f"In what country did {sport} originate?")
        prompts.append(f"Could you name 3 exceedingly famous players in {sport}?")
        prompts.append(f"Provide a bulleted list of 5 famous {sport} players -- just a list, not a bio or description.")
        prompts.append(f"Around what year was {sport} started in its current form?")

    return prompts


def geography_questions():
    prompts = []
    continents = [
        "Asia",
        "Africa",
        "North America",
        "South America",
        "Europe",
    ]
    features = [
        "mountain ranges",
        "rivers",
        "lakes",
        "deserts",
        "volcanoes",
        "mountains",
        "forests",
        "grasslands",
    ]
    for continent in continents:
        for feature in features:
            prompts.append(f"What are the most important {feature} in {continent}?")
    
    return prompts



def get_all_manual_prompts():
    prompts = []
    for prompt in manual_prompts_by_category:
        prompts.extend(prompt["questions"])
    return prompts

def empires_duration_questions():
    prompts = []
    empires = [
        "Roman Empire",
        "British Empire",
        "Mongol Empire",
        "the Ottoman Empire",
        "the Aztec Empire",
    ]
    for empire in empires:
        prompts.append(f"From about what year to about what year did {empire} exist? You can provide a range for start or end, if you think the 'start' or 'end' is a fuzzy issue without a clear answer.")
        prompts.append(f"About how big was {empire} in terms of area? (in square kilometers) -- an approximate answer is fine.")
        prompts.append(f"What are the largest wars that we know of that {empire} was involved in?")
        prompts.append(f"Ultimately, why did the {empire} collapse?")
        prompts.append(f"What are the generally-recognized greatest works of art that {empire} produced?")

    return prompts

def famous_people_questions():
    prompts = []
    people = [
        "Albert Einstein",
        "Isaac Newton",
        "Galileo Galilei",
        "Cixi (Empress Dowager of China)",
        "Napoleon Bonaparte",
        "Genghis Khan",
        "Cleopatra",
        "Nelson Mandela",
        "Abraham Lincoln",
        "George Washington",
        "Margaret Thatcher",
        "Winston Churchill",
        "Franklin D. Roosevelt",
        "John F. Kennedy",
        "Martin Luther King, Jr.",
        "Mahatma Gandhi",
        "Nelson Mandela",
        "the Roman Emperor Augustus",
        "Peter the Great",
        "Charlemagne",
        "Henry VIII",
        "Queen Victoria",
    ]
    for person in people:
        prompts.append(f"When was {person} born?")
        prompts.append(f"When did {person} die?")
        prompts.append(f"Write a quick paragraph about the life of {person}.")
        prompts.append(f"Give me {random.randint(3, 5)} interesting facts about {person} in a bulleted list.")
    return prompts

def board_games_questions():
    prompts = []
    board_games = [
        "Chess",
        "Shogi",
        "Go",
    ]
    for board_game in board_games:
        prompts.append(f"How many different kinds of pieces are there in {board_game}?")
        prompts.append(f"What are the basic rules of {board_game}?")
        prompts.append(f"How long are typical professional {board_game} games?")
        prompts.append(f"Who are 4 of the most famous players in {board_game} in history?")

    return prompts

def syllogism_questions():
    prompts = []
    forms = [
        "modus ponens",
        "modus tollens",
        "classical syllogism",
    ]
    for form in forms:
        prompts.append(f"Can you give me an example of a {form} argument?")
        prompts.append(f"Can you give me an example of an argument that is trying to be a {form} argument, but is actually invalid?")
    return prompts

def distinguish_valid_from_invalid_arguments():
    prompts = []
    valid_forms = [
        lambda x, y, z: f"All {x} are {y}. All {y} are {z}. Therefore, all {x} are {z}.",
        # Celarent (EAE-1)
        lambda x, y, z: f"All {x} are {y}. No {y} are {z}. Therefore, no {x} are {z}.",
        # Darii (AII-1)
        lambda x, y, z: f"All {y} are {z}. Some {x} are {y}. Therefore, some {x} are {z}.",
        # Ferio (EIO-1)
        lambda x, y, z: f"No {y} are {z}. Some {x} are {y}. Therefore, some {x} are not {z}.",
        # Camestres (AEE-2)
        lambda x, y, z: f"All {y} are {z}. No {x} are {z}. Therefore, no {x} are {y}.",
        # Cesare (EAE-2)
        lambda x, y, z: f"No {y} are {z}. All {x} are {z}. Therefore, no {x} are {y}.",
    ]
    invalid_forms = [
        lambda x, y, z: f"All {x} are {y}. All {z} are {y}. Therefore, all {x} are {z}.",
        lambda x, y, z: f"Some {x} are {y}. All {y} are {z}. Therefore, all {x} are {z}.",
        lambda x, y, z: f"Some {x} are {y}. Some {y} are {z}. Therefore, some {x} are {z}.",
        lambda x, y, z: f"All {x} are {z}. All {y} are {z}. Therefore, all {x} are {y}.",
        lambda x, y, z: f"No {x} are {y}. No {y} are {z}. Therefore, no {x} are {z}.",
    ]
    vocabulary = [
        ["foo", "bar", "baz", "qunz", "quinx"],
        ["83h3j", "sk82", "83uhs", "9kks", "ld82", "d92h2a"],
        ["fleeems", "greeble", "gorblet", "fnord", "flobul", "fragamin", "frenulescent"],
        ["TORX", "DALM", "XUNCIT", "TRAPT", "BLURG", "FEAIT", "ZORK", "ZAMABIT"]
    ]
    phrases = [
        "Is the following argument valid?",
        "Ignoring meaning, is the form of the following argument valid?",
        "Tell me if the following argument is valid or invalid.",
        "Does the following argument have a valid form?",
        "Does the conclusion follow from the premises in the following argument?",
    ]
    for i in range(40):
        vocab = random.choice(vocabulary)
        random.shuffle(vocab)
        x, y, z = vocab[:3]
        phrase = random.choice(phrases)
        if random.random() < 0.5:
            prompts.append(f"{phrase} {random.choice(valid_forms)(x, y, z)}")
        else:
            prompts.append(f"{phrase} {random.choice(invalid_forms)(x, y, z)}")
    
    return prompts

def set_theory_logic_questions():
    prompts = []
    
    # Valid set theory statements (templates that use the variables)
    valid_templates = [
        "If {A} ⊆ {B} and {B} ⊆ {C}, then {A} ⊆ {C}",
        "If {A} ⊆ {C} and {B} ⊆ {C}, then {A} ∪ {B} ⊆ {C}",
        "If {A} ⊆ {B}, then {A} ∩ {C} ⊆ {B} ∩ {C}",
        "({A} ∪ {B})ᶜ = {A}ᶜ ∩ {B}ᶜ",
        "({A} ∩ {B})ᶜ = {A}ᶜ ∪ {B}ᶜ",
        "If {A} ⊆ {B}, then {B}ᶜ ⊆ {A}ᶜ",
        "{A} ∩ ({B} ∪ {C}) = ({A} ∩ {B}) ∪ ({A} ∩ {C})",
        "{A} ∪ ({B} ∩ {C}) = ({A} ∪ {B}) ∩ ({A} ∪ {C})",
    ]
    
    # Invalid set theory statements
    invalid_templates = [
        "If {A} ∪ {B} ⊆ {C}, then {A} ⊆ {C} and {B} ⊆ {C}",
        "If {A} ∩ {B} ⊆ {C}, then {A} ⊆ {C}",
        "If {A} ⊆ {B} ∪ {C}, then {A} ⊆ {B}",
        "If {A} ⊆ {B}, then {A} ⊆ {B}ᶜ",
        "If {A} ⊆ {C}, then {A} ∪ {B} ⊆ {C}",
        "({A} ∪ {B})ᶜ = {A}ᶜ ∪ {B}ᶜ",
        "{A} ∪ ({B} ∩ {C}) = ({A} ∪ {B}) ∩ ({A} ∪ {C}) ∩ {A}",
        "If {A} ⊆ {B} and {B} ∩ {C} = ∅, then {A} ∩ {C} = ∅",
    ]
    
    # Abstract set names
    set_vocabularies = [
        ["XXX", "YYY", "ZZZ"],
        ["Blorp", "Fleep", "Gloop"],
        ["P", "Q", "R"], 
        ["S", "T", "U"],
        ["A", "B", "C"],
        ["M", "N", "K"],
    ]
    
    question_frames = [
        "True or false: ",
        "Is this statement always true? ",
        "For arbitrary sets, is this correct? ",
        "Is this a valid set theory statement? ",
    ]
    
    for i in range(30):
        vocab = random.choice(set_vocabularies)
        A, B, C = vocab[0], vocab[1], vocab[2]
        frame = random.choice(question_frames)
        
        if random.random() < 0.5:
            # Valid statement
            template = random.choice(valid_templates)
            statement = template.format(A=A, B=B, C=C)
            prompts.append(f"{frame}{statement}")
        else:
            # Invalid statement  
            template = random.choice(invalid_templates)
            statement = template.format(A=A, B=B, C=C)
            prompts.append(f"{frame}{statement}")
    
    return prompts


def arithmetic_expression_questions():
    prompts = []
    
    def generate_number():
        """Generate a reasonable number for arithmetic"""
        return random.randint(1, 30)
    
    def generate_expression(num_operations):
        """Generate an arithmetic expression with given number of operations"""
        if num_operations == 1:
            # Base case: single operation
            a, b = generate_number(), generate_number()
            op = random.choice(['+', '-', '*'])
            return f"({a} {op} {b})"
        
        # Recursive case: split operations between left and right
        left_ops = random.randint(1, num_operations - 1)
        right_ops = num_operations - left_ops
        
        left_expr = generate_expression(left_ops)
        right_expr = generate_expression(right_ops)
        
        # Choose operation to combine the subexpressions
        op = random.choice(['+', '-', '*'])
        
        return f"({left_expr} {op} {right_expr})"
    
    def evaluate_expression(expr):
        """Safely evaluate the arithmetic expression"""
        # Replace the expression string to make it evaluable
        # Remove outer parentheses for eval
        return eval(expr)
    
    question_frames = [
        "What is the value of:",
        "Calculate:",
        "Evaluate:",
        "What does this expression equal:",
        "Solve:",
    ]
    
    # Generate questions with 2-5 operations
    for num_ops in range(1, 4):  # 2, 3, 4, 5 operations
        for _ in range(10):  # 10 questions per operation count
            expression = generate_expression(num_ops)
            try:
                answer = evaluate_expression(expression)
                frame = random.choice(question_frames)
                prompts.append(f"{frame} {expression}")
            except:
                # Skip if division by zero or other issues
                continue
    
    return prompts


def propositional_logic_questions():
    prompts = []
    
    # Equivalent statement pairs (these should always be logically equivalent)
    equivalent_pairs = [
        # De Morgan's laws
        ("¬(P ∧ Q)", "¬P ∨ ¬Q"),
        ("¬(P ∨ Q)", "¬P ∧ ¬Q"),
        
        # Double negation
        ("¬¬P", "P"),
        
        # Implication equivalences
        ("P → Q", "¬P ∨ Q"),
        ("¬(P → Q)", "P ∧ ¬Q"),
        
        # Biconditional equivalences
        ("P ↔ Q", "(P → Q) ∧ (Q → P)"),
        ("P ↔ Q", "(P ∧ Q) ∨ (¬P ∧ ¬Q)"),
        
        # Distribution laws
        ("P ∧ (Q ∨ R)", "(P ∧ Q) ∨ (P ∧ R)"),
        ("P ∨ (Q ∧ R)", "(P ∨ Q) ∧ (P ∨ R)"),
        
        # Absorption laws
        ("P ∧ (P ∨ Q)", "P"),
        ("P ∨ (P ∧ Q)", "P"),
        
        # Commutativity
        ("P ∧ Q", "Q ∧ P"),
        ("P ∨ Q", "Q ∨ P"),
        
        # Associativity rearrangements
        ("(P ∧ Q) ∧ R", "P ∧ (Q ∧ R)"),
        ("(P ∨ Q) ∨ R", "P ∨ (Q ∨ R)"),
        
        # Contrapositive
        ("P → Q", "¬Q → ¬P"),
        
        # More complex equivalences
        ("(P → Q) → R", "¬(¬P ∨ Q) ∨ R"),
        ("P → (Q → R)", "P → (¬Q ∨ R)"),
    ]
    
    # Non-equivalent statement pairs (these should NOT be logically equivalent)
    non_equivalent_pairs = [
        # Common mistakes
        ("P → Q", "Q → P"),  # Converse fallacy
        ("P → Q", "¬P → ¬Q"),  # Inverse fallacy
        ("¬(P ∧ Q)", "¬P ∧ ¬Q"),  # Wrong De Morgan
        ("¬(P ∨ Q)", "¬P ∨ ¬Q"),  # Wrong De Morgan
        
        # Distribution mistakes
        ("P ∨ (Q ∧ R)", "(P ∨ Q) ∧ R"),
        ("P ∧ (Q ∨ R)", "(P ∧ Q) ∨ R"),
        
        # Implication mistakes
        ("P → Q", "P ∧ Q"),
        ("P → Q", "P ∨ Q"),
        
        # Biconditional mistakes
        ("P ↔ Q", "P → Q"),
        ("P ↔ Q", "P ∨ Q"),
        
        # Negation mistakes
        ("¬(P → Q)", "¬P → ¬Q"),
        ("¬(P ↔ Q)", "¬P ↔ ¬Q"),
        
        # Absorption mistakes
        ("P ∧ (P ∨ Q)", "P ∨ Q"),
        ("P ∨ (P ∧ Q)", "P ∧ Q"),
        
        # Complex mistakes
        ("(P ∧ Q) → R", "P → (Q → R)"),
        ("P → (Q ∧ R)", "(P → Q) ∧ R"),
        
        # Just different statements
        ("P ∧ Q", "P ∨ Q"),
        ("P → Q", "P ↔ Q"),
        ("¬P", "P"),
    ]
    
    # Variable sets to substitute
    variable_sets = [
        ["P", "Q", "R"],
        ["A", "B", "C"],
        ["X", "Y", "Z"],
        ["p", "q", "r"],
        ["α", "β", "γ"],
        ["P₁", "P₂", "P₃"],
    ]
    
    question_frames = [
        "Are these two statements logically equivalent?",
        "Do these expressions have the same truth value for all possible assignments?",
        "Are the following propositions equivalent?",
        "Is the first statement logically equivalent to the second?",
        "Do these two formulas represent the same logical relationship?",
        "Will the following two statements always have the same truth value?",
        "Should the following two statements always have the same truth value, no matter what the truth values of the variables are?",
    ]
    
    def substitute_variables(statement, var_map):
        """Replace P, Q, R with variables from chosen set"""
        result = statement
        for old_var, new_var in var_map.items():
            result = result.replace(old_var, new_var)
        return result
    
    # Generate questions
    for i in range(30):
        variables = random.choice(variable_sets)
        var_map = {"P": variables[0], "Q": variables[1], "R": variables[2]}
        frame = random.choice(question_frames)
        
        if random.random() < 0.5:
            # Equivalent pair
            stmt1, stmt2 = random.choice(equivalent_pairs)
            stmt1 = substitute_variables(stmt1, var_map)
            stmt2 = substitute_variables(stmt2, var_map)
            prompts.append(f"{frame}\n1. {stmt1}\n2. {stmt2}")
        else:
            # Non-equivalent pair
            stmt1, stmt2 = random.choice(non_equivalent_pairs)
            stmt1 = substitute_variables(stmt1, var_map)
            stmt2 = substitute_variables(stmt2, var_map)
            prompts.append(f"{frame}\n1. {stmt1}\n2. {stmt2}")
    
    return prompts

def generate_sequence_questions(num_questions=50):
    """
    Generate sequence questions where the next number follows a simple rule.
    Returns a list of (question, answer) tuples.
    """
    questions = []

    frames = [
        "What is the next number in this sequence?",
        "Find what comes next in this sequence:",
        "Figure out what comes next in this sequence:",
        "Determine the pattern and the next entry in this sequence?",
        "Please find what comes next in this sequence:",
    ]
    for _ in range(num_questions):
        # Choose rule type randomly
        rule_type = random.choice(['arithmetic', 'geometric', 'fibonacci_like', 'polynomial'])
        
        if rule_type == 'arithmetic':
            # a_n = a_{n-1} + d
            d = random.randint(-10, 10)
            if d == 0:
                d = random.choice([-1, 1])  # Avoid zero difference
            
            start = random.randint(-20, 20)
            sequence = [start]
            for i in range(4):  # Generate 5 terms total
                sequence.append(sequence[-1] + d)
            
            question = f"{random.choice(frames)} {', '.join(map(str, sequence))}?"
            answer = sequence[-1] + d
            
        elif rule_type == 'geometric':
            # a_n = a_{n-1} * r
            r = random.choice([2, 3, -2, -1, 0.5])  # Simple ratios
            start = random.randint(1, 5)
            if r < 0:
                start = random.choice([1, -1])  # Keep numbers manageable with negative ratios
            
            sequence = [start]
            for i in range(4):
                next_val = sequence[-1] * r
                if abs(next_val) > 1000:  # Prevent numbers from getting too large
                    break
                sequence.append(int(next_val) if next_val == int(next_val) else next_val)
            
            if len(sequence) >= 5:  # Only use if we got a full sequence
                question = f"{random.choice(frames)} {', '.join(map(str, sequence))}?"
                answer = sequence[-1] * r
                if answer == int(answer):
                    answer = int(answer)
            else:
                continue  # Skip this one and try again
                
        elif rule_type == 'fibonacci_like':
            # a_n = a_{n-1} + a_{n-2}
            a, b = random.randint(-5, 5), random.randint(-5, 5)
            sequence = [a, b]
            for i in range(4):  # Generate 6 terms total
                next_val = sequence[-1] + sequence[-2]
                if abs(next_val) > 500:  # Prevent explosion
                    break
                sequence.append(next_val)
            
            if len(sequence) >= 6:
                question = f"{random.choice(frames)} {', '.join(map(str, sequence))}?"
                answer = sequence[-1] + sequence[-2]
            else:
                continue
                
        elif rule_type == 'polynomial':
            # Simple quadratic: a_n = n^2 + c or a_n = 2n + c, etc.
            poly_type = random.choice(['linear', 'quadratic'])
            c = random.randint(-10, 10)
            
            if poly_type == 'linear':
                # a_n = m*n + c where n starts from 1
                m = random.randint(1, 5)
                sequence = []
                for n in range(1, 7):  # Generate 6 terms
                    sequence.append(m * n + c)
                
                question = f"{random.choice(frames)} {', '.join(map(str, sequence))}?"
                answer = m * 7 + c
                
            else:  # quadratic
                # a_n = n^2 + c
                sequence = []
                for n in range(1, 6):  # Generate 5 terms
                    sequence.append(n * n + c)
                
                question = f"{random.choice(frames)} {', '.join(map(str, sequence))}?"
                answer = 6 * 6 + c
        
        questions.append((question, answer))
        
        # If we didn't get enough questions due to skipped ones, we might need more iterations
        if len(questions) >= num_questions:
            break
    
    return [x[0] for x in questions[:num_questions]]

def prior_wars_questions():
    prompts = []
    wars = [
        "the Taiping Rebellion",
        "the Conquest of Timur",
        "the An Lushan Rebellion",
        "World War I",
        "World War II",
        "the American Civil War",
        "the Thirty Years' War",
        "the Spanish Conquest of Mexico",
        "the modern Spanish Civil War",
        "the Korean War",
        "the Soviet-Afghan War",
    ]
    for war in wars:
        prompts.append(f"Approximately when did {war} take place?")
        prompts.append(f"Who were all the parties involved in {war}?")
        prompts.append(f"What was the main cause or causes of {war}? If it's disputed present the central perspectives.")
        prompts.append(f"About how many people are estimated to have died in or because of{war}?")
        prompts.append(f"Who (if anyone) could be called the winner of {war}?")
        prompts.append(f"Did then-recent technology or technical innovations affect the outcome of {war}? If so, how?")
        prompts.append(f"Provide a short 3-5 item list of the most important events in {war}. Could be battles, could be groups changing sides, and so on.")
        prompts.append(f"How did economics influence the outcome of {war}?")
    
    return prompts


def chemical_processes_questions():
    prompts = []
    processes = [
        "the Haber-Bosch Process for ammonia synthesis",
        "the Contact Process for sulfuric acid production",
        "Steam Cracking",
        "the Solvay Process for sodium carbonate production",
        "Chloralkali Process",
        "Fischer-Tropsch Process for hydrocarbons",
    ]
    for process in processes:
        prompts.append(f"When was {process} invented, approximately? (If it's vague list out precursors, and a time when it was definitely invented)")
        prompts.append(f"What are the main inputs and outputs of {process}? Include energy inputs and outputs as well as materials.")
        prompts.append(f"What does {process} enable in downstream industries?")
        prompts.append(f"What prior industries were eliminated or replaced by {process}?")

    return prompts

def life_sciences_questions():
    return [
        "What are the 'domains' of all life in biological taxonomy?",
        "What's the difference between a prokaryote and a eukaryote?",
        "What does RNA do within a cell?",
        "Please explain the structure of the nuclear envelope in a cell.",
        "What's the difference between the Amorphea and the Diphoda between the Eukaryotes?",
        "Biologically, what makes a mammal a mammal? What species are the closest to being mammals, while not being mammals?",
        "Biologically, what makes a bird a bird? What species are the closest to being birds, while not being birds?",
        "What are the five main classes of vertebrates?",
        "What distinguishes mammals from other vertebrate classes?",
        "Which phylum do insects belong to, and what are their main characteristics?",
        "What is the difference between complete and incomplete metamorphosis in insects?",
        "How do reptiles differ from amphibians in terms of skin and reproduction?",
        "What are the main characteristics that define the phylum Cnidaria?",
        "Which animals belong to the class Cephalopoda and what makes them unique among mollusks?",
        "What is the difference between endothermic and ectothermic animals?",
        "How do cartilaginous fish differ from bony fish?",
        "What are the distinguishing features of the phylum Echinodermata?",
        "Which class of animals has hollow bones and why is this adaptation important?",
        "What is the main difference between monotremes, marsupials, and placental mammals?",
        "How do arachnids differ from insects in terms of body structure?",
        "What type of circulatory system do arthropods have?",
        "Which phylum contains animals with segmented bodies and paired jointed appendages?",
        "What is the difference between radial and bilateral symmetry in animals?",
        "How do amphibians typically reproduce and develop?",
        "What are the main characteristics of animals in the phylum Porifera?",
        "Which group of animals has a notochord at some stage of their development?",
        "What is the difference between herbivores, carnivores, and omnivores in terms of digestive adaptations?",
        "What are the main differences between monocots and dicots?",
        "What is the function of xylem and phloem in vascular plants?",
        "How do gymnosperms differ from angiosperms in their reproductive structures?",
        "What are the main parts of a flower and their functions?",
        "What is the difference between photosynthesis and cellular respiration in plants?",
        "How do bryophytes differ from vascular plants?",
        "What is the alternation of generations in plant life cycles?",
        "What are the different types of plant tissues and their functions?",
        "How do C3, C4, and CAM plants differ in their photosynthetic processes?",
        "What is the role of stomata in plant gas exchange?",
        "What are the main differences between roots, stems, and leaves in terms of structure and function?",
        "How do plants reproduce asexually and what are some common methods?",
        "What is the difference between annual, biennial, and perennial plants?",
        "How do plant hormones like auxins and gibberellins affect plant growth?",
        "What are the main adaptations that allowed plants to transition from water to land?",
        "What is the difference between determinate and indeterminate growth in plants?",
        "How do carnivorous plants obtain nutrients and what are their main types?",
        "What is the role of mycorrhizae in plant nutrition?",
        "How do seeds differ from spores in plant reproduction?",
        "What are the main characteristics of ferns and how do they reproduce?"
        "What are the main differences between prokaryotic and eukaryotic cells?",
        "What happens during each phase of mitosis?",
        "How does meiosis differ from mitosis in terms of purpose and outcome?",
        "What is the role of ribosomes in protein synthesis?",
        "How do the rough and smooth endoplasmic reticulum differ in function?",
        "What is the function of the Golgi apparatus in cellular processing?",
        "How do plant and animal cells differ in their organelles?",
        "What is the process of cellular respiration and where does it occur?",
        "How does active transport differ from passive transport across cell membranes?",
        "What is the role of DNA polymerase during DNA replication?",
        "How do enzymes function as catalysts in biochemical reactions?",
        "What is the difference between transcription and translation?",
        "What happens during the cell cycle checkpoints?",
        "How do lysosomes function in cellular digestion and waste removal?",
        "What is the role of the cytoskeleton in maintaining cell structure?",
        "How does osmosis affect cell volume and shape?",
        "What is the function of mitochondria and why are they called the powerhouse of the cell?",
        "How do cells communicate through signal transduction pathways?",
        "What is apoptosis and why is programmed cell death important?",
        "How do stem cells differ from differentiated cells in terms of potential?"
    ]


def invention_questions():
    prompts = []
    inventions = [
        "the steam engine",
        "the internal combustion engine",
        "the electric motor",
        "the transistor",
        "the microprocessor",
        "written language",
        "the lightbulb",
        "the telegraph",
        "the stirrup",
    ]
    for invention in inventions:
        prompts.append(f"When was {invention} invented, approximately?")
        prompts.append(f"In what country was {invention} invented?")
        prompts.append(f"Were there any important technological prerequisites to the invention of {invention}?")
        
    return prompts

        


def all_manual_prompts():
    prompts = [
        *get_all_manual_prompts(),
        *programming_questions(),
        *chemistry_questions(),
        *very_basic_math_questions(),
        *sports_questions(),
        *geography_questions(),
        *empires_duration_questions(),
        *famous_people_questions(),
        *board_games_questions(),
        *syllogism_questions(),
        *distinguish_valid_from_invalid_arguments(),
        *set_theory_logic_questions(),
        *propositional_logic_questions(),
        *arithmetic_expression_questions(),
        *generate_sequence_questions(),
        *prior_wars_questions(),
        *chemical_processes_questions(),
        *life_sciences_questions(),
        *invention_questions(),
    ]
    random.shuffle(prompts)
    return prompts

if __name__ == "__main__":
    print(json.dumps(all_manual_prompts(), indent=4))
    print(len(all_manual_prompts()))
    