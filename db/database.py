import sqlite3

def get_connection():
    return sqlite3.connect("db/bowling_balls.db")

def create_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS bowling_balls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        link TEXT UNIQUE,
        image_url TEXT,
        original_price TEXT,
        discounted_price TEXT,
        coverstock TEXT,
        core TEXT,
        brand TEXT
    )
    """)


def save_product(conn, product):
    conn.execute("""
    INSERT OR REPLACE INTO bowling_balls 
    (title, link, image_url, original_price, discounted_price, coverstock, core, brand)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        product.get("Title"),
        product.get("Link"),
        product.get("Image URL"),
        product.get("Original Price"),
        product.get("Discounted Price"),
        product.get("coverstock"),
        product.get("core"),
        product.get("brand")
    ))