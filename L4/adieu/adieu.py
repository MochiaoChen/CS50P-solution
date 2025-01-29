import inflect

names = []
p = inflect.engine()

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print(f"Adieu, adieu, to {p.join(names)}")
        break
