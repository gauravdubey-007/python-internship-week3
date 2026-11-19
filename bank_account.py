"""Assignment 1: Bank Account class with deposit, withdraw, display balance."""


class InsufficientFundsError(Exception):
    """Raised when withdrawal amount is more than the balance."""


class BankAccount:
    def __init__(self, holder_name, account_number, balance=0.0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Rs. {amount:.2f} deposited.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient balance.")
        self.balance -= amount
        print(f"Rs. {amount:.2f} withdrawn.")

    def display_balance(self):
        print(f"Account Holder : {self.holder_name}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : Rs. {self.balance:.2f}")


def get_amount(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        raise ValueError("Please enter a valid number.")


def main():
    print("=== Bank Account ===")
    name = input("Enter account holder name: ").strip() or "Customer"
    account = BankAccount(name, "AC1001", 1000.0)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Display Balance\n4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        try:
            if choice == "1":
                account.deposit(get_amount("Enter amount to deposit: "))
            elif choice == "2":
                account.withdraw(get_amount("Enter amount to withdraw: "))
            elif choice == "3":
                account.display_balance()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1-4.")
        except (ValueError, InsufficientFundsError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
