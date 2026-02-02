import sqlite3
conn = sqlite3.connect('academic.db')
conn.execute("UPDATE users SET role = 'admin' WHERE email = 'admin@uni.edu'")
conn.commit()
conn.close()
print("Success: admin@uni.edu is now an admin.")
