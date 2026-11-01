
import random
import datetime as dt
import expense_utils as eu
from report_utils import generate_monthly_report


expenses = []

print("Expense Tracker")

while True:
    description = input("Enter description: ")
    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount (₹): "))

        if not eu.validate_expense(amount):
            print("Amount must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid amount.")
        continue

    expense_date = input(
        "Enter date (YYYY-MM-DD, blank for today): "
    )

    if expense_date == "":
        expense_date = dt.date.today().strftime("%Y-%m-%d")
    else:
        try:
            dt.datetime.strptime(expense_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            continue

    reference_id = f"EXP-{random.randint(100000, 999999)}"

    expense = {
        "reference_id": reference_id,
        "date": expense_date,
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print(f"Reference ID: {reference_id}")

    choice = input("Add another expense? (yes/no): ").lower()

    if choice != "yes":
        break

generate_monthly_report(expenses)
