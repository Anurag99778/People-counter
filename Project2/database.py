import mysql.connector

def connect_db():
    """Connect to the MySQL database and return the connection and cursor."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # replace with your MySQL username
        password="An@210803",  # replace with your MySQL password
        database="people_counting"  # replace with your database name
    )
    cursor = conn.cursor()
    return conn, cursor

def insert_counts(count_up, count_down):
    """Insert count_up and count_down into the people_counts table."""
    conn, cursor = connect_db()
    cursor.execute('INSERT INTO people_counts (count_up, count_down) VALUES (%s, %s)', (count_up, count_down))
    conn.commit()
    conn.close()
