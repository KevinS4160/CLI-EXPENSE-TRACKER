# expense_tracker/cli.py
import argparse
from expense_tracker.db import init_db, add_expense, list_expenses

def main():
    parser = argparse.ArgumentParser(description="CLI Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Sub-command to add an expense
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Expense amount")
    add_parser.add_argument("--category", type=str, required=True, help="Expense category")
    add_parser.add_argument("--description", type=str, default="", help="Expense description")

    # Sub-command to list all expenses
    subparsers.add_parser("list", help="List all expenses")

    args = parser.parse_args()

    # Initialize the database if it doesn't exist
    init_db()

    if args.command == "add":
        add_expense(args.amount, args.category, args.description)
        print("Expense added successfully!")
    elif args.command == "list":
        expenses = list_expenses()
        for expense in expenses:
            print(f"ID: {expense['id']}, Amount: {expense['amount']}, "
                  f"Category: {expense['category']}, Description: {expense['description']}, "
                  f"Date: {expense['date']}")
