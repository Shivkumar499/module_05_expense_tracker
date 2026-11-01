
import datetime as dt
from tabulate import tabulate


def generate_monthly_report(expenses):
    current_month = dt.date.today().strftime("%b %Y")
    current_year = dt.date.today().year
    current_month_number = dt.date.today().month

    monthly_expenses = []

    for expense in expenses:
        expense_date = dt.datetime.strptime(
            expense["date"], "%Y-%m-%d"
        ).date()

        if (
            expense_date.year == current_year
            and expense_date.month == current_month_number
        ):
            monthly_expenses.append(expense)

    print("\n----- MONTHLY EXPENSE REPORT -----")

    table_data = []

    for expense in monthly_expenses:
        table_data.append([
            expense["reference_id"],
            expense["date"],
            expense["description"],
            expense["category"],
            f"₹{expense['amount']:.2f}"
        ])

    print(tabulate(
        table_data,
        headers=["Reference ID", "Date", "Description", "Category", "Amount"],
        tablefmt="grid"
    ))

    from expense_utils import calculate_total, calculate_category_totals

    total = calculate_total(monthly_expenses)
    category_totals = calculate_category_totals(monthly_expenses)

    print(f"\nTotal spending: ₹{total:.2f}")

    for category, amount in category_totals.items():
        print(f"{category} total: ₹{amount:.2f}")

    print(f"Report month: {current_month}")
