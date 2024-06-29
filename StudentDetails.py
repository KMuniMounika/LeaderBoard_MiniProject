import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('leaderboard.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to create the STUDENT_DETAILS table
create_table_sql = """
CREATE TABLE STUDENT_DETAILS (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    RollNumber TEXT UNIQUE NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    Phone TEXT NOT NULL,
    Address TEXT,
    DateOfJoining DATE NOT NULL,
    Status TEXT NOT NULL
);
"""

# Execute the SQL command
cursor.execute(create_table_sql)
print("StudentDetails table has been created")

# Commit the changes and close the connection
conn.commit()
conn.close()
