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
           