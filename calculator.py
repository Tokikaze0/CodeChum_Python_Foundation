# Importing modules for file operations
import json

# Arithmetic operation functions
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
        json.dump(history, file, indent=4)

# Function to load calculation history from a file
def load_from_file():
    try:
        with open("calculation_history.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to get the operator function from the list of operators
def get_operator_function(operation, operators):
    return next((op["function"] for op in operators if op["symbol"] == operation), None)

# Main function
def main():
    # Load calculation history from file
    history = load_from_file()

    # List of supported operators
    operators = [
        {"symbol": "+", "function": addition},
        {"symbol": "-", "function": subtraction},
        {"symbol": "*", "function": multiplication},
        {"symbol": "/", "function": division},
    ]

    print("Welcome to the Calculator!")

    while True:
        try:
            # Get user inputs
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter an operation (+, -, *, /): ")

            # Find the corresponding function for the operation
            operator_function = get_operator_function(operation, operators)

            if operator_function:
                # Perform the calculation
                result = operator_function(num1, num2)
                print(f"Result: {num1} {operation} {num2} = {result}")

                # Save the calculation details
                history.append({
                    "operand1": num1,
                    "operand2": num2,
                    "operation": operation,
                    "result": result,
                })
            else:
                print("Invalid operation. Please try again.")
                continue

            # Ask user if they want to continue
            continue_calculation = input("Do you want to continue? (yes/no): ").strip().lower()
            if continue_calculation == "no":
                break
            elif continue_calculation != "yes":
                print("Invalid input. Exiting...")
                break

        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"An unexpected error occurred: {error}")

    # Save the calculation history before exiting
    save_to_file(history)
    print("Calculation history saved. Goodbye!")

# Entry point of the program
if __name__ == "__main__":
    main()
