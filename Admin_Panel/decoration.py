from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import time
import ttkthemes
from tkinter import ttk, BOTH


#functionality





#GUI
root=ttkthemes.ThemedTk('Radiance')
root.geometry('1174x680+50+20')
root.resizable(0,0)
root.title('Add Decor')

bgImage = ImageTk.PhotoImage(file='Images/add.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

datetimelabel=Label(root,font=('times new Roman',18,'bold'),bg='#DFA7E4', fg='#A5256B')
datetimelabel.place(x=10,y=5)
clock()

heading2 = Label(root, text='Decoration Details', font=('arial', 28), bg='#DFA7E4', fg='#A5256B')
heading2.place(x=580, y=50)


leftFrame=Frame(root,bg='#DFA7E4')
leftFrame.place(x=5,y=250,width=320,height=525)

addbutton=Button(leftFrame,text='Add Data ',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
addbutton.grid(row=1,column=0,pady=20,padx=100)

updatevenuebutton=Button(leftFrame,text='Update Data',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
updatevenuebutton.grid(row=2,column=0,pady=20,padx=100)

deletebutton=Button(leftFrame,text='Delete Data',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
deletebutton.grid(row=3,column=0,pady=20,padx=100)

showbutton=Button(leftFrame,text='Show Data',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
showbutton.grid(row=4,column=0,pady=20,padx=100)

exitbutton=Button(leftFrame,text='Exit',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
exitbutton.grid(row=5,column=0,pady=20,padx=100)

rightFrame=Frame(root,bg='white')
rightFrame.place(x=365,y=130,width=820,height=550)

ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(rightFrame)

decorTable=ttk.Treeview(rightFrame,columns=('Decor-Company Name','Decor-Company Address','Decor-Contact'),
                         xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
ScrollbarX.config(command=decorTable.xview)
ScrollbarY.config(command=decorTable.yview)
ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)
decorTable.pack(fill=BOTH,expand=1)
                        
decorTable.heading('Decor-Company Name',text='Decor-Company Name')
# decorTable.heading('Decor-Manager Name',text='Decor-Manager Name')
decorTable.heading('Decor-Company Address',text='Decoration Address')
decorTable.heading('Decor-Contact',text='Decoration Contact')


decorTable.config(show='headings')

root.mainloop()
