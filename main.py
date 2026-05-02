from expense import Expense
from storage import load_data, save_data
from analytics import total_spending, category_summary, monthly_spending
from utils import export_to_csv


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

    print("Expense added successfully!")


def view_expenses():
    data = load_data()

    if not data:
        print("No expenses found.")
        return

    print("\n--- Expense List ---")
    for i, exp in enumerate(data, start=1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']} | {exp['date']}")


def delete_expense():
    data = load_data()
    view_expenses()

    try:
        index = int(input("Enter index to delete: ")) - 1
        data.pop(index)
        save_data(data)
        print("Deleted successfully!")
    except:
        print("Invalid index!")


def edit_expense():
    data = load_data()
    view_expenses()

    try:
        index = int(input("Enter index to edit: ")) - 1

        data[index]["amount"] = float(input("New Amount: "))
        data[index]["category"] = input("New Category: ")
        data[index]["note"] = input("New Note: ")

        save_data(data)
        print("Updated successfully!")

    except:
        print("Invalid input!")


def search_by_category():
    data = load_data()
    category = input("Enter category: ")

    results = [exp for exp in data if exp["category"].lower() == category.lower()]

    if not results:
        print("No results found.")
        return

    for exp in results:
        print(exp)


def show_summary():
    data = load_data()

    print("\nTotal Spending: ₹", total_spending(data))

    print("\nCategory Summary:")
    for k, v in category_summary(data).items():
        print(k, ":", v)

    print("\nMonthly Spending:")
    for k, v in monthly_spending(data).items():
        print(k, ":", v)


def budget_alert():
    data = load_data()
    budget = float(input("Enter your monthly budget: ₹"))

    total = total_spending(data)

    if total > budget:
        print("⚠️ Budget exceeded!")
    else:
        print("You are within budget.")


while True:
    print("\n==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Edit Expense")
    print("5. Search by Category")
    print("6. Summary")
    print("7. Export to CSV")
    print("8. Budget Alert")
    print("9. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        edit_expense()
    elif choice == "5":
        search_by_category()
    elif choice == "6":
        show_summary()
    elif choice == "7":
        export_to_csv(load_data())
    elif choice == "8":
        budget_alert()
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")