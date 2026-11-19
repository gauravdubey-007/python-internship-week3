"""Assignment 3: Calculator class with exception handling."""

import math


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def power(self, a, b):
        return a ** b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(a)


def read_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        raise ValueError("Invalid input. Please enter a number.")


def main():
    calc = Calculator()
    print("=== Calculator ===")
    while True:
        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        print("5. Power\n6. Square Root\n7. Exit")
        choice = input("Choose an option (1-7): ").strip()
        if choice == "7":
            print("Goodbye!")
            break
        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid option. Please choose 1-7.")
            continue

        try:
            if choice == "6":
                print("Result:", calc.square_root(read_number("Enter number: ")))
            else:
                a = read_number("Enter first number: ")
                b = read_number("Enter second number: ")
                operations = {
                    "1": calc.add, "2": calc.subtract, "3": calc.multiply,
                    "4": calc.divide, "5": calc.power,
                }
                print("Result:", operations[choice](a, b))
        except (ValueError, ZeroDivisionError, OverflowError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
