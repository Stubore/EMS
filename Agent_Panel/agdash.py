from tkinter import*
from PIL import ImageTk

#Graphical User interrface
root = Tk()
root.geometry('990x660+50+50')
root.resizable(0,0)
root.title('Agent Dashboard')


bgImage=ImageTk.PhotoImage(file='Images/dashboard.png')
bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)


heading=Label(root,text='Welcome To Agent Panel!',font=('Microsoft Yahei UI Light',30,'bold'),bg='white',fg='#A5256B')
heading.place(x=280, y=20)

heading1=Label(root,text='Dasboard',font=('Microsoft Yahei UI Light',22),bg='white',fg='#A5256B')
heading1.place(x=280,y=90)





LoginButton = Button(root, text='Create Booking', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1)
LoginButton.place(x=280, y=200)

exitbutton=Button(root,text='Exit',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
exitbutton.place(x=50,y=550)


root.mainloop()
