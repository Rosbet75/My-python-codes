def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choose = input("Enter operation: ").strip()
result = operation[choose](num1, num2)
print(f"Your result is {result}")
