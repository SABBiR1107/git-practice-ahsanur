# utils.py

def add(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        return "Error: Invalid input. Please enter numbers only."


def subtract(a, b):
    try:
        return float(a) - float(b)
    except ValueError:
        return "Error: Invalid input. Please enter numbers only."


def multiply(a, b):
    try:
        return float(a) * float(b)
    except ValueError:
        return "Error: Invalid input. Please enter numbers only."

def divide(a, b):
    try:
        return float(a) / float(b)
    except ValueError:
        return "Error: Invalid input. Please enter numbers only."
