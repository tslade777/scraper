import sqlite3

def get_connection():
    return sqlite3.connect("db/bowling_balls.db")

def create_table(conn):
    conn.execute("""CREATE TABLE IF NOT EXISTS bowling_balls (...)""")

def save_products(conn, product):
    # insert or update