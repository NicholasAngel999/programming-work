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
        print("")