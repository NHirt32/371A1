import knapsack_item
from cell import *
# Methods for solving the knapsack problem


def solve_01_knapsack(capacity, item_list):
    item_list.insert(0, knapsack_item.item(0, 0, 0))
    capacities = range(0, capacity + 1)

    table = init_table(capacity + 1, len(item_list))

    maximum = Cell([])

    for row in range(0, len(item_list)):
        for col in capacities:

            item = item_list[row]

            # If it fits
            if item.weight <= col:

                # If its more valuable
                if item.price + table[row - 1][col - item.weight].value > table[row - 1][col].value:
                    # set price
                    table[row][col].value = table[row - 1][col - item.weight].value + item.price
                    # set weight
                    table[row][col].weight = table[row - 1][col - item.weight].weight + item.weight
                    # set items
                    table[row][col].items = table[row - 1][col - item.weight].items.copy()

                    # add to cell's collection of items
                    table[row][col].items.append(item)

                    # dynamically set our returned best solution.
                    if maximum.value < table[row][col].value:
                        maximum = Cell(table[row][col].items)

                else:
                    table[row][col] = table[row - 1][col]
            else:
                table[row][col] = table[row - 1][col]

    table_info = (table, maximum)
    return table_info


def solve_unbounded_knapsack(capacity, item_list):
    item_list.insert(0, knapsack_item.item(0, 0, 0))
    capacities = range(0, capacity + 1)
    table = init_table(capacity + 1, len(item_list))

    maximum = Cell([])

    list = [0 for i in range(capacity + 1)]
    for col in range(capacity + 1):
        for row in range(len(item_list)):
            item = item_list[row]
            weight = item_list[row].weight
            value = item_list[row].price
            if weight <= col:
                list[col] = max(list[col], list[col-weight] + value)

                if table[row-1][col].value < table[row][col-weight].value + value:
                    table[row][col].value = table[row][col - weight].value + value
                    table[row][col].weight = table[row][col - weight].weight + weight
                    table[row][col].items = table[row][col - weight].items.copy()
                    table[row][col].items.append(item)

                    if maximum.value < table[row][col].value:
                        maximum = Cell(table[row][col].items)

                else:
                    table[row][col] = table[row-1][col]

            else:
                table[row][col] = table[row-1][col]
    print(list)
    returner = (table, maximum)
    return returner


def solve_01_knapsack_constraints(capacity, item_list):
    item_list.insert(0, knapsack_item.item(0, 0, 0))
    capacities = range(0, capacity + 1)
    maximum = Cell([])

    table = init_table(capacity + 1, len(item_list))

    for row in range(0, len(item_list)):
        for col in capacities:

            item = item_list[row]

            # If it fits
            if item.weight <= col:

                # If its more valuable
                if item.price + table[row - 1][col - item.weight].value > table[row - 1][col].value:
                    # set price
                    table[row][col].value = table[row - 1][col - item.weight].value + item.price
                    # set weight
                    table[row][col].weight = table[row - 1][col - item.weight].weight + item.weight
                    # set items
                    table[row][col].items = table[row - 1][col - item.weight].items.copy()

                    # add to cell's collection of items
                    table[row][col].items.append(item)

                    # dynamically set our returned best solution, add cases for the constraints.
                    if maximum.value < table[row][col].value:
                        if table[row][col].value % 2 == 0:
                            if table[row][col].weight % 2 == 1:
                                maximum = Cell(table[row][col].items)

                else:
                    table[row][col] = table[row - 1][col]
            else:
                table[row][col] = table[row - 1][col]

    table_info = (table, maximum)
    return table_info


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


# Returns table string. Takes a table_info tuple.
def table_string(table_info):
    string = ""
    maximum = Cell([])
    for row in range(len(table_info[0])):
        string = string + "\n"
        for col in range(len(table_info[0][row])):
            string = string + '\t' + str(table_info[0][row][col].value) + " "

    string = string + "\nThe max value is: " + str(table_info[1].value) + "\n"
    string = string + "\nThe IDs of the items for the max value are: " + "\n"
    for item in table_info[1].items:
        string = string + str(item.ID) + "\n"

    string = string + "\n"

    return string
