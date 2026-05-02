import csv

def export_to_csv(data):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["amount", "category", "note", "date"])
        writer.writeheader()
        writer.writerows(data)

    print("Exported to expenses.csv")