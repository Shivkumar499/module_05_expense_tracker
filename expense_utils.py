
import math


def validate_expense(amount):
    return amount > 0


def calculate_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    return math.ceil(total * 100) / 100


def calculate_category_totals(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals
