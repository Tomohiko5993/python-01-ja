def add(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "bad input"
    return a + b


def subtract(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "bad input"
    return a - b


def multiply(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "bad input"
    return a * b


def divide(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "bad input"
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Example usage:
if __name__ == "__main__":
    print(add(3,4))
    print(subtract(10,5))
    print(multiply(2,3))
    print(divide(10,2))
    print(divide(10,0))
    print(add("a",3))
