from random import randrange

while True:
    try:
        n = int(input("Level: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        pass

ans = randrange(n) + 1

while True:
    try:
        gs = int(input("Guess:"))
        if gs < ans:
            print("Too small!")
            continue
        elif gs > ans:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
    except ValueError:
        pass

