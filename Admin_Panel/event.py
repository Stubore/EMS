from tkinter import *
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk
import time
import ttkthemes
from tkinter import messagebox
from tkinter import ttk, BOTH
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Event Management System"
)


#function
def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimelabel.config(text=f'Date:{date}\nTime:{currenttime}')
    datetimelabel.after(1000,clock)

#delete agent
def deleteagent():
    selected_item = eventTable.focus()
    
    if not selected_item:
        messagebox.showerror('Error', 'Please select an event to delete')
        return
    else:
        try:
           
            item_values = eventTable.item(selected_item, 'values')
            event_id = item_values[0]
            
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("DELETE FROM event WHERE id=%s", (event_id,))
            con.commit()
            con.close()
            messagebox.showinfo('Deleted', 'Agent successfully deleted')
        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error deleting agent: {e}')






def showagent():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
    cursor = con.cursor()
    cursor.execute("SELECT * from event")
    fetched_data = cursor.fetchall()
    eventTable.delete(*eventTable.get_children())
    for data in fetched_data:
        eventTable.insert('',END,values=data)
    






def updateagent():
    def updatedata():
        if nameEntry.get() == '' or start_dateEntry.get() == '' or end_dateEntry.get() == '' :
            messagebox.showerror('Error', 'All Fields Must Be Filled', parent=update_window)
            return
        else:
            try:
                con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
                cursor = con.cursor()
                cursor.execute("UPDATE event SET event_name=%s, start_date=%s, end_date=%s, WHERE event_id=%s", (nameEntry.get(), start_dateEntry.get(), end_dateEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Status", "Agent details updated successfully")
                update_window.destroy()  # Close the update window after successful update
            except Exception as e:
                messagebox.showerror("Error", f"Error in updating agent: {str(e)}")

    selected_item = eventTable.focus()
    
    if not selected_item:
        messagebox.showerror('Error', 'Please select an agent to update')
        return
    
    item_values = eventTable.item(selected_item, 'values')
    event_id = item_values[0]

    update_window = Toplevel()
    update_window.grab_set()
    update_window.resizable(0, 0)

    namelabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=0, column=1, padx=10, pady=15)
    nameEntry.insert(0, item_values[0])  # Pre-fill with existing value
    
    start_datelabel = Label(update_window, text='Start Date', font=('times new roman', 20, 'bold'))
    start_datelabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    start_dateEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    start_dateEntry.grid(row=1, column=1, padx=10, pady=15)
    start_dateEntry.insert(0, item_values[1])  # Pre-fill with existing value
    
    end_datelabel = Label(update_window, text='End Date', font=('times new roman', 20, 'bold'))
    end_datelabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    end_dateEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    end_dateEntry.grid(row=2, column=1, padx=10, pady=15)
    end_dateEntry.insert(0, item_values[2])  # Pre-fill with existing value
    
    

    submitbutton = ttk.Button(update_window, text='Update Event', command=updatedata)
    submitbutton.grid(row=6, columnspan=2)




def addagent():
    # def add_data():
    #     if nameEntry.get() == '' or start_dateEntry.get() == '' or end_dateEntry.get() == '' :
    #         messagebox.showerror('Error', 'All Fields Must Be Filled', parent=add_window)
    #         return
    #     try:
    #         con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
    #         cursor = con.cursor()
    #         cursor.execute("INSERT INTO event ( event_name,start_date,end_date) VALUES ( %s, %s, %s)", ( nameEntry.get(), start_dateEntry.get(), end_dateEntry.get()))
    #         con.close()
    #         messagebox.showinfo("Status", "Successfully registered")
    #         print(nameEntry.get())
    #     except Exception as e:
    #         messagebox.showerror("Error", f"Error in connecting to database: {str(e)}")
    def add_data():
        if nameEntry.get() == '' or start_dateEntry.get() == '' or end_dateEntry.get() == '':
            messagebox.showerror('Error', 'All Fields Must Be Filled', parent=add_window)
            return
        try:
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("INSERT INTO event (event_name, start_date, end_date) VALUES (%s, %s, %s)", (nameEntry.get(), start_dateEntry.get(), end_dateEntry.get()))
            con.commit()  # Commit changes to the database
            con.close()
            messagebox.showinfo("Status", "Successfully registered")
        except Exception as e:
            messagebox.showerror("Error", f"Error in connecting to database: {str(e)}")
            print("Data added successfully")  # Add this line for debugging
    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)
    # idlabel=Label(add_window,text='Id',font=('times new roman',20,'bold'))
    # idlabel.grid(row=0,column=0,padx=30,pady=15,sticky= W)                                             
    # idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    # idEntry.grid(row=0,column=1,padx=10,pady=15)

    namelabel=Label(add_window,text='Event Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,padx=30,pady=15,sticky= W)
    nameEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=10,pady=15)
    
    start_datelabel=Label(add_window,text='Start Date',font=('times new roman',20,'bold'))
    start_datelabel.grid(row=2,column=0,padx=30,pady=15,sticky= W)

    start_dateEntry = DateEntry(add_window, width= 16, background= "magenta3", foreground= "white",bd=2)    
    start_dateEntry.grid(row=2,column=1,padx=10,pady=15, sticky= W)
    start_dateEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    start_dateEntry.grid(row=2,column=1,padx=10,pady=15)
    
    end_datelabel=Label(add_window,text='End Date',font=('times new roman',20,'bold'))
    end_datelabel.grid(row=3,column=0,padx=30,pady=15,sticky= W)
    end_dateEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    end_dateEntry.grid(row=3,column=1,padx=10,pady=15)
    
    submitbutton=ttk.Button(add_window,text='Add Event',command=add_data)
    submitbutton.grid(row=7,columnspan=2) 



#GUI
root=ttkthemes.ThemedTk('Radiance')
root.get_themes()

root.geometry('1174x680+50+20')
root.resizable(0,0)
root.title('Add Event')

bgImage = ImageTk.PhotoImage(file='Images/add.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

datetimelabel=Label(root,font=('times new Roman',18,'bold'),bg='#DFA7E4', fg='#A5256B')
datetimelabel.place(x=10,y=5)
clock()

heading2 = Label(root, text='Event Details', font=('arial', 28), bg='#DFA7E4', fg='#A5256B')
heading2.place(x=600, y=40)


leftFrame=Frame(root,bg='#DFA7E4')
leftFrame.place(x=5,y=250,width=320,height=525)

addeventbutton=Button(leftFrame,text='Add Event',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=addagent)
addeventbutton.grid(row=1,column=0,pady=20,padx=100)

update_eventbutton=Button(leftFrame,text='Update Event',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=updateagent)
update_eventbutton.grid(row=2,column=0,pady=20,padx=100)

deletebutton=Button(leftFrame,text='Delete Event',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=deleteagent)
deletebutton.grid(row=3,column=0,pady=20,padx=100)

showbutton=Button(leftFrame,text='Show Event',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=showagent)
showbutton.grid(row=4,column=0,pady=20,padx=100)

exitbutton=Button(leftFrame,text='Exit',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
exitbutton.grid(row=5,column=0,pady=20,padx=100)

rightFrame=Frame(root,bg='white')
rightFrame.place(x=365,y=130,width=820,height=550)

ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(rightFrame)

eventTable=ttk.Treeview(rightFrame,columns=('event_name','start_date','end_date'),
                        xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
ScrollbarX.config(command=eventTable.xview)
ScrollbarY.config(command=eventTable.yview)
ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)
eventTable.pack(fill=BOTH,expand=1)


eventTable.heading('event_name',text='Name')
eventTable.heading('start_date',text='Start Date')
eventTable.heading('end_date',text='End Date')


eventTable.config(show='headings')

root.mainloop()
