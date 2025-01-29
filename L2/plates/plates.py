def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False

    if not s[0:2].isalpha():
        return False

    num_check = False
    for char in s:
        if char.isdigit():
            if not num_check:
                if char == '0':
                    return False
                num_check = True
        elif num_check:
            return False

    if not s.isalnum():
        return False

    return Ture


main()
