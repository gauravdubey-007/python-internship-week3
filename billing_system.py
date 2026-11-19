"""Mini Project (W3): Billing System (OOP-based).

Product class -> name, price, quantity
Bill class    -> total calculation + tax
Final bill is displayed in a table.
"""

from datetime import datetime

TAX_RATE = 0.18  # 18% GST


class Product:
    def __init__(self, name, price, quantity):
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, customer_name, tax_rate=TAX_RATE):
        self.customer_name = customer_name
        self.tax_rate = tax_rate
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def subtotal(self):
        return sum(p.total() for p in self.products)

    def tax(self):
        return self.subtotal() * self.tax_rate

    def grand_total(self):
        return self.subtotal() + self.tax()

    def display(self):
        line = "-" * 56
        print("\n" + "=" * 56)
        print(f"{'BILL':^56}")
        print("=" * 56)
        print(f"Customer: {self.customer_name}")
        print(f"Date    : {datetime.now().strftime('%d-%m-%Y %H:%M')}")
        print(line)
        print(f"{'No.':<5}{'Product':<22}{'Price':>9}{'Qty':>6}{'Total':>12}")
        print(line)
        for i, p in enumerate(self.products, start=1):
            print(f"{i:<5}{p.name:<22}{p.price:>9.2f}{p.quantity:>6}{p.total():>12.2f}")
        print(line)
        print(f"{'Subtotal':<44}{self.subtotal():>12.2f}")
        print(f"{f'Tax ({self.tax_rate * 100:.0f}%)':<44}{self.tax():>12.2f}")
        print(f"{'GRAND TOTAL':<44}{self.grand_total():>12.2f}")
        print("=" * 56)
        print("Thank you for shopping with us!")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def main():
    print("=== Billing System ===")
    customer = input("Customer name: ").strip() or "Customer"
    bill = Bill(customer)

    while True:
        name = input("\nProduct name (or press Enter to finish): ").strip()
        if not name:
            if not bill.products:
                print("Add at least one product.")
                continue
            break
        price = read_float("Price: ")
        quantity = read_int("Quantity: ")
        try:
            bill.add_product(Product(name, price, quantity))
            print(f"Added {name}.")
        except ValueError as e:
            print(f"Error: {e}")

    bill.display()


if __name__ == "__main__":
    main()
