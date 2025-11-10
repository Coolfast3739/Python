print("Welcome to the calculator program!")
expression = input("Enter a mathematical expression to evaluate: ")
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
def function(): 
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

print("Thank you for using the calculator program!")
input("do you want to run again? (press enter to exit, type 'yes' to continue): ")
if (input().lower() == "yes"):
    expression = input("Enter a mathematical expression to evaluate: ")
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")
    function()

elif (input().lower() != "yes"):
    function()
    expression = input("Enter a mathematical expression to evaluate: ")
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")
elif (input().lower() == "no"):
    print("Goodbye!")
else:
    print("Invalid input. Exiting the program.")
input("Press Enter to exit...")


