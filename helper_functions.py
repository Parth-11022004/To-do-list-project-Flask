import sqlite3

def create_table():
    conn = sqlite3.connect("my_db.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        status TEXT DEFAULT 'pending'
    )
    """)
    conn.close()

def get_all_tasks(status):
    conn = sqlite3.connect("my_db.db")
    cursor = conn.cursor()
    if not status:
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
    else:
        cursor.execute("SELECT * FROM tasks WHERE status = ?",(status,))
        rows = cursor.fetchall()
    conn.close()
    result = [{"id":row[0],"name":row[1],"status":row[2]} for row in rows]
    return result
    
def insert_task(task):
    conn = sqlite3.connect("my_db.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (name) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect("my_db.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?",(task_id,))
    conn.commit()
    conn.close()

def clear_all_tasks():
    conn = sqlite3.connect("my_db.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks")
    conn.commit()
    conn.close()

def update_status(task_id, status):
    conn = sqlite3.connect("my_db.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?",(status,task_id))
    conn.commit()
    conn.close()
