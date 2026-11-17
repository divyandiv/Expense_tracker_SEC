def calculate_total(expenses):
    return sum(float(exp["amount"]) for exp in expenses)
def filter_by_category(expenses, category):
    return [exp for exp in expenses if exp["category"].lower() == category.lower()]
def check_budget(expenses, monthly_limit=5000):
    total = calculate_total(expenses)
    if total > monthly_limit:
        print(f"WARNING: Budget Exceeded! Spent: ₹{total:.2f} / Limit: ₹{monthly_limit:.2f}")
    else:
        remaining = monthly_limit - total
        print(f"Safe. Spent: ₹{total:.2f} | Remaining Monthly Budget: ₹{remaining:.2f}")
