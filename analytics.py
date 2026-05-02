from collections import defaultdict

def total_spending(data):
    return sum(exp["amount"] for exp in data)

def category_summary(data):
    summary = defaultdict(float)
    for exp in data:
        summary[exp["category"]] += exp["amount"]
    return summary

def monthly_spending(data):
    summary = defaultdict(float)
    for exp in data:
        month = exp["date"][:7]  # YYYY-MM
        summary[month] += exp["amount"]
    return summary