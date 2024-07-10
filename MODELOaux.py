import pandas as pd
import pyautogui
import time
import subprocess
from Newprecess_func import func_mes
from Newprecess_mes import selec_mes



def redutora():
        link = 'https://docs.google.com/spreadsheets/d/1CiRe1cbT6MVjp5j_v2S3-EYvZNLTyFWjKBua9DCx3xc/edit#gid=1410983719'
        subprocess.run(r'C:\Users\Olá\AppData\Local\Programs\Opera\opera.exe')
        
        time.sleep(2)

        pyautogui.write(link)
        time.sleep(1.5)
        pyautogui.press('enter')
        time.sleep(1.5)

def repetição(df, click_nome):
        pyautogui.click(click_nome.x, click_nome.y)
        pyautogui.press('down')

        pyautogui.PAUSE = 0.2
        for lin in df.index:
                nome = df.loc[lin, 'Nome'].upper()
                pyautogui.write(nome)
                pyautogui.press('down')

        pyautogui.scroll(500)
        pyautogui.click(click_nome.x, click_nome.y)
        pyautogui.press('down')
        pyautogui.press('tab')

        for lin in df.index:
                horas = df.loc[lin,'Horas']
                pyautogui.write(horas)
                pyautogui.press('down')

        pyautogui.scroll(500)
        pyautogui.click(click_nome.x, click_nome.y)
        selec_mes(1)
        func_mes(2)

        for lin in df.index:
                motivo = df.loc[lin,'Motivo']
                pyautogui.write(motivo)
                pyautogui.press('down')

        pyautogui.scroll(500)
        time.sleep(1)
