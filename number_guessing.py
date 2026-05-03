import random


secret_number = random.randint(1, 100)

attempts = 0

print("🎮 Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")


while True:
    guess = int(input("Enter your guess: "))

    attempts += 1


    if guess > secret_number:
        print("📈 Too High!")

    elif guess < secret_number:
        print("📉 Too Low!")

    else:
        print("🎉 Correct Guess!")
        print(f"You guessed the number in {attempts} attempts.")


        score = 100 - attempts


        if score < 0:
            score = 0

        print(f"🏆 Your Score: {score}")

        break
