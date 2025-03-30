import sys
import time


score = 0  # Start with 0 points
total_score = 30  # Total possible points

def type_text(text, delay=0.05):
    """Prints text as if it's being typed in real time."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)  # Simulate typing effect
    print()  # Move to the next line

def countdown(seconds):
    """Visible countdown before the next question."""
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\r⏳ Next question in {i} seconds... ")  # Overwrites line
        sys.stdout.flush()
        time.sleep(1)
    print("\n")  # Ensure next question starts on a new line

# Question 1
valid_answers_q1 = ["florida", "orlando", "disney world"]

type_text("🛫 What was my favourite holiday? ")
question_1 = input().strip().lower()
if question_1 in valid_answers_q1:
    type_text(Fore.LIGHTGREEN_EX + "✅ Yes! 1 point!")
    score += 1
else:
    type_text(Fore.RED + "❌ Oooh no! The correct answer was Florida!")

# Countdown before the next question
countdown(3)

# Question 2
valid_answers_q2 = ["hollywood studios", "disney’s hollywood studios"]

type_text("🎢 What was my favourite park at Disney World in Florida? ")
question_2 = input().strip().lower()
if question_2 in valid_answers_q2:
    type_text(Fore.LIGHTGREEN_EX + "🎯 Great job! 1 point!")
    score += 1
else:
    type_text(Fore.RED + "🤔 Good guess! No points")

# Countdown before the final score
countdown(3)

# Display Final Score with Typing Effect
type_text(Fore.MAGENTA + f"🏆 Your final score is: {score}/{total_score}! 🏆", delay=0.03)
