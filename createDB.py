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
cur.execute("INSERT INTO Products VALUES('Apple', 111, 'Laptop')")
cur.execute("INSERT INTO Products VALUES('Sony', 222, 'Printer')")
cur.execute("INSERT INTO Products VALUES('Microsoft', 333, 'PC')")

cur.execute("INSERT INTO PCs VALUES(333, 16, 8, 20, 150)")
cur.execute("INSERT INTO Laptops VALUES(111, 20, 6, 23, 10, 100)")
cur.execute("INSERT INTO Printers VALUES(222, TRUE, 'laser-jet', 200)")


cur.execute("INSERT INTO Products VALUES('Google',343, 'PC')")
cur.execute("INSERT INTO Products VALUES('Apple',353,'PC')")
cur.execute("INSERT INTO Products VALUES('Samasung',363, 'PC')")
cur.execute("INSERT INTO Products VALUES('Sony',373, 'PC')")
cur.execute("INSERT INTO Products VALUES('Toshiba', 383, 'PC')")
cur.execute("INSERT INTO Products VALUES('Lenovo',393, 'PC')")
cur.execute("INSERT INTO Products VALUES('Acer',433, 'PC')")
cur.execute("INSERT INTO Products VALUES('Apple',443, 'PC')")
cur.execute("INSERT INTO Products VALUES('Microsoft',453, 'PC')")
cur.execute("INSERT INTO Products VALUES('Samsung',463, 'PC')")

cur.execute("INSERT INTO PCs VALUES(343, 16, 8, 20, 150)")
cur.execute("INSERT INTO PCs VALUES(353, 32, 10, 23, 250)")
cur.execute("INSERT INTO PCs VALUES(363, 8, 14, 24, 130)")
cur.execute("INSERT INTO PCs VALUES(373, 64, 12, 12, 155)")
cur.execute("INSERT INTO PCs VALUES(383, 16, 8, 19, 200)")
cur.execute("INSERT INTO PCs VALUES(393, 32, 5, 12, 300)")
cur.execute("INSERT INTO PCs VALUES(433, 64, 12, 50, 400)")
cur.execute("INSERT INTO PCs VALUES(443, 16, 5, 18, 255)")
cur.execute("INSERT INTO PCs VALUES(453, 24, 19, 16, 1000)")
cur.execute("INSERT INTO PCs VALUES(463, 18, 8, 32, 100)")


cur.execute("INSERT INTO Products VALUES('Microsoft', 141,'Laptops')")
cur.execute("INSERT INTO Products VALUES('Toshiba',151, 'Laptops')")
cur.execute("INSERT INTO Products VALUES('Lenovo',161, 'Laptops')")
cur.execute("INSERT INTO Products VALUES('Samsung',171, 'Laptops')")
cur.execute("INSERT INTO Products VALUES('Apple',181, 'Laptops')")
cur.execute("INSERT INTO Products VALUES('Acer',191, 'Laptops')")
cur.execute("INSERT INTO Products VALUES('Microsoft',211, 'Laptops')")
cur.execute("INSERT INTO Products VALUES('Apple', 121,'Laptops')")
cur.execute("INSERT INTO Products VALUES('Google',221, 'Laptops')")
cur.execute("INSERT INTO Products VALUES('Lenovo', 231,'Laptops')")
cur.execute("INSERT INTO Products VALUES('Apple',241, 'Laptops')")
cur.execute("INSERT INTO Products VALUES('Google', 131,'Laptops')")
cur.execute("INSERT INTO Laptops VALUES(121, 22, 12, 44, 12, 200)")
cur.execute("INSERT INTO Laptops VALUES(131, 24, 14, 55, 13, 223)")
cur.execute("INSERT INTO Laptops VALUES(141, 45, 8, 23, 56, 444)")
cur.execute("INSERT INTO Laptops VALUES(151, 44, 10, 13, 12, 222)")
cur.execute("INSERT INTO Laptops VALUES(161, 66, 20, 56, 34, 1233)")
cur.execute("INSERT INTO Laptops VALUES(171, 99, 60, 23, 12, 333)")
cur.execute("INSERT INTO Laptops VALUES(191, 23, 46, 12, 56, 345)")
cur.execute("INSERT INTO Laptops VALUES(211, 12, 12, 67, 77, 123)")
cur.execute("INSERT INTO Laptops VALUES(221, 23, 11, 18, 44, 1234)")
cur.execute("INSERT INTO Laptops VALUES(231, 34, 11, 18, 44, 1234)")
cur.execute("INSERT INTO Laptops VALUES(241, 78, 11, 18, 44, 1234)")


cur.execute("INSERT INTO Printers VALUES(555, FALSE, 'ink-jet', 400)")
cur.execute("INSERT INTO Printers VALUES(666, TRUE, 'laser-jet', 500)")
cur.execute("INSERT INTO Printers VALUES(777, FALSE, 'ink-jet', 600)")
cur.execute("INSERT INTO Printers VALUES(888, TRUE, 'laser-jet', 700)")
cur.execute("INSERT INTO Printers VALUES(999, FALSE, 'ink-jet', 300)")
cur.execute("INSERT INTO Printers VALUES(543, TRUE, 'laser-jet', 233)")
cur.execute("INSERT INTO Printers VALUES(545, FALSE, 'ink-jet', 123)")
cur.execute("INSERT INTO Printers VALUES(546, TRUE, 'laser-jet', 555)")
cur.execute("INSERT INTO Printers VALUES(656, FALSE, 'ink-jet', 777)")
cur.execute("INSERT INTO Printers VALUES(756, TRUE, 'laser-jet', 555)")
cur.execute("INSERT INTO Printers VALUES(856, FALSE, 'ink-jet', 345)")
cur.execute("INSERT INTO Printers VALUES(956, TRUE, 'laser-jet', 567)")
cur.execute("INSERT INTO Printers VALUES(789, FALSE, 'ink-jet', 654)")
cur.execute("INSERT INTO Products VALUES('Apple',555, 'Printer')")
cur.execute("INSERT INTO Products VALUES('Samsung',666, 'Printer')")
cur.execute("INSERT INTO Products VALUES('Samsung',777, 'Printer')")
cur.execute("INSERT INTO Products VALUES('Toshiba',888, 'Printer')")
cur.execute("INSERT INTO Products VALUES('Apple', 999, 'Printer')")
cur.execute("INSERT INTO Products VALUES('Google', 543, 'Printer')")
cur.execute("INSERT INTO Products VALUES('Google',545, 'Printer')")
cur.execute("INSERT INTO Products VALUES('Lenovo', 546, 'Printer')")
cur.execute("INSERT INTO Products VALUES('Lenovo', 656, 'Printer')")
cur.execute("INSERT INTO Products VALUES('Toyota', 756, 'Printer')")
cur.execute("INSERT INTO Products VALUES('Toyota', 856, 'Printer')")
cur.execute("INSERT INTO Products VALUES('Toyota',956, 'Printer')")
cur.execute("INSERT INTO Products VALUES('Apple',789, 'Printer')")



# Save (commit) the changes
conn.commit()