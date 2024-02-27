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

#functionality
def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimelabel.config(text=f'Date:{date}\nTime:{currenttime}')
    datetimelabel.after(1000,clock)

def deletedecor():
    selected_item = decorTable.focus()
    
    if not selected_item:
        messagebox.showerror('Error', 'Please select an venue to delete')
        return
    else:
        try:
            # Retrieve the venue ID from the selected item
            item_values = decorTable.item(selected_item, 'values')
            decor_id = item_values[0]
            
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("DELETE FROM decoration WHERE decor_id = %s", (decor_id,))
            con.commit()
            con.close()
            messagebox.showinfo('Deleted', 'Data successfully deleted')
        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error deleting venue: {e}')



# def showdecor():
#     con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
#     cursor = con.cursor()
#     cursor.execute("SELECT decor_id, agency_name, agency_manager, decor_address, decor_contact FROM decor")
#     fetched_data = cursor.fetchall()
#     # print(fetched_data)
#     decorTable.delete(*decorTable.get_children())
#     for data in fetched_data:
#         decorTable.insert('',END,values=data)
#     con.close()
            



def showdecor():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
    cursor = con.cursor()
    cursor.execute("SELECT agency_name, decor_address, decor_contact FROM decoration")
    fetched_data = cursor.fetchall()
    decorTable.delete(*decorTable.get_children())
    for data in fetched_data:
        decorTable.insert('', END, values=data)





















def updatedecor():
    def update_data():
         if nameEntry.get() == '' or decoraddressEntry.get() == '' or  decorcontactEntry.get() == '':
            messagebox.showerror('Error', 'All Fields Must Be Filled', parent=update_window)
            return
         else:

            try:
                con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
                cursor = con.cursor()
                cursor.execute("UPDATE decoration SET   decor_address = %s, decor_contact = %s WHERE agency_name = %s", (nameEntry.get(),decoraddressEntry.get(), decorcontactEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Status", "Decor details updated successfully")
                update_window.destroy()  # Close the update window after successful update
            except Exception as e:
                messagebox.showerror("Error", f"Error in updating agent: {str(e)}")

    selected_item = decorTable.focus()
    
    if not selected_item:
        messagebox.showerror('Error', 'Please select decor to update')
        return
    
    item_values = decorTable.item(selected_item, 'values')
    decor_id = item_values[0]

    update_window = Toplevel()
    update_window.grab_set()
    update_window.resizable(0, 0)

    namelabel=Label(update_window,text='Company Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,padx=30,pady=15,sticky= W)
    nameEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=10,pady=15)
    nameEntry.insert(0, item_values[0]) 
    
    # decormanagerlabel=Label(update_window,text='Decor Manager Name',font=('times new roman',20,'bold'))
    # decormanagerlabel.grid(row=2,column=0,padx=30,pady=15,sticky= W)
    # decormanagerEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    # decormanagerEntry.grid(row=2,column=1,padx=10,pady=15)
    # decormanagerEntry.insert(0, item_values[2]) 


    decoraddresslabel=Label(update_window,text='Decor Company Address',font=('times new roman',20,'bold'))
    decoraddresslabel.grid(row=5,column=0,padx=30,pady=15,sticky= W)
    decoraddressEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    decoraddressEntry.grid(row=5,column=1,padx=10,pady=15)
    decoraddressEntry.insert(0, item_values[1]) 
    
    decorcontactlabel=Label(update_window,text='Decor Contact',font=('times new roman',20,'bold'))
    decorcontactlabel.grid(row=3,column=0,padx=30,pady=15,sticky= W)
    decorcontactEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    decorcontactEntry.grid(row=3,column=1,padx=10,pady=15)
    decorcontactEntry.insert(0, item_values[2]) 
    

    

    submitbutton=ttk.Button(update_window,text='Update',command=update_data)
    submitbutton.grid(row=7,columnspan=2) 







def adddecor():
    def add_data():
        if nameEntry.get() == ''  or decoraddressEntry.get() == '' or  decorcontactEntry.get() == '':
            messagebox.showerror('Error', 'All Fields Must Be Filled', parent=add_window)
            return

        try:
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("INSERT INTO decoration ( agency_name, decor_address,decor_contact) VALUES ( %s, %s, %s)", ( nameEntry.get(), decoraddressEntry.get(), decorcontactEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Status", "Successfully registered")
        except Exception as e:
            messagebox.showerror("Error", f"Error in connecting to database: {str(e)}")

    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)
   
    namelabel=Label(add_window,text='Company Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,padx=30,pady=15,sticky= W)
    nameEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=10,pady=15)
    
    # decormanagerlabel=Label(add_window,text='Decor Manager Name',font=('times new roman',20,'bold'))
    # decormanagerlabel.grid(row=2,column=0,padx=30,pady=15,sticky= W)
    # decormanagerEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    # decormanagerEntry.grid(row=2,column=1,padx=10,pady=15)

    decoraddresslabel=Label(add_window,text='Decor Company Address',font=('times new roman',20,'bold'))
    decoraddresslabel.grid(row=5,column=0,padx=30,pady=15,sticky= W)
    decoraddressEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    decoraddressEntry.grid(row=5,column=1,padx=10,pady=15)
    
    
    decorcontactlabel=Label(add_window,text='Decor Contact',font=('times new roman',20,'bold'))
    decorcontactlabel.grid(row=3,column=0,padx=30,pady=15,sticky= W)
    decorcontactEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    decorcontactEntry.grid(row=3,column=1,padx=10,pady=15)

    submitbutton=ttk.Button(add_window,text='Add',command=add_data)
    submitbutton.grid(row=7,columnspan=2) 




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

addbutton=Button(leftFrame,text='Add Data ',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=adddecor)
addbutton.grid(row=1,column=0,pady=20,padx=100)

updatevenuebutton=Button(leftFrame,text='Update Data',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=updatedecor)
updatevenuebutton.grid(row=2,column=0,pady=20,padx=100)

deletebutton=Button(leftFrame,text='Delete Data',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=deletedecor)
deletebutton.grid(row=3,column=0,pady=20,padx=100)

showbutton=Button(leftFrame,text='Show Data',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=showdecor)
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