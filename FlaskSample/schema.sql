-- This file defines the schema for the Player table.
-- It is used for manual initialization or as a reference.

CREATE TABLE IF NOT EXISTS Player (
    playerID INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    position TEXT NOT NULL,
    bat_order INTEGER NOT NULL,
    at_bats INTEGER DEFAULT 0,
    hits INTEGER DEFAULT 0
);
