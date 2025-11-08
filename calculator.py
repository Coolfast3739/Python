print("Welcome to the calculator program!")
def function(): 
    expression = input("Enter a mathematical expression to evaluate: ")
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")
    if expression == "add" or expression == "+":
        final = int(first_number) + int(second_number)
        print(f"The result of adding {first_number} and {second_number} is: {final}")
    elif expression == "subtract" or expression == "-":
        final = int(first_number) - int(second_number)
        print(f"The result of subtracting {second_number} from {first_number} is: {final}")
    elif expression == "multiply" or expression == "*":
        final = int(first_number) * int(second_number)
        print(f"The result of multiplying {first_number} and {second_number} is: {final}")
    elif expression == "divide" or expression == "/":
        if int(second_number) == 0:
            print("Error: Division by zero is not allowed.")
        else:
            final = int(first_number) / int(second_number)
            print(f"The result of dividing {first_number} by {second_number} is: {final}")
    else:
        print("Invalid operation. Please enter add (+), subtract (-), multiply (*), or divide (/).")
function()




