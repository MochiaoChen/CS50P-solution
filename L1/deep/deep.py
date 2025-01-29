prompt = input()
match prompt:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
