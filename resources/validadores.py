import pyautogui as auto
import pyperclip as clip
from .credenciais import infos

def inserir_credencial(email, password, directory):
    emails_validos = ['@bild.com.br', '@vittaresidencial.com.br']
    if email == '' or password == '' or directory == '':
        return 'nan'
    else:
        for final in emails_validos:
            if final in email:
                infos['email'] = email
                infos['password'] = password
                infos['caminho'] = directory
                print(infos)
                return True
        else:
            return 'invalid'



def validador_planilha(dados:dict) -> bool:
    for i in dados:
        if str(dados[i]) == 'nan':
            print('A planilha contém campos vazios')
            return False
        else: return True

def looping_tentativa(nome:str) -> bool:
    parar_while = False
    anterior = ''

    while parar_while != True:
        auto.press(['enter', 'down', 'f2'])
        auto.hotkey('ctrl', 'c')
        copia_while = clip.paste()

        if copia_while == nome:
            auto.press(['enter', 'enter'])
            parar_while = True
            return True
        if anterior == copia_while:
            parar_while = True
            return False
        
        anterior = copia_while

def conferir_arq(nome:str) -> bool:
    copia = clip.paste()

    if copia == nome:
        print('valido')
        auto.press(['enter', 'enter'])
        return True
    else: 
        looping = looping_tentativa(nome)
        if looping == True:
            print('valido')
        else:
            print('Não encontrei')
        return looping
