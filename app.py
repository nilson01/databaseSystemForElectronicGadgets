
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

InsertProduct = "INSERT INTO Products(maker, model, type) VALUES( ?, ?,'PC');"
InsertPCs = "INSERT INTO PCs(model, speed, ram, hd, price) VALUES(?, ?, ?, ?, ?);"
query_Pc = "SELECT P.maker, P.model, P.type, Pc.speed, Pc.ram, Pc.hd, Pc.price from Products P, PCs Pc  where P.maker = (?) and P.model = Pc.model;"
query_L = "SELECT P.maker, P.model, P.type, L.speed, L.ram, L.hd, L.screen, L.price from Products P, Laptops L where   P.maker = (?) and P.model = L.model;"
query_Pn = "SELECT P.maker, P.model, Pn.color, Pn.type, Pn.price from Products P, Printers Pn  where  P.maker = (?) and P.model = Pn.model;"


# Homepage
@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('homepage.html')


# A

def get_results():
    conn = sqlite3.connect('ncps5.db')
    cur = conn.cursor()
    results = []
    query_p = "SELECT Pr.maker, PCs.model, PCs.speed, PCs.price from Products Pr, PCs where Pr.model = PCs.model"
    res = cur.execute(query_p)

    for row in res:
        results.append(row)
        print(row)
    conn.close()
    return results

@app.route('/pcsearch', methods=['GET', 'POST']) # To render PC Search
def pc_search():
    return render_template('pcsearch.html')


@app.route('/pcresults',  methods=['GET', 'POST']) # To render results
def pc_results():
    # if (request.method=='POST'):
    search_price = str(request.form['content'])
    results = get_results()

    for i in range(len(results)):
        x = abs(int(search_price) - results[i][3])
        results[i] = [x] + list(results[i])
    results = sorted(results)

    return render_template('pcresults.html', results=results)



# B

def check_laptop(speed, ram, hd, screen):
    conn = sqlite3.connect('ncps5.db')
    cur = conn.cursor()
    results = []
    query_p = "SELECT P.maker, L.model, L.speed, L.ram, L.hd, L.screen, L.price from Laptops L, Products P where P.model = L.model and L.speed >=speed and L.ram>=ram and L.hd>=hd and L.screen>= screen"
    res = cur.execute(query_p)
    for row in res:
        results.append(row)
    conn.close()
    return results

@app.route('/laptopMinRequirement', methods=['GET', 'POST']) # To render Homepage
def laptop_Requirement():
    return render_template('min_requirement.html')

@app.route('/minRequirementresults',  methods=['GET', 'POST']) # To render results
def min_requirement():
    # if (request.method=='POST'):
    speed = int(request.form['speed'])
    ram = int(request.form['ram'])
    hd = int(request.form['hd'])
    screen = int(request.form['screen'])
    result_laptop = check_laptop(speed, ram, hd, screen)
    return render_template('laptopresults.html', results=result_laptop)


# C

def find_products(manufacturer):
    conn = sqlite3.connect('ncps5.db')
    cur = conn.cursor()
    res = cur.execute(query_Pc, (manufacturer,))
    Pcs= []
    for row in res:
        Pcs.append(row)
    res = cur.execute(query_L, (manufacturer,))
    Laptops = []
    for row in res:
        Laptops.append(row)
    res = cur.execute(query_Pn, (manufacturer,))
    Printers = []
    for row in res:
        Printers.append(row)
    conn.close()
    return Pcs, Laptops, Printers

@app.route('/manufacturer_products', methods=['GET', 'POST']) # To render Homepage
def manufacturer_products():
    return render_template('manufacturer_products.html')

@app.route('/m_productresults',  methods=['GET', 'POST']) # To render results
def manu_prod_res():
    # if (request.method=='POST'):
    manufacturer = str(request.form['manufacturer']).lower()
    Pcs, Laptops, Printers = find_products(manufacturer)

    return render_template('m_productresults.html', manufacturer=manufacturer, Pcs=Pcs, Laptops=Laptops, Printers=Printers)



# D

def findsystem(budget,speed):
    conn = sqlite3.connect('ncps5.db')
    cur = conn.cursor()
    results = []
    query_p = f"SELECT Pn.color, PCs.model, Pn.model from PCs, Printers Pn where PCs.price + Pn.price <={budget} and PCs.speed>={speed}"
    res = cur.execute(query_p)
    for row in res:
        results.append(row)
    conn.close()
    return results

@app.route('/findsystem', methods=['GET', 'POST']) # To render Homepage
def find_system():
    return render_template('findsystem.html')

@app.route('/systemresults',  methods=['GET', 'POST']) # To render results
def system_results():
    # if (request.method=='POST'):
    budget = int(request.form['budget'])
    speed = int(request.form['speed'])
    model_numbers = findsystem(budget, speed)
    model_numbers = sorted(model_numbers, reverse= True)
    print(model_numbers)
    return render_template('systemresults.html', model_numbers= model_numbers)



# E

def check_PC(search_maker, search_model, search_speed, search_ram, search_hd, search_price):
    conn = sqlite3.connect('ncps5.db')
    cur = conn.cursor()
    res = cur.execute(f"SELECT model from Products where Products.model = {search_model}")
    cPC = []
    for row in res:
        cPC.append(row)
    print(cPC, "CPC")

    if len(cPC) != 0:
        conn.close()
        return "<h1>WARNING: The PC information is already in the Database</h1>"
    else:
        cur.execute(InsertProduct, (search_maker, search_model))
        cur.execute(InsertPCs, (search_model, search_speed, search_ram, search_hd, search_price))
        conn.commit()
        query_p = "SELECT * from Products"
        res = cur.execute(query_p)
        for row in res:
            print(row)
        conn.close()
        return "<h1>New PC information added to the database</h1>"

@app.route('/checkpc', methods=['GET', 'POST']) # To render Homepage
def check_pc():
    return render_template('checkpc.html')

@app.route('/checkPcResults',  methods=['GET', 'POST'])
def pc_check_results():
    # if (request.method=='POST'):
    maker = str(request.form['maker']).lower()
    model = int(request.form['model'])
    print(model)
    speed = float(request.form['speed'])
    ram = int(request.form['ram'])
    hd = int(request.form['hd'])
    price = float(request.form['price'])
    result_message = check_PC(maker, model, speed, ram, hd, price)
    return result_message


if __name__ == '__main__':
    app.run(debug=True)



