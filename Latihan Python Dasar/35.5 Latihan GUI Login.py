from tkinter import *

def register_user():
    username_info = username.get()
    password_info = password.get()

    file=open(username_info+".txt",'w')
    file.write(username_info+'\n')
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1,text =  'Registrasi Sukses', fg = 'green', font = {'Calibri',11}).pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title('Registrasi')
    screen1.geometry('400x350')

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = 'Please enter details below').pack()
    Label(screen1, text = '').pack()
    Label(screen1, text = 'Username :').pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = 'Password : ').pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = '').pack()
    Button(screen1, text = 'Register',width = 10, height =1, command = register_user()).pack()

def login():
    print('Login')

def main_screen():
    global screen
    screen = Tk()
    screen.geometry('400x350')
    screen.title('LOGIN PAGE 1.0')
    Label(text = 'LOGIN PAGE 1.0', bg = 'grey', width = '300', height = '2', font = {'Calibri',11}).pack()
    Label(text = '').pack()
    Button(text = 'Login', width = '30',height = '2',command = login()).pack()
    Label(text = '').pack()
    Button(text = 'Registrasi',width = '30',height = '2',command = register()).pack()
    screen.mainloop()
main_screen()