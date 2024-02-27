from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import time
import ttkthemes
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

#function for delete venue
def deletevenue():
    selected_item = venueTable.focus()
    
    if not selected_item:
        messagebox.showerror('Error', 'Please select an venue to delete')
        return
    else:
        try:
            # Retrieve the venue ID from the selected item
            item_values = venueTable.item(selected_item, 'values')
            venue_id = item_values[0]
            
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("DELETE FROM venue WHERE venue_id = %s", (venue_id,))
            con.commit()
            con.close()
            messagebox.showinfo('Deleted', 'Venue successfully deleted')
        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error deleting venue: {e}')



# def showvenue():
#     con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
#     cursor = con.cursor()
#     cursor.execute("SELECT  * from venue")
#     fetched_data = cursor.fetchall()
#     venueTable.delete(*venueTable.get_children())
#     for data in fetched_data:
#         venueTable.insert('',END,values=data)
            






def showvenue():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
    cursor = con.cursor()
    cursor.execute("SELECT venue_name, venue_address, venue_contact FROM venue")
    fetched_data = cursor.fetchall()
    venueTable.delete(*venueTable.get_children())
    for data in fetched_data:
        venueTable.insert('', END, values=data)

    
# 

def updatevenue():
    def update_data():
         if nameEntry.get() == ''  or  venueaddressEntry.get() == ''or venuecontactEntry.get() == '':
            messagebox.showerror('Error', 'All Fields Must Be Filled', parent=update_window)
            return
         else:

            try:
                con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
                cursor = con.cursor()
                cursor.execute("UPDATE venue SET  venue_address = %s, venue_contact = %s WHERE venue_name = %s", (nameEntry.get(), venueaddressEntry.get(), venuecontactEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Status", "Venue details updated successfully")
                update_window.destroy()  # Close the update window after successful update
            except Exception as e:
                messagebox.showerror("Error", f"Error in updating agent: {str(e)}")

    selected_item = venueTable.focus()
    
    if not selected_item:
        messagebox.showerror('Error', 'Please select an venue to update')
        return
    
    item_values = venueTable.item(selected_item, 'values')
    venue_id = item_values[0]

    update_window = Toplevel()
    update_window.grab_set()
    update_window.resizable(0, 0)

    namelabel=Label(update_window,text='Venue Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,padx=30,pady=15,sticky= W)
    nameEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=10,pady=15)
    nameEntry.insert(0, item_values[0]) 
    
    # managerlabel=Label(update_window,text='Venue Manager Name',font=('times new roman',20,'bold'))
    # managerlabel.grid(row=2,column=0,padx=30,pady=15,sticky= W)
    # managerEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    # managerEntry.grid(row=2,column=1,padx=10,pady=15)
    # managerEntry.insert(0, item_values[2]) 


    venueaddresslabel=Label(update_window,text='Address',font=('times new roman',20,'bold'))
    venueaddresslabel.grid(row=2,column=0,padx=30,pady=15,sticky= W)
    venueaddressEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    venueaddressEntry.grid(row=2,column=1,padx=10,pady=15)
    venueaddressEntry.insert(0, item_values[1]) 
    
    venuecontactlabel=Label(update_window,text='Venue Contact',font=('times new roman',20,'bold'))
    venuecontactlabel.grid(row=5,column=0,padx=30,pady=15,sticky= W)
    venuecontactEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    venuecontactEntry.grid(row=5,column=1,padx=10,pady=15)
    venuecontactEntry.insert(0, item_values[2]) 
    

    

    submitbutton=ttk.Button(update_window,text='Update Venue',command=update_data)
    submitbutton.grid(row=7,columnspan=2) 



def addvenue():
    def add_data():
        if nameEntry.get() == ''  or venueaddressEntry.get() == '' or  venuecontactEntry.get() == '':
            messagebox.showerror('Error', 'All Fields Must Be Filled', parent=add_window)
            return

        try:
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("INSERT INTO venue ( venue_name,  venue_address,venue_contact) VALUES ( %s, %s, %s)", ( nameEntry.get(),  venueaddressEntry.get(), venuecontactEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Status", "Successfully registered")
        except Exception as e:
            messagebox.showerror("Error", f"Error in connecting to database: {str(e)}")

    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)
    # idlabel=Label(add_window,text='Id',font=('times new roman',20,'bold'))
    # idlabel.grid(row=0,column=0,padx=30,pady=15,sticky= W)                                             
    # idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    # idEntry.grid(row=0,column=1,padx=10,pady=15)

    namelabel=Label(add_window,text='Venue Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,padx=30,pady=15,sticky= W)
    nameEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=10,pady=15)
    
    # managerlabel=Label(add_window,text='Venue Manager Name',font=('times new roman',20,'bold'))
    # managerlabel.grid(row=2,column=0,padx=30,pady=15,sticky= W)
    # managerEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    # managerEntry.grid(row=2,column=1,padx=10,pady=15)

    venueaddresslabel=Label(add_window,text='Address',font=('times new roman',20,'bold'))
    venueaddresslabel.grid(row=5,column=0,padx=30,pady=15,sticky= W)
    venueaddressEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    venueaddressEntry.grid(row=5,column=1,padx=10,pady=15)
    
    
    venuecontactlabel=Label(add_window,text='Venue Contact',font=('times new roman',20,'bold'))
    venuecontactlabel.grid(row=3,column=0,padx=30,pady=15,sticky= W)
    venuecontactEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    venuecontactEntry.grid(row=3,column=1,padx=10,pady=15)
    
    
   

    submitbutton=ttk.Button(add_window,text='Add Agent',command=add_data)
    submitbutton.grid(row=7,columnspan=2) 



    

#GUI
root=ttkthemes.ThemedTk('Radiance')
root.geometry('1174x680+50+20')
root.resizable(0,0)
root.title('Add Venue')

bgImage = ImageTk.PhotoImage(file='Images/add.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

datetimelabel=Label(root,font=('times new Roman',18,'bold'),bg='#DFA7E4', fg='#A5256B')
datetimelabel.place(x=10,y=5)
clock()

heading2 = Label(root, text='Venue Details', font=('arial', 28), bg='#DFA7E4', fg='#A5256B')
heading2.place(x=580, y=50)


leftFrame=Frame(root,bg='#DFA7E4')
leftFrame.place(x=5,y=250,width=320,height=525)

venuebutton=Button(leftFrame,text='Add Venue',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=addvenue)
venuebutton.grid(row=1,column=0,pady=20,padx=100)

updatevenuebutton=Button(leftFrame,text='Update Venue',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=updatevenue)
updatevenuebutton.grid(row=2,column=0,pady=20,padx=100)

deletebutton=Button(leftFrame,text='Delete Venue',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=deletevenue)
deletebutton.grid(row=3,column=0,pady=20,padx=100)

showbutton=Button(leftFrame,text='Show Venue',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=showvenue)
showbutton.grid(row=4,column=0,pady=20,padx=100)

exitbutton=Button(leftFrame,text='Exit',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
exitbutton.grid(row=5,column=0,pady=20,padx=100)

rightFrame=Frame(root,bg='white')
rightFrame.place(x=365,y=130,width=820,height=550)

ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(rightFrame)

venueTable=ttk.Treeview(rightFrame,columns=('Venue Name','Venue Address','Contact'),
                        xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
ScrollbarX.config(command=venueTable.xview)
ScrollbarY.config(command=venueTable.yview)
ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)
venueTable.pack(fill=BOTH,expand=1)

venueTable.heading('Venue Name',text='Venue Name')
# venueTable.heading('Manager Name',text='Manager Name')
venueTable.heading('Venue Address',text='Venue Address')
venueTable.heading('Contact',text='Contact')


venueTable.config(show='headings')

root.mainloop()
