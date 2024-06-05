import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# Function to handle button click
def enter_data():
    # Get data from form fields
    plant_name = plant_name_entry.get()
    plant_id = plant_id_entry.get()
    plant_color = plantColor_combobox.get()
    fruit_color = fruitColor_combobox.get()
    fruit_season = fruitSeason_combobox.get()
    benefits = Benefits_combobox.get()
    kingdom = kingdom_combobox.get()
    code = code_entry.get()
    order = order_combobox.get()
    family = family_combobox.get()
    genus = genus_combobox.get()
    description = description_entry.get("1.0", tkinter.END).strip()

    # Check if any field is empty
    if not plant_name or not plant_id or not plant_color or not fruit_color or not fruit_season or not benefits or not kingdom or not code or not order or not family or not genus or not description:
        messagebox.showerror("Error", "All fields are required.")
        return

    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('plants.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS plant_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plant_name TEXT,
            plant_id TEXT,
            plant_color TEXT,
            fruit_color TEXT,
            fruit_season TEXT,
            benefits TEXT,
            kingdom TEXT,
            code TEXT,
            plant_order TEXT,
            family TEXT,
            genus TEXT,
            description TEXT
        )
    ''')

    # Insert the data into the table
    cursor.execute('''
        INSERT INTO plant_info (plant_name, plant_id, plant_color, fruit_color, fruit_season, benefits, kingdom, code, plant_order, family, genus, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (plant_name, plant_id, plant_color, fruit_color, fruit_season, benefits, kingdom, code, order, family, genus, description))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    # Optionally, clear the form fields
    plant_name_entry.delete(0, tkinter.END)
    plant_id_entry.delete(0, tkinter.END)
    plantColor_combobox.set('')
    fruitColor_combobox.set('')
    fruitSeason_combobox.set('')
    Benefits_combobox.set('')
    kingdom_combobox.set('')
    code_entry.delete(0, tkinter.END)
    order_combobox.set('')
    family_combobox.set('')
    genus_combobox.set('')
    description_entry.delete("1.0", tkinter.END)

    messagebox.showinfo("Success", "Data Entered Successfully")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Plant Information
plant_info_frame = tkinter.LabelFrame(frame, text="Plant Information")
plant_info_frame.grid(row=0, column=0, padx=20, pady=10)

plant_name_label = tkinter.Label(plant_info_frame, text="Plant Name")
plant_name_label.grid(row=0, column=0)
plant_id_label = tkinter.Label(plant_info_frame, text="Plant ID")
plant_id_label.grid(row=0, column=1)

plant_name_entry = tkinter.Entry(plant_info_frame)
plant_name_entry.grid(row=1, column=0)
plant_id_entry = tkinter.Entry(plant_info_frame)
plant_id_entry.grid(row=1, column=1)

plantColor_label = tkinter.Label(plant_info_frame, text="Plant Color")
plantColor_label.grid(row=0, column=2)
plantColor_combobox = ttk.Combobox(plant_info_frame, values=["", "Red", "Yellow", "Orange", "Green", "Purple", "Brown", "Black", "White", "Blue"])
plantColor_combobox.grid(row=1, column=2)

fruitColor_label = tkinter.Label(plant_info_frame, text="Fruit Colour")
fruitColor_label.grid(row=0, column=3)
fruitColor_combobox = ttk.Combobox(plant_info_frame, values=["","No Fruit", "Red", "Yellow", "Orange", "Green", "Purple", "Brown", "Black", "White"])
fruitColor_combobox.grid(row=1, column=3)

fruitSeason_label = tkinter.Label(plant_info_frame, text="Season")
fruitSeason_label.grid(row=2, column=0)
fruitSeason_combobox = ttk.Combobox(plant_info_frame, values=["", "All Season","Summer", "Winter", "Rainy", "Spring", "Autumn"])
fruitSeason_combobox.grid(row=3, column=0)

Benefits_label = tkinter.Label(plant_info_frame, text="Benefits")
Benefits_label.grid(row=2, column=1)
Benefits_combobox = ttk.Combobox(plant_info_frame, values=["", "Health", "Beauty", "Food", "Medicine", "Ornamental", "Environmental", "Aromatic", "Culinary"])
Benefits_combobox.grid(row=3, column=1)

# Additional Fields
kingdom_label = tkinter.Label(plant_info_frame, text="Kingdom")
kingdom_label.grid(row=2, column=2)
kingdom_combobox = ttk.Combobox(plant_info_frame, values=["", "Plantae", "Fungi", "Protista", "Animalia"])
kingdom_combobox.grid(row=3, column=2)

code_label = tkinter.Label(plant_info_frame, text="Code")
code_label.grid(row=2, column=3)
code_entry = tkinter.Entry(plant_info_frame)
code_entry.grid(row=3, column=3)

order_label = tkinter.Label(plant_info_frame, text="Order")
order_label.grid(row=4, column=0)
order_combobox = ttk.Combobox(plant_info_frame, values=["", "Rosales", "Asterales", "Fabales", "Lamiales", "Solanales"])
order_combobox.grid(row=5, column=0)

family_label = tkinter.Label(plant_info_frame, text="Family")
family_label.grid(row=4, column=1)
family_combobox = ttk.Combobox(plant_info_frame, values=["", "Rosaceae", "Asteraceae", "Fabaceae", "Lamiaceae", "Solanaceae"])
family_combobox.grid(row=5, column=1)

genus_label = tkinter.Label(plant_info_frame, text="Genus")
genus_label.grid(row=4, column=2)
genus_combobox = ttk.Combobox(plant_info_frame, values=["", "Rosa", "Helianthus", "Pisum", "Mentha", "Solanum"])
genus_combobox.grid(row=5, column=2)

description_label = tkinter.Label(plant_info_frame, text="Description")
description_label.grid(row=6, column=0, columnspan=4)

# Adding a frame to hold the Text widget and the scrollbar
description_frame = tkinter.Frame(plant_info_frame)
description_frame.grid(row=7, column=0, columnspan=4, padx=10, pady=5)

# Adding the Text widget for the description
description_entry = tkinter.Text(description_frame, height=10, width=80)
description_entry.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

# Adding a scrollbar to the Text widget
description_scrollbar = tkinter.Scrollbar(description_frame, command=description_entry.yview)
description_scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
description_entry.config(yscrollcommand=description_scrollbar.set)

for widget in plant_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Button
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=8, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
