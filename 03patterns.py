import time, sys

def draw(choice):
    params = {
        "indent":0,
        "indentIncreasing":True,
        "direction":1,
        "counter":0
    }

    if choice == 1:
        zigzag(params)
    else:
        diagonal(params)

def zigzag(params):
    counter = params["counter"]
    while True:
        try:
            print(" " * params["indent"], end="")
            print("********")
            time.sleep(0.1)

            params["indent"] +=params["direction"]
            counter += 1

            if counter == 20:
                params["indentIncreasing"] = not params["indentIncreasing"]
                params["direction"] *= -1
                counter = 0

        except KeyboardInterrupt:
            sys.exit(0)

def diagonal(params):

    while True:
        try:
            print(" " * params["indent"], end="")
            print("********")
            time.sleep(0.1)

            params["indent"] +=params["direction"]

            if params["counter"] == 20:
                params["indentIncreasing"] = not params["indentIncreasing"]
                params["direction"] *= -1
                params["counter"] = 0

        except KeyboardInterrupt:
            sys.exit(0)


def main():
    print("Would you like a stripe or a zigzag?")
    print("1: Zigzag")
    print("2: Stripe")
    while True:
        try:
            choice = int(input())

            while choice != 1 or 2:
                if choice == 1 or choice == 2:
                    draw(choice)
                else:
                    print("That is not a valid choice. Please choose 1 or 2")
                    choice = int(input())
        except ValueError:
            print("That is not a valid choice. Please choose 1 or 2")
            choice = int(input())

if __name__ == "__main__":
    main()