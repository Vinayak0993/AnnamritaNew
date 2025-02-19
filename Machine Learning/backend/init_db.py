import sqlite3

def create_database():
    # Connect to SQLite (it will create the DB file if it doesn't exist)
    conn = sqlite3.connect('food_waste.db')
    
    # Create a cursor object
    cursor = conn.cursor()

    # Create the sensor_data table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL,
            gas_level REAL NOT NULL,
            spoilage INTEGER DEFAULT 0,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

if __name__ == '__main__':
    create_database()
