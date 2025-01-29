def main():
    time = input("What time is it? ").strip()
    time_dig = convert(time)
    if 7 <= time_dig <= 8:
        print("breakfast time")
    elif 12 <= time_dig <= 13:
        print("lunch time")
    elif 18 <= time_dig <= 19:
        print("dinner time")
    else:
        print()

def convert(time):
    hours,minutes = time.split(":")
    hours = int(hours)
    minutes = float(minutes) / 60
    return (hours + minutes)


if __name__ == "__main__":
    main()
