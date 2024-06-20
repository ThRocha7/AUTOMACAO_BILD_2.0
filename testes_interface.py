import tkinter as tk
from resources import validadores, credenciais

def pegar_infos():
    email = email_field.get()
    password = password_field.get()
    directory = dir_field.get()
    infos_validadas = validadores.inserir_credencial(email, password, directory)
    if infos_validadas == 'invalid':
        text_error['text'] = 'Email inválido'
    elif infos_validadas == 'nan':
        text_error['text'] = 'Há alguma informação vazia'
    else: print('valido')


window = tk.Tk()

window.title('AUTOMAÇÃO - CDNF')


mensagem_infos = tk.Label(text="Coloque suas informações de Login do ICM e selecione em que pasta estão os PDF's")
mensagem_infos.grid(row=0, column=0, columnspan=2)

text_email = tk.Label(text='Email:')
text_email.grid(row=1, column=0, sticky='W')
email_field = tk.Entry()
email_field.grid(row=2, column=0, columnspan=2, sticky='EW')

text_password = tk.Label(text='Senha:')
text_password.grid(row=4, column=0, sticky='W')
password_field = tk.Entry()
password_field.grid(row=5, column=0, columnspan=2, sticky='EW')

text_dir = tk.Label(text='Diretório:')
text_dir.grid(row=6, column=0, sticky='W')
dir_field = tk.Entry()
dir_field.grid(row=7, column=0, columnspan=2, sticky='EW')

btn_start = tk.Button(text='Iniciar', command=pegar_infos)
btn_start.grid(row=9, column=1)

text_error = tk.Label(text='', fg='red')
text_error.grid(row=8, column=1)



window.mainloop()