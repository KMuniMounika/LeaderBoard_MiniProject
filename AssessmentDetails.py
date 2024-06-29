import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('leaderboard.db')

# Create a cursor object
cursor = conn.cursor()

# SQL command to create the AssessmentDetails table
create_table_sql = """
CREATE TABLE AssessmentDetails (
    AssessmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    AssessmentName TEXT NOT NULL,
    TotalMarks INTEGER NOT NULL,
    PassingMarks INTEGER NOT NULL,
    DateCreated DATE NOT NULL,
    DateScheduled DATE NOT NULL,
    Duration INTEGER NOT NULL
);
"""

# Execute the SQL command
cursor.execute(create_table_sql)
print("AssessmentDetails table has been created")

# Commit the changes and close the connection
conn.commit()
conn.close()
