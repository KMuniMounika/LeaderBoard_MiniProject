import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('leaderboard.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to create the AssessmentResult table
create_table_sql = """
CREATE TABLE AssessmentResult (
    ResultID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID INTEGER NOT NULL,
    AssessmentID INTEGER NOT NULL,
    Score INTEGER NOT NULL,
    Grade TEXT NOT NULL,
    DateTaken DATE NOT NULL,
    Comments TEXT,
    Status TEXT NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES STUDENT_DETAILS(StudentID),
    FOREIGN KEY (AssessmentID) REFERENCES AssessmentDetails(AssessmentID)
);
"""

# Execute the SQL command
cursor.execute(create_table_sql)
print("AssessmentResult table has been created")

# Commit the changes and close the connection
conn.commit()
conn.close()
