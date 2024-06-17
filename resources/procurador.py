from pyautogui import press, hotkey, write
from pyperclip import copy
from .credenciais import infos
from time import sleep

def procurar_pdf(dados, caminho = infos['caminho']):
    press(['tab', 'tab', 'tab', 'tab', 'tab', 'enter'])
    copy(caminho)
    hotkey('ctrl', 'v')
    press(['enter', 'tab'])
    write(dados['nome_abrev'])
    sleep(3)
    press(['tab', 'tab', 'tab', 'down', 'up', 'f2'])
    hotkey('ctrl', 'c')