import pyautogui as auto
import pyperclip as clip

def validador_planilha(dados):
    for i in dados:
        if str(dados[i]) == 'nan':
            print('A planilha contém campos vazios')
            return False
        else: return True

def looping_tentativa(nome):
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

def conferir_arq(nome):
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
