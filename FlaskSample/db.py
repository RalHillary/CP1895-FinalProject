import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "FlaskSample.player_management.db")

def create_database():
    """Create the Player table if it does not exist."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Player (
                playerID INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                position TEXT NOT NULL,
                bat_order INTEGER NOT NULL,
                at_bats INTEGER DEFAULT 0,
                hits INTEGER DEFAULT 0
            );
            """)
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def read_all_players():
    """Retrieve all player data."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Player;")
            players = cursor.fetchall()
        return players
    except sqlite3.Error as e:
        print(f"Error reading players: {e}")
        return []

def add_player(player_data):
    """
    Add a new player.
    player_data: Tuple containing (first_name, last_name, position, bat_order, at_bats, hits)
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO Player (first_name, last_name, position, bat_order, at_bats, hits)
            VALUES (?, ?, ?, ?, ?, ?);
            """, player_data)
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding player: {e}")

def delete_player(player_id):
    """Remove a player by ID."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Player WHERE playerID = ?;", (player_id,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting player: {e}")

def update_player(player_id, updated_data):
    """
    Update details for a player.
    updated_data: Dictionary with keys matching column names.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            updates = ", ".join([f"{key} = ?" for key in updated_data.keys()])
            values = list(updated_data.values()) + [player_id]
            cursor.execute(f"UPDATE Player SET {updates} WHERE playerID = ?;", values)
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating player: {e}")
