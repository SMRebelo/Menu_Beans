###############################################################################################
########################################## <<<<< INSTALAR REQUIREMENTS >>>>>> #################

#                                            pip install -r requirements.txt
###############################################################################################
from funcoes_aux import *
from funcoes import *
from flask import Flask
from flask import Flask, render_template, request, jsonify, session, redirect, send_file, url_for
from rich.console import Console
import mysql.connector
from rich.console import Console
from rich.table import Table
import os 


console = Console()

app = Flask(__name__)
app.secret_key = '123'

drinks = [
    {'Porto Tônico': 6.0},
    {'Porto Sangria': 7.0},
    {'Mr Beans': 6.0},
    {'Cuba Libre': 7.0},
    {'Gin Tônico': 7.0},
    {'Moskow Mule': 8.0},
    {'Long Island': 9.0},
    {'Expresso Martini': 8.0},
    {'Beirão Sour': 7.0},
    {'Mr Beans Virgin': 4.0},
    {'Bebida Branca': 5.0},
    
    {'Beer 20cl': 2.0},
    {'Beer 30cl': 3.0},
    {'Beer 50cl': 4.0},
    {'Super Bock': 2.5},
    {'Cidra': 3.0},
    
    {'Vinho Branco': 3.0},
    {'Vinho B. Rev': 5.0},
    {'Vinho Tinto': 3.0},
    {'Vinho T. Rev': 5.0},
    {'Vinho Porto B': 3.0},
    {'Vinho Porto T': 3.0},
    
    {'Água': 1.0},
    {'Água Pedras': 2.0},
    {'Ginger Ale': 2.0},
    {'Coca Cola': 2.0},
    {'Ginger Beer': 3.0},
    {'Café': 1.0},
    {'Limonada': 3.0},
    {'Amendoins': 1.0}
    
]

@app.route('/')
def index():
    return render_template('index.html', drinks=drinks)

@app.route('/order', methods=['POST'])
def order():
    drink_name = request.form.get('drink')
    num_drinks2 = request.form.get('num_drinks')
    meth_pay = request.form.get('method_payment')

    if not drink_name or not num_drinks2 or not meth_pay:
        return redirect(url_for('index'))
    try:
        num_drinks = int(num_drinks2)
    except ValueError:
        return redirect(url_for('index'))
            #app.logger.info('drink_name: %s, num_drinks: %s, method_payment: %s', drink_name, num_drinks, meth_pay) # APAGAR
    for item in drinks: 
        if drink_name in item:
            value = item[drink_name]
            break
    total_price = num_drinks * value

    if meth_pay == 'cash':
        orders_cash = session.get('orders_cash', {})
        if drink_name in orders_cash:
            orders_cash[drink_name] = (orders_cash[drink_name][0] + total_price, meth_pay)
        else:
            orders_cash[drink_name] = (total_price, meth_pay)
        session['orders_cash'] = orders_cash
    else:
        orders_card = session.get('orders_card', {})
        if drink_name in orders_card:
            orders_card[drink_name] = (orders_card[drink_name][0] + total_price, meth_pay)
        else:
            orders_card[drink_name] = (total_price, meth_pay)
        session['orders_card'] = orders_card
    #app.logger.info(session['orders_cash']) # APGAR MAIS TARDE 
    #app.logger.info(session['orders_card']) # APGAR MAIS TARDE 
    return render_template('index.html', drinks=drinks)

@app.route('/menu')
def menu():
    total_cash = 0
    total_card = 0
    orders_cash = session.get('orders_cash', {})
    orders_card = session.get('orders_card', {})
    
    for drink, details in orders_cash.items():
        total_cash += details[0]  
    
    for drink, details in orders_card.items():
        total_card += details[0]  
        
    return render_template('menu.html', orders_cash=orders_cash, orders_card=orders_card, total_cash=total_cash, total_card=total_card)

def view_session(session_keys):
    """
    View contents of the Flask session for specific keys.
    """
    session_data = {}
    for key in session_keys:
        session_data[key] = session.get(key, {})
    return session_data

@app.route('/view_session')
def display_session():
    session_keys = ['orders_cash', 'orders_card']
    session_data = view_session(session_keys)
    formatted_session_data = ""
    for key, data in session_data.items():
        formatted_session_data += f"<h3>{key}</h3>"
        formatted_session_data += "<pre>" + "\n".join([f"{drink}: {details}" for drink, details in data.items()]) + "</pre>"
    return formatted_session_data

@app.route('/clear_session')
def clear_session():
    # Clear the session
    session.clear()
    
    # Redirect the user to the index page
    return redirect(url_for('menu'))



@app.route('/export_orders', methods=['POST'])
def export_orders():
    orders = []
    orders_cash = session.get('orders_cash', {})
    orders_card = session.get('orders_card', {})
    
    for drink, details in orders_cash.items():
        orders.append({'drink_name': drink, 'num_drinks': details[0], 'meth_payment': 'cash'})
    for drink, details in orders_card.items():
        orders.append({'drink_name': drink, 'num_drinks': details[0], 'meth_payment': 'card'})

    if orders:
        file_name = 'orders.txt'
        file_path = os.path.join(app.root_path, file_name)
        try:
            with open(file_path, 'w') as file:
                for order in orders:
                     file.write(f"{order['drink_name']}, {order['num_drinks']}, {order['meth_payment']}\n")
        except FileNotFoundError:
            print("File not found!")
            return render_template('index.html', drinks=drinks)

        return send_file(file_path, as_attachment=True)
    else:
        return 'No orders to export'
    




if __name__ == '__main__':
    app.run(debug=True)
    