from expense import Expense
from storage import load_data, save_data


def add_expense():
    try:
        amount = float(input("Amount: ₹"))
    except ValueError:
        print("Invalid amount!")
        return

    category = input("Category: ")
    note = input("Note: ")

    expense = Expense(amount, category, note)

    data = load_data()
    data.append(expense.to_dict())
    save_data(data)

    print("Expense added successfully!\n")


def view_expenses():
    data = load_data()

    if not data:
        print("No expenses found.\n")
        return

    print("\n--- Expense List ---")
    for i, exp in enumerate(data, start=1):
        print(f"{i}. Amount: ₹{exp['amount']}")
        print(f"   Category: {exp['category']}")
        print(f"   Note: {exp['note']}")
        print("-" * 20)


while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")