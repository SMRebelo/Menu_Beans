import mysql.connector
from datetime import date
import sys
from funcoes_aux import *
import beaupy
from rich.console import Console
from rich.table import Table
import json
from mysql.connector import Error
from flask import Flask, render_template, url_for, request, redirect, flash, session
import mysql.connector

console = Console()  # A variável console foi definida como uma instância da classe Console do módulo rich. Esta classe fornece métodos para exibir texto formatado e tabelas de forma colorida no terminal. Ao instanciar a classe Console, você pode usar seus métodos para imprimir mensagens de forma mais elaborada e formatada no terminal.

mysql_config = {  # Para evitar repetição de código, a varivel 'mysql_config', é criada fora de funções e contem as definições para
    # ligar á base de dados.
    'user': 'root',
    'host': 'localhost',
    'database': 'cesae',
    'raise_on_warnings': True, }


def conectar_bd():
    """
    Função para conectar ao banco de dados MySQL.

    Retorna:
    connection: Objeto de conexão se a conexão for bem-sucedida, None caso contrário.
    """
    try:
        conn = mysql.connector.connect(**mysql_config)
        return conn
    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)
        time.sleep(2)
        return None

drinks = [
    {'porto tônico': 6.0},
    {'porto beans': 6.0},
    {'porto sangria': 7.0},
    {'gin tônico': 7.0},
    {'cuba libre': 6.5},
    {'moskow mule': 8.0},
    {'long island': 9.0},
    {'beirão sour': 7.0},
    {'expresso martini': 8.0},
    {'mr beans virgin': 4.0},
    {'vinho branco': 3.0},
    {'vinho branco r': 5.0},
    {'vinho tinto': 3.0},
    {'vinho tinto r': 5.0},
    {'água': 1.0},
    {'água pedras': 2.0},
    {'água tônica': 2.0},
    {'ginger ale': 2.0},
    {'coca cola': 2.0},
    {'ginger beer': 3.0},
    {'café': 1.0},
    {'ice coffe': 2.0},
    {'limonada': 3.0},
    {'beer 20cl': 2.0},
    {'beer 30cl': 3.0},
    {'beer 40cl': 4.0},
    {'super bock': 2.5}
]





