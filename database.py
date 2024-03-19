####import sqlite3
####
##### Connect to the database (create it if it doesn't exist)
####conn = sqlite3.connect('Attendance.dbb')
####cursor = conn.cursor()
####
##### Create a table if it doesn't exist
####cursor.execute('''CREATE TABLE IF NOT EXISTS attendance(id INTEGER PRIMARY KEY, name TEXT NOT NULL)''')
####
##### Commit the changes
####conn.commit()
####
##### Close the connection
####conn.close()



import sqlite3

class AttendanceDatabase:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cur = self.conn.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY,
            employee_id TEXT,
            date TEXT,
            status TEXT
        )
        """
        self.cur.execute(sql)
        self.conn.commit()

    def insert(self, employee_id, date, status):
        self.cur.execute("INSERT INTO attendance (employee_id, date, status) VALUES (?, ?, ?)",
                         (employee_id, date, status))
        self.conn.commit()

    def get(self):
        self.cur.execute("SELECT * FROM attendance")
        rows = self.cur.fetchall()
        return rows

    def close(self):
        self.conn.close()
