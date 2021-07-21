from typing import Any, List, Optional
import copy


def join_l(l, sep):
    li = iter(l)
    string = str(next(li))
    for i in li:
        string += str(sep) + str(i)
    return string


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """

    # Setup ################################################

    debug = False

    consolidated = copy.deepcopy(rows[:])

    if labels != None:
        labels_temp = copy.deepcopy(labels[:])

    if labels:
        consolidated.insert(0,labels_temp)
    if debug:
        print(consolidated)

    width = len(consolidated[0])

    # Find Largest ##########################################

    largest_entry = ['']*width

    for i in consolidated:
        for x in range(0, width):
            a = len(str(i[x]))
            b = len(largest_entry[x])
            if (a > b):
                largest_entry[x] = str(i[x])

    # Adjust Entries to Match Largest ###############################

    for RowIndex, x in enumerate(consolidated):
        for ColIndex, y in enumerate(x):
            if y is not int:
                y = str(y)
            if len(y) < len(str(largest_entry[ColIndex])):
                if centered:
                    # centered
                    consolidated[RowIndex][ColIndex] = y.center(
                        len(largest_entry[ColIndex]), ' ')
                else:
                    # left adjusted
                    consolidated[RowIndex][ColIndex] = y.ljust(
                        len(largest_entry[ColIndex]), ' ')

    RowsJoined = []
    for index, x in enumerate(consolidated):
        RowsJoined.append("│ " + join_l(consolidated[index], " │ ") + " │")

    # Make Top and Bottom ##########################################

    # ┌────────────┬───────────┬─────────┐
    top = []
    for i in range(width):
        top.append("─"*(len(largest_entry[i])+2) + "┬")
    top[width-1] = top[width-1].replace('┬', '')
    if debug:
        print('┌'+''.join(top)+'┐')

    # └────────────┴───────────┴─────────┘
    bottom = []
    for i in range(width):
        bottom.append("─"*(len(largest_entry[i])+2) + "┴")
    bottom[width-1] = bottom[width-1].replace('┴', '')
    if debug:
        print('└'+''.join(bottom)+'┘')

    # ├────────────┼───────────┼─────────┤

    if labels != None:
        seperator = []

        for i in range(width):
            seperator.append("─"*(len(largest_entry[i])+2) + "┼")
        seperator[width-1] = seperator[width-1].replace('┼', '')
        if debug:
            print('├'+''.join(seperator)+'┤')

    RowsJoined.insert(0, '┌'+''.join(top)+'┐')
    if labels:
        RowsJoined.insert(2, '├'+''.join(seperator)+'┤')
    RowsJoined.append('└'+''.join(bottom)+'┘')
    #################################################################

    # Final #########################################################

    for i in RowsJoined:
        if debug:
            print(i)

    output = '\n'.join(RowsJoined)

    #################################################################

    if debug:
        print(f'labels: {labels}')
    if debug:
        print(f'rows:  {rows}')

    return output


if __name__ == "__main__":


    rows = [
        ["Apple", 5, 70]
    ]
    labels = ["Fruit", "Tastiness", "Sweetness"]
    table = make_table(rows, labels)

    print(table)
