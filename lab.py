import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import database

app = customtkinter.CTk()
app.title('Daily Work Plan')
app.geometry('1700x900')
app.config(bg='#600170')
app.resizable(FALSE, FALSE)

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 12, 'bold')

image_path = r'C:\Users\Arhelle John\Desktop\python\valo.jpg'
image = Image.open(image_path)
image = image.resize((1700, 900), Image.LANCZOS)
image = ImageTk.PhotoImage(image)
image1_label = Label(app, image=image, bg='#FFF')
image1_label.place(x=0, y=0)
image1_label.image = image

def add_to_treeview():
    plans = database.fetch_plans()
    tree.delete(*tree.get_children())
    for plan in plans:
        tree.insert('', END, values=plan)

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    date_entry.delete(0, END)
    username_entry.delete(0, END)
    time_entry.delete(0, END)
    variable1.set('Select Day')
    plan_entry.delete(1.0, END)

def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        date_entry.insert(0, row[1])
        username_entry.insert(0, row[0])
        time_entry.insert(0, row[2])
        variable1.set(row[3])
        plan_entry.insert(END, row[4])

def delete():
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showerror('ERROR', 'Choose a plan to delete.') 
    else:
        for item in selected_items:
            times = tree.item(item, 'values')[0]
            database.delete_plan(times)
            tree.delete(item)
        clear()
        messagebox.showinfo('Success', 'Data has been deleted')

def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Select a plan to update')
    else:
        date = date_entry.get()
        username = username_entry.get()
        time = time_entry.get()
        day = variable1.get()
        plan = plan_entry.get(1.0, END).strip()
        database.update_plan(username, date, time, day, plan)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success', 'Data has been updated')

def insert():
    date = date_entry.get()
    username = username_entry.get()
    time = time_entry.get()
    day = variable1.get()
    plan = plan_entry.get(1.0, END).strip()
    if not (time and username and date and day and plan):
        messagebox.showerror('Error', 'Fill up the info.')
    elif database.time_exists(time):
        messagebox.showerror('Error', 'Time already exists.')
    else:
        database.insert_plan(username, date, time, day, plan)
        add_to_treeview()
        messagebox.showinfo('Success', 'Data has been inserted.')

username_label = customtkinter.CTkLabel(app, font=font1, text='Username:', text_color='#FFFFFF', bg_color='#253f4b')
username_label.place(x=20, y=20)

username_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#FFFFFF', border_width=2, width=180)
username_entry.place(x=130, y=20)

date_label = customtkinter.CTkLabel(app, font=font1, text='Date:', text_color='#FFFFFF', bg_color='#253f4b')
date_label.place(x=70, y=80)

date_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#FFFFFF', border_width=2, width=180)
date_entry.place(x=130, y=80)

time_label = customtkinter.CTkLabel(app, font=font1, text='Time:', text_color='#FFFFFF', bg_color='#253f4b')
time_label.place(x=540, y=20)

time_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#FFFFFF', border_width=2, width=180)
time_entry.place(x=600, y=20)

day_label = customtkinter.CTkLabel(app, font=font1, text='Day:', text_color='#FFFFFF', bg_color='#253f4b')
day_label.place(x=550, y=80)

options = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
variable1 = StringVar()

day_options = customtkinter.CTkComboBox(app, font=font1, text_color='#000', fg_color='#FFFFFF', dropdown_hover_color='#0C9295', button_color='#0C9295', button_hover_color='#0C9295', border_color='#7F00FF', width=180, variable=variable1, values=options, state='readonly')
day_options.set('Select Day')
day_options.place(x=600, y=80)

plan_label = customtkinter.CTkLabel(app, font=font1, text='PLAN', text_color='#FFFFFF', bg_color='#253f4b')
plan_label.place(x=350, y=130)

plan_entry = Text(app, font=font1, fg='#000', bg='#FFFFFF', borderwidth=2, width=40, height=15)
plan_entry.place(x=100, y=160)

add_button = customtkinter.CTkButton(app, command=insert, font=font1, text_color='#FFFFFF', text='Add Plan', fg_color='#FF4654', hover_color='#000', bg_color='#253f4b', cursor='hand2', corner_radius=15, width=260)
add_button.place(x=250, y=660)

clear_button = customtkinter.CTkButton(app, command=lambda: clear(True), font=font1, text_color='#FFFFFF', text='New Plan', fg_color='#FF4654', hover_color='#000', bg_color='#253f4b', cursor='hand2', corner_radius=15, width=260)
clear_button.place(x=820, y=660)

update_button = customtkinter.CTkButton(app, command=update, font=font1, text_color='#FFFFFF', text='Update Plan', fg_color='#FF4654', hover_color='#000', bg_color='#253f4b', cursor='hand2', corner_radius=15, width=260)
update_button.place(x=1110, y=660)

delete_button = customtkinter.CTkButton(app, command=delete, font=font1, text_color='#FFFFFF', text='Delete Plan', fg_color='#FF4654', hover_color='#000', bg_color='#253f4b', cursor='hand2', corner_radius=15, width=260)
delete_button.place(x=1400, y=660)

style = ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview', font=font2, foreground='#FFFFFF', background='#2A475E', fieldbackground='#313837')
style.map('Treeview', background=[('selected', '#FF4654')])

tree = ttk.Treeview(app, height=30)
tree['columns'] = ('Username', 'Date', 'Time', 'Day', 'Plan')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('Username', anchor=tk.CENTER, width=120)
tree.column('Date', anchor=tk.CENTER, width=120)
tree.column('Time', anchor=tk.CENTER, width=100)
tree.column('Day', anchor=tk.CENTER, width=80)
tree.column('Plan', anchor=tk.CENTER, width=450)

tree.heading('Username', text='Username')
tree.heading('Date', text='Date')
tree.heading('Time', text='Time')
tree.heading('Day', text='Day')
tree.heading('Plan', text='Plan')

tree.place(x=800, y=20)
tree.bind('<ButtonRelease>', display_data)

add_to_treeview()

app.mainloop()