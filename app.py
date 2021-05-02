
# Installing the dependencies from requirements folder: pip install -r requirements.txt
# if access is denied in the environment use following command: pip install --user -r requirements.txt
# TO GET THE LIST OF ALL THE DEPENDENCIES USED: pip freeze

import sqlite3
from flask import Flask, render_template, request
from flask import g
app = Flask(__name__)


DATABASE = 'ncps5.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('pcsearch.html')

@app.route('/pcresults',  methods=['GET', 'POST']) # To render results
def pc_results():
    # if (request.method=='POST'):
    search_price = str(request.form['content'])
    print(search_price)

    results = []
    query_p = "SELECT Pr.maker, PCs.model, PCs.speed from Products Pr, PCs where Pr.model = PCs.model "
    for row in query_db(query_p):
        results.append(row)
        print(row)

    return render_template('pcresults.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)






"""
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
# Save (commit) the changes
conn.commit()
"""
