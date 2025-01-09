repeat = True
def addition(num1, num2):
    return num1 + num2
    
def subtraction(num1, num2):
    return num1 - num2
    
def multiplication(num1, num2):
    return num1 * num2
    
def division(num1, num2):
    return num1 / num2

try:
    while repeat == True:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")
        while operation in ["+", "-", "*", "/"]:
            match operation:
                case "+": print("The sum of the two numbers is: ", addition(num1, num2))
                case "-": print("The difference of the two numbers is: ", subtraction(num1, num2))
                case "*": print("The product of the two numbers is: ", multiplication(num1, num2))
                case "/": print("The quotient of the two numbers is: ", division(num1, num2))
            break
        condition = input("Do you want to continue? (yes/no): ")
        if condition.lower() == "yes":
            repeat = True
        elif condition.lower() == "no":
            repeat = False
        else:
            print("Invalid input.")
            repeat = False
except:
    print("An Error occur, please try again")