from tkinter import *
from tkinter import messagebox
from PIL import ImageTk







# functionality
def login_admin():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error','All fields must be filled')
    elif usernameEntry.get() == 'Admin' and passwordEntry.get() == '1234':
        messagebox.showinfo('Success','Welcome')
        login.destroy()
        
    else:
        messagebox.showerror('Error','Please provide correct details')







# GUI
login = Tk()
login.geometry('990x660+50+50')
login.resizable(0, 0)
login.title('Login Page')

bgImage = ImageTk.PhotoImage(file='Images/login.jpg')
bgLabel = Label(login, image=bgImage)
bgLabel.place(x=0, y=0)
heading0 = Label(login, text='WELCOME!', font=('Microsoft Yahei UI Light', 30, 'bold'), bg='#DFA7E4', fg='#A5256B')
heading0.place(x=700, y=120)

heading = Label(login, text='Sign in to your account, Admin Panel', font=('Microsoft Yahei UI Light', 20, ), bg='#DFA7E4', fg='#A5256B')
heading.place(x=630, y=160)

Username = Label(login, text='Username:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
Username.place(x=600, y=250)

usernameEntry = Entry(login, width=40, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#A5256B',
                      highlightbackground='white')
usernameEntry.place(x=670, y=250)


frame1 = Frame(login, width=288, height=2, bg='#A5256B')
frame1.place(x=670, y=270)

Password = Label(login, text='Password:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
Password.place(x=600, y=300)

passwordEntry = Entry(login, width=40, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#A5256B',
                      highlightbackground='white')
passwordEntry.place(x=670, y=300)
passwordEntry.config(show='*')


frame2 = Frame(login, width=288, height=2, bg='#A5256B')
frame2.place(x=670, y=320)

forgetButton = Button(login, text='Forgot Password?', bd=0, bg='#DFA7EA', activebackground='#DFA7E4', cursor='hand2',
                      highlightbackground='#DFA7E4', font=('Microsoft Yahei UI Light', 9), fg='#A5256B')
forgetButton.place(x=825, y=350)

LoginButton = Button(login, text='Login', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#A5256B',
                     activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=login_admin)
LoginButton.place(x=715, y=450)



login.mainloop()