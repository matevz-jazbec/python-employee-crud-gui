"""
Employee CRUD App with Tkinter and MySQL

This script provides a simple GUI application for managing employee records. It supports Create, Read, Update, and Delete (CRUD) operations on a MySQL database. 
"""

# --- Import required libraries ---
from tkinter import *
from tkinter import messagebox
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# --- Helper functions ---
def get_db_connection():
    """Establishes a connection to the MySQL database using .env settings."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSWD"),
        database=os.getenv("DB_DATABASE")
    )

def get_input_data():
    """Reads data from input fields (ID, name, department)."""
    return entry_id.get(), entry_name.get(), entry_dept.get()

def reset_fields():
    """Clears all input fields."""
    entry_id.delete(0, "end"); entry_name.delete(0, "end"); entry_dept.delete(0, "end")

# --- Data manipulation functions (CRUD operations) ---
def insert_data():
    """Inserts a new record into the empDetails table and refreshes the display."""
    emp_id, name, dept = get_input_data()
    if not emp_id or not name or not dept:
        messagebox.showwarning("Cannot Insert", "All the fields are required!")
        return

    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    
    sql = "INSERT INTO empDetails (empID, empName, empDept) VALUES (%s, %s, %s)"
    val = (emp_id, name, dept)
    cursor.execute(sql, val)
    
    db_connection.commit()
    db_connection.close()
    
    reset_fields()
    show_all_data()
    messagebox.showinfo("Insert Status", "Data inserted successfully")

def update_data():
    """Updates an existing record in the empDetails table and refreshes the display."""
    emp_id, name, dept = get_input_data()
    if not emp_id or not name or not dept:
        messagebox.showwarning("Cannot Update", "All the fields are required!")
        return

    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    
    sql = "UPDATE empDetails SET empName = %s, empDept = %s WHERE empID = %s"
    val = (name, dept, emp_id)
    cursor.execute(sql, val)
    
    db_connection.commit()
    db_connection.close()

    reset_fields()
    show_all_data()
    messagebox.showinfo("Update Status", "Data updated successfully")

def get_data():
    """Fetches employee data by ID and displays it in the input fields."""
    emp_id = entry_id.get()
    if not emp_id:
        messagebox.showwarning("Fetch Status", "Please provide the Employee ID.")
        return

    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    
    sql = "SELECT * FROM empDetails WHERE empID = %s"
    val = (emp_id,)
    cursor.execute(sql, val)
    row = cursor.fetchone()
    
    db_connection.close()

    if row:
        entry_name.delete(0, "end"); entry_dept.delete(0, "end")
        entry_name.insert(0, row[1]); entry_dept.insert(0, row[2])
    else:
        messagebox.showwarning("Fetch Status", "No data found for the provided ID")

def show_all_data():
    """Displays all records from the empDetails table in the listbox."""
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    
    cursor.execute("SELECT * FROM empDetails")
    rows = cursor.fetchall()
    
    db_connection.close()
    
    listbox_data.delete(0, "end")
    for row in rows:
        add_data = f"{row[0]}     {row[1]}     {row[2]}"
        listbox_data.insert("end", add_data)

def delete_data():
    """Deletes a record by ID and refreshes the display."""
    emp_id = entry_id.get()
    if not emp_id:
        messagebox.showwarning("Cannot Delete", "Please provide the Employee ID.")
        return

    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    
    sql = "DELETE FROM empDetails WHERE empID = %s"
    val = (emp_id,)
    cursor.execute(sql, val)
    
    db_connection.commit()
    db_connection.close()
    
    reset_fields()
    show_all_data()
    messagebox.showinfo("Delete Status", "Data deleted successfully")

# --- Graphical User Interface (GUI) ---
"""
GUI with input fields for ID, name, department, buttons for CRUD operations, and a listbox for displaying data.
"""
window = Tk()
window.geometry("600x270")
window.title("Employee CRUD App")

label_id = Label(window, text="Employee ID", font=("Sans", 12))
label_id.grid(row=0, column=0, padx=20, pady=5, sticky='w')
entry_id = Entry(window)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_name = Label(window, text="Employee Name", font=("Sans", 12))
label_name.grid(row=1, column=0, padx=20, pady=5, sticky='w')
entry_name = Entry(window)
entry_name.grid(row=1, column=1, padx=10, pady=5)

label_dept = Label(window, text="Employee Dept", font=("Sans", 12))
label_dept.grid(row=2, column=0, padx=20, pady=5, sticky='w')
entry_dept = Entry(window)
entry_dept.grid(row=2, column=1, padx=10, pady=5)

button_frame = Frame(window)
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

insert_btn = Button(button_frame, text="Insert", font=("Sans", 12), bg="white", command=insert_data)
insert_btn.grid(row=0, column=0, padx=5)
update_btn = Button(button_frame, text="Update", font=("Sans", 12), bg="white", command=update_data)
update_btn.grid(row=0, column=1, padx=5)
get_btn = Button(button_frame, text="Fetch", font=("Sans", 12), bg="white", command=get_data)
get_btn.grid(row=0, column=2, padx=5)
delete_btn = Button(button_frame, text="Delete", font=("Sans", 12), bg="white", command=delete_data)
delete_btn.grid(row=0, column=3, padx=5)
reset_btn = Button(button_frame, text="Reset", font=("Sans", 12), bg="white", command=reset_fields)
reset_btn.grid(row=1, column=0, columnspan=4, pady=5, padx=5)

listbox_data = Listbox(window)
listbox_data.grid(row=0, column=2, rowspan=4, padx=10, pady=10)

show_all_data()
window.mainloop()