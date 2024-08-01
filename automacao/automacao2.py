from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd
from pyautogui import write
import resources as rs

def main() -> None:

    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.get('https://app-icm-bild-dnpk5acdua-uc.a.run.app/login')

    #Colocando email para realizar o login
    try:
        field_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        field_email.send_keys(rs.infos['email'])
    except:
        driver.quit()

    #Colocando senha 
    field_senha = driver.find_element(By.ID, 'password')
    field_senha.send_keys(rs.infos['password'])

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
    contador = 0

    for linha in df.index:

        dados = {
        'tomador': df.loc[linha, 'bu'],
        'prestador': df.loc[linha,'fornecedor'],
        'data': df.loc[linha, 'competencia'],
        'valor': str(df.loc[linha,'valor']),
        'num_doc': str(df.loc[linha,'num_doc']),
        'servico': df.loc[linha,'servico'],
        'nome_arq': str(df.loc[linha,'nome_arquivo']),
        'nome_abrev': str(df.loc[linha, 'nome_abrev'])
        }
            
        dados_validados= rs.validador_planilha(dados)
        if dados_validados == False:
            break
        
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
            write(dados['tomador'])
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
            write(dados['prestador'])
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
        write(dados['data'])
        field_base_cal = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[6]')
        field_base_cal.click()

        # Preenche o total
        field_total = driver.find_element(By.XPATH, '/html/body/div/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div[8]')
        field_total.click()
        dados['valor'] = dados['valor'].replace('.', ',')
        write(dados['valor'])

        # Preenche número do documento
        field_num_doc = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]')
        field_num_doc.click()
        write(dados['num_doc'])

        # Preenche serviço
        field_servico = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[4]')
        field_servico.click()
        write(dados['servico'])

        # Preenche base de cal
        field_base_cal.click()
        write(dados['valor'])

        # Abre janela de arquivos
        field_pdf = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/section/div/div/div/div/div')
        field_pdf.click()
        sleep(2)

        # Procurando PDF
        rs.procurar_pdf(dados, rs.infos['caminho'])
        nome_arq_validado = rs.conferir_arq(dados['nome_arq'])

        if nome_arq_validado == False:
            print(f'parei na linha {linha + 2}')
            rs.notificacao_erro.show()
            break
        else:  
            sleep(2)  
            btn_cadastrar_doc = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[10]/section/button')
            btn_cadastrar_doc.click()
            sleep(15)

            # Reiniciar processo
            outras_entradas_reiniciar = driver.find_element(By.XPATH, '//*[@id="sidebar-container"]/nav/ul/li[4]/div/div/section/header')
            outras_entradas_reiniciar.click()
            nao_fiscais_reiniciar = driver.find_element(By.XPATH, '//*[@id="ul"]/div[2]/li')
            nao_fiscais_reiniciar.click()

            contador += 1
            print(contador)
            
    rs.notificacao_finalizado.show()

if __name__ == '__main__':
    main()