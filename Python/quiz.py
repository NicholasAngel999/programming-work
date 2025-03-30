import time
import sys


def countdown(seconds):
    #pass
    for i in range(seconds, 0, -1):
        print(i, end="...\n", flush=True)
        time.sleep(1)

def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


score = 0

type_text("Happy Mother's Day")

type_text("Your the best mum ever! Here's a quiz to remember some amazing holiday memories")

type_text('''FYI! when writing your answers please keep everything lower case and dont put a
      space at the end! If your answer is obviously right but it comes back wrong it
      will be a syntax error just note it down for later. once your done you can open 
      the other file i have sent you and you can look at the code and see all the right answers''')

type_text(' Are you ready!')


while True:
    start = input("type 'yes' to continue: ").strip().lower()
    if start =="yes":
        print('Starting the quiz...')
        break # Exit the loop and start the quiz
    else:
        print("Try Again.")

while True:
    countdown(3)
    type_text("what was my favourite Holiday? ")
    Question_1 = input().strip().lower()
    if Question_1 == "florida":
        print("Yes! 1 point!")
        score += 1
        break # Exit the loop go to question_2
    else:
        print("Oooh no! It was Florida! No points")
        break # Exit the loop go to question_2
    

while True:
    countdown(3)
    type_text("what was my favourite park at Disney World in Florida? ")
    question_2 = input().strip().lower()
    if question_2 == "hollywood studios":
        print("Great Job! 1 Point!")
        score += 1
        break
    else:
        print("Good Guess! No Points")
        break


while True:
    countdown(3)
    type_text("Which of our 3 visits to the USA was my favourite? Please answer either 1 2 or 3 ")
    question_3 = input().strip().lower()
    if question_3 == "1":
        print("Yess! It was a great first experience 1 Point!")
        score += 1
        break
    else:
        print("It could have been any of them it was hard to decide. 0 Points")
        break


while True:
    countdown(3)
    type_text("What was my Favourite ride throughout all of the Disney Parks in Florida? ")
    question_4 = input().strip().lower()
    
    correct_answers_4 = ["tower of terror", "the tower of terror"]

    if question_4 in correct_answers_4:
        print("It was a great ride! Especially with Kirsty. 1 Point!")
        score += 1
        break
    else:
        print("close but not quite. 0 Points")
        break


while True:
    countdown(3)
    type_text("which was my favourite universal studios park? florida or california? ")
    question_5 = input().strip().lower()
    if question_5 == "florida":
        print("It was close but still florida")
        score += 1
        break
    else:
        print("you had a 50/50!")
        break


while True:
    countdown(3)
    type_text("look at image help yeti, and tell me what ride we were in the queue for when we saw this? ")
    q_6 = input().strip().lower()
    if q_6 == "expedition everest":
        print("amazing memory")
        score += 1
        break
    else:
        print("that was a tough one")
        break

while True:
    countdown(3)
    type_text("do you remember which park that ride was from? ")
    q_7 = input().strip().lower()
    if q_7 == "animal kingdom":
        print("tough one")
        score += 1
        break
    else:
        print("it could have been loads")
        break


while True:
    countdown(3)
    type_text("Which of the four swimming pools was the best at the art of animation? ")
    q_8 = input().strip().lower()
    if q_8 == "finding nemo":
        score += 1
        break
    else:
        print("cars was a close second for the cones")
        break


while True:
    countdown(3)
    type_text("on the 27th of october we went to the chocolate emporium. What milkshake did i get and which did mum get? ")
    q_9 = input().strip().lower()

    correct_answers_9 = ["chocolate brownie red velvet", "chocolate brownie and red velvet"]

    if q_9 == "chocolate brownie red velvet" or "chocolate brownie and red velvet":
        score += 1 
        break
    else:
        print("even i may be wrong here")
        break


while True:
    countdown(3)
    type_text("before the chocolate emporium we were in universal what ride caused mum to get a new shirt? just use character name. ")
    q_10 = input().strip().lower()
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
    
    correct_answers_15 = ["jags vs eagles", "jacksonville vs philidelphia", "jaguars vs eagles", "jacksonville jaguars vs philidelphia eagles", "eagles vs jags", "philidelphia vs jacksonville", "eagles vs jaguars", "philidelphia eagles vs jacksonville jaguars"]

    if q_15 in correct_answers_15:
        print("what a game!")
        score += 1
        break
    else:
        print("it was a great day and it was your team!")
        break

while True:
    countdown(3)
    q_16 = input("where else did we go on that trip? ").strip().lower()

    correct_answers_16 = ["wizarding world", "harry potter studio", "harry potter"]

    if q_16 in correct_answers_16:
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
    q_188 = input("where did me and mum go mountain biking in august of 2019? ").strip().lower()

    correct_answers_188 = ["kielder forrest", "cresswell towers"]

    if q_188 in correct_answers_188:
        print("was a pretty cool diamond back")
        score += 1 
        break
    else:
        print("how can you forget that day we got lost")
        break

while True:
    countdown(3)
    q_18 = input("what hotel did we stay in at california? ").strip().lower()

    correct_answers_18 = ["knotts berry farm", "knotts farm", "knott's farm"]

    if q_18 in correct_answers_18:
        print("easy")
        score += 1
        break
    else:
        print("come on")
        break

while True:
    countdown(3)
    q_19 = input("what was the best find of the first day? ").strip().lower()

    correct_asnwers_19 = ["johnny rockets", "snoopy", "finding johnny rockets", "finding snoopy"]

    if q_19 in correct_asnwers_19:
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
    'studios hollywood ''').strip().lower()
    correct_answers_22 = ["the forbidden journey", "harry potter and the forbidden journey"]

    if q_22 in correct_answers_22:
        print("that one was crazy hard")
        score += 1 
        break
    else:
        print("i didnt expect you to know that")
        break

while True:
    countdown(3)
    q_23 = input("what date did we go to watch the ice hockey? ").strip().lower()

    correct_answers_23 = ["29th october", "29 october", "29 oct", "29th oct"]

    if q_23 in correct_answers_23:
        print("amazing day!")
        score += 1
        break
    else:
        print("can you get the next one?")
        break

while True:
    countdown(3)
    q_24 = input("what was the final score of the game? please write highest score - lowest score ").strip().lower()

    correct_answers_24 = ["7-4", "7 - 4"]

    if q_24 in correct_answers_24:
        print("at least you got that one")
        score += 1
        break
    else:
        print(":(")
        break

while True:
    countdown(3)
    q_25 = input('''what was the date we set off from england headed for holland?'
    'please format your answer to be 25 february 2025 ''').strip().lower()
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

    correct_answers_26 = ["ducking", "crouching", "bending over"]
    if q_26 in correct_answers_26:
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

    correct_answers_28 = ["big bike ride", "long bike ride", "cycle all day", "cycle"]

    if q_28 in correct_answers_28:
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

    correct_asnwers_30 = ["market hall rotterdam", "rotterdam"]

    if q_30 in correct_asnwers_30:
        print("they were funny")
        score += 1 
        break
    else:
        print("it was the market hall rotterdam")
        break



type_text(''' thank you for playing my quiz i hope it was fun and it made yoy remember some amazing'
'memories. I hope the quiz worked propely and you have an amazing mothers day as an amazing mother!''')

type_text(f"🏆 Your final score is: {score}/30! 🏆")


type_text("happy mothers day!!!")






