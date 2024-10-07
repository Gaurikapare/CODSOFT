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





