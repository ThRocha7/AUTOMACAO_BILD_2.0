# Automação de Cadastro de Documentos Não Fiscais
---

## Visão Geral:

Essa é uma automação baseada em Selenium e Pyautogui que, cadastrará documentos não fiscais no site ICM.

## Pastas e Arquivos:

Segue uma breve explicação do que em cada arquivo:

* Na pasta 

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
    import resources as rs #
    import pyperclip as clip 
```
 
