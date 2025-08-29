# Employee CRUD App

This is a simple study project that demonstrates how to build a CRUD (Create, Read, Update, Delete) application in Python using Tkinter for the graphical user interface (GUI) and MySQL for database storage. The app allows you to manage employee records (ID, name, department) via a graphical interface.

---

## Features
- Insert a new employee  
- Update employee details  
- Fetch employee by ID 
- Delete employee  
- Reset input fields 
- View all employees  

---

## Requirements
- Python 3
- MySQL server  
- Installed Python packages:  
  ```bash
  pip install mysql-connector-python python-dotenv
  ```

---

## Database Setup
Create a database (e.g. `employee`):  
   ```sql
   CREATE DATABASE employee;
   USE employee;
   CREATE TABLE empDetails (
       empID INT PRIMARY KEY,
       empName VARCHAR(50),
       empDept VARCHAR(50)
   );
   ```

---

## Configuration
Database credentials are stored in a `.env` file in the project root:

```
DB_HOST=localhost
DB_USER=your_user
DB_PASSWD=your_password
DB_DATABASE=employee
```

---

## Run the App
Start the program with:

```bash
python3 employee_crud_app.py   # macOS / Linux
python employee_crud_app.py    # Windows
```

The GUI will open and you can begin managing employee records.

---

## Notes
This is a basic educational project for learning Python, Tkinter, and MySQL integration. It is not optimized for production use. 
Make sure to run the script from the same folder where the `.env` file is located, otherwise the database connection may not work.
