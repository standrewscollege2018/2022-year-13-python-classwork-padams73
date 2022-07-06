class Item():

    def __init__(self, name, value):

        self._name = name
        self._value = value

        all_items.append(self)

  
    def get_name(self):
        ''' Return name of item '''

        return self._name

    def get_value(self):
        ''' Return value of item '''

        return self._value
    

def generate_items():
    ''' Import students from a csv file'''
    
    # Import the csv package to enable the program to work with a csv
    import csv
    # Open the csv file, call is csvfile
    with open('products2.csv', newline='') as csvfile:
        # use the reader() function and put the results into a variable called filereader
        filereader = csv.reader(csvfile)
        # Loop through the csv, one row at a time
        
        for line in filereader:
            # For each row, create a new item


            Item(line[0], int(line[1]))

def print_selection():
    ''' Print out the selected item '''

    print(items_listbox.curselection())
    for num in items_listbox.curselection():
        print(all_items[num].get_name())
        # Display name and value in a label
        details.set(f"{all_items[num].get_name()} costs ${all_items[num].get_value()}")
        
# List of all objects
all_items = []

# Import the items from csv file
generate_items()

######### Set up the GUI ##############
from tkinter import *
root = Tk()
root.title("Listbox demo")
root.geometry("800x500")

# Set up listbox
items_listbox = Listbox(root, selectmode=SINGLE)
items_listbox.grid(row=0)
# Populate listbox with names of items
for i in all_items:
    items_listbox.insert(END, i.get_name())

# Button to enter selection
select_btn = Button(root, text="Select", command=print_selection)
select_btn.grid(row=1)

# Label to display information about selected item
details = StringVar()
details_lbl = Label(root, textvariable=details)
details_lbl.grid(row=2)


root.mainloop()
