# Importing modules for file operations
import json

# Custom functions for arithmetic operations
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

# Function to save calculation history to a file
def save_to_file(history):
    with open("calculation_history.json", "w") as file:
        json.dump(history, file)

# Function to load calculation history from a file
def load_from_file():
    try:
        with open("calculation_history.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Main function to organize the program
def main():
    repeat = True
    history = load_from_file()  # Load history from file

    try:
        while repeat:
            # Using different data types: int, float, str
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter an operation (+, -, *, /): ")

            result = None
            if operation == "+":
                result = addition(num1, num2)
            elif operation == "-":
                result = subtraction(num1, num2)
            elif operation == "*":
                result = multiplication(num1, num2)
            elif operation == "/":
                result = division(num1, num2)
            else:
                print("Invalid operation. Please try again.")
                continue

            print(f"The result is: {result}")
            history.append(f"{num1} {operation} {num2} = {result}")  # Save to history

            condition = input("Do you want to continue? (yes/no): ")
            if condition.lower() == "no":
                repeat = False
            elif condition.lower() != "yes":
                print("Invalid input. Exiting...")
                repeat = False

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        save_to_file(history)  # Save history to file before exiting
        print("Calculation history saved.")

# Entry point of the program
if __name__ == "__main__":
    main()