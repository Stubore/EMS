from tkinter import *
from PIL import ImageTk
import mysql.connector
from tkinter import messagebox
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Event Management System"
)

# functionality
def register():
    if not (usernameEntry.get() and EmailEntry.get() and passwordEntry.get() and ConfirmpasswordEntry.get()):
        messagebox.showerror('Error', 'All fields must be filled')
    elif passwordEntry.get() != ConfirmpasswordEntry.get():
        messagebox.showerror('Error', 'Passwords do not match')
    else:
        try:
            # Connect to the database and insert user data
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("INSERT INTO customer_table (Username, Password, Email) VALUES (%s, %s, %s)", (usernameEntry.get(), passwordEntry.get(), EmailEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Status", "Successfully registered")
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to database: {str(e)}")



# GUI
root = Tk()
root.geometry('990x660+50+50')
root.resizable(0, 0)
root.title('Register Page')

bgImage = ImageTk.PhotoImage(file='Images/register.jpg')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(root, text='Create an Account', font=('Microsoft Yahei UI Light', 30, 'bold'), bg='#DFA7E4', fg='#A5256B')
heading.place(x=400, y=80)

heading1 = Label(root, text='Already have an account?', font=('Microsoft Yahei UI Light', 18), bg='#DFA7E4',
                 fg='#A5256B')
heading1.place(x=390, y=120)

LoginButton = Button(root, text='Log In', font=('Open Sans', 9, 'bold'), fg='#A5256B', bg='#A5256B', activebackground='#DFA7E4',highlightbackground='#DFA7E4',cursor='hand2',bd=0)
LoginButton.place(x=600, y=125)

Username = Label(root, text='Username:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
Username.place(x=330, y=210)

usernameEntry = Entry(root, width=38, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#DFA7E4',
                      highlightbackground='white')  # Set white border color
usernameEntry.place(x=400, y=210)


Email = Label(root, text='Email:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
Email.place(x=355, y=260)
EmailEntry = Entry(root, width=38, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#DFA7E4',
                      highlightbackground='white')  # Set white border color
EmailEntry.place(x=400, y=260)


Password = Label(root, text='Password:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
Password.place(x=330, y=310)

passwordEntry = Entry(root, width=38, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#DFA7E4',
                       highlightbackground='white')  # Set white border color
passwordEntry.place(x=400, y=310)


ConfirmPass = Label(root, text='Confirm Password:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
ConfirmPass.place(x=285, y=360)

ConfirmpasswordEntry = Entry(root, width=38, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#DFA7E4',
                       highlightbackground='white')  # Set white border color
ConfirmpasswordEntry.place(x=400, y=360)
ConfirmpasswordEntry.config(show='*')



CreateButton = Button(root, text='Creat Account', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#A5256B', activebackground='#DFA7E4',highlightbackground='#DFA7E4',cursor='hand2',bd=0,width=13,height=1,command=register)
CreateButton.place(x=450, y=450)



root.mainloop()