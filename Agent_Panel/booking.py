from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Event Management System"
)

cursor = connection.cursor()

# Execute query to retrieve data
cursor.execute("SELECT venue_name FROM venue")

venue_records = cursor.fetchall()

cursor.execute("SELECT agency_name FROM decoration")

decor_records = cursor.fetchall()

cursor.execute("SELECT catering_agency FROM catering")

catering_records = cursor.fetchall()

cursor.execute("SELECT event_name FROM event")

event_records = cursor.fetchall()
# Fetch all the records


# Close cursor and connection
cursor.close()
connection.close()

def on_select_decor(event):
    selected_decor = event.widget.get()
    print("You selected:", selected_decor)

def on_select_venue(event):
    selected_venue = event.widget.get()
    print("You selected:", selected_venue)

def on_select_catering(event):
    selected_catering = event.widget.get()
    print("You selected:", selected_catering)

def on_select_event(event):
    selected_event = event.widget.get()
    print("You selected:", selected_event)


# functionality
def add_booking():
    # if not (Customer_nameEntry.get() and Event_nameEntry.get() and venue_drop_down.get() and decor_drop_down.get() and catering_drop_down.get() and Customer_AddressEntry.get() and Customer_ContactEntry.get()):
    #     messagebox.showerror('Error', 'All fields must be filled')
    # # elif passwordEntry.get() != ConfirmpasswordEntry.get():
    # #     messagebox.showerror('Error', 'Passwords do not match')
    # else:
        try:
            # Connect to the database and insert user data
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("INSERT INTO booking (customer_name,event_name,venue_name,catering_agency,agency_name,address, contact) VALUES (%s, %s, %s, %s, %s, %s, %s)", (Customer_nameEntry.get(), event_drop_down.get(), venue_drop_down.get(),decor_drop_down.get(),catering_drop_down.get(),Customer_AddressEntry.get(),Customer_ContactEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Status", "Successfully Booked")
        except Exception as e:
            print("Error", f"Error connecting to database: {str(e)}")
            # messagebox.showerror("Error", f"Error connecting to database: {str(e)}")
root = Tk()
root.geometry('990x660+50+50')
root.resizable(0,0)
root.title('Create Booking')

bgImage = ImageTk.PhotoImage(file='Images/add.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

# Customer name, Event name, Venue, Decoration, Catering, Customer Address, and Customer Contact, 


heading=Label(root,text='Create Booking',font=('Microsoft Yahei UI Light',28,'bold'),bg='#DFA7E4',fg='#A5256B')
heading.place(x=550,y=40)


Customer_name = Label(root, text='Customer Name ', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white', fg='#A5256B')
Customer_name .place(x=355, y=150)
Customer_nameEntry = Entry(root, width=38, font=('Microsoft Yahei UI Light', 18), bg='white', bd=0, fg='#DFA7E4',
                      highlightbackground='black')  # Set white border color
Customer_nameEntry.place(x=500, y=150)

Event_name = Label(root, text='Event name', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white', fg='#A5256B')
Event_name .place(x=355, y=200)
# Event_nameEntry = Entry(root, width=38, font=('Microsoft Yahei UI Light', 18), bg='white', bd=0, fg='#DFA7E4',
#                       highlightbackground='black')  # Set white border color
# Event_nameEntry.place(x=500, y=200)

# # VenueEntry.place(x=500, y=250)
# decor_drop_down = ttk.Combobox(root, state="readonly", width= 33, font=('Microsoft Yahei UI Light', 18, 'bold'))
# decor_drop_down.place(x=500, y=200)
# # Populate the drop-down menu with data from MySQL
# decor_drop_down['values'] = [record[0] for record in decor_records]


Venue= Label(root, text='Venue', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white', fg='#A5256B')
Venue .place(x=355, y=250)
# VenueEntry = Entry(root, width=38, font=('Microsoft Yahei UI Light', 18), bg='white', bd=0, fg='#DFA7E4',
#                       highlightbackground='black')  # Set white border color
# VenueEntry.place(x=500, y=250)
venue_drop_down = ttk.Combobox(root, state="readonly", width= 33, font=('Microsoft Yahei UI Light', 18, 'bold'))
venue_drop_down.place(x=500, y=250)
# Populate the drop-down menu with data from MySQL
venue_drop_down['values'] = [record[0] for record in venue_records]


# VenueEntry.place(x=500, y=250)
decor_drop_down = ttk.Combobox(root, state="readonly", width= 33, font=('Microsoft Yahei UI Light', 18, 'bold'))
decor_drop_down.place(x=500, y=300)
# Populate the drop-down menu with data from MySQL
decor_drop_down['values'] = [record[0] for record in decor_records]


# VenueEntry.place(x=500, y=250)
catering_drop_down = ttk.Combobox(root, state="readonly", width= 33, font=('Microsoft Yahei UI Light', 18, 'bold'))
catering_drop_down.place(x=500, y=350)
# Populate the drop-down menu with data from MySQL
catering_drop_down['values'] = [record[0] for record in catering_records]


# VenueEntry.place(x=500, y=250)
event_drop_down = ttk.Combobox(root, state="readonly", width= 33, font=('Microsoft Yahei UI Light', 18, 'bold'))
event_drop_down.place(x=500, y=200)
# Populate the drop-down menu with data from MySQL
event_drop_down['values'] = [record[0] for record in event_records]


# Bind selection event
venue_drop_down.bind('<<ComboboxSelected>>', on_select_venue)
decor_drop_down.bind('<<ComboboxSelected>>', on_select_decor)
catering_drop_down.bind('<<ComboboxSelected>>', on_select_catering)
event_drop_down.bind('<<ComboboxSelected>>', on_select_event)

# Set initial selection
venue_drop_down.current(0)
decor_drop_down.current(0)
catering_drop_down.current(0)
event_drop_down.current(0)

# Place the drop-down menu in the window
# drop_down.pack(pady=10)

Decoration = Label(root, text='Decoration ', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white', fg='#A5256B')
Decoration.place(x=355, y=300)
# DecorationEntry = Entry(root, width=38, font=('Microsoft Yahei UI Light', 18), bg='white', bd=0, fg='#DFA7E4',
#                       highlightbackground='black')  # Set white border color
# DecorationEntry.place(x=500, y=300)

Catering = Label(root, text='Catering ', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white', fg='#A5256B')
Catering .place(x=355, y=350)
# CateringEntry = Entry(root, width=38, font=('Microsoft Yahei UI Light', 18), bg='white', bd=0, fg='#DFA7E4',
#                       highlightbackground='black')  # Set white border color
# CateringEntry.place(x=500, y=350)

Customer_Address = Label(root, text='Address ', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white', fg='#A5256B')
Customer_Address .place(x=355, y=400)
Customer_AddressEntry = Entry(root, width=38, font=('Microsoft Yahei UI Light', 18), bg='white', bd=0, fg='#DFA7E4',
                      highlightbackground='black')  # Set white border color
Customer_AddressEntry.place(x=500, y=400)


Customer_Contact = Label(root, text=' Contact ', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white', fg='#A5256B')
Customer_Contact .place(x=355, y=450)
Customer_ContactEntry = Entry(root, width=38, font=('Microsoft Yahei UI Light', 18), bg='white', bd=0, fg='#DFA7E4',
                      highlightbackground='black')  # Set white border color
Customer_ContactEntry.place(x=500, y=450)


bookButton = Button(root, text='Book', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#A5256B',
                     activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=add_booking)
bookButton.place(x=600, y=550)


root.mainloop()
