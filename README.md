# CodSoft Python Programming Internship Projects
<h3>  OVERVIEW </h3>
"This repository features projects I developed during my Python programming internship at CodSoft.
The projects include a basic calculator, a password generator, and a rock-paper-scissors game, each demonstrating various core aspects of Python programming, such as handling user input, utilizing conditionals and loops, and incorporating Python libraries."

### Projects

### 1.Basic Calculator
A command-line calculator designed to perform essential arithmetic operations interactively.

#### Features
- Supports basic operations: addition, subtraction, multiplication, and division.
- Provides error handling for division by zero, displaying a clear error message.
- Allows users to exit the calculator anytime by typing 'exit'.
- Continuously prompts for new calculations until 'exit' is entered.
- Displays formatted results for clarity.

#### Usage
Run the script, then follow the on-screen prompts to enter two numbers and an operator (`+`, `-`, `*`, or `/`). Type 'exit' at any point to quit the calculator.

```python
while True:
     num1 = int(input("Enter first value: "))
     num2 = int(input("Enter second value: "))
     opr = input("Enter the Operator (+, -, *, /) or 'exit' to quit:")
   
     if opr == 'exit':
            print("Calculator exiting...")
            break
    
     if opr in ['+', '-', '*', '/']:
                if opr == '+':
                     print(f"Result: {num1 + num2}")
                elif opr == '-':
                     print(f"Result: {num1 - num2}")
                elif opr == '*':
                     print(f"Result: {num1 * num2}")
                elif opr == '/':
                     if num2 == 0:
                         print("Error: Division by zero!")
                     else:
                         print(f"Result: {num1 / num2}")
     else:
           print("Invalid operator")
```

### 2.Password Generator
A command-line tool designed to generate secure, customizable passwords interactively.

### Features
-Generates random passwords with customizable lengths and complexity.
-Options for including/excluding uppercase letters, lowercase letters, numbers, and special characters.
-Ensures password security by using a strong randomization algorithm.
-Allows users to generate multiple passwords in one session.
-Prompts the user for preferences each time a new password is generated.
-Users can type exit at any time to quit the program.
### Usage
Run the script, then follow the on-screen prompts to select the desired password length and character preferences (e.g., include/exclude numbers or symbols). Type exit at any point to quit the password generator.

```python

import string
import random

'''This line imports a module called 'string' which contains useful functions and variables to work strings (text). It includes things like a list of all letters,digits,punctuation,etc.'''

if __name__ == "__main__": # this condition checks if the scrift is being run directly (not imported as a module).
    s1 = string.ascii_lowercase # s1 contains all the lowercase letters in english alphabet (a to z).
    #print(s1)
    
    s2 = string.ascii_uppercase # s2 contains all the uppercase letters in the english alphabet (a to z).
    #print(s2)
    
    s3 = string.digits # s3 contains all the digits (0 to 9).
    # print(s3)
    
    s4 = string.punctuation # s4 contains all the punctuation character (like !, @,#,$,etc.).
    #print(s4)
    
    plen = int(input("Enter password length\n"))
    # this line promts the user to enter the desired length of the password.
    # thee input is converted to an integer and stored in the variable 'plen'.
    
    s = []
    # an empty list 's' is created to hold all the charcters of the password.
    
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))#difference between extend and append is that when u use append  it will add the list in the list and when you use extend it will.
    #print(s)
    
    random.shuffle(s)
    
    print("your password is:")
    print("".join(s[0:plen]))

     ```

### 3.Rock, Paper, Scissors Game
A command-line game where users compete against the computer by choosing between "rock," "paper," or "scissors."

### Features
- Play the classic game of Rock, Paper, Scissors against the computer.
- The computer randomly chooses its move each round.
- Displays results immediately after each round, indicating if the user won, lost, or tied.
- Tracks the number of rounds played.
- Allows users to play multiple rounds in one session.
- Users can type `exit` at any time to quit the game.

### Usage
Run the script, then enter your choice (`rock`, `paper`, or `scissors`) when prompted. The computer will also make a random choice, and the result will be displayed. To continue playing, answer “yes” when prompted; type `exit` at any time to quit the game.

```python
import random

def rock_paper_scissors_game():
    print("\nWELCOME TO THE ROCK, PAPER, SCISSORS GAME")
    print("Choices: rock, paper, or scissors")
    print("Type 'exit' to quit the game at any time.\n")

    choices = ["rock", "paper", "scissors"]
    rounds_played = 0

    while True:
        user_choice = input("Enter your choice: ").lower()
        if user_choice == "exit":
            print("Game ended. Thanks for playing!")
            break
        elif user_choice not in choices:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.\n")
            continue

        computer_choice = random.choice(choices)
        rounds_played += 1

        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("Congratulations, you won!")
        else:
            print("You lost this round.")

        play_again = input("Do you want to play again? (yes to continue, or 'exit' to quit): ").lower()
        if play_again != "yes":
            print(f"Game over. You played {rounds_played} round(s).")
            break

# Run the game
rock_paper_scissors_game()


```
