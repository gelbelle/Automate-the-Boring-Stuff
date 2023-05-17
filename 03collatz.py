def collatz(num: int):
    if num <= 1:
        return num

    if num % 2 == 0:
        num = num//2
    else:
        num = 3*num+1
    print(num)

    return collatz(num)


def main():
    print("Please enter the number you would like to run through the Collatz sequene: ")

    while True:
        try:
            num = int(input())
            collatz(num)
            break
        except ValueError:
            print("You must enter a whole number: ")


if __name__ == "__main__":
    main()
