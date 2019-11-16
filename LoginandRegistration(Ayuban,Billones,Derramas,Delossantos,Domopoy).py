import tkinter as tk


from tkinter import *

import os

def delete2():
  screen3.destroy()
 
def delete3():
  screen4.destroy()
 
def delete4():
  screen5.destroy()
   
def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login Sucess").pack()
  Button(screen3, text = "OK", command =delete2).pack()
  newWindow=Toplevel(z)
  app=Register(newWindow)
 
def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()
 
def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()
 
   
def register_user():
  print("working")
   
  username_info = username.get()
  password_info = password.get()
 
  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()
 
  username_entry.delete(0, END)
  password_entry.delete(0, END)
 
  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()
 
def login_verify():
   
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
 
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()
 
  else:
        user_not_found()
   
 
 
def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  screen1.config(background="#202020")
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
 
  Label(screen1, text = "Fill up the required information",fg="#e75480",bg="#202020",font=("Arial Black", 10,'bold')).pack()
 
  nameuser=Label(screen1, text = "Username",fg="#e75480",bg="#202020",font=("Arial Black", 10,'bold'))
  nameuser.pack()
  nameuser.place(x=110,y=40)
  username_entry = Entry(screen1, textvariable = username,bg="#e75480",fg="#020202",width=20)
  username_entry.pack()
  username_entry.place(x=90,y=70,height="32")
  passpass=Label(screen1, text = "Password",fg="#e75480",bg="#202020",font=("Arial Black", 10,'bold'))
  passpass.pack()
  passpass.place(x=110,y=113)
  password_entry =  Entry(screen1, textvariable = password,bg="#e75480",fg="#020202")
  password_entry.pack()
  password_entry.place(x=90,y=140,height="32")
 
  reg=Button(screen1, text = "Register", width = 10, height = 1, command = register_user)
  reg.pack()
  reg.place(x=110,y=190,height="32")

   
   
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("360x430")
  screen.title("Login")
  screen.resizable(0, 0)
  screen.config(background="#202020")
  Label(text="WELCOME!",bg="#020202",fg="#e75480",width="360",height="3",font=("Tahoma", 16,'bold')).pack()
 
        
  global username_verify
  global password_verify
   
  username_verify = StringVar()
  password_verify = StringVar()
 
  global username_entry1
  global password_entry1
   
  uname=Label(screen, text = "Username",fg="#e75480",bg="#202020",font=("Arial Black", 10,'bold'))
  uname.pack()
  uname.place(x=130,y=112)
  username_entry1 = Entry(screen, textvariable = username_verify,bg="#e75480",fg="#020202",font=("Arial Black", 10,'bold'),width=20)
  username_entry1.pack()
  username_entry1.place(x=90,y=140,height="32")
  
  upass=Label(screen, text = "Password",fg="#e75480",bg="#202020",font=("Arial Black", 10,'bold'))
  upass.pack()
  upass.place(x=130,y=190)
  password_entry1 = Entry(screen, textvariable = password_verify,bg="#e75480",fg="#020202",font=("Arial Black", 10,'bold'),width=20)
  password_entry1.pack()
  password_entry1.place(x=90,y=220,height="32")
  
  blogin=Button(screen, text = "Log in",width=13,command = login_verify,font=("Arial Black", 11))
  blogin.pack()
  blogin.place(x=105,y=280,height="32")
  
  bregister=Button(screen, text = "Register",width=13,command = register,font=("Arial Black", 11))
  bregister.pack()
  bregister.place(x=105,y=320,height="32")
  
  screen.mainloop()
 
main_screen()
