import customUtils as utils

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def main():
    """
    Find the longest word in the nested lists then uses that as the padding to right justify each word
    The nested loops print each item in the same position of each line. 
    Eg. line1 position 0, line2 position 0, line3 position 0, line1 position 1
    """
    longest = utils.get_nested_longest(tableData)

    for i in range(len(tableData[0])):
        for line in tableData:
            print(line[i].rjust(longest + 1), end="")
        print("")


if __name__ == "__main__":
    main()
