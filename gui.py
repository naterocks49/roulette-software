import tkinter as tk
from functions import find_equivalent, grab_spins, add_last_spin, backspace_spin, clear_spins,ex_shared_eq, filter_num_shared, pretty_eq, nonex_shared_eq, pretty_output
import json

# Create the main window
root = tk.Tk()
root.geometry("800x1200")

# Create a label
label = tk.Label(root, text="Enter the numbers seperated by a space:")
spins_label = tk.Label(root, text="Enter the last spin:")
number_of_spins_label = tk.Label(root, text="Number of last spins to exclude:")
find_by_num_shared_label = tk.Label(root, text="Filter by number of times shared:")

# Create a text input field
entry = tk.Entry(root)
last_spins = tk.Entry(root)
number_last_spins = tk.Entry(root)
find_by_num_shared = tk.Entry(root)

# Checkboxes
selected_option = tk.StringVar()
plus_20_var = tk.BooleanVar()
minus_20_var = tk.BooleanVar()
plus_10_var = tk.BooleanVar()
minus_10_var = tk.BooleanVar()
plus_1_var = tk.BooleanVar()
minus_1_var = tk.BooleanVar()
LEFT_var = tk.BooleanVar()
RIGHT_var = tk.BooleanVar()
SPECIAL_var = tk.BooleanVar()

# Default drop down
selected_option.set("ALL VALUES")

# Create a checkbox with the BooleanVar as its variable
dropdown = tk.OptionMenu(root, selected_option, "ALL VALUES", "NON-EXCLUSIVE SHARED", "EXCLUSIVE SHARED")
plus_20 = tk.Checkbutton(root, text="+20", variable=plus_20_var)
minus_20 = tk.Checkbutton(root, text="-20", variable=minus_20_var)
plus_10 = tk.Checkbutton(root, text="+10", variable=plus_10_var)
minus_10 = tk.Checkbutton(root, text="-10", variable=minus_10_var)
plus_1 = tk.Checkbutton(root, text="+1", variable=plus_1_var)
minus_1 = tk.Checkbutton(root, text="-1", variable=minus_1_var)
LEFT = tk.Checkbutton(root, text="LEFT", variable=LEFT_var)
RIGHT = tk.Checkbutton(root, text="RIGHT", variable=RIGHT_var)
SPECIAL = tk.Checkbutton(root, text="SPECIAL", variable=SPECIAL_var)

# Add last spins
def add_spins():

    add_last_spin(last_spins.get())

    spins_list = grab_spins()

    lastspinslabel.config(text=spins_list)

# Del last spins
def backspace_spins():

    backspace_spin()

    spins_list = grab_spins()

    lastspinslabel.config(text=spins_list)

def clear_spins_func():

    clear_spins()

    spins_list = grab_spins()

    lastspinslabel.config(text=spins_list)

def submit():
    
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
    option = selected_option.get()

    if option == "EXCLUSIVE SHARED":

        if find_by_num_shared.get():

            equivalent = ex_shared_eq(find_equivalent(entry.get(), type_dict, excluded_spins))

            equivalent = filter_num_shared(equivalent[0], equivalent[1], int(find_by_num_shared.get()))

            equivalent = pretty_eq(equivalent[0], equivalent[1])

            outputlabel.delete(1.0, tk.END)
            outputlabel.insert(tk.END, equivalent)
        
        else:

            equivalent = ex_shared_eq(find_equivalent(entry.get(), type_dict, excluded_spins))

            equivalent = pretty_eq(equivalent[0], equivalent[1])

            outputlabel.delete(1.0, tk.END)
            outputlabel.insert(tk.END, equivalent)

    elif option == "NON-EXCLUSIVE SHARED":

        if find_by_num_shared.get():

            equivalent = nonex_shared_eq(find_equivalent(entry.get(), type_dict, excluded_spins))

            equivalent = filter_num_shared(equivalent[0], equivalent[1], int(find_by_num_shared.get()))

            equivalent = pretty_eq(equivalent[0], equivalent[1])

            outputlabel.delete(1.0, tk.END)
            outputlabel.insert(tk.END, equivalent)
        
        else:

            equivalent = nonex_shared_eq(find_equivalent(entry.get(), type_dict, excluded_spins))

            equivalent = pretty_eq(equivalent[0], equivalent[1])

            outputlabel.delete(1.0, tk.END)
            outputlabel.insert(tk.END, equivalent)
    
    elif option == "ALL VALUES":

        equivalent = find_equivalent(entry.get(), type_dict, excluded_spins)

        equivalent = pretty_output(equivalent)
        outputlabel.delete(1.0, tk.END)
        outputlabel.insert(tk.END, equivalent)

    

    

# Get last spins
spins_list = grab_spins()

# Create a button
button = tk.Button(root, text="Submit", command=submit)
last_spins_add = tk.Button(root, text="Enter Last Spin", command=add_spins)
last_spins_backspace = tk.Button(root, text="Backspace", command=backspace_spins)
last_spins_clear = tk.Button(root, text="Clear spins", command=clear_spins_func)

# Output label
outputlabel = tk.Text(root,font=("Arial", 18), fg="red")
lastspinslabel = tk.Label(root, text=spins_list,font=("Arial", 18), fg="red")

# Pack the label, entry, and button into the main window
label.pack()
entry.pack()
spins_label.pack()
last_spins.pack()
last_spins_add.pack()
lastspinslabel.pack()
last_spins_backspace.pack()
last_spins_clear.pack()
number_of_spins_label.pack()
number_last_spins.pack()
dropdown.pack()
find_by_num_shared_label.pack()
find_by_num_shared.pack()
plus_20.pack()
minus_20.pack()
plus_10.pack()
minus_10.pack()
plus_1.pack()
minus_1.pack()
LEFT.pack()
RIGHT.pack()
SPECIAL.pack()
button.pack()
outputlabel.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, command=outputlabel.yview)
scrollbar.pack( fill=tk.Y)
outputlabel.config(yscrollcommand=scrollbar.set)

# Start the event loop
root.mainloop()