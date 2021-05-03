import sqlite3
conn = sqlite3.connect('ncps5.db')
cur = conn.cursor()

query_1 = "INSERT INTO Products VALUES('Microsoft', 343633, 'PC')"
query_2 = "INSERT INTO PCs VALUES(343633, 16, 8, 20, 150)"

# cur.execute(f"INSERT INTO Products(maker, model, type) VALUES({search_maker},{search_model},'PC')")
cur.execute(query_1)
# cur.execute(f"INSERT INTO PCs(model, speed, ram, hd, price) VALUES({search_model}, {search_speed}, {search_ram}, {search_hd}, {search_price})")
cur.execute(query_2)
conn.close()