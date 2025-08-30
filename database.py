import sqlite3

DB_NAME = "flights.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def create_reservation(name, flight_number, departure, destination, date, seat_number):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number) VALUES (?, ?, ?, ?, ?, ?)",
              (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()

def get_all_reservations():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM reservations")
    rows = c.fetchall()
    conn.close()
    return rows

def update_reservation(res_id, name, flight_number, departure, destination, date, seat_number):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        UPDATE reservations
        SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
        WHERE id=?
    """, (name, flight_number, departure, destination, date, seat_number, res_id))
    conn.commit()
    conn.close()

def delete_reservation(res_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM reservations WHERE id=?", (res_id,))
    conn.commit()
    conn.close()