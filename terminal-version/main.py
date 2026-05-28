### julia.goes.dev CHALLENGE Monat 1 ###
import random


#### Functions ###
# Prüft den Tipp gegen die geheime Zahl.
def check_guess(user_number, secret_number):
    if user_number == secret_number:
        return "correct"
    elif user_number > secret_number:
        return "too_high"
    elif user_number < secret_number:
        return "too_low"


# Prüft, ob die Nutzereingabe eine gültige Zahl ist.
def is_valid_number(user_number):
    if not user_number.isdigit() or int(user_number) > 100:
        return False
    return True


# Startet das Spiel
def play_game():
    secret_number = random.randint(0, 100)
    attempts = 0

    print("Welcome to Secret Number!")

    ### Gameloop ###
    while True:
        user_number = input(
            "Please enter a number between 0 and 100 or quit for exit: "
        )

        if user_number == "quit":
            break
        elif not is_valid_number(user_number):
            continue

        # Convert input string to integer.
        user_number = int(user_number)
        # Erhöt um 1 pro Durchlauf
        attempts += 1

        # Holt das Ergebnis aus der Funktion check_guess.
        result = check_guess(user_number, secret_number)

        if result == "correct":
            print(f"Correct! You needed {attempts} attempts.")
            break
        elif result == "too_low":
            print("Your number is too low.")
        elif result == "too_high":
            print("Your number is too high")

    print("Program closed")


play_game()
