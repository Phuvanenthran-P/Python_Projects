def add_expense():
    amount = float(input("Amount: "))
    category = input("Category: ")
    note = input("Note: ")

    with open("expenses.txt", "a") as f:
        f.write(f"{amount},{category},{note}\n")

    print("Expense added.")


def view_expenses():
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No expense file found.")


print("1. Add Expense")
print("2. View Expenses")

choice = int(input("Choose option: "))

if choice == 1:
    add_expense()
else:
    view_expenses()
