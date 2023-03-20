import tkinter as tk
from functions import find_equivalent, grab_spins, add_last_spin, backspace_spin, clear_spins,ex_shared_eq, clean_grab_spins, pretty_eq, pretty_output, filter_num_shared, nonex_shared_eq
import customtkinter

# Set customtkinter defaults
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Create the main window
root = customtkinter.CTk()
root.geometry("800x1200")

# Create a label
label = customtkinter.CTkLabel(master=root, text="Enter the numbers seperated by a space:")
spins_label =  customtkinter.CTkLabel(master=root, text="Enter the last spin:")
number_of_spins_label = customtkinter.CTkLabel(master=root, text="Number of last spins to exclude:")
find_by_num_shared_label = customtkinter.CTkLabel(master=root, text="Filter by number of times shared:")

# Create a text input field
entry = customtkinter.CTkEntry(root)
last_spins = customtkinter.CTkEntry(root)
number_last_spins = customtkinter.CTkEntry(root)
find_by_num_shared = customtkinter.CTkEntry(root)

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

# Add last spins
def add_spins():

    add_last_spin(last_spins.get())

    spins_list = grab_spins()

    spins_list = clean_grab_spins(spins_list)

    lastspinslabel.configure(text=spins_list)

# Del last spins
def backspace_spins():

    backspace_spin()

    spins_list = grab_spins()

    spins_list = clean_grab_spins(spins_list)

    lastspinslabel.configure(text=spins_list)

def clear_spins_func():

    clear_spins()

    spins_list = grab_spins()

    spins_list = clean_grab_spins(spins_list)

    lastspinslabel.configure(text=spins_list)

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
    
    main_option = option.get()
    if main_option == "EXCLUSIVE SHARED":

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

    elif main_option == "NON-EXCLUSIVE SHARED":

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
    
    elif main_option == "ALL VALUES":
        print('Got here')

        equivalent = find_equivalent(entry.get(), type_dict, excluded_spins)

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

# Output label
outputlabel = customtkinter.CTkTextbox(master=root,font=("Arial", 18))
lastspinslabel = customtkinter.CTkLabel(master=root, text=spins_list,font=("Arial", 18))

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
outputlabel.configure(yscrollcommand=scrollbar.set)

# Start the event loop
root.mainloop()