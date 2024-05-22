import sqlite3

def create_table():
    conn = sqlite3.connect('plans.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS plans(
            username TEXT,
            date TEXT,
            time TEXT PRIMARY KEY,
            day TEXT,
            plan TEXT
        )
    ''')
    conn.commit()
    conn.close()

def fetch_plans():
    conn = sqlite3.connect('plans.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM plans')
    plans = cursor.fetchall()
    conn.close()
    return plans

def insert_plan(username, date, time, day, plan):
    conn = sqlite3.connect('plans.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO plans (username, date, time, day, plan) VALUES (?, ?, ?, ?, ?)',
                   (username, date, time, day, plan))
    conn.commit()
    conn.close()

def delete_plan(times):
    conn = sqlite3.connect('plans.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM plans WHERE time IN ({})'.format(','.join(['?']*len(times))), times)
    conn.commit()
    conn.close()

def update_plan(username, date, time, day, plan):
    conn = sqlite3.connect('plans.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE plans SET username=?, date=?, day=?, plan=? WHERE time=?',
                   (username, date, day, plan, time))
    conn.commit()
    conn.close()

def time_exists(time):
    conn = sqlite3.connect('plans.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM plans WHERE time=?', (time,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

# Create the table
create_table()