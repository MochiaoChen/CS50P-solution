camel = input("camelCase: ")
snake = ""


for c in camel:
    if c.isupper() is True:
        snake += "_" +c.lower()
    else:
        snake += c

print("snake_case:",snake)
