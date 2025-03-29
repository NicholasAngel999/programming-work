print("Happy Mother's Day")

print("Your the best mum ever! Here's a quiz to remember some amazing holiday memories")

print('''FYI! when writing your answers please keep everything lower case and dont put a
      space at the end! If your answer is obviously right but it comes back wrong it
      will be a syntax error just note it down for later. once your done you can open 
      the other file i have sent you and you can look at the code and see all the right answers''')

print(' Are you ready!')

import time

score = 0

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(i, end="...\n", flush=True)
        time.sleep(1)

while True:
    start = input("type 'yes' to continue: ").strip().lower()
    if start =="yes":
        print('Starting the quiz...')
        break # Exit the loop and start the quiz
    else:
        print("Try Again.")

while True:
    countdown(3)
    Question_1 = input("what was my favourite Holiday? ").strip().lower()
    if Question_1 == "florida":
        print("Yes! 1 point!")
        score += 1
        break # Exit the loop go to question_2
    else:
        print("Oooh no! It was Florida! No points")
        break # Exit the loop go to question_2
    

while True:
    countdown(3)
    question_2 = input("what was my favourite park at Disney World in Florida? ").strip().lower()
    if question_2 == "hollywood studios":
        print("Great Job! 1 Point!")
        score += 1
        break
    else:
        print("Good Guess! No Points")
        break


while True:
    countdown(3)
    question_3 = input("Which of our 3 visits to the USA was my favourite? Please answer either 1 2 or 3 ").strip().lower()
    if question_3 == "1":
        print("Yess! It was a great first experience 1 Point!")
        score += 1
        break
    else:
        print("It could have been any of them it was hard to decide. 0 Points")
        break


while True:
    countdown(3)
    question_4 = input("What was my Favourite ride throughout all of the Disney Parks in Florida? ").strip().lower()
    if question_4 == "tower of terror" or "the tower of terror":
        print("It was a great ride! Especially with Kirsty. 1 Point!")
        score += 1
        break
    else:
        print("close but not quite. 0 Points")
        break


while True:
    countdown(3)
    question_5 = input("which was my favourite universal studios park? florida or california? ").strip().lower()
    if question_5 == "florida":
        print("It was close but still florida")
        score += 1
        break
    else:
        print("you had a 50/50!")
        break


while True:
    countdown(3)
    q_6 = input("look at image help yeti, and tell me what ride we were in the queue for when we saw this? ").strip().lower()
    if q_6 == "expedition everest":
        print("amazing memory")
        score += 1
        break
    else:
        print("that was a tough one")
        break

while True:
    countdown(3)
    q_7 = input("do you remember which park that ride was from? ").strip().lower()
    if q_7 == "animal kingdom":
        print("tough one")
        score += 1
        break
    else:
        print("it could have been loads")
        break


while True:
    countdown(3)
    q_8 = input("Which of the four swimming pools was the best at the art of animation? ").strip().lower()
    if q_8 == "finding nemo":
        score += 1
        break
    else:
        print("cars was a close second for the cones")
        break


while True:
    countdown(3)
    q_9 = input("on the 27th of october we went to the chocolate emporium. What milkshake did i get and which did mum get? ").strip().lower()
    if q_9 == "chocolate brownie red velvet" or "chocolate brownie and red velvet":
        score += 1 
        break
    else:
        print("even i may be wrong here")
        break


while True:
    countdown(3)
    q_10 = input("before the chocolate emporium we were in universal what ride caused mum to get a new shirt? just use character name. ").strip().lower()
    if q_10 == "popeye":
        score += 1
        break
    else:
        print("how do you forget that!")
        break


while True:
    countdown(3)
    q_11 = input("what did mum do to annoy one of the toy soldiers whilst trying to take pictures? ").strip().lower()
    if q_11 == "stand on his feet":
        print("so many times")
        score += 1
        break
    else: 
        print("that felt like an easy one")
        break


while True:
    countdown(3)
    q_12 = input("look at the attached q 12 help file. Where was this picture taken? ").strip().lower()
    if q_12 == "durham":
        print("yes! do you remember the bus questions?")
        score += 1
        break
    else:
        print("How do you forget?")
        break

while True:
    countdown(3)
    q_13 = input("whos harry potter room was in here? ").strip().lower()
    if q_13 == "mcgonagall":
        print("easy!")
        score += 1
        break
    else:
        print("i basically gave you a point!")
        break

while True:
    countdown(3)
    q_14 = input("in York in 2018, who won the clay pigeon shoot out? ").strip().lower()
    if q_14 == "cole":
        print("yes i did")
        score += 1
        break
    else:
        print("Dont Lie!")
        break

while True:
    countdown(3)
    q_15 = input('''on the 28th of october 2018 what nfl game did we watch? 
                 name the two teams - answer with "team vs team" ''').strip().lower()
    if q_15 == "jags vs eagles" or "jacksonville vs philidelphia" or "jaguars vs eagles" or "jacksonville jaguars vs philidelphia eagles" or "eagles vs jags" or "philidelphia vs jacksonville" or "eagles vs jaguars" or "philidelphia eagles vs jacksonville jaguars":
        print("what a game!")
        score += 1
        break
    else:
        print("it was a great day and it was your team!")
        break

while True:
    countdown(3)
    q_16 = input("where else did we go on that trip? ").strip().lower()
    if q_16 == "wizarding world" or "harry potter studio" or "harry potter":
        print("yes! and i got some chocolate!")
        score += 1
        break
    else:
        print("aw howd you forget!")
        break

while True:
    countdown(3)
    q_17 =input("where did mum and i take esme in june of 2019? ").strip().lower()
    if q_17 == "roche abbey":
        print("we even found a little waterfall")
        score += 1 
        break
    else:
        print("not a holiday but it was a fun day")
        break

while True:
    countdown(3)
    q_18 = input("where did me and mum go mountain biking in august of 2019? ").strip().lower()
    if q_18 == "kielder forrest" or "cresswell towers":
        print("was a pretty cool diamond back")
        score += 1 
        break
    else:
        print("how can you forget that day we got lost")
        break

while True:
    countdown(3)
    q_18 = input("what hotel did we stay in at california? ").strip().lower()
    if q_18 == "knotts berry farm" or "knotts farm" or "knott's farms":
        print("easy")
        score += 1
        break
    else:
        print("come on")
        break

while True:
    countdown(3)
    q_19 = input("what was the best find of the first day? ").strip().lower()
    if q_19 == "johnny rockets" or "snoopy" or "finding johnny rockets" or "finding snoopy":
        print("obviously!")
        score += 1 
        break
    else:
        print("i even gave you two possible answers")
        break

while True:
    countdown(3)
    q_20 = input("what ride did we go on after meeting mike wazowski? ").strip().lower()
    if q_20 == "ferris wheel":
        print("stepping up now")
        score += 1 
        break
    else:
        print("getting harder")
        break

while True:
    countdown(3)
    q_21 = input("What did me and abbey have for breakfast in the hotel? ").strip().lower()
    if q_21 == "pancakes":
        print("they were massive!!!")
        score += 1
        break
    else:
        print("they were massive pancakes!")
        break

while True:
    countdown(3)
    q_22 = input('''where can the entrance to dumbledores office be found in universal'
    'studios hollywood''').strip().lower()
    if q_22 == "the forbidden journey" or "harry potter and the forbidden journey":
        print("that one was crazy hard")
        score += 1 
        break
    else:
        print("i didnt expect you to know that")
        break

while True:
    countdown(3)
    q_23 = input("what date did we go to watch the ice hockey? ").strip().lower()
    if q_23 == "29th october" or "29 october" or "29 oct" or "29th oct":
        print("amazing day!")
        score += 1
        break
    else:
        print("can you get the next one?")
        break

while True:
    countdown(3)
    q_24 = input("what was the final score of the game? please write highest score - lowest score").strip().lower()
    if q_24 == "7-4" or "7 - 4":
        print("at least you got that one")
        score += 1
        break
    else:
        print(":(")
        break

while True:
    countdown(3)
    q_25 = input('''what was the date we set off from england headed for holland?'
    'please format your answer to be 25 february 2025''').strip().lower()
    if q_25 == "14 july 2023":
        print("great")
        score += 1 
        break
    else:
        print("that one was recent")
        break

while True:
    countdown(3)
    q_26 = input('''we took a river boat ride through bruges with nana and grandpa.'
    'what did nana keep doing at every bridge? ''').strip().lower()
    if q_26 == "ducking" or "crouching" or "bedning over":
        print("it was very amusing")
        score += 1 
        break
    else:
        print("how do you forget her ducking!")
        break

while True:
    countdown(3)
    q_27 = input("what happened to dads shorts in brugges? ").strip().lower()
    if q_27 == "ripped":
        print("hahaha")
        score += 1 
        break 
    else:
        print("no way you forgot!")
        break

while True:
    countdown(3)
    q_28 = input("what did we do on the 21 july 2023? ").strip().lower()
    if q_28 == "big bike ride" or "long bike ride" or "cycle for a day" or "cycle" or "long day on the bike":
        print("that was a long day")
        score += 1
        break
    else:
        print("it was a massive bike ride")
        break

while True:
    countdown(3)
    q_29 = input("what was mine and dads favourite drink whilst away? ").strip().lower()
    if q_29 == "amstel radler":
        print("it was refreshing")
        score += 1 
        break
    else:
        print("it was a refreshing amstel radler")
        break

while True:
    q_30 = input("where did we get dragons breath from? ").strip().lower()
    if q_30 == "market hall rotterdam" or "rotterdam":
        print("they were funny")
        score += 1 
        break
    else:
        print("it was the market hall rotterdam")
        break



print(''' thank you for playing my quiz i hope it was fun and it made yoy remember some amazing'
'memories. I hope the quiz worked propely and you have an amazing mothers day as an amazing mother!''').strip().lower()

print(score"/30")

print("happy mothers day!!!")






