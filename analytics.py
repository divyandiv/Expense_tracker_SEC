def calculate_total(expenses):
    return sum(float(exp["amount"]) for exp in expenses)
def filter_by_category(expenses, category):
    return [exp for exp in expenses if exp["category"].lower() == category.lower()]
