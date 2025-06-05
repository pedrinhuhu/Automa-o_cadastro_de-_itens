import pyautogui
import time
import pandas

#abrir o navegador
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
time.sleep(2)

#acessar o site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#fazer login no site
time.sleep(4)
pyautogui.click(x=589, y=391)
pyautogui.write('baguga@josney.com')
pyautogui.press('tab')
pyautogui.write('senha123')
pyautogui.press('tab')
pyautogui.press('enter')

#importar a tabela de produtos
tabela = pandas.read_csv('produtos.csv')

#preencher formulario
for linha in tabela.index:
    pyautogui.click(x=554, y=271)
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    if not pandas.isna(tabela.loc[linha, 'obs']):
        pyautogui.write(tabela.loc[linha, 'obs'])
    pyautogui.press('tab')
    pyautogui.press('enter')    
    pyautogui.scroll(10000)
    pyautogui.click(x=554, y=271)