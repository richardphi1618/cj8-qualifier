from typing import Any, List, Optional
from terminaltables import SingleTable

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:

    example_table = rows
    example_table.insert(0,labels)

    table_instance = SingleTable(example_table)
    if centered:
        for i in range(0, len(labels)):
            table_instance.justify_columns[i] = 'center'
            print(i)
    print(table_instance.table)

    return None

if __name__ == "__main__":

    rows = [
        ["Apple", 5, 70, "Red", 76],
        ["Banana", 3, 5, "Yellow", 8],
        ["Cherry", 7, 31, "Red", 92],
        ["Kiwi", 4, 102, "Green", 1],
        ["Strawberry", 6, 134, "Red", 28]
    ]
    labels = ["Fruit", "Tastiness", "Sweetness", "Colour", "Smell"]
    centered = False

    table = make_table(rows, labels, centered)
    print(table)

    
