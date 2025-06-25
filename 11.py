import random

computer = random.randint(1, 100)
computer1 = random.randint(1, 50)
computer2 = random.randint(1, 100)

status = True
i = 1
j = 1

# Stage 1
while status:
    user = int(input("Guess a number between 1 and 100: "))

    if user > computer:
        print("HINT: Try a smaller number.")
    elif user < computer:
        print("HINT: Try a bigger number.")
    else:
        print("Correct! Moving to the next round.")
        status = False

# Stage 2
while i <= 7:
    user = int(input(f"[Attempt {i}/7] Guess a number between 1 and 50: "))

    if (i == 7 and user != computer1):
        print("Oops! You've used all your attempts. You lost this round.")
    elif user > computer1:
        print("HINT: Try a smaller number.")
    elif user < computer1:
        print("HINT: Try a bigger number.")
    else:
        print("Great! Proceeding to the final round.")
        break
    i += 1

# Stage 3
while j <= 7:
    user = int(input("Final round! Guess a number between 1 and 100: "))

    if (j == 7 and user != computer2):
        print("Game over! You've used all your attempts.")
        break
    if user > computer2:
        print("HINT: Try a smaller number.")
    elif user < computer2:
        print("HINT: Try a bigger number.")
    else:
        print("Congratulations! You've won the game!")
        break
    j += 1
