from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd
import pyautogui as auto
from credenciais import *
from validadores import validador_planilha, conferir_arq
import pyperclip as clip

auto.PAUSE = .5
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://app-icm-bild-dnpk5acdua-uc.a.run.app/login')

# Fazer login
#Colocando email
try:
    field_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    field_email.send_keys(email)
except:
    driver.quit()

#Colocando senha 
field_senha = driver.find_element(By.ID, 'password')
field_senha.send_keys(senha)

#Apertando botão de login
conectar_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div[2]/div/div[3]/div/section[4]/button')
conectar_btn.click()

#Entrando na tela de cadastro de documentos não fiscais
try:
    outras_entradas = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="sidebar-container"]/nav/ul/li[4]/div'))
    )
    outras_entradas.click()
except:
    driver.quit()

nao_fiscais = driver.find_element(By.XPATH, '//*[@id="ul"]/div[2]')
nao_fiscais.click()

#ler planilha
df = pd.read_excel('ROBO THIAGO.xlsx')

dados = {
'tomador': df.loc[0, 'bu'],
'prestador': df.loc[0,'fornecedor'],
'data': df.loc[0, 'competencia'],
'valor': str(df.loc[0,'valor']),
'num_doc': str(df.loc[0,'num_doc']),
'servico': df.loc[0,'servico'],
'nome_arq': df.loc[0,'nome_arquivo'],
'nome_abrev': str(df.loc[0, 'nome_abrev'])
}

# Tomador
try:
    # Abrindo aba de pesquisa
    field_tomador = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/section[1]/div/div[2]'))
)
    field_tomador.click()
except:
    driver.quit()

try:
    # Seleciona o campo para digitar
    field_cnpj_tomador = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section/div[2]/div[1]/div[2]/div/div[2]'))
)
    field_cnpj_tomador.click()
    auto.write(dados['tomador'])
    sleep(.5)
except:
    print('não encontrei')
    driver.quit()    

# Pesquisa o tomador
btn_pesquisar = driver.find_element(By.XPATH, '/html/body/div[2]/section/div[2]/div[1]/section[1]/button')
btn_pesquisar.click()
sleep(1)

# Seleciona a pesquisa
resultado_pesquisa = driver.find_element(By.XPATH, '/html/body/div[2]/section/div[2]/div[2]/section/table/tbody')
resultado_pesquisa.click()
sleep(1)

#Prestador
try:
    # Abrindo aba de pesquisa
    field_prestador = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/section[2]/div/div[2]'))
)
    field_prestador.click()
except:
    driver.quit()

try:
    # Seleciona o campo para digitar
    field_cnpj_prestador = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section/div[2]/div[1]/div[2]/div/div[2]'))
)
    field_cnpj_prestador.click()
    auto.write(dados['prestador'])
    sleep(.5)
except:
    print('não encontrei')
    driver.quit()    

# Pesquisa o Prestador
btn_pesquisar = driver.find_element(By.XPATH, '/html/body/div[2]/section/div[2]/div[1]/section[1]/button')
btn_pesquisar.click()
sleep(1)

# Seleciona a pesquisa
resultado_pesquisa = driver.find_element(By.XPATH, '/html/body/div[2]/section/div[2]/div[2]/section/table/tbody')
resultado_pesquisa.click()
sleep(1)

# Preenche a data de emissão
field_data_emissao = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/div')
field_data_emissao.click()
auto.write(dados['data'])
field_base_cal = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[6]')
field_base_cal.click()

# Preenche o total
field_total = driver.find_element(By.XPATH, '/html/body/div/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div[8]')
field_total.click()
dados['valor'] = dados['valor'].replace('.', ',')
auto.write(str(dados['valor']))

# Preenche número do documento
field_num_doc = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]')
field_num_doc.click()
auto.write(str(dados['num_doc']))

# Preenche serviço
field_servico = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[4]')
field_servico.click()
auto.write(dados['servico'])

# Preenche base de cal
field_base_cal.click()
auto.write(dados['valor'])

# Abre janela de arquivos
field_pdf = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/section/div/div/div/div/div')
field_pdf.click()
sleep(2)

# Procurando PDF
auto.press(['tab', 'tab', 'tab', 'tab', 'tab', 'enter'])
clip.copy(caminho)
auto.hotkey('ctrl', 'v')
auto.press(['enter', 'tab'])
auto.write(dados['nome_abrev'])
sleep(3)
auto.press(['tab', 'tab', 'tab', 'down', 'up', 'f2'])
auto.hotkey('ctrl', 'c')
nome_arq_validado = conferir_arq(dados['nome_arq'])

btn_cadastrar_doc = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[10]/section/button')
btn_cadastrar_doc.click()
sleep(12)

btn_voltar = driver.find_element(By.XPATH, '//*[@id="rollback"]')
btn_voltar.click()


sleep(5)