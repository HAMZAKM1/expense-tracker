# ==============================
# EXPENSE TRACKER PROJECT
# ==============================

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Store expense data
data = []

while True:

    print("\n==============================")
    print("      EXPENSE TRACKER")
    print("==============================")
    print("1. Add Expense")
    print("2. Show Expense Report")
    print("3. Show Total Expense")
    print("4. Save to CSV")
    print("5. Show Pie Chart")
    print("6. Show Bar Chart")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # ==============================
    # ADD EXPENSE
    # ==============================
    if choice == "1":

        name = input("Enter Expense Name: ")

        try:
            amount = float(input("Enter Amount: "))
        except ValueError:
            print("Invalid amount! Please enter numbers only.")
            continue

        category = input("Enter Category (Food/Travel/Shopping/etc): ")

        # Add current date automatically
        date = datetime.now().strftime("%Y-%m-%d")

        # Add data to list
        data.append([name, amount, category, date])

        print("Expense added successfully!")

    # ==============================
    # SHOW REPORT
    # ==============================
    elif choice == "2":

        if len(data) == 0:
            print("No expenses found!")

        else:
            df = pd.DataFrame(
                data,
                columns=["Name", "Amount", "Category", "Date"]
            )

            print("\n========== EXPENSE REPORT ==========")
            print(df)

    # ==============================
    # TOTAL EXPENSE
    # ==============================
    elif choice == "3":

        if len(data) == 0:
            print("No expenses found!")

        else:
            df = pd.DataFrame(
                data,
                columns=["Name", "Amount", "Category", "Date"]
            )

            total = df["Amount"].sum()

            print("\nTotal Expense =", total)

    # ==============================
    # SAVE CSV
    # ==============================
    elif choice == "4":

        if len(data) == 0:
            print("No expenses to save!")

        else:
            df = pd.DataFrame(
                data,
                columns=["Name", "Amount", "Category", "Date"]
            )

            df.to_csv("expenses.csv", index=False)

            print("CSV file saved successfully!")

    # ==============================
    # PIE CHART
    # ==============================
    elif choice == "5":

        if len(data) == 0:
            print("No expenses found!")

        else:
            df = pd.DataFrame(
                data,
                columns=["Name", "Amount", "Category", "Date"]
            )

            plt.figure(figsize=(6, 6))

            df.groupby("Category")["Amount"].sum().plot(
                kind="pie",
                autopct="%1.1f%%"
            )

            plt.title("Expense Distribution")
            plt.ylabel("")

            plt.show()

    # ==============================
    # BAR CHART
    # ==============================
    elif choice == "6":

        if len(data) == 0:
            print("No expenses found!")

        else:
            df = pd.DataFrame(
                data,
                columns=["Name", "Amount", "Category", "Date"]
            )

            plt.figure(figsize=(6, 4))

            df.groupby("Category")["Amount"].sum().plot(
                kind="bar"
            )

            plt.title("Expenses By Category")
            plt.xlabel("Category")
            plt.ylabel("Amount")

            plt.show()

    # ==============================
    # EXIT
    # ==============================
    elif choice == "7":

        print("Thank you for using Expense Tracker!")
        break

    # ==============================
    # INVALID OPTION
    # ==============================
    else:
        print("Invalid choice! Please try again.")