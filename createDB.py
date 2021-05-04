import sqlite3
conn = sqlite3.connect('ncps5.db')
cur = conn.cursor()

# Create tables
cur.execute('''DROP TABLE IF EXISTS Products''')
cur.execute('''CREATE TABLE Products(
                maker varchar(20),
                model real,
                type varchar(20),
                PRIMARY KEY(model))''')

cur.execute('''DROP TABLE IF EXISTS PCs''')
cur.execute('''CREATE TABLE PCs(
                    model real,
                    speed integer,
                    ram integer,
                    hd integer,
                    price real,
                    PRIMARY KEY(model))''')


cur.execute('''DROP TABLE IF EXISTS Laptops''')
cur.execute('''CREATE TABLE Laptops(
                model real,
                speed integer,
                ram integer,
                hd integer,
                screen integer,
                price real,
                PRIMARY KEY(model))''')


cur.execute('''DROP TABLE IF EXISTS Printers''')
cur.execute('''CREATE TABLE Printers(
                model real,
                color boolean,
                type varchar(10),
                price real,
                PRIMARY KEY(model))''')

# Insert rows of data

cur.execute("INSERT INTO Products (maker, model, type) VALUES('microsoft', 333, 'PC')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('dell',343, 'PC')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('apple',353,'PC')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('samsung',363, 'PC')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('sony',373, 'PC')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('toshiba', 383, 'PC')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('lenovo',393, 'PC')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('acer',433, 'PC')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('apple',443, 'PC')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('microsoft',453, 'PC')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('samsung',463, 'PC')")
cur.execute("INSERT INTO PCs (model, speed, ram, hd, price) VALUES(333, 16, 8, 20, 150)")
cur.execute("INSERT INTO PCs (model, speed, ram, hd, price) VALUES(343, 16, 8, 20, 150)")
cur.execute("INSERT INTO PCs (model, speed, ram, hd, price) VALUES(353, 32, 10, 23, 250)")
cur.execute("INSERT INTO PCs (model, speed, ram, hd, price) VALUES(363, 8, 14, 24, 130)")
cur.execute("INSERT INTO PCs (model, speed, ram, hd, price) VALUES(373, 64, 12, 12, 155)")
cur.execute("INSERT INTO PCs (model, speed, ram, hd, price) VALUES(383, 16, 8, 19, 200)")
cur.execute("INSERT INTO PCs (model, speed, ram, hd, price) VALUES(393, 32, 5, 12, 300)")
cur.execute("INSERT INTO PCs (model, speed, ram, hd, price) VALUES(433, 64, 12, 50, 400)")
cur.execute("INSERT INTO PCs (model, speed, ram, hd, price) VALUES(443, 16, 5, 18, 255)")
cur.execute("INSERT INTO PCs (model, speed, ram, hd, price) VALUES(453, 24, 19, 16, 1000)")
cur.execute("INSERT INTO PCs (model, speed, ram, hd, price) VALUES(463, 18, 8, 32, 100)")


cur.execute("INSERT INTO Products (maker, model, type) VALUES('apple', 111, 'Laptops')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('microsoft', 141,'Laptops')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('toshiba',151, 'Laptops')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('lenovo',161, 'Laptops')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('samsung',171, 'Laptops')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('apple',181, 'Laptops')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('acer',191, 'Laptops')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('microsoft',211, 'Laptops')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('apple', 121,'Laptops')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('dell',221, 'Laptops')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('lenovo', 231,'Laptops')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('apple',241, 'Laptops')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('dell', 131,'Laptops')")
cur.execute("INSERT INTO Laptops (model, speed, ram, hd, screen, price) VALUES(111, 20, 6, 23, 10, 100)")
cur.execute("INSERT INTO Laptops (model, speed, ram, hd, screen, price) VALUES(121, 22, 12, 44, 12, 200)")
cur.execute("INSERT INTO Laptops (model, speed, ram, hd, screen, price) VALUES(131, 24, 14, 55, 13, 223)")
cur.execute("INSERT INTO Laptops (model, speed, ram, hd, screen, price) VALUES(141, 45, 8, 23, 56, 444)")
cur.execute("INSERT INTO Laptops (model, speed, ram, hd, screen, price) VALUES(151, 44, 10, 13, 12, 222)")
cur.execute("INSERT INTO Laptops (model, speed, ram, hd, screen, price) VALUES(161, 66, 20, 56, 34, 1233)")
cur.execute("INSERT INTO Laptops (model, speed, ram, hd, screen, price) VALUES(171, 99, 60, 23, 12, 333)")
cur.execute("INSERT INTO Laptops (model, speed, ram, hd, screen, price) VALUES(191, 23, 46, 12, 56, 345)")
cur.execute("INSERT INTO Laptops (model, speed, ram, hd, screen, price) VALUES(211, 12, 12, 67, 77, 123)")
cur.execute("INSERT INTO Laptops (model, speed, ram, hd, screen, price) VALUES(221, 23, 11, 18, 44, 1234)")
cur.execute("INSERT INTO Laptops (model, speed, ram, hd, screen, price) VALUES(231, 34, 11, 18, 44, 1234)")
cur.execute("INSERT INTO Laptops (model, speed, ram, hd, screen, price) VALUES(241, 78, 11, 18, 44, 1234)")


cur.execute("INSERT INTO Products (maker, model, type) VALUES('sony', 222, 'Printer')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('apple',555, 'Printer')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('samsung',666, 'Printer')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('samsung',777, 'Printer')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('toshiba',888, 'Printer')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('apple', 999, 'Printer')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('dell', 543, 'Printer')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('dell',545, 'Printer')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('lenovo', 546, 'Printer')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('lenovo', 656, 'Printer')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('toyota', 756, 'Printer')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('toyota', 856, 'Printer')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('toyota',956, 'Printer')")
cur.execute("INSERT INTO Products (maker, model, type) VALUES('apple',789, 'Printer')")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(222, TRUE, 'laser-jet', 200)")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(555, FALSE, 'ink-jet', 400)")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(666, TRUE, 'laser-jet', 500)")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(777, FALSE, 'ink-jet', 600)")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(888, TRUE, 'laser-jet', 700)")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(999, FALSE, 'ink-jet', 300)")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(543, TRUE, 'laser-jet', 233)")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(545, FALSE, 'ink-jet', 123)")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(546, TRUE, 'laser-jet', 555)")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(656, FALSE, 'ink-jet', 777)")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(756, TRUE, 'laser-jet', 555)")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(856, FALSE, 'ink-jet', 345)")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(956, TRUE, 'laser-jet', 567)")
cur.execute("INSERT INTO Printers (model, color, type, price) VALUES(789, FALSE, 'ink-jet', 654)")




# Save (commit) the changes
conn.commit()