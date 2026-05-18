### julia.goes.dev CHALLENGE Monat 1 ###
import random

secret_number = random.randint(0, 100)
attempts = 0
print("Welcome to Secret Number!")

while True:
    user_number = input("Please enter a number between 0 and 100 or quit for exit: ")

    if user_number == "quit":
        break
    elif not user_number.isdigit():
        print("Please enter a number.")
        continue

    elif int(user_number) > 100:
        print("Please enter a number between 0 and 100!")
        continue

    user_number = int(user_number)
    attempts += 1

    if user_number == secret_number:
        print(f"Correct! You needed {attempts} attempts.")
        break
    elif user_number < secret_number:
        print("Your number is too low.")
    elif user_number > secret_number:
        print("Your number is too high")

print("Program closed")

print(
    f"Debug: user_number={user_number}, secret_number={secret_number}, attempts={attempts}"
)
