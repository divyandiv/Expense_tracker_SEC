def calculate_total(expenses):
    return sum(float(exp["amount"]) for exp in expenses)
