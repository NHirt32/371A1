from knapsack_item import item


def parse_file(input_file):
    # Take an input file and parses each line to an index in a list, trimming white space
    input_file = open(input_file.name)
    file_list = input_file.readlines()
    for index, line in enumerate(file_list):
        line = line.strip()
        file_list[index] = line
    return file_list


def object_list(initial_list):
    # This method is designed to take a list, split it's elements to distinguish between item attributes, and create a list of item objects
    item_list = []

    # Each index changes from a series of numbers to a list that contains each number
    for index, element in enumerate(initial_list):
        white_space_removed = element.split()
        print(white_space_removed[0] +
              white_space_removed[1] + white_space_removed[2])
        new_item = item(
            white_space_removed[0], white_space_removed[1], white_space_removed[2])
        item_list.append(new_item)

    return item_list
