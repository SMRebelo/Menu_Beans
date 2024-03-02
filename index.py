###############################################################################################
########################################## <<<<< INSTALAR REQUIREMENTS >>>>>> #################

#                                            pip install -r requirements.txt
###############################################################################################
from flask import Flask
from flask import Flask, render_template, request, session, redirect, send_file, url_for
from rich.console import Console
from rich.console import Console
from rich.table import Table
import os 
######################### <<<<<<  FICHEIRO DE FUNÇOES AUXILIARES >>>>>> ###################
import os
from beaupy import confirm, prompt
# Módulo para manipulação de tempo, utilizado para pausar a execução do programa em determinados pontos.
import time
# Submódulo contendo vários estilos de indicadores de progresso (spinners).
from beaupy.spinners import *
from prompt_toolkit import prompt
# Classes para manipulação de datas e horas, utilizadas para lidar com informações temporais.
from datetime import datetime

export FLASK_APP=index.py   
export FLASK_ENV=development


def get_data_atual():
    """
    Retorna a data atual no formato 'YYYY-MM-DD'.

    Returns:
    str: Data atual no formato 'YYYY-MM-DD'.
    """
    data_atual = datetime.now().strftime('%Y-%m-%d')
    return data_atual


def select_date(mensagem):
    """
    Solicita ao usuário que insira uma data no formato 'Ano-Mês-Dia' (YYYY-MM-DD).

    Args:
    mensagem (str): Mensagem a ser exibida ao solicitar a data.

    Returns:
    str: Data selecionada no formato 'YYYY-MM-DD'.
    """
    date_format = "%Y-%m-%d"
    while True:
        selected_date = prompt(f"{mensagem}(Ano-Mês-Dia): ")
        # Verificar se a data está no formato correto
        try:
            selected_date = datetime.strptime(
                selected_date, date_format).strftime(date_format)
        except ValueError:
            print("Formato de data incorreto. Use o formato Ano-Mês-Dia.")
            time.sleep(2)
            continue  # Chama a função novamente em caso de formato incorreto

        return selected_date


def listar_arquivos_txt():
    '''
    Função para listar os arquivos .txt disponíveis na pasta atual e exibi-los na tela.
    '''
    arquivos_disponiveis = os.listdir()
    write_title("Ficheiros Disponíveis")
    for arquivo in arquivos_disponiveis:
        if arquivo.endswith('.txt'):
            print(arquivo)


def clear():
    '''
    Função para limpar ecrâ.
    '''
    os.system('cls')


def wait_clear(mensagem):
    '''
    Função para limpar ecrâ com uma funcionalidade extra: fornece ao User uma condição de saida antes de limpar o ecrã.

    Argumento:
    - mensagem (String): Mensagem que desejamos gerar para o User confirmar.
    '''
    if confirm(f"{mensagem}"):
        os.system('cls')


def thinking(num, mensagem):
    '''
    Função auxilar que permite gerar uma mensagem dinâmica na consola.

    Argumentos: 
    - num (integer): Número de segundos que a mensagem deve aparecer na consola.
    - mensagem (string): Mensagem que será apresentada à consola.
    '''
    clear()
    # 'DOTS' é uma das muitas possibilidades de animações do Beaupy.
    spinner = Spinner(DOTS, f"{mensagem}")
    spinner.start()
    time.sleep(num)
    spinner.stop()
    os.system('cls')  # No fim da animação limpa o ecrã.


def animacao_inicial(mensagem):
    """
    Exibe uma animação de spinner na tela para mostrar uma mensagem de boas-vindas.
    """
    clear()  # Limpa a tela do console.
    # Define a sequência de frames para a animação do spinner.
    spinner_animation = ['▉▉', '▌▐', '  ', '▌▐', '▉▉']

    # Cria um objeto de spinner com a sequência de frames e a mensagem "BEM VINDO".
    spinner = Spinner(spinner_animation, f"{mensagem}")
    # Inicia a animação do spinner.
    spinner.start()
    # Aguarda por 3 segundos para exibir a animação.
    time.sleep(2)
    # Para a animação do spinner.
    spinner.stop()


def write_title(title):
    '''
    Função para escrever um título formatado.
    Recebe como argumento:

    - title: Título a ser exibido.
    '''
    design = ""
    comp = int((30 - len(title))/2)
    for i in range(comp):
        design += "-"

    print(f"{design}{title}{design}")
    print("-"*30)


def is_valid_name(nome):
    '''
    Função para validar nomes.
    Recebe um argumento: 
    - nome: String contendo o nome a ser validado.

    Retorna:    
    - bool: True se o nome for válido, False caso contrário.
    '''
    lista = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
             ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
    if not nome:
        print("O nome não pode estar vazio.")
        return False

    if not nome[0].isalpha():
        print("O primeiro caractere deve ser uma letra!")
        return False

    for i in range(1, len(nome)):
        if nome[i].isspace() and nome[i-1].isspace():
            print("Digite apenas um espaço entre as palavras!")
            return False
    for i in nome:
        if i in lista:
            print("O nome não pode conter caracteres especiais!")
            return False
    return True


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
    