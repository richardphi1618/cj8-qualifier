from typing import Any, List, Optional
import copy

TOP = "┌┬┐"
MID = "├┼┤"
BOT = "└┴┘"
BAR = "│"
LINE = "─"

def join_l(l, sep):
    """Join list with seperator"""
    li = iter(l)
    string = str(next(li))
    for i in li:
        string += str(sep) + str(i)
    return string


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`). All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """

    # Setup ################################################

    debug = False  # this is for troubleshooting code

    consolidated: List[Any] = copy.deepcopy(rows[:])  # copies source to new object

    labels_temp: List[Any] = []

    if labels != None:
        labels_temp: list[Any] = copy.deepcopy(labels[:])

    if labels:
        consolidated.insert(0, labels_temp)
    if debug:
        print(consolidated)

    width_of_grid: int = len(consolidated[0])

    # Find Largest ##########################################

    largest_entry: list[str] = [""] * width_of_grid

    for i in consolidated:
        for x in range(0, width_of_grid):
            a = len(str(i[x]))
            b = len(largest_entry[x])
            if a > b:
                largest_entry[x] = str(i[x])

    # Adjust Entries to Match Largest ###############################

    for row_index, x in enumerate(consolidated):
        for col_index, y in enumerate(x):
            
            if y is not int:
                y = str(y)

            if len(y) < len(str(largest_entry[col_index])):
                if centered:
                    # centered
                    consolidated[row_index][col_index] = y.center(len(largest_entry[col_index]), " ")
                else:
                    # left adjusted
                    consolidated[row_index][col_index] = y.ljust(len(largest_entry[col_index]), " ")

    rows_joined = []
    for index, x in enumerate(consolidated):
        rows_joined.append("│ " + join_l(consolidated[index], " │ ") + " │")

    # Make Top and Bottom ##########################################
    # ┌────────────┬───────────┬─────────┐
    top = []
    for i in range(width_of_grid):
        top.append("─" * (len(largest_entry[i]) + 2) + "┬")
    top[width_of_grid - 1] = top[width_of_grid - 1].replace("┬", "")

    if debug:
        print("┌" + "".join(top) + "┐")

    # └────────────┴───────────┴─────────┘
    bottom = []
    for i in range(width_of_grid):
        bottom.append("─" * (len(largest_entry[i]) + 2) + "┴")
    bottom[width_of_grid - 1] = bottom[width_of_grid - 1].replace("┴", "")

    if debug:
        print("└" + "".join(bottom) + "┘")

    # Make Seperator ##########################################
    # ├────────────┼───────────┼─────────┤
    seperator: list[Any] = []
    if labels != None:
        for i in range(width_of_grid):
            seperator.append("─" * (len(largest_entry[i]) + 2) + "┼")
        seperator[width_of_grid - 1] = seperator[width_of_grid - 1].replace("┼", "")

        if debug:
            print("├" + "".join(seperator) + "┤")

    rows_joined.insert(0, "┌" + "".join(top) + "┐")
    if labels:
        rows_joined.insert(2, "├" + "".join(seperator) + "┤")
    rows_joined.append("└" + "".join(bottom) + "┘")

    # Final #########################################################

    for i in rows_joined:
        if debug:
            print(i)

    output = "\n".join(rows_joined)

    if debug:
        print(f"labels: {labels}")
    if debug:
        print(f"rows: {rows}")

    return output


if __name__ == "__main__":
    rows = [["Apple", 5, 70]]
    labels = ["Fruit", "Tastiness", "Sweetness"]
    table = make_table(rows, labels)

    print(table)
