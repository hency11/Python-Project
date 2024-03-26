from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from dbb import Database
from database import AttendanceDatabase

root = Tk()
root.title("Login")
root.geometry("1920x1080+0+0")
root.configure(bg="#535c68")
label = Label( text=" Employee Management System Login" , bg="#535c68", fg="white", font=("Arial", 50, "bold"))
label.pack(pady=40)

# Create login functionality (assuming username and password check)
def login():
    # Replace this with your actual login logic
    if entry_username.get() == "admin" and entry_password.get() == "password":
        messagebox.showinfo("Login Successful", "Welcome, admin!")
        root.withdraw()  # Hide the login window
        open_employee_management_window()
        #open_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

 #Create labels and entry fields for username and password
label_username = Label(root, text="Username:" , bg="#535c68", fg="white", font=("Arial", 22))
label_username.pack(pady=5)
entry_username = Entry(root,font=("Arial", 20))
entry_username.pack(pady=20)

label_password = Label(root, text="Password:" , bg="#535c68", fg="white", font=("Arial", 22))
label_password.pack(pady=5)
entry_password = Entry(root, show="*",font=("Arial", 20) )
entry_password.pack(pady=20)

# Create login button
btn_login = Button(root, text="Login", command=login,font=("Arial", 16))
btn_login.pack(pady=10)

def open_employee_management_window():
    global  employee_window#root  #, dbb, details_window,employee_id
    #root.withdraw()  # Hide the login window
    employee_window = Toplevel(root)
    employee_window.title("Employee Management System")
    employee_window.geometry("800x600")
    label = Label(employee_window, text="Welcome to the Employee Management System",font=("Arial", 20))
    label.pack()
    
# Add a button labeled "Employee" with blue background
    btn_employee = Button(employee_window, text="Employee", bg="#3CAEA3" , font=("Arial", 24),command=dbb_window)# command=open_manage_employee_window)dbb_window
    btn_employee.pack(pady=10)

    btn_salary = Button(employee_window, text="Salary", bg="#3CAEA3", font=("Arial", 24), command=open_salary_window)
    btn_salary.pack()

    btn_mark_attendance = Button(employee_window, text="Mark Attendance", bg="#3CAEA3", font=("Arial", 24), command=open_mark_attendance_window)
    btn_mark_attendance.pack(pady=10)


def open_salary_window():
    salary_window = Toplevel()
    salary_window.title("Calculate Salary")
    salary_window.geometry("800x600")
    salary_window.configure(bg="#97C1A9") 

    label_employee_id = Label(salary_window, text="Enter Employee ID:" , font=("Arial", 26), anchor='center', fg="black", bg="#97C1A9")
    label_employee_id.pack(pady=10)

    entry_employee_id = Entry(salary_window, font=("Calibri", 26), width=30)
    entry_employee_id.pack(pady=10)

    label_working_days = Label(salary_window, text="Enter Number of Working Days:", font=("Arial", 26), anchor='center', fg="black", bg="#97C1A9")
    label_working_days.pack(pady=10)

    entry_working_days = Entry(salary_window, font=("Calibri", 26), width=30)
    entry_working_days.pack(pady=10)

    btn_calculate_salary = Button(salary_window, text="Calculate Salary", command=lambda: calculate_salary(entry_employee_id.get(), entry_working_days.get()),font=("Arial", 16),fg="black")
    btn_calculate_salary.pack(pady=10)

def calculate_salary(employee_id, working_days):
    try:
        # Convert the employee ID and working days to integers
        employee_id = int(employee_id)
        working_days = int(working_days)

        # Implement your salary calculation logic here
        # For now, let's assume a simple calculation
        salary_amount = 1000 * working_days

        # Convert the salary amount to Indian Rupees
        salary_in_rupees = "₹" + str(salary_amount)

        # Create a new window to display the salary details
        salary_details_window = Toplevel()
        salary_details_window.title("Salary Details")
        salary_details_window.geometry("800x600")
        salary_details_window.configure(bg="#97C1A9")

        # Display the employee ID, working days, and salary amount
        Label(salary_details_window, text=f"Employee ID: {employee_id}", font=("Arial", 20), bg="#97C1A9").pack()
        Label(salary_details_window, text=f"Working Days: {working_days}", font=("Arial", 20), bg="#97C1A9").pack()
        Label(salary_details_window, text=f"Salary Amount: {salary_in_rupees}", font=("Arial", 20), bg="#97C1A9").pack()

    except ValueError:
        messagebox.showerror("Error", "Please enter valid employee ID and working days.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def dbb_window():
    dbb = Database("Employee.dbb")
    root = Toplevel()
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="#2c3e50")
    root.state("zoomed")

    name = StringVar()
    age = StringVar()
    doj = StringVar()
    gender = StringVar()
    email = StringVar()
    contact = StringVar()

    # Entries Frame
    entries_frame = Frame(root,bg="#535c68")
    entries_frame.pack(side=TOP, fill=X)
    #entries_frame.config(bg="#535c68")  # Set background color here
    title = Label(entries_frame, text="Employee Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
    title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")


    lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
    lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
    txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")



    lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
    lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    txtAge = Entry(entries_frame, textvariable= age, font=("Calibri", 16), width=30)#,validate="key"
    txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")


    lbldoj = Label(entries_frame, text="D.O.J", font=("Calibri", 16), bg="#535c68", fg="white")
    lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    calDoj = DateEntry(entries_frame, textvariable=doj, font=("Calibri", 16), width=30,foreground="white", bd=2,date_pattern='yyyy/mm/dd')
    calDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    


    lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
    lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
    txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
    txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")


    lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
    lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
    comboGender['values'] = ("Male", "Female")
    comboGender.grid(row=3, column=1, padx=10, sticky="w")


    lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
    lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
    txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
    txtContact.grid(row=3, column=3, padx=10, sticky="w")


    lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
    lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")


    txtAddress = Text(entries_frame, width=85, height=5, font=("Calibri", 16))
    txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

    

    global row
    def getData(event):
        #global row
        try:
            selected_row = tv.focus()
            data = tv.item(selected_row)
            #global row
            row = data["values"]
            #print(row)
            name.set(row[1])
            age.set(row[2])
            age_val = int(row[2])
            if age_val < 18 or age_val > 65:
                messagebox.showerror("Error", "Age must be between 18 and 65")
                return
            doj.set(row[3])
            email.set(row[4])
            gender.set(row[5])
            contact.set(row[6])
            txtAddress.delete(1.0, END)
            txtAddress.insert(END, row[7])
        except IndexError:
            messagebox.showerror("Error","Please select a record")


    def displayAll():
        try:
            tv.delete(*tv.get_children())
            for row in dbb.fetch():
                tv.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_employee():
        try:
            if txtName.get() == "" or txtAge.get() == "" or calDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(1.0, END) == "":
                messagebox.showerror("Error in Input", "Please Fill All the Details")
                return
            age_val = int(txtAge.get())
            if age_val < 18 or age_val > 65:
                raise ValueError("Age must be between 18 and 65")

            contact_val = txtContact.get()
            if not contact_val.isdigit() or len(contact_val) != 10:
                raise ValueError("Contact number must be a 10-digit number")

            email_val = txtEmail.get()
            if "@" not in email_val or "." not in email_val:
                raise ValueError("Invalid email format")
            
            dbb.insert(txtName.get(), txtAge.get(),calDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(), txtAddress.get(1.0, END))
            messagebox.showinfo("Success", "Record Inserted")#txtDoj.get()
            clearAll()
            displayAll()
        except Exception as ve:
            messagebox.showerror("Error", str(ve))
    def update_employee():
        try:
            if txtName.get() == "" or txtAge.get() == "" or calDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(1.0, END) == "":
                messagebox.showerror("Error in Input", "Please Fill All the Details")
                return
            dbb.update(row[0], txtName.get(), txtAge.get(), calDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(), txtAddress.get(1.0, END))
            messagebox.showinfo("Success", "Record Update")
            clearAll()
            displayAll()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_employee():
        try:
            dbb.remove(row[0])
            clearAll()
            displayAll()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clearAll():
            name.set("")
            age.set("")
            doj.set("")
            gender.set("")
            email.set("")
            contact.set("")
            txtAddress.delete(1.0, END)


    btn_frame = Frame(entries_frame, bg="#535c68")
    btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
    btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                    bg="#16a085", bd=0)
    btnAdd.grid(row=0, column=0)
    btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                    fg="white", bg="#2980b9",
                    bd=0)
    btnEdit.grid(row=0, column=1, padx=10)
    btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                    fg="white", bg="#c0392b",
                    bd=0)
    btnDelete.grid(row=0, column=2, padx=10)
    btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                    bg="#f39c12",
                    bd=0)
    btnClear.grid(row=0, column=3, padx=10)

    # Table Frame
    tree_frame = Frame(root,bg="#ecf0f1" )
    tree_frame.place(x=0, y=480, width=1300, height=400)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 15),
                    rowheight=40)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 15))  # Modify the font of the headings
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8),style="mystyle.Treeview")
    tv.heading("1", text="ID")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.B")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Address")
    tv.column("8", width=3)
    tv['show'] = 'headings'
    tv.bind("<ButtonRelease-1>", getData)
    tv.pack(fill=X)

    for row in dbb.fetch():
            tv.insert("", "end", values=row)

    
    displayAll()

def open_mark_attendance_window():
    mark_attendance_window = Toplevel()
    mark_attendance_window.title("Mark Attendance")
    mark_attendance_window.geometry("800x600")
    mark_attendance_window.configure(bg="#B8CEC2") 

    label_employee_id = Label(mark_attendance_window, text="Enter Employee ID:", font=("Arial", 26), bg="#B8CEC2", fg="black")
    label_employee_id.pack()

    entry_employee_id = Entry(mark_attendance_window, font=("Calibri", 16), width=30)
    entry_employee_id.pack()

    cal = DateEntry(mark_attendance_window, width=12, background='darkblue', foreground='white', borderwidth=2 , date_pattern='yyyy-mm-dd')
    cal.pack(pady=20)



    
    def mark_attendance ():#():(employee_id, date):
       try:
           employee_id = entry_employee_id.get()
           date = cal.get()#entry_date.get()


           # Check if the employee ID and date are not empty
           if not employee_id or not date:
                raise ValueError("Employee ID and date cannot be empty")

            # Check if the employee is absent
           is_absent = messagebox.askyesno("Absent?", "Is the employee absent?")
           status = "Absent" if is_absent else "Present"



        # Insert the attendance record into the database
           #dbb_attendance
           database= AttendanceDatabase("Attendance.database")
           #dbb_attendance
           database.insert(employee_id, date,status)
        # Implement the attendance marking logic here
        # For now, let's assume a simple message to indicate successful marking
           messagebox.showinfo("Attendance Marked", f"Attendance marked for Employee ID: {employee_id} on {date}as {status}")
       except Exception as e:
           messagebox.showerror("Error", str(e))


    btn_mark_attendance = Button(mark_attendance_window, text="Mark Attendance", command=lambda: mark_attendance(), font=("Arial", 16))
    btn_mark_attendance.pack(pady=10)


root.mainloop()
