import pymysql
from config import DB_HOST, DB_USER, DB_PASS, DB_NAME

def save_data(quotes):
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

    cursor = db.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS quotes (id INT PRIMARY KEY AUTO_INCREMENT, quote TEXT)")

    for q in quotes:
        cursor.execute("INSERT INTO quotes (quote) VALUES (%s)", (q,))

    db.commit()
    db.close()
