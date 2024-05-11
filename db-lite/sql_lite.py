import sqlite3

# creating db connection
# creates file if it doesn't already exist
conn = sqlite3.connect("test.db")

helper = conn.cursor()

# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS people (
#         id integer,
#         name VARCHAR(50),
#         city CHAR(2),
#         income DECIMAL(6,2)
#     )
#     """
# )

# helper.execute("INSERT INTO people (id, name, city, income) VALUES (1, 'matt', 'NY', 34.50)")
# helper.execute("INSERT INTO people (id, name, city, income) VALUES (2, 'kevin', 'WA', 100.50)")
# helper.execute("INSERT INTO people (id, name, city, income) VALUES (3, 'sarah', 'GA', 75.10)")

# conn.commit()

helper.execute("SELECT * FROM people")
rows = helper.fetchall()
for row in rows:
    print(row)
