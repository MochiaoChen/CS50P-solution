def main():
    x, y, z = input("Expression:").split()
    x, z = int(x), int(z)
    if y == "/" and z == 0:
        print("Error: Division by zero!")
    else:
        print(f"{calculate(x, y, z):.1f}")

def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0 :
            return False
        else:
            return a / b

main()