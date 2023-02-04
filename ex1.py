import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Style

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
DIALOGUE_FONT = ("Consolas", 18)
SELECTION_FONT = ("Consolas", 12)
FRAME_PADDING_X = (WIDTH/50, WIDTH/40)
FRAME_PADDING_Y = (HEIGHT/50, HEIGHT/11)

# ============================================================================ #
# Window Variables
output_file = ""
input_file = ""
algorithm_code = 0

# ============================================================================ #
# Window Functions


def select_output():
    output_file = filedialog.askopenfile(
        initialdir="/", title="Select an Output File", filetypes=[("Text files", "*.txt*")])
    output_label.config(text=output_file.name, bg=MENU_COLOR, padx=10)
    output_label.update()


def select_input():
    input_file = filedialog.askopenfile(
        initialdir="/", title="Select an Input File", filetypes=[("Text files", "*.txt*")])
    input_label.config(text=input_file.name, bg=MENU_COLOR, padx=10)
    input_label.update()


def knap_sack():
    print("KnapSack")


def knap_sack_01():
    print("KnapSack 0-1")


def knap_sack_con():
    print("KnapSack with constraints")


def compute_all():
    print("All Knapsack Problems.")


# ============================================================================ #
# Window Attributes
root.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, 0, 0))
root.config(bg=MENU_COLOR)
root.title("Assignment 1: Knapsack Problem")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)

# ============================================================================ #
# selection_frame Attributes
selection_frame = tk.Frame(root, bg=SELECTION_COLOR)
selection_frame.grid(row=0, column=0, padx=(WIDTH/50, WIDTH/130),
                     pady=FRAME_PADDING_Y, sticky="nsew")
selection_frame.grid_columnconfigure(0, weight=1)

selection_frame.update()
BUTTON_WIDTH = int(selection_frame.winfo_width()/15)

selection_label = tk.Label(
    selection_frame, bg=SELECTION_COLOR, text="Assignment 1: Knapsack Problem")
selection_label.config(
    font=(DIALOGUE_FONT[0], DIALOGUE_FONT[1], 'underline'), foreground=LIGHT_ACCENT,)
selection_label.grid(padx=5, pady=(15, 5))

# Input File Select
input_btn = tk.Button(
    selection_frame, text="Select input", command=select_input, width=BUTTON_WIDTH, bg=BUTTON_COLOR, foreground=LIGHT_ACCENT, font=SELECTION_FONT)
input_btn.grid(padx=5, pady=5)

input_label = tk.Label(selection_frame, text=input_file)
input_label.config(bg=SELECTION_COLOR, font=SELECTION_FONT,
                   foreground=LIGHT_ACCENT)
input_label.grid(padx=5, pady=5)

# Define Export Label/Button
export_label = tk.Label(selection_frame, text="File Exporting Options")
export_label.config(bg=SELECTION_COLOR, font=(DIALOGUE_FONT[0], DIALOGUE_FONT[1], 'underline'),
                    foreground=LIGHT_ACCENT)
export_label.grid(padx=5, pady=(10, 5))

# Output File Select
output_btn = tk.Button(
    selection_frame, text="Select Output", command=select_output,
    width=BUTTON_WIDTH, bg=BUTTON_COLOR, foreground=LIGHT_ACCENT, font=SELECTION_FONT)
output_btn.grid(padx=5, pady=5)

output_label = tk.Label(selection_frame, text=output_file)
output_label.config(bg=SELECTION_COLOR, font=SELECTION_FONT,
                    foreground=LIGHT_ACCENT)
output_label.grid(padx=5, pady=5)


# Algorithm Selection Radio
algorithm_label = tk.Label(
    selection_frame, text="Knapsack Problem Variant", bg=SELECTION_COLOR)
algorithm_label.config(
    font=(DIALOGUE_FONT[0], DIALOGUE_FONT[1], 'underline'), foreground=LIGHT_ACCENT)
algorithm_label.grid(padx=5, pady=(10, 5))

algorithmn_values = [("Part I: Knapsack 0-1", knap_sack), ("Part II: General Knapsack", knap_sack_01),
                     ("Part III: Knapsack 0-1 With Constraints", knap_sack_con), ("Compute All", compute_all)]

for (btn_text, command) in algorithmn_values:
    tk.Button(selection_frame, text=btn_text, command=command,
              width=BUTTON_WIDTH, bg=BUTTON_COLOR, foreground=LIGHT_ACCENT,
              font=SELECTION_FONT).grid(padx=10, pady=10)


desc_label = tk.Label(selection_frame, text="Quick Instructions", bg=SELECTION_COLOR,
                      font=(DIALOGUE_FONT[0], DIALOGUE_FONT[1], 'underline'), foreground=LIGHT_ACCENT)
desc_label.grid(padx=5, pady=(10, 5))

desc_text = tk.Text(selection_frame, bg=MENU_COLOR,
                    width=int(BUTTON_WIDTH*1.5), height=(BUTTON_WIDTH/2), foreground=LIGHT_ACCENT, borderwidth=0, highlightthickness=0)
desc_text.insert(
    tk.INSERT, "Sample text about how to use the program...........")
desc_text.grid(padx=5, pady=5)
desc_text.configure(state='disabled')

# ============================================================================ #

# dialogue_frame Attributes
dialogue_frame = tk.Frame(
    root, bg=MENU_COLOR, borderwidth=0, highlightthickness=0)
dialogue_frame.grid(row=0, column=1, padx=FRAME_PADDING_X,
                    pady=FRAME_PADDING_Y, sticky="nsew")
dialogue_frame.grid_columnconfigure(0, weight=1)
dialogue_frame.grid_rowconfigure(0, weight=1)

# Define Scroll bar
vertical_scroll = tk.Scrollbar(dialogue_frame, orient='vertical')
vertical_scroll.grid(row=0, column=1, sticky="ns")


# Define Dialogue Window
result_box = tk.Text(dialogue_frame, bg=SELECTION_COLOR,
                     padx=10, pady=10, borderwidth=0, highlightthickness=0,
                     yscrollcommand=vertical_scroll.set)
result_box.config(font=DIALOGUE_FONT, foreground=LIGHT_ACCENT)
result_box.insert(tk.INSERT, "**Problem Output**")
result_box.grid(row=0, column=0, sticky="nsew")

# Attach Scroll bar
vertical_scroll.config(command=result_box.yview)

# result_box.configure(state='disabled')
# ============================================================================ #

root.mainloop()
