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
