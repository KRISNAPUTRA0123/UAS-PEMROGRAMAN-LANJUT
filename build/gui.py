
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, font, ttk, colorchooser
import tkinter.font as font 

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ASUS\Desktop\Tugas Kuliah Krisna\UAS PEMROGRAMAN LANJUT\Tkinter-Designer-master\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title('Teks Editor')
window.geometry("700x450")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 450,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    350.0,
    39.0,
    image=image_image_1
)

entry_image_1 = tk.PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(350.0, 268.5, image=entry_image_1)

entry_1 = tk.Text(
    window, font=('arial', 12)  # Enable word wrapping
)
entry_1.place(x=0.0, y=80.0, width=700.0)

def saveFile():
    """Saves the content of the entry_1 widget to a user-selected file."""

    # Open a file dialog for user selection
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text File", ".txt"), ("All files", ".*")])

    # Check if the user selected a file
    if file is not None:
        # Open the selected file in append mode with proper encoding (UTF-8)
        with open(file.name, 'a', encoding='utf-8') as f:
            # Get the text content from the entry_1 widget
            text_to_save = entry_1.get(0.0, END)  # Get all text (1.0 refers to the beginning)
            # Write the text content to the file
            f.write(text_to_save)

            # Display a success message
            message = tk.messagebox.showinfo(title="Success!", message="Data saved successfully.")
            file.close()

    else:
        # Display a message if user cancels the selection
        message = tk.messagebox.showinfo(title="No File Selected", message="Please select a file to save.")
        file.close()

button_image_1 = tk.PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= saveFile,
    relief="flat"
)
button_1.place(
    x=16.0,
    y=10.0,
    width=15.0,
    height=15.0
)

def openFile():
    """Opens a text file and displays its content in the entry_1 widget."""

    # Open a file dialog for user selection
    file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text File", ".txt"), ("All files", ".*")])

    # Check if the user selected a file
    if file is not None:
        # Read the selected file contents
        with open(file.name, 'r', encoding='utf-8') as f:
            text_to_display = f.read()

        # Clear the existing text in the entry_1 widget
        entry_1.delete("1.0", tk.END)

        # Insert the read text into the entry_1 widget
        entry_1.insert(tk.END, text_to_display)

        # Display a success message
        message = tk.messagebox.showinfo(title="Success!", message="File opened and displayed successfully.")
        file.close()

    else:
        # Display a message if user cancels the selection
        message = tk.messagebox.showinfo(title="No File Selected", message="Please select a file to open.")
        file.close()
   

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= openFile,
    relief="flat"
)
button_2.place(
    x=35.0,
    y=10.0,
    width=15.0,
    height=15.0
)

def exit():
    """Exits the application after asking for confirmation."""

    # Ask the user for confirmation before exiting
    response = tk.messagebox.askyesno(title="Exit Confirmation", message="Are you sure you want to exit?")

    # Check the user's response
    if response:
        # Destroy the main window (assuming it's already defined globally as `root`)
        window.destroy()
        print("Exiting the application...")  # Optional message

# Create the main Tkinter window (assuming it's not defined elsewhere)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command= exit,
    relief="flat"
)

button_3.place(
    x=54.0,
    y=10.0,
    width=15.0,
    height=15.0
)

canvas.create_text(
    319.0,
    10.0,
    anchor="nw",
    text="Text Editor ",
    fill="#000000",
    font=("Inter", 12 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    281.0,
    52.0,
    image=image_image_2
)

def make_underline():
    underline_font = font.Font(entry_1, entry_1.cget("font"))
    underline_font.configure(underline=True)

    entry_1.tag_configure("underline", font=underline_font)
    current_tags = entry_1.tag_names("sel.first")

    if "underline" in current_tags:
        entry_1.tag_remove("underline", "sel.first", "sel.last")
    else:
        entry_1.tag_add("underline", "sel.first", "sel.last")

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=make_underline,
    relief="flat"
)
button_5.place(
    x=280.0,
    y=39.0,
    width=27.0,
    height=26.0
)

def make_italic():
    italics_font = font.Font(entry_1, entry_1.cget("font"))
    italics_font.configure(slant="italic")

    entry_1.tag_configure("italic", font=italics_font)
    current_tags = entry_1.tag_names("sel.first")

    if "italic" in current_tags:
        entry_1.tag_remove("italic", "sel.first", "sel.last")
    else:
        entry_1.tag_add("italic", "sel.first", "sel.last")

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=make_italic,
    relief="flat"
)
button_6.place(
    x=254.0,
    y=39.0,
    width=27.0,
    height=26.0
)

def align_left():
    data = entry_1.get(0.0, END)
    entry_1.tag_config('left',justify=LEFT)
    entry_1.delete(0.0, END)
    entry_1.insert(INSERT, data, 'left')

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command= align_left,
    relief="flat"
)
button_7.place(
    x=350.0,
    y=43.0,
    width=22.0,
    height=17.0
)

def align_center():
    data = entry_1.get(0.0, END)
    entry_1.tag_config('center',justify=CENTER)
    entry_1.delete(0.0, END)
    entry_1.insert(INSERT, data, 'center')

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command= align_center,
    relief="flat"
)
button_8.place(
    x=387.0,
    y=43.0,
    width=22.0,
    height=17.0
)

def align_right():
    data = entry_1.get(0.0, END)
    entry_1.tag_config('right',justify=RIGHT)
    entry_1.delete(0.0, END)
    entry_1.insert(INSERT, data, 'right')

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=align_right,
    relief="flat"
)
button_9.place(
    x=424.0,
    y=43.0,
    width=22.0,
    height=17.0
)


def align_justify():
    data = entry_1.get(0.0, END)
    entry_1.tag_config('justify',justify=LEFT)
    entry_1.delete(0.0, END)
    entry_1.insert(INSERT, data, 'justify')

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=align_justify,
    relief="flat"
)
button_10.place(
    x=461.0,
    y=43.0,
    width=22.0,
    height=17.0
)

def font_color():
    color=colorchooser.askcolor()
    entry_1.config(fg=color[1])

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command= font_color,
    relief="flat"
)
button_11.place(
    x=306.0,
    y=39.0,
    width=27.0,
    height=26.0
)

fontSize = 12
fontStyle = 'arial'

def update_font(event):
  global fontSize, fontStyle
  fontStyle = font_family_variable.get()
  fontSize = size_variable.get()
  entry_1.config(font=(fontStyle, fontSize))

# FONT FAMILIES
font_families = font.families()
font_family_variable = StringVar(value=fontStyle)  # Pre-set with initial style
font_family_dropdown = ttk.Combobox(window, width=17, values=font_families, state='readonly', textvariable=font_family_variable)
font_family_dropdown.current(font_families.index('Arial'))
font_family_dropdown.place(x=16.0, y=42.0)

# FONT SIZE
size_variable = IntVar(value=fontSize)  # Pre-set with initial size
font_size_dropdown = ttk.Combobox(window, width=8, textvariable=size_variable, state='readonly', values=tuple(range(8, 80)))
font_size_dropdown.current(4)
font_size_dropdown.place(x=148.0, y=42.0)

# JARAK ANTAR BARIS (line spacing)
baris_variable = ["KARYA BY", "1. KRISNA PUTRA NUR QODRI", "2. FAAZA FEBRIYAN ARRIFQI", "3. MOH HARUN"]
baris_variable_dropdown = ttk.Combobox(window, width=24, textvariable=baris_variable, state='readonly', values=baris_variable)
baris_variable_dropdown.current(baris_variable.index("KARYA BY"))
baris_variable_dropdown.place(x=500.0, y=42.0)

# Bind to a single function for both font style and size updates
font_family_dropdown.bind('<<ComboboxSelected>>', update_font)
font_size_dropdown.bind('<<ComboboxSelected>>', update_font)

def make_bold():
    bold_font = font.Font(entry_1, entry_1.cget("font"))
    bold_font.configure(weight="bold")

    entry_1.tag_configure("bold", font=bold_font)
    current_tags = entry_1.tag_names("sel.first")

    if "bold" in current_tags:
        entry_1.tag_remove("bold", "sel.first", "sel.last")
    else:
        entry_1.tag_add("bold", "sel.first", "sel.last")

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command= make_bold,
    relief="flat"
)
button_4.place(
    x=228.0,
    y=39.0,
    width=27.0,
    height=26.0
)

window.resizable(False, False)
window.mainloop()
