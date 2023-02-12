import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Style
from knapsackProblems import *

import parse
from knapsack_item import item

root = tk.Tk()
# ============================================================================ #
# Window Constants

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
MENU_COLOR = "#0d1b2a"
SELECTION_COLOR = "#1b263b"
DIALOGUE_COLOR = "#0d1b2a"
BUTTON_COLOR = "#1b4965"
DARK_ACCENT = "#000814"
LIGHT_ACCENT = "#00b4d8"
DIALOGUE_FONT = ("Cambria", 18)
SELECTION_FONT = ("Cambria", 14)
FRAME_PADDING_X = (WIDTH/50, WIDTH/40)
FRAME_PADDING_Y = (HEIGHT/50, HEIGHT/11)

# ============================================================================ #
# Window Variables
output_file = open("dynamicTable.txt", 'w')
input_file = open("SampleKnapsackData.txt")
algorithm_code = 0
capacity = 0  # Variable used to store KP capacity


# ============================================================================ #
# Window Functions


def select_output():
    # Opens dialogue window to select and set the output file
    output_file = filedialog.askopenfile(
        initialdir="/",
        title="Select an Output File",
        filetypes=[("Text files", "*.txt*")])
    if output_file is None:
        output_file = open("dynamicTable.txt", 'w')
    output_label.config(text=output_file.name, bg=MENU_COLOR, padx=10)
    output_label.update()


def select_input():
    # Opens dialogue window to select and set the input file
    global input_file  # input_file needs to be global for it to be associated with outside value
    prev_input = input_file.name
    input_file = filedialog.askopenfile(
        initialdir="/",
        title="Select an Input File",
        filetypes=[("Text files", "*.txt*")])
    if input_file is None:
        input_file = open(prev_input)
    input_label.config(text=input_file.name, bg=MENU_COLOR, padx=10)
    input_label.update()


def knap_sack_01():
    # Runs the code to solve the 0-1 Knapsack problem
    #global capacity

    append_dialogue("0-1 KnapSack\n")

    parsed_list = parse.parse_file(input_file)
    capacity = int(parsed_list[0])
    append_dialogue("Our Knapsacks weight capacity is: " +
                    str(capacity) + "\n")
    item_list = parse.object_list(parsed_list[1:])
    # Debug printing loop
    for index, element in enumerate(item_list):
        print("The item's ID at index " + str(index) +
              " is " + str(element.get_ID()))
        print("The item's weight at weight " + str(index) +
              " is " + str(element.get_weight()))
        print("The item's price at index " + str(index) +
              " is " + str(element.get_price()))

    table = str(table_string(solve_01_knapsack(capacity, item_list)))

    append_dialogue(table)
    append_dialogue("="*60 + "\n\n")

    # Print the contents to the file
    clear_output()
    print_to_output()


def knap_sack():
    # Runs the code to solve the Unbounded Knapsack problem
    #global capacity

    append_dialogue("Unbounded KnapSack\n")

    parsed_list = parse.parse_file(input_file)
    capacity = int(parsed_list[0])
    append_dialogue("Our Knapsacks weight capacity is: " +
                    str(capacity) + "\n")
    item_list = parse.object_list(parsed_list[1:])
    # Debug printing loop
    for index, element in enumerate(item_list):
        print("The item's ID at index " + str(index) +
              " is " + str(element.get_ID()))
        print("The item's weight at weight " + str(index) +
              " is " + str(element.get_weight()))
        print("The item's price at index " + str(index) +
              " is " + str(element.get_price()))

    table = str(table_string(solve_unbounded_knapsack(capacity, item_list)))

    append_dialogue(table)
    append_dialogue("="*60 + "\n\n")

    # Print the contents to the file
    clear_output()
    print_to_output()


def knap_sack_con():
    # Runs the code to solve the Knapsack problem with constraints
    append_dialogue("KnapSack with constraints\n")


def compute_all():
    # Runs the code to solve all of the knapsack problems
    append_dialogue("All Knapsack Problems.\n")

    parsed_list = parse.parse_file(input_file)
    capacity = int(parsed_list[0])
    append_dialogue("Our Knapsacks weight capacity is: " +
                    str(capacity) + "\n")
    item_list = parse.object_list(parsed_list[1:])
    # Debug printing loop
    for index, element in enumerate(item_list):
        print("The item's ID at index " + str(index) +
              " is " + str(element.get_ID()))
        print("The item's weight at weight " + str(index) +
              " is " + str(element.get_weight()))
        print("The item's price at index " + str(index) +
              " is " + str(element.get_price()))

    append_dialogue("Knapsack 0-1")
    table = str(table_string(solve_01_knapsack(capacity, item_list)))
    append_dialogue(table)
    append_dialogue("="*60 + "\n\n")

    append_dialogue("General Unbounded Knapsack")
    table = str(table_string(solve_unbounded_knapsack(capacity, item_list)))
    append_dialogue(table)
    append_dialogue("="*60 + "\n\n")

    # Print the contents to the file
    clear_output()
    print_to_output()


def print_to_output():
    # Prints the str input to the output file
    output_file.write(result_box.get(1.0, "end-1c"))


def clear_output():
    # Deletes the contents of the output file
    output_file.truncate(0)


def append_dialogue(text):
    # Appends the text field to the output dialogue window
    result_box.configure(state='normal')
    result_box.insert(tk.INSERT, text)
    result_box.configure(state='disabled')
    result_box.update()


def clear_dialogue():
    # Clears the input dialogue window
    result_box.configure(state='normal')
    result_box.delete('1.0', tk.END)
    result_box.configure(state='disabled')


# ============================================================================ #
# Window Attributes
root.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, 0, 0))
root.config(bg=MENU_COLOR)
root.title("Assignment 1: Knapsack Problem")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)
root.resizable(False, False)

# ============================================================================ #
# selection_frame Attributes - stores all of the selection settings
selection_frame = tk.Frame(root, bg=SELECTION_COLOR)
selection_frame.grid(row=0,
                     column=0,
                     padx=(WIDTH/50, WIDTH/130),
                     pady=FRAME_PADDING_Y,
                     sticky="nsew")
selection_frame.grid_columnconfigure(0, weight=1)
selection_frame.update()


BUTTON_WIDTH = int(selection_frame.winfo_width()/15)


# Selection Frame Label - Labels the selection frame
selection_label = tk.Label(selection_frame,
                           bg=SELECTION_COLOR,
                           text="Assignment 1: Knapsack Problem",
                           font=(DIALOGUE_FONT[0],
                                 DIALOGUE_FONT[1],
                                 'underline'),
                           foreground=LIGHT_ACCENT,)
selection_label.grid(padx=5, pady=(15, 5))


# Input Select Button - Allows input file to be selected
input_btn = tk.Button(selection_frame,
                      text="Select input",
                      command=select_input,
                      width=BUTTON_WIDTH,
                      bg=BUTTON_COLOR,
                      foreground=LIGHT_ACCENT,
                      font=SELECTION_FONT)
input_btn.grid(padx=5, pady=5)


# Input File Label - Displays current input file
input_label = tk.Label(selection_frame,
                       text=input_file.name,
                       bg=SELECTION_COLOR,
                       font=SELECTION_FONT,
                       foreground=LIGHT_ACCENT)
input_label.grid(padx=5, pady=5)


# Output Select Button - Allows output file to be selected
output_btn = tk.Button(selection_frame,
                       text="Select Output",
                       command=select_output,
                       width=BUTTON_WIDTH,
                       bg=BUTTON_COLOR,
                       foreground=LIGHT_ACCENT,
                       font=SELECTION_FONT)
output_btn.grid(padx=5, pady=5)


# Output File Label - Displays current output file
output_label = tk.Label(selection_frame,
                        text=output_file.name,
                        bg=SELECTION_COLOR,
                        font=SELECTION_FONT,
                        foreground=LIGHT_ACCENT)
output_label.grid(padx=5, pady=5)


# Label denoting Available algorithm problems
algorithm_label = tk.Label(selection_frame,
                           text="Knapsack Problem Variant",
                           bg=SELECTION_COLOR,
                           font=(DIALOGUE_FONT[0],
                                 DIALOGUE_FONT[1],
                                 'underline'),
                           foreground=LIGHT_ACCENT)
algorithm_label.grid(padx=5, pady=(10, 5))

# List of tuples containing the name of each knapsack problem variant, and the
# problem's associated function
algorithmn_values = [("Part I: Knapsack 0-1", knap_sack_01),
                     ("Part II: General Knapsack", knap_sack),
                     ("Part III: Knapsack 0-1 With Constraints", knap_sack_con),
                     ("Compute All", compute_all)]


# Create all of the algorithm buttons
for (btn_text, command) in algorithmn_values:
    tk.Button(selection_frame, text=btn_text, command=command,
              width=BUTTON_WIDTH,
              bg=BUTTON_COLOR,
              foreground=LIGHT_ACCENT,
              font=SELECTION_FONT).grid(padx=10, pady=10)


# Label Denoting Quick Start Section
desc_label = tk.Label(selection_frame, text="Quick Instructions",
                      bg=SELECTION_COLOR,
                      font=(DIALOGUE_FONT[0], DIALOGUE_FONT[1], 'underline'),
                      foreground=LIGHT_ACCENT)
desc_label.grid(padx=5, pady=(10, 5))


# Quick Start Dialogue Window
desc_text = tk.Text(selection_frame,
                    bg=MENU_COLOR,
                    width=int(BUTTON_WIDTH*1.5),
                    height=(BUTTON_WIDTH/2),
                    foreground=LIGHT_ACCENT,
                    borderwidth=0,
                    highlightthickness=0)


# Adding Quick Start Text
desc_text.insert(tk.INSERT,
                 "Sample text about how to use the program...........")
desc_text.grid(padx=5, pady=5)
desc_text.configure(state='disabled')

# ============================================================================ #


# Create Dialogue Frame - Used to store program output and errors
dialogue_frame = tk.Frame(root,
                          bg=MENU_COLOR,
                          borderwidth=0,
                          highlightthickness=0)
dialogue_frame.grid(row=0, column=1, padx=FRAME_PADDING_X,
                    pady=FRAME_PADDING_Y, sticky="nsew")
dialogue_frame.grid_columnconfigure(0, weight=1)
dialogue_frame.grid_rowconfigure(0, weight=1)


# Create Vertical Scroll bar
vertical_scroll = tk.Scrollbar(dialogue_frame,
                               orient='vertical')
vertical_scroll.grid(row=0, column=1, sticky="ns")


# Create Dialogue Window
result_box = tk.Text(dialogue_frame,
                     bg=SELECTION_COLOR,
                     padx=10,
                     pady=10,
                     borderwidth=0,
                     highlightthickness=0,
                     yscrollcommand=vertical_scroll.set)
result_box.config(font=DIALOGUE_FONT, foreground=LIGHT_ACCENT)
result_box.grid(row=0, column=0, sticky="nsew")


# Bind Vertical Scroll Bar
vertical_scroll.config(command=result_box.yview)
result_box.configure(state='disabled')

# ============================================================================ #

root.mainloop()
