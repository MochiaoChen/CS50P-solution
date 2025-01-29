from random import randint


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        sum = x + y
        tries = 0
        while tries < 3:
            try:
                ans = int(input(f'{x} + {y} = '))
                if ans == sum:
                    score += 1
                    break
                else:
                    print('EEE')
                    tries += 1
            except ValueError:
                print('EEE')
                tries += 1
        if tries == 3:
            print(f"{x} + {y} = {sum}")
    print(f"Score: {score}")


def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input('Level: '))
            if level in levels:
                return level
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
