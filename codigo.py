import pyautogui

    #https:/dlp.hashtagtreinamentos.com/python/intenivao/login

import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

pyautogui.sleep(3)
pyautogui.click(x=582, y=495)

pyautogui.write("meirianbarbosa.s@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

import pandas as pd

tabela = pd.read_csv("produtos.csv")
  
print(tabela)

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])

    pyautogui.click(x=577, y=349)

    pyautogui.write(codigo)

    pyautogui.press("tab")
   
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    pyautogui.press("tab")
  
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    pyautogui.press("tab")
 
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    
    pyautogui.press("tab")
    
    obs = (str(tabela.loc[linha, "obs"]))
    if obs != "nan":
         pyautogui.write(str(tabela.loc[linha, "obs"]))
        
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)
