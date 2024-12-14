import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "FlaskSample.player_management.db")

def insert_test_data():
    """Insert test data into the Player table."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.executemany("""
            INSERT INTO Player (first_name, last_name, position, bat_order, at_bats, hits)
            VALUES (?, ?, ?, ?, ?, ?);
            """, [
                ("John", "Doe", "Pitcher", 1, 10, 5),
                ("Jane", "Smith", "Catcher", 2, 15, 7),
                ("Emily", "Jones", "Batter", 3, 20, 10),
            ])
            conn.commit()
            print("Test data inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting test data: {e}")

if __name__ == "__main__":
    insert_test_data()
