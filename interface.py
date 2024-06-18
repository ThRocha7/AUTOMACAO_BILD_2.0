import automacao
from resources import validadores, credenciais

infos_inseridas = validadores.inserir_credencial(credenciais.infos)
if infos_inseridas == False:
    print('Automação finalizada')
else: 
    automacao.main()


if __name__ == '__main__':
    validadores.inserir_credencial(credenciais.infos)
    automacao.main()