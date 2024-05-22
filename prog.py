import customtkinter
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk

app= customtkinter.CTk()
app.title('Daily Work Planner')
app.geometry('1700x900')
app.config(bg='#7F00FF')
app.resizable(FALSE, FALSE)

font1=('Palatino', 30, 'bold')
font2=('Arial', 17, 'bold')
font3=('Arial', 14, 'bold')
font4=('Arial', 14, 'bold','underline')
conn=sqlite3.connect('data.db')
cursor=conn.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
              username TEXT NOT NULL,
              password TEXT NOT NULL)''' )

def signup():
    username = username_entry.get()
    password = password_entry.get()
    if username!= '' and password !='':
        cursor.execute('SELECT username FROM users WHERE username=?', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Error', 'Username already exists')
          
        else:
            encoded_password =password.encode('utf-8')
            hashed_password =bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            #print(hashed_password)
            cursor.execute('INSERT INTO users VALUES (?, ?)', [username,hashed_password])
            conn.commit()
            messagebox.showinfo('Success', 'Account has been created.')
    else:
        messagebox.showerror('Error', 'Enter all data!')


def login_account():
    username = username_entry2.get()
    password = password_entry2.get()
    if username!= '' and password !='':
        cursor.execute('SELECT password FROM users WHERE username=?', [username])
        result=cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                messagebox.showinfo('Success', 'Logged in successfully')
            else:
                messagebox.showerror('Error', 'Invalid password')
        else:
            messagebox.showerror('Error', 'Invalid Username')
    else:
        messagebox.showerror('Error', 'Enter all data!')        

def login():
    frame1.destroy()
    frame2=customtkinter.CTkFrame(app, bg_color='#000000',fg_color='#fff', width=1700, height=900)
    frame2.place(x=0, y=0)
    
    image_path = r"C:\Users\Arhelle John\Desktop\python\VALLLL.jpg"
    image = Image.open(image_path)
    image = image.resize((1300, 900), Image.LANCZOS)
    image2 = ImageTk.PhotoImage(image)
    image2_label = Label(frame2, image=image2, bg='#FFF') 
    image2_label.place(x=470, y=0)  
    image2_label.image = image2

    Piplup_label2 = customtkinter.CTkLabel(frame2, font=font1, text='Daily Work Planner',text_color='#FF0000', bg_color='#fff')
    Piplup_label2.place(x=115, y=125)

    login_label2 = customtkinter.CTkLabel(frame2, font=font1, text='Login',text_color='#000000', bg_color='#fff',)
    login_label2.place(x=190, y=200)

    global username_entry2
    global password_entry2

    username_entry2 = customtkinter.CTkEntry(frame2, font=font2, text_color='#000000', fg_color='#d3d3d3', bg_color='#fff', border_color='#000000', border_width=3, placeholder_text='User Name', placeholder_text_color='#808080', width=200, height=50)
    username_entry2.place(x=130, y=300)

    password_entry2 = customtkinter.CTkEntry(frame2, font=font2, show='*', text_color='#000000', fg_color='#d3d3d3', bg_color='#fff', border_color='#000000', border_width=3, placeholder_text='Password', placeholder_text_color='#808080', width=200, height=50)
    password_entry2.place(x=130, y=385)

    login_button2= customtkinter.CTkButton(frame2,command=login_account, font=font4, text='Login',text_color='#fff',fg_color='#FF0000',bg_color='#fff')
    login_button2.place(x=155, y=485)

frame1=customtkinter.CTkFrame(app, bg_color='#fff', fg_color='#fff', width=1700, height=900)
frame1.place(x=0, y=0)

image_path = r"C:\Users\Arhelle John\Desktop\python\VALLLL.jpg"
image = Image.open(image_path)
image = image.resize((1300, 900), Image.LANCZOS)
image1 = ImageTk.PhotoImage(image)
image1_label = Label(frame1, image=image1, bg='#FFF') 
image1_label.place(x=470, y=0)  
image1_label.image = image1

Piplup_label = customtkinter.CTkLabel(frame1, font=font1, text='Daily Work Planner',text_color='#FF0000', bg_color='#fff')
Piplup_label.place(x=115, y=125)

signup_label = customtkinter.CTkLabel(frame1, font=font1, text='Sign up',text_color='#000000', bg_color='#fff')
signup_label.place(x=185, y=200)

username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#000000', fg_color='#d3d3d3', bg_color='#fff', border_color='#000000', border_width=3, placeholder_text='Username', placeholder_text_color='#808080', width=200, height=50)
username_entry.place(x=135, y=280)

password_entry = customtkinter.CTkEntry(frame1, font=font2, show='*', text_color='#000000', fg_color='#d3d3d3', bg_color='#fff', border_color='#000000', border_width=3, placeholder_text='Password', placeholder_text_color='#808080', width=200, height=50)
password_entry.place(x=135, y=350)

signup_button=customtkinter.CTkButton(frame1,command=signup, font=font2, text_color='#FFF', text='Sign up', fg_color='#FF0000', hover_color='#000000', bg_color='#fff', cursor='hand2', corner_radius=5, width=120)
signup_button.place(x=170, y=420)

login_label = customtkinter.CTkLabel(frame1, font=font3, text='Already have an account',text_color='#808080',fg_color='#d3d3d3',bg_color='#FFF')
login_label.place(x=145, y=550)

login_button= customtkinter.CTkButton(frame1, command=login, font=font3, text='Login',text_color='#fff',fg_color='#FF0000',hover_color='#000000',bg_color='#fff')
login_button.place(x=160, y=600)

app.mainloop()
