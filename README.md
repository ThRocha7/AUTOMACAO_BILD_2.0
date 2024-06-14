# Automação de Cadastro de Documentos Não Fiscais

Essa é uma automação baseada em Selenium e Pyautogui que, cadastrará documentos não fiscais no site ICM.

## Pastas e Arquivos:

Na pasta **resources**, temos 4 arquivos sendo eles:

* __credenciais.py__: Possui uma lista com algumas informações que serão necessárias para o funcionamento da automação; 
* __notificacoes.py__: Importa a biblioteca **Winotify** e configura algumas notificações;
* __validadores.py__: Possui algumas funções que validaram alguns dados da automação;

## Instalações Necessárias: 

Para que a automação funcione, é necessario instalar as seguintes bibliotecas:

* ` pip install selenium ` 
* ` pip install webdriver-manager ` 
* ` pip install pyautogui ` 
* ` pip install pandas ` 
* ` pip install openpyxl ` 
* ` pip install pyperclip `
* ` pip install winotify `

Depois de instalá-las, importe-as com assim:

```
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from time import sleep
    import pandas as pd
    import pyautogui as auto
    import resources as rs
    import pyperclip as clip 
```
 
