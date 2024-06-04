import pandas as pd
from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
import pyautogui
import time
import subprocess
from Newprecess_func import func_mes
from Newprecess_mes import selec_mes
from Newprocess_redutor import reduzir
import cv2
from MODELOaux import redutora
from MODELOaux import repetição



ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


class ap(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.apparence()


    def layout_config(self):
        self.title('Automação CEM')
        self.geometry('250x250')
        self.maxsize(width=500,height=500)
        self.minsize(width=250, height=250)        
        
        #self.resizable(width=False, height=False)



    def apparence(self):

        pyautogui.PAUSE = 1.5


        # PROECESSO MELHORADO!!!
        def INICIAR():
        
            redutora()

            typesemestre = pyautogui.confirm(text='ESCOLHA O SEMESTRE', title='CEM AUTOMATION', buttons=['1º SEMESTRE','2º SEMESTRE'])

            if typesemestre == '1º SEMESTRE':
                time.sleep(1)

                confirmar = 'SIM'
                while(confirmar == 'SIM'):
                    typemes = pyautogui.confirm(text='ESCOLHA O MÊS', title='CEM AUTOMATION', buttons=['JAN','FEV','MARÇO','ABRIL','MAIO','JUN'])

                    if typemes == 'JAN':

                        pyautogui.hotkey('alt','tab')
                        click_mes = pyautogui.locateCenterOnScreen('OUTUBRO.png', confidence=0.7)
                        pyautogui.click(click_mes.x, click_mes.y)

                        filepath = filedialog.askopenfilename(filetypes=[("CSV files",'*.csv')]) 


                        if filepath:
                                df = pd.read_csv(filepath, header=None).drop(0).drop(columns=0)
                                df.columns = ['Nome','Horas','Motivo']


                                semana = pyautogui.confirm(text='ESCOLHA A SEMANA', title='SEMANA', buttons=['S1', 'S2', 'S3','S4'])
                                time.sleep(1.5)
                                pyautogui.hotkey('alt','tab')


                                if semana == 'S1':
                                    click_nome = pyautogui.locateCenterOnScreen('quatro.png', confidence=0.7)
                                    repetição(df, click_nome)



                                if semana == 'S2':
                                    click_nome = pyautogui.locateCenterOnScreen('ABRIL_S2.png', confidence=0.7)
                                    repetição(df, click_nome)



                                if semana == 'S3':
                                    click_nome = pyautogui.locateCenterOnScreen('ABRIL_S3.png', confidence=0.7)
                                    repetição(df, click_nome)





                    if typemes == 'FEV':

                        pyautogui.hotkey('alt','tab')
                        click_mes = pyautogui.locateCenterOnScreen('FEVEREIRO.png', confidence=0.7)
                        pyautogui.click(click_mes.x, click_mes.y)

                        filepath = filedialog.askopenfilename(filetypes=[("CSV files",'*.csv')]) 


                        if filepath:
                                df = pd.read_csv(filepath, header=None).drop(0).drop(columns=0)
                                df.columns = ['Nome','Horas','Motivo']


                                semana = pyautogui.confirm(text='ESCOLHA A SEMANA', title='SEMANA', buttons=['S1', 'S2', 'S3','S4'])
                                time.sleep(1.5)
                                pyautogui.hotkey('alt','tab')
                                

                                if semana == 'S1':
                                    click_nome = pyautogui.locateCenterOnScreen('quatro.png', confidence=0.7)
                                    repetição(df, click_nome)



                                if semana == 'S2':
                                    click_nome = pyautogui.locateCenterOnScreen('ABRIL_S2.png', confidence=0.7)
                                    repetição(df, click_nome)



                                if semana == 'S3':
                                    click_nome = pyautogui.locateCenterOnScreen('ABRIL_S3.png', confidence=0.7)
                                    repetição(df, click_nome)



                    if typemes == 'MARÇO':

                        pyautogui.hotkey('alt','tab')
                        click_mes = pyautogui.locateCenterOnScreen('MARC.png', confidence=0.7)
                        pyautogui.click(click_mes.x, click_mes.y)

                        filepath = filedialog.askopenfilename(filetypes=[("CSV files",'*.csv')]) 


                        if filepath:
                                df = pd.read_csv(filepath, header=None).drop(0).drop(columns=0)
                                df.columns = ['Nome','Horas','Motivo']


                                semana = pyautogui.confirm(text='ESCOLHA A SEMANA', title='SEMANA', buttons=['S1', 'S2', 'S3','S4'])
                                time.sleep(1.5)
                                pyautogui.hotkey('alt','tab')
                                

                                if semana == 'S1':
                                    click_nome = pyautogui.locateCenterOnScreen('quatro.png', confidence=0.7)
                                    repetição(df, click_nome)



                                if semana == 'S2':
                                    click_nome = pyautogui.locateCenterOnScreen('ABRIL_S2.png', confidence=0.7)
                                    repetição(df, click_nome)



                                if semana == 'S3':
                                    click_nome = pyautogui.locateCenterOnScreen('ABRIL_S3.png', confidence=0.7)
                                    repetição(df, click_nome)





                    if typemes == 'ABRIL':

                        pyautogui.hotkey('alt','tab')
                        click_mes = pyautogui.locateCenterOnScreen('ABRIL.png', confidence=0.7)
                        pyautogui.click(click_mes.x, click_mes.y)

                        filepath = filedialog.askopenfilename(filetypes=[("CSV files",'*.csv')]) 


                        if filepath:
                                df = pd.read_csv(filepath, header=None).drop(0).drop(columns=0)
                                df.columns = ['Nome','Horas','Motivo']


                                semana = pyautogui.confirm(text='ESCOLHA A SEMANA', title='SEMANA', buttons=['S1', 'S2', 'S3','S4'])
                                time.sleep(1.5)
                                pyautogui.hotkey('alt','tab')
                                

                                if semana == 'S1':
                                    click_nome = pyautogui.locateCenterOnScreen('quatro.png', confidence=0.7)
                                    repetição(df, click_nome)



                                if semana == 'S2':
                                    click_nome = pyautogui.locateCenterOnScreen('ABRIL_S2.png', confidence=0.7)
                                    repetição(df, click_nome)



                                if semana == 'S3':
                                    click_nome = pyautogui.locateCenterOnScreen('ABRIL_S3.png', confidence=0.7)
                                    repetição(df, click_nome)



                    if typemes == 'MAIO':

                        pyautogui.hotkey('alt','tab')
                        click_mes = pyautogui.locateCenterOnScreen('MAIO.png', confidence=0.7)
                        pyautogui.click(click_mes.x, click_mes.y)

                        filepath = filedialog.askopenfilename(filetypes=[("CSV files",'*.csv')]) 


                        if filepath:
                                df = pd.read_csv(filepath, header=None).drop(0).drop(columns=0)
                                df.columns = ['Nome','Horas','Motivo']


                                semana = pyautogui.confirm(text='ESCOLHA A SEMANA', title='SEMANA', buttons=['S1', 'S2', 'S3','S4'])
                                time.sleep(1.5)
                                pyautogui.hotkey('alt','tab')
                                

                                if semana == 'S1':
                                    click_nome = pyautogui.locateCenterOnScreen('quatro.png', confidence=0.7)
                                    repetição(df, click_nome)



                                if semana == 'S2':
                                    click_nome = pyautogui.locateCenterOnScreen('ABRIL_S2.png', confidence=0.7)
                                    repetição(df, click_nome)



                                if semana == 'S3':
                                    click_nome = pyautogui.locateCenterOnScreen('ABRIL_S3.png', confidence=0.7)
                                    repetição(df, click_nome)



                    if typemes == 'JUN':

                        pyautogui.hotkey('alt','tab')
                        click_mes = pyautogui.locateCenterOnScreen('JUNHO.png', confidence=0.7)
                        pyautogui.click(click_mes.x, click_mes.y)

                        filepath = filedialog.askopenfilename(filetypes=[("CSV files",'*.csv')]) 


                        if filepath:
                                df = pd.read_csv(filepath, header=None).drop(0).drop(columns=0)
                                df.columns = ['Nome','Horas','Motivo']


                                semana = pyautogui.confirm(text='ESCOLHA A SEMANA', title='SEMANA', buttons=['S1', 'S2', 'S3','S4'])
                                time.sleep(1.5)
                                pyautogui.hotkey('alt','tab')
                                

                                if semana == 'S1':
                                    click_nome = pyautogui.locateCenterOnScreen('quatro.png', confidence=0.7)
                                    repetição(df, click_nome)



                                if semana == 'S2':
                                    click_nome = pyautogui.locateCenterOnScreen('ABRIL_S2.png', confidence=0.7)
                                    repetição(df, click_nome)



                                if semana == 'S3':
                                    click_nome = pyautogui.locateCenterOnScreen('ABRIL_S3.png', confidence=0.7)
                                    repetição(df, click_nome)




                    confirmar = pyautogui.confirm(text='DESEJA CONTINUAR?', title='CONTINUAÇÃO', buttons=['SIM','NÃO'])


                    if confirmar == 'NÃO':
                        pyautogui.alert(text='SAINDO DO PROGRAMA',title='PROGRAMA FINALIZADO')
                        self.destroy()

                                
    


        btn_maio = ctk.CTkButton(self, text='INICIAR',width=80, command=INICIAR, fg_color=('black','green'), text_color='white', 
                                 border_width=2, font=('Helvetica',18), corner_radius=50, hover_color='lightgreen', border_color='black')
        btn_maio.place(relx=0.3, y=150)


        
if __name__=='__main__':
    Acess_Drive_copy2 = ap()
    Acess_Drive_copy2.mainloop()