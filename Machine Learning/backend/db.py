import sqlite3

def get_db_connection():
    conn = sqlite3.connect('food_waste.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_sensor_data():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM sensor_data').fetchall()
    conn.close()
    return [dict(row) for row in data]

def insert_sensor_data(sensor_data):
    conn = get_db_connection()
    conn.execute('INSERT INTO sensor_data (temperature, humidity, gas_level) VALUES (?, ?, ?)', 
                 (sensor_data['temperature'], sensor_data['humidity'], sensor_data['gas_level']))
    conn.commit()
    conn.close()
