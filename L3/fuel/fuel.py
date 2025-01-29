while True:
    try:
        a,b = input("Fraction: ").split('/')
        a,b = int(a), int(b)
        if a == 0:
            raise ZeroDivisionError
        if a > b:
            raise ValueError
        break
    except (ZeroDivisionError, ValueError):
        pass

value = round(a / b * 100)
if value <= 1:
    print('E')
if value >= 99:
     print('F')
else:
     print(f"{value}%")
