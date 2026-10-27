import sqlite3
from pathlib import Path
from flask import current_app, g

ROOT = Path(__file__).parent

SCHEMA = """
CREATE TABLE IF NOT EXISTS bins (
    code TEXT PRIMARY KEY,
    location TEXT NOT NULL,
    category TEXT NOT NULL CHECK (category IN ('wet','dry','recyclable','ewaste'))
);
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bin_code TEXT NOT NULL REFERENCES bins(code),
    status TEXT NOT NULL,
    note TEXT DEFAULT '',
    resolved INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS waste_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bin_code TEXT NOT NULL REFERENCES bins(code),
    weight_kg REAL NOT NULL CHECK (weight_kg >= 0),
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
"""


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(_exc=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db(path, load_sample=False):
    con = sqlite3.connect(path)
    con.executescript(SCHEMA)
    if load_sample:
        con.executescript((ROOT / "data" / "sample_data.sql").read_text(encoding="utf-8"))
    con.commit()
    con.close()
