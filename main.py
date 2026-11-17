import analytics

def main():
    # Initial state for tracking features locally before merging files
    expenses = [] 
    while True:
        print("\n=== Student Expense Tracker ===")
        print("1. Add Expense")
        # Options 2 & 3 belong to Student 1's features
        print("4. Filter by Category")
        print("5. Check Budget Status")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category (Food/Books/Travel): ")
            expenses.append({"amount": amount, "category": category})
        elif choice == "4":
            cat = input("Enter category to filter: ")
            filtered = analytics.filter_by_category(expenses, cat)
            for exp in filtered:
                print(f"- {exp['category']}: ₹{exp['amount']}")
        elif choice == "5":
            analytics.check_budget(expenses)
        elif choice == "6":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
