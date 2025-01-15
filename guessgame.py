import random
import time

def generate_hints(secret_number):
    hints = []
    if secret_number % 2 == 0:
        hints.append("Hint: The number is even.")
    else:
        hints.append("Hint: The number is odd.")

    if secret_number % 3 == 0:
        hints.append("Hint: The number is divisible by 3.")
    if secret_number % 5 == 0:
        hints.append("Hint: The number is divisible by 5.")

    return hints

def invite_friend():
    print("\n-- Invite a Friend! --")
    name = input("Enter your friend's name: ")
    print(f"Sending an invite to {name}...\n")
    time.sleep(1)
    print(f"{name} has joined the game! Let's begin.\n")

def math_hurdle():
    print("\n--- Solve This Mathematical Hurdle to Proceed! ---")
    operators = ['+', '-', '*', '/']
    num1 = random.randint(10, 50)
    num2 = random.randint(1, 10)
    operator = random.choice(operators)

    if operator == '/':
        while num1 % num2 != 0:
            num1 = random.randint(10, 50)
            num2 = random.randint(1, 10)

    question = f"{num1} {operator} {num2}"
    correct_answer = eval(question)
    print(f"Solve: {question}")

    try:
        player_answer = float(input("Your answer: "))
    except ValueError:
        print("Invalid input. You failed the hurdle.")
        return False

    if player_answer == correct_answer:
        print("Correct! Proceeding with the game.\n")
        return True
    else:
        print(f"Wrong! The correct answer was {correct_answer}.\n")
        return False

def guessing_game():
    print("Welcome to the Enhanced Multiplayer Guess the Number Game!")

    multiplayer = input("Do you want to invite a friend to play with you? (y/n): ").lower()
    if multiplayer == 'y':
        invite_friend()
        player_1 = input("Player 1, enter your name: ")
        player_2 = input("Player 2, enter your name: ")
        players = [player_1, player_2]
    else:
        player_1 = input("Enter your name: ")
        players = [player_1]

    print("\n--- Level 1: Guess a Number Between 1-100 ---")
    secret_number = random.randint(1, 100)
    max_attempts = 10
    max_time = 30  # Time limit in seconds
    print(f"\n{players[0]} must guess the number within {max_attempts} attempts and {max_time} seconds!\n")

    start_time = time.time()
    attempts = 0
    current_player = 0

    while attempts < max_attempts:
        player = players[current_player]

        elapsed_time = time.time() - start_time
        if elapsed_time > max_time:
            print(f"\nTime's up! You had {max_time} seconds. Game Over!")
            return

        try:
            guess = int(input(f"{player}, make your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess < secret_number:
            print(f"{player}: Too low!")
        elif guess > secret_number:
            print(f"{player}: Too high!")
        else:
            time_taken = round(time.time() - start_time, 2)
            print(f"\nCongratulations {player}! You guessed the number {secret_number} in {attempts} attempts!")
            print(f"It took you {time_taken} seconds to win.")
            print("\n--- Proceeding to Next Level ---")
            break

        if attempts >= 2:
            hints = generate_hints(secret_number)
            for hint in hints:
                print(hint)

        if len(players) > 1:
            current_player = 1 - current_player

    if guess != secret_number:
        print(f"\nSorry, you used all {max_attempts} attempts.")
        print(f"The correct number was {secret_number}. Game Over!\n")
        return

    print("\nYou have completed Level 1!\n")
    if not math_hurdle():
        print("Failed the mathematical hurdle. Game Over!\n")
        return

    continue_game = input("Do you want to continue to the next level (Easy, Medium, Hard)? (y/n): ").lower()
    if continue_game == 'y':
        difficulty_levels(players)

def difficulty_levels(players):
    print("\n--- Difficulty Levels ---")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-100, with fewer hints and harder hurdles)")
    difficulty = input("Choose your difficulty (1, 2, 3): ")

    if difficulty == '1':
        number_range = 50
        max_attempts = 10
        max_time = 20
        print("\n(Easy mode selected: Guess a number between 1 and 50)")
    elif difficulty == '2':
        number_range = 100
        max_attempts = 8
        max_time = 15
        print("\n(Medium mode selected: Guess a number between 1 and 100)")
    elif difficulty == '3':
        number_range = 100
        max_attempts = 7
        max_time = 10
        print("\n(Hard mode selected: Guess a difficult number between 1 and 100)")
    else:
        print("Invalid choice, defaulting to Easy mode.")
        number_range = 50
        max_attempts = 10
        max_time = 20

    if difficulty == '3':
        hard_numbers = [29, 37, 41, 47, 53, 61, 67, 73, 83, 97]
        secret_number = random.choice(hard_numbers)
    else:
        secret_number = random.randint(1, number_range)

    print(f"\nGuess the number in {max_attempts} attempts and {max_time} seconds.\n")

    attempts = 0
    current_player = 0
    start_time = time.time()

    while attempts < max_attempts:
        player = players[current_player]

        elapsed_time = time.time() - start_time
        if elapsed_time > max_time:
            print(f"\nTime's up! You had {max_time} seconds. Game Over!")
            return

        try:
            guess = int(input(f"{player}, make your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess < secret_number:
            print(f"{player}: Too low!")
        elif guess > secret_number:
            print(f"{player}: Too high!")
        else:
            time_taken = round(time.time() - start_time, 2)
            print(f"\nCongratulations {player}! You guessed the number {secret_number} in {attempts} attempts!")
            print(f"It took you {time_taken} seconds to win.")
            break

        if attempts >= 2:
            hints = generate_hints(secret_number)
            for hint in hints:
                print(hint)

        if len(players) > 1:
            current_player = 1 - current_player

    if attempts == max_attempts and guess != secret_number:
        print(f"\nSorry, you have used all {max_attempts} attempts.")
        print(f"The correct number was {secret_number}.\nGame over!")

if __name__ == "__main__":
    guessing_game()
    