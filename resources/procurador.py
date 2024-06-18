from pyautogui import press, hotkey, write, PAUSE
from pyperclip import copy
from .credenciais import infos
from time import sleep

PAUSE = .5

def procurar_pdf(dados, caminho):
    press(['tab', 'tab', 'tab', 'tab', 'tab', 'enter'])
    copy(caminho)
    hotkey('ctrl', 'v')
    sleep(1)
    press(['enter', 'tab'])
    write(dados['nome_abrev'])
    sleep(3)
    press(['tab', 'tab', 'tab', 'down', 'up', 'f2'])
    hotkey('ctrl', 'c')

