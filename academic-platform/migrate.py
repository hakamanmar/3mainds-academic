import sqlite3
import os

DB_PATH = 'academic.db'

def migrate():
    if not os.path.exists(DB_PATH):
        print("DB not found")
        return
        
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Check if columns exist
    c.execute("PRAGMA table_info(users)")
    columns = [col[1] for col in c.fetchall()]
    
    if 'device_id' not in columns:
        print("Adding device_id column...")
        c.execute("ALTER TABLE users ADD COLUMN device_id TEXT")
        
    if 'must_change_pw' not in columns:
        print("Adding must_change_pw column...")
        c.execute("ALTER TABLE users ADD COLUMN must_change_pw INTEGER DEFAULT 0")
        
    conn.commit()
    conn.close()
    print("Migration finished")

if __name__ == "__main__":
    migrate()
