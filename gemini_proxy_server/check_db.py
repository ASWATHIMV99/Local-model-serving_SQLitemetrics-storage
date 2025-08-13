import sqlite3
conn = sqlite3.connect('metrics.db')
cursor = conn.cursor()

# Check request_logs
cursor.execute("SELECT * FROM request_logs LIMIT 5")
print("Request logs:", cursor.fetchall())

# Check response_logs  
cursor.execute("SELECT * FROM response_logs LIMIT 5")
print("Response logs:", cursor.fetchall())

# Exit when done
exit()