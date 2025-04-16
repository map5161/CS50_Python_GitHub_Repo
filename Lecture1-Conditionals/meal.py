def main():
    time = input("Time: ").strip()
    x = convert(time)
    if x >= 7 and x <= 8:
        print("breakfast time")
    elif x >= 12 and x <= 13:
        print("lunch time")
    elif x >= 18 and x <= 19:
        print("dinner time")


def convert(t):
    hours, minutes = t.split(":")
    hours = int(hours)
    minutes = int(minutes)/60
    return (hours + minutes)

if __name__ == "__main__":
    main()