import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, department TEXT)''')

# Insert data into the table
cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)", ('John Doe', 30, 'HR'))
cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)", ('Jane Smith', 35, 'Finance'))

# Retrieve data from the table
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# Update a record in the table
cursor.execute("UPDATE employees SET age = ? WHERE name = ?", (32, 'John Doe'))

# Delete a record from the table
cursor.execute("DELETE FROM employees WHERE name = ?", ('Jane Smith',))

# Commit the changes and close the connection
conn.commit()
conn.close()
