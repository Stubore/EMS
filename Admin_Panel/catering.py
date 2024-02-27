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

def deletecatering():
    selected_item = cateringTable.focus()
    
    if not selected_item:
        messagebox.showerror('Error', 'Please select an venue to delete')
        return
    else:
        try:
            # Retrieve the venue ID from the selected item
            item_values = cateringTable.item(selected_item, 'values')
            catering_id = item_values[0]
            
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("DELETE FROM catering WHERE catering_id = %s", (catering_id,))
            con.commit()
            con.close()
            messagebox.showinfo('Deleted', 'Catering data successfully deleted')
        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error deleting catering details: {e}')







def showcatering():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
    cursor = con.cursor()
    cursor.execute("SELECT catering_agency, catering_address, catering_contact FROM catering")
    fetched_data = cursor.fetchall()
    cateringTable.delete(*cateringTable.get_children())
    for data in fetched_data:
        cateringTable.insert('', END, values=data)





def updatecatering():
    def update_data(catering_id, nameEntry, cateringaddressEntry, cateringcontactEntry):
        if nameEntry.get() == '' or cateringaddressEntry.get() == '' or cateringcontactEntry.get() == '':
            messagebox.showerror('Error', 'All Fields Must Be Filled', parent=update_window)
            return
        else:
            try:
                con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
                cursor = con.cursor()
                cursor.execute("UPDATE catering SET catering_agency = %s, catering_address = %s, catering_contact = %s WHERE catering_id = %s", (nameEntry.get(), cateringaddressEntry.get(), cateringcontactEntry.get(), catering_id))
                con.commit()
                con.close()
                messagebox.showinfo("Status", "Catering details updated successfully")
                update_window.destroy()  # Close the update window after successful update
            except Exception as e:
                messagebox.showerror("Error", f"Error in updating catering: {str(e)}")

    selected_item = cateringTable.focus()

    if not selected_item:
        messagebox.showerror('Error', 'Please select a catering to update')
        return

    item_values = cateringTable.item(selected_item, 'values')
    catering_id = item_values[0]

    update_window = Toplevel()
    update_window.grab_set()
    update_window.resizable(0, 0)

    namelabel = Label(update_window, text='Catering Name', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=15)
    nameEntry.insert(0, item_values[0])

    cateringaddresslabel = Label(update_window, text='Catering Address', font=('times new roman', 20, 'bold'))
    cateringaddresslabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    cateringaddressEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    cateringaddressEntry.grid(row=2, column=1, padx=10, pady=15)
    cateringaddressEntry.insert(0, item_values[1])

    cateringcontactlabel = Label(update_window, text='Catering Contact', font=('times new roman', 20, 'bold'))
    cateringcontactlabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    cateringcontactEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    cateringcontactEntry.grid(row=3, column=1, padx=10, pady=15)
    cateringcontactEntry.insert(0, item_values[2])

    submitbutton = ttk.Button(update_window, text='Update Catering', command=lambda: update_data(catering_id, nameEntry, cateringaddressEntry, cateringcontactEntry))
    submitbutton.grid(row=4, columnspan=2)








def addcatering():
    def add_data():
        if nameEntry.get() == '' or  cateringaddressEntry.get() == '' or   cateringcontactEntry.get() == '':
            messagebox.showerror('Error', 'All Fields Must Be Filled', parent=add_window)
            return

        try:
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("INSERT INTO catering ( catering_agency, catering_address,catering_contact) VALUES ( %s, %s, %s)", ( nameEntry.get(),  cateringaddressEntry.get(),  cateringcontactEntry.get()))
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

    namelabel=Label(add_window,text='Catering Agency Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,padx=30,pady=15,sticky= W)
    nameEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=10,pady=15)
    
    # managerlabel=Label(add_window,text='Catering Manager Name',font=('times new roman',20,'bold'))
    # managerlabel.grid(row=2,column=0,padx=30,pady=15,sticky= W)
    # managerEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    # managerEntry.grid(row=2,column=1,padx=10,pady=15)

    cateringaddresslabel=Label(add_window,text='Catering Address',font=('times new roman',20,'bold'))
    cateringaddresslabel.grid(row=3,column=0,padx=30,pady=15,sticky= W)
    cateringaddressEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    cateringaddressEntry.grid(row=3,column=1,padx=10,pady=15)
    
    
    cateringcontactlabel=Label(add_window,text='Catering Contact',font=('times new roman',20,'bold'))
    cateringcontactlabel.grid(row=5,column=0,padx=30,pady=15,sticky= W)
    cateringcontactEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    cateringcontactEntry.grid(row=5,column=1,padx=10,pady=15)
    
    
   

    submitbutton=ttk.Button(add_window,text='Add catering',command=add_data)
    submitbutton.grid(row=7,columnspan=2) 


#GUI
root=ttkthemes.ThemedTk('Radiance')
root.geometry('1174x680+50+20')
root.resizable(0,0)
root.title('Add Catering')

bgImage = ImageTk.PhotoImage(file='Images/add.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

datetimelabel=Label(root,font=('times new Roman',18,'bold'),bg='#DFA7E4', fg='#A5256B')
datetimelabel.place(x=10,y=5)
clock()

heading2 = Label(root, text='Catering Details', font=('arial', 28), bg='#DFA7E4', fg='#A5256B')
heading2.place(x=580, y=50)


leftFrame=Frame(root,bg='#DFA7E4')
leftFrame.place(x=5,y=250,width=320,height=525)

venuebutton=Button(leftFrame,text='Add Data',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=addcatering)
venuebutton.grid(row=1,column=0,pady=20,padx=100)

updatevenuebutton=Button(leftFrame,text='Update Data',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=updatecatering)
updatevenuebutton.grid(row=2,column=0,pady=20,padx=100)

deletebutton=Button(leftFrame,text='Delete Data',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=deletecatering)
deletebutton.grid(row=3,column=0,pady=20,padx=100)

showbutton=Button(leftFrame,text='Show Data',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=showcatering)
showbutton.grid(row=4,column=0,pady=20,padx=100)

exitbutton=Button(leftFrame,text='Exit',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
exitbutton.grid(row=5,column=0,pady=20,padx=100)

rightFrame=Frame(root,bg='white')
rightFrame.place(x=365,y=130,width=820,height=550)

ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(rightFrame)

cateringTable=ttk.Treeview(rightFrame,columns=('Catering Company Name','Catering Address','Catering Contact'),
                        xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
ScrollbarX.config(command=cateringTable.xview)
ScrollbarY.config(command=cateringTable.yview)
ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)
cateringTable.pack(fill=BOTH,expand=1)

cateringTable.heading('Catering Company Name',text='Catering Company Name')
# cateringTable.heading('Catering Manager Name',text='Catering Manager Name')
cateringTable.heading('Catering Address',text='Catering Address')
cateringTable.heading('Catering Contact',text='Catering Contact')


cateringTable.config(show='headings')

root.mainloop()
