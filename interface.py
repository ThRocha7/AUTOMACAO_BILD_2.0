import automacao
from resources import validadores, credenciais

infos_inseridas = validadores.inserir_credencial(credenciais.infos)
if infos_inseridas == False:
    print('Automação finalizada')
else: 
    automacao.call_automacao()
