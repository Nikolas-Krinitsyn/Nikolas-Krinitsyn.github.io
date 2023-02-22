#This is my test python file for learining python

#This will be a basic math function in the calculator that we will later call at the end of the code.
def calculator(number1, operation, number2):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        if number2 == 0:
            return "cant divide with 0"
        else:
            return number1 / number2
    else:
        return "input error"
#This i sthe welcome statement
print("Welcome to Nik's Super Scientific Calculator!\n\n")

#These are the vairables for the calculator
number1 = float(input("Please input your first number: "))

operation = input("\nPlease input the desired operation (+,-,*,/): ")

number2 = float(input("\nPlease input your second number: ")) 

answer = calculator(number1, operation, number2)
print("Thank you for using Nik's Super Scientifc calculator!\nYou result: " + str(answer) + "\nThank You!!!!")
