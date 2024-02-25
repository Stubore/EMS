from tkinter import*
from PIL import ImageTk



def Admin():
    root.destroy()
    import admin_log

def Agent():
    root.destroy()
    import login

#GUI
root = Tk()
root.geometry('990x660+50+50')
root.resizable(0,0)
root.title('Ask')


bgImage=ImageTk.PhotoImage(file='Images/ask.png')
bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)


heading=Label(root,text='Welcome',font=('Microsoft Yahei UI Light',28,'bold'),bg='#DFA7E4',fg='#A5256B')
heading.place(x=710,y=20)

heading1=Label(root,text='Streamline Your Events with Evento',font=('Microsoft Yahei UI Light',18),bg='#DFA7E4',fg='#A5256B')
heading1.place(x=630,y=90)
heading2=Label(root,text='Your Ultimate Event Management Solution',font=('Microsoft Yahei UI Light',18),bg='#DFA7E4',fg='#A5256B')
heading2.place(x=630,y=120)



AdminButton = Button(root, text='Admin', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=Admin)
AdminButton.place(x=630, y=300)


AgentButton = Button(root, text='Agent', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=Agent)
AgentButton.place(x=800, y=300)




root.mainloop()