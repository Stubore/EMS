from tkinter import*
from PIL import ImageTk

#functionality
def event():
    root.destroy()
    import event

def venue():
    root.destroy()
    import venue

def decoration():
    root.destroy()
    import decoration

def catering():
    root.destroy()
    import catering

#GUI
root = Tk()
root.geometry('990x660+50+50')
root.resizable(0,0)
root.title('Admin Dashboard')


bgImage=ImageTk.PhotoImage(file='Images/dashboard.png')
bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)


heading=Label(root,text='Welcome To Admin Panel!',font=('Microsoft Yahei UI Light',30,'bold'),bg='white',fg='#A5256B')
heading.place(x=280,y=20)

heading1=Label(root,text='Dasboard',font=('Microsoft Yahei UI Light',22),bg='white',fg='#A5256B')
heading1.place(x=280,y=90)




EventButton = Button(root, text='Event', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=event)
EventButton.place(x=300, y=175)


VenueButton = Button(root, text='Venue', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=venue)
VenueButton.place(x=600, y=175)

DecorationButton = Button(root, text='Decoration', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=decoration)
DecorationButton.place(x=600, y=300)

CateringButton = Button(root, text='Catering', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=catering)
CateringButton.place(x=300, y=300)

exitbutton=Button(root,text='Exit',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
exitbutton.place(x=50,y=550)

root.mainloop()