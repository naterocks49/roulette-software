import tkinter as tk
from functions import find_equivalent, grab_spins, add_last_spin, backspace_spin, clear_spins,ex_shared_eq, clean_grab_spins, pretty_eq, pretty_output, filter_num_shared, nonex_shared_eq, replace_with_file
import customtkinter
from tkinter.filedialog import askopenfilename

# Set customtkinter defaults
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Create the main window
root = customtkinter.CTk()
root.geometry("1000x1400")

# Initial last spins list
initial_spins = clean_grab_spins(grab_spins())

# Create a label
label = customtkinter.CTkLabel(master=root, text="Enter the numbers seperated by a space:")
spins_label =  customtkinter.CTkLabel(master=root, text="Enter the last spin:")
number_of_spins_label = customtkinter.CTkLabel(master=root, text="Number of last spins to exclude:")
find_by_num_shared_label = customtkinter.CTkLabel(master=root, text="Filter by MINIMUM number of times shared:")
exclusion_nums_label = customtkinter.CTkLabel(master=root, text='Enter numbers to exclude:')

# Create a text input field
entry = customtkinter.CTkEntry(root)
last_spins = customtkinter.CTkEntry(root)
number_last_spins = customtkinter.CTkEntry(root)
find_by_num_shared = customtkinter.CTkEntry(root)
exclusion_nums = customtkinter.CTkEntry(root)

# Checkboxes
selected_option = tk.BooleanVar()
plus_20_var = tk.BooleanVar()
minus_20_var = tk.BooleanVar()
plus_10_var = tk.BooleanVar()
minus_10_var = tk.BooleanVar()
plus_1_var = tk.BooleanVar()
minus_1_var = tk.BooleanVar()
LEFT_var = tk.BooleanVar()
RIGHT_var = tk.BooleanVar()
SPECIAL_var = tk.BooleanVar()
option = customtkinter.StringVar(value="ALL VALUES")
ignore_inputs_var = tk.BooleanVar()

# Create a checkbox with the BooleanVar as its variable
dropdown = customtkinter.CTkOptionMenu(master=root,  values= ["ALL VALUES", "NON-EXCLUSIVE SHARED", "EXCLUSIVE SHARED"], variable=option)
dropdown.set("ALL VALUES")
plus_20 = customtkinter.CTkCheckBox(master=root, text="+20", variable=plus_20_var)
minus_20 = customtkinter.CTkCheckBox(master=root, text="-20", variable=minus_20_var)
plus_10 = customtkinter.CTkCheckBox(master=root, text="+10", variable=plus_10_var)
minus_10 = customtkinter.CTkCheckBox(master=root, text="-10", variable=minus_10_var)
plus_1 = customtkinter.CTkCheckBox(master=root, text="+1", variable=plus_1_var)
minus_1 = customtkinter.CTkCheckBox(master=root, text="-1", variable=minus_1_var)
LEFT = customtkinter.CTkCheckBox(master=root, text="LEFT", variable=LEFT_var)
RIGHT = customtkinter.CTkCheckBox(master=root, text="RIGHT", variable=RIGHT_var)
SPECIAL = customtkinter.CTkCheckBox(master=root, text="SPECIAL", variable=SPECIAL_var)
ignore_inputs = customtkinter.CTkCheckBox(master=root, text="Ignore Input Values", variable=ignore_inputs_var)

def open_file():
    fn = askopenfilename()

    replace_with_file(fn)

    spins_list = grab_spins()

    spins_list = clean_grab_spins(spins_list)

    lastspinslabel.delete("0.0", "end")
    lastspinslabel.insert("0.0", spins_list)


# Add last spins
def add_spins():

    add_last_spin(last_spins.get())

    spins_list = grab_spins()

    spins_list = clean_grab_spins(spins_list)

    lastspinslabel.delete("0.0", "end")
    lastspinslabel.insert("0.0", spins_list)

# Del last spins
def backspace_spins():

    backspace_spin()

    spins_list = grab_spins()

    spins_list = clean_grab_spins(spins_list)

    lastspinslabel.delete("0.0", "end")
    lastspinslabel.insert("0.0", spins_list)

def clear_spins_func():

    clear_spins()

    spins_list = grab_spins()

    spins_list = clean_grab_spins(spins_list)

    lastspinslabel.delete("0.0", "end")
    lastspinslabel.insert("0.0", spins_list)

def submit():
    if ignore_inputs_var.get():
        ignored_vals = entry.get()
        ignored_vals = [num for num in ignored_vals.split()]
        for i, val in enumerate(ignored_vals):
            ignored_vals[i] = int(val)

        print(ignored_vals)
    else:
        ignored_vals = []

    excluded = exclusion_nums.get()
    excluded = [num for num in excluded.split()]
    for i, val in enumerate(excluded):
            excluded[i] = int(val)

    ignored_vals = ignored_vals + excluded
    print(ignored_vals)
    
    excluded_spins_amount = number_last_spins.get()
    if excluded_spins_amount != '':
        spins = grab_spins()
        excluded_spins = []
        for i in range(int(excluded_spins_amount)):
            excluded_spins.append(int(spins[i]))
    else:
        excluded_spins = []
    
    type_dict = {
        "20": plus_20_var.get(),
        "-20": minus_20_var.get(),
        "10": plus_10_var.get(),
        "-10": minus_10_var.get(),
        "1": plus_1_var.get(),
        "-1": minus_1_var.get(),
        "LEFT": LEFT_var.get(),
        "RIGHT": RIGHT_var.get(),
        "SPECIAL": SPECIAL_var.get()
    }
    
    main_option = option.get()
    if main_option == "EXCLUSIVE SHARED":

        if find_by_num_shared.get():

            equivalent = ex_shared_eq(find_equivalent(entry.get(), type_dict, excluded_spins, ignored_vals))

            equivalent = filter_num_shared(equivalent[0], equivalent[1], int(find_by_num_shared.get()))

            equivalent = pretty_eq(equivalent[0], equivalent[1])

            outputlabel.delete(1.0, tk.END)
            outputlabel.insert(tk.END, equivalent)
        
        else:

            equivalent = ex_shared_eq(find_equivalent(entry.get(), type_dict, excluded_spins, ignored_vals))

            equivalent = pretty_eq(equivalent[0], equivalent[1])

            outputlabel.delete(1.0, tk.END)
            outputlabel.insert(tk.END, equivalent)

    elif main_option == "NON-EXCLUSIVE SHARED":

        if find_by_num_shared.get():

            equivalent = nonex_shared_eq(find_equivalent(entry.get(), type_dict, excluded_spins, ignored_vals))

            equivalent = filter_num_shared(equivalent[0], equivalent[1], int(find_by_num_shared.get()))

            equivalent = pretty_eq(equivalent[0], equivalent[1])

            outputlabel.delete(1.0, tk.END)
            outputlabel.insert(tk.END, equivalent)
        
        else:

            equivalent = nonex_shared_eq(find_equivalent(entry.get(), type_dict, excluded_spins, ignored_vals))

            equivalent = pretty_eq(equivalent[0], equivalent[1])

            outputlabel.delete(1.0, tk.END)
            outputlabel.insert(tk.END, equivalent)
    
    elif main_option == "ALL VALUES":

        equivalent = find_equivalent(entry.get(), type_dict, excluded_spins, ignored_vals)

        equivalent = pretty_output(equivalent)
        outputlabel.delete("0.0", 'end')
        outputlabel.insert("0.0", equivalent)

    

    

# Get last spins
spins_list = grab_spins()

# Create a button
button = customtkinter.CTkButton(master=root, text="Submit", command=submit)
last_spins_add = customtkinter.CTkButton(master=root, text="Enter Last Spin", command=add_spins)
last_spins_backspace = customtkinter.CTkButton(master=root, text="Backspace", command=backspace_spins)
last_spins_clear = customtkinter.CTkButton(master=root, text="Clear spins", command=clear_spins_func)
open_file_button = customtkinter.CTkButton(master=root, text="Replace Last Spins with File", command=open_file)

# Output label
outputlabel = customtkinter.CTkTextbox(master=root,font=("Arial", 18),width=400,height=1200)
lastspinslabel = customtkinter.CTkTextbox(master=root, font=("Arial", 14))
lastspinslabel.insert("0.0", initial_spins)

# Pack the label, entry, and button into the main window
label.grid(row=0, column=0)
entry.grid(row=1, column=0)
spins_label.grid(row=0, column=2)
last_spins.grid(row=1, column=2)
last_spins_add.grid(row=2, column=2)
last_spins_backspace.grid(row=3, column=2)
last_spins_clear.grid(row=4, column=2)
number_of_spins_label.grid(row=5, column=2)
number_last_spins.grid(row=6, column=2)
lastspinslabel.grid(row=7, column=2, rowspan=5)
open_file_button.grid(row=13, column=2)
dropdown.grid(row=2, column=0)
ignore_inputs.grid(row=3, column=0)
find_by_num_shared_label.grid(row=4, column=0)
find_by_num_shared.grid(row=5, column=0)
plus_20.grid(row=6, column=0)
minus_20.grid(row=7, column=0)
plus_10.grid(row=8, column=0)
minus_10.grid(row=9, column=0)
plus_1.grid(row=10, column=0)
minus_1.grid(row=11, column=0)
LEFT.grid(row=12, column=0)
RIGHT.grid(row=13, column=0)
SPECIAL.grid(row=14, column=0)
exclusion_nums_label.grid(row=15, column=0)
exclusion_nums.grid(row=16, column=0)
button.grid(row=17, column=0)
outputlabel.grid(row=0, column=1, rowspan=22, padx=20, pady=20)

# Start the event loop
root.mainloop()