def parse_file(input_file):
    #Take an input file and parses each line to an index in a list, trimming white space
    file_list = input_file.readlines()
    for index, line in enumerate(file_list):
        line = line.strip()
        file_list[index] = line
    return file_list
