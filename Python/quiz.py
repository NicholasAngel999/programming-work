print("Happy Mother's Day")

print("Your the best mum ever! Here's a quiz to remember some amazing holiday memories")

print('''FYI! when writing your answers please keep everything lower case and dont put a
      space at the end! If your answer is obviously right but it comes back wrong it
      will be a syntax error just note it down for later''')

print(' Are you ready!')

score = 0

while True:
    start = input("type 'yes' to continue: ").strip().lower()
    if start =="yes":
        print('Starting the quiz...')
        break # Exit the loop and start the quiz
    else:
        print("Try Again.")

while True:
    Question_1 = input("what was my favourite Holiday? ").strip().lower()
    if Question_1 == "florida":
        print("Yes! 1 point!")
        score += 1
        break # Exit the loop go to question_2
    else:
        print("Oooh no! It was Florida! No points")
        break # Exit the loop go to question_2

while True:
    question_2 = input("what was my favourite park at Disney World in Florida? ").strip().lower()
    if question_2 == "hollywood studios":
        print("Great Job! 1 Point!")
        score += 1
        break
    else:
        print("Good Guess! No Points")
        break

while True:
    question_3 = input("Which of our 3 visits to the USA was my favourite? Please answer either 1 2 or 3 ").strip().lower()
    if question_3 == "1":
        print("Yess! It was a great first experience 1 Point!")
        score += 1
        break
    else:
        print("It could have been any of them it was hard to decide. 0 Points")
        break

while True:
    question_4 = input("What was my Favourite ride throughout all of the Disney Parks in Florida? ").strip().lower()
    if question_4 == "tower of terror" or "the tower of terror":
        print("It was a great ride! Especially with Kirsty. 1 Point!")
        score += 1
        break
    else:
        print("close but not quite. 0 Points")
        break

while True:
    question_5 = input("which was my favourite universal studios park? florida or california? ").strip().lower()
    if question_5 == "florida":
        print("It was close but still florida")
        score += 1
        break
    else:
        print("you had a 50/50!")
        break

while True:
    q_6 = input("look at image help yeti, and tell me what ride we were in the queue for when we saw this? ").strip().lower()
    if q_6 == "expedition everest":
        print("amazing memory")
        score += 1
        break
    else:
        print("that was a tough one")
        break

while True:
    q_7 = input("do you remember which park that ride was from? ").strip().lower()
    if q_7 == "animal kingdom":
        print("tough one")
        score += 1
        break
    else:
        print("it could have been loads")

while True:
    q_8 = input("Which of the four swimming pools was the best at the art of animation? ").strip().lower()
    if q_8 == "finding nemo":
        score += 1
        break
    else:
        print("cars was a close second for the cones")
        break

while True:
    q_9 = input("on the 27th of october we went to the chocolate emporium. What milkshake did i get and which did mum get? ").strip().lower()
    if q_9 == "chocolate brownie red velvet" or "chocolate brownie and red velvet":
        score += 1 
        break
    else:
        print("even i may be wrong here")

while True:
    q_10 = input("before the chocolate emporium we were in universal what ride caused mum to get a new shirt? just use character name. ").strip().lower()
    if q_10 == "popeye":
        score += 1
        break
    else:
        print("how do you forget that!")
        break

while True:
    q_11 = input("what did mum do to annoy one of the toy soldiers whilst trying to take pictures? ").strip().lower()
    if q_11 == "stand on his feet":
        print("so many times")
        score += 1
        break
    else: 
        print("that felt like an easy one")
        break

while True:
    q_12 = input("look at the attached q 12 help file. Where was this picture taken? ").strip().lower()
    if q_12 == "Durham":
        print("yes! do you remember the bus questions?")
        score += 1
        break
    else:
        print("How do you forget?")


