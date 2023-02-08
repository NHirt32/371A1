import knapsack_item
from cell import *
from knapsack_item import *
# Methods for solving the knapsack problem


def solve_01_knapsack(capacity, item_list):
    item_list.insert(0, knapsack_item.item(0, 0, 0))
    capacities = range(0, capacity + 1)

    table = init_table(capacity + 1, len(item_list))

    for row in range(0, len(item_list)):
        for col in capacities:

            item = item_list[row]

            # If it fits
            if item.weight <= col:

                # If its more valuable
                if item.price + table[row - 1][col - item.weight].value > table[row - 1][col].value:
                    # set price
                    table[row][col].value = table[row -
                                                  1][col - item.weight].value + item.price
                    # set items
                    table[row][col].items = table[row -
                                                  1][col - item.weight].items.copy()

                    # add to cell's collection of items
                    table[row][col].items.append(item)

                else:
                    table[row][col] = table[row - 1][col]
            else:
                table[row][col] = table[row - 1][col]

    return table

# Initializes a table with cells,


def init_table(capacity, item_list_size):
    table = []

    for row in range(0, item_list_size):
        record = []
        table.append(record)

        # Empty cell.
        for col in range(0, capacity):
            table[row].append(Cell([]))

    return table

# returns table string


def table_string(table):
    string = ""
    maximum = Cell([])
    for row in range(len(table)):
        string = string + "\n"
        for col in range(len(table[row])):
            string = string + '\t' + str(table[row][col].value) + " "
            if table[row][col].value > maximum.value:
                maximum = table[row][col]

    string = string + "\nThe max value is: " + str(maximum.value) + "\n"
    string = string + "\nThe IDs of the items for the max value are: " + "\n"
    for item in maximum.items:
        string = string + str(item.ID) + "\n"

    string = string + "\n"

    return string
