from tkinter import *

# window set-up

window = Tk()
window.title("External Fire Spread Calculator")
window.config(padx=20, pady=20)
canvas = Canvas(height=100, width=100)
logo_img = PhotoImage(file="logo.png")
logo = canvas.create_image(50,50, image=logo_img)
canvas.grid(row=0, column=0, padx=20, pady=20)

# set up labels

height_label = Label(text="Height of compartment: ")
height_label.grid(row=1, column=0)

width_label = Label(text="Width of compartment: ")
width_label.grid(row=2, column=0)

unprotected_area_label = Label(text="Percentage of unprotected area: ")
unprotected_area_label.grid(row=4, column=0)

distance_label = Label(text="Distance to relevant boundary")
distance_label.grid(row=5, column=0)

enclosing_rectangle_label = Label(text="Enclosing Rectangle: ")
enclosing_rectangle_label.grid(row=3, column=0)

# set up units

height_m_label = Label(text="m")
height_m_label.grid(row=1, column=2)

width_m_label = Label(text="m")
width_m_label.grid(row=2, column=2)

unprotected_area_pct_label = Label(text="%")
unprotected_area_pct_label.grid(row=4, column=2)

distance_m_label = Label(text="m")
distance_m_label.grid(row=5, column=2)

# set up entries

height_entry = Entry(width=5)
height_entry.grid(row=1, column=1)

width_entry = Entry(width=5)
width_entry.grid(row=2, column=1)

unprotected_area_entry = Entry(width=5)
unprotected_area_entry.grid(row=4, column=1)

distance_entry = Entry(width=5)
distance_entry.grid(row=5, column=1)

# set up radio buttons
office_button = Radiobutton(text="office")
office_button.grid(row=6, column=0)

office_button = Checkbutton(text="Office, Residential, Assembly/Recreational usage")
office_button.grid(row=6, column=0, columnspan=2)

# set up calculate buttons

calculate_area_button = Button(text="Calculate maximum unprotected area")
calculate_area_button.grid(row=7, column=0)

calculate_distance_button = Button(text="Calculate maximum separation distance")
calculate_distance_button.grid(row=7, column=1)

window.mainloop()