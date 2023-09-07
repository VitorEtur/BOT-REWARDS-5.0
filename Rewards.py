import threading
import time
import pyautogui
import os
import keyboard
import random

py = pyautogui
numero_aleatorio = random.randint(1, 99999999)

def confirm():
    resposta = py.confirm(text='Start Bot --- Version 5?', buttons=['Yes', 'No'])
    if resposta == 'Yes':
        return True
    else:
        return False

if confirm():

    time.sleep(0.3)
    py.hotkey('winleft','r')
    time.sleep(0.3)
    py.write('msedge')
    time.sleep(0.3)
    py.press('enter')
    time.sleep(2)
    py.press('f4')
    time.sleep(1)
    py.typewrite('https://rewards.bing.com/redeem/pointsbreakdown')
    time.sleep(0.5)
    py.press('enter')
    py.hotkey('ctrl','t')
    pyautogui.typewrite(str(numero_aleatorio))
    py.press('enter')


    def x(): ## Função x inicia o looping com 37 repetições
        for _ in range(37): ## Repete o processo 37 vezes
            numero_aleatorio = random.randint(1, 99999999) ## Definindo que numero_aleatorio pode ser de 1 a 9999999
            pyautogui.typewrite(str(numero_aleatorio)) ## Digita um número aleatório
            py.press('enter') ## Confirma com enter
            py.press('f4') ## F4 - atalho para pesquisar no navegador
        ## --- Termina o looping de 37 repetições e inicia o processo de pesquisa mobile ---

        py.press('f12') ## F12 - atalho para abrir o DevTools do navegador (LEMBRETE - tem que estar configurado para não perguntar novamente quando abrir a ferramenta, caso contrário, não funcionará)
        time.sleep(3) ## Tempo seguro para abaixar a janela do DevTools
        py.hotkey('winleft','down') ## Atalho para minimizar a janela do DevTools
        time.sleep(1) ## Tempo seguro para realizar a pesquisa
        py.press('f4') ## F4 - atalho para pesquisar no navegador
        pyautogui.typewrite(str(numero_aleatorio)) ## Digita um número aleatório
        py.press('enter') ## Confirma com enter

        ## --- Começa o processo mobile de repetições ---
        for _ in range(20): ## Repete o processo 20 vezes
            numero_aleatorio = random.randint(1, 99999999) ## Definindo que numero_aleatorio pode ser de 1 a 9999999
            py.press('f4') ## F4 - atalho para pesquisar no navegador
            pyautogui.typewrite(str(numero_aleatorio)) ## Digita um número aleatório
            py.press('enter') ## Confirma com enter
        
        os._exit(0) ## Encerra o bot



    def y(): ## Tranca ao apertar a letra 'q'
        while True:
            if keyboard.is_pressed('q'): 
                os._exit(0) ## Encerra o bot ao apertar a letra 'q'

    threading.Thread(target=y).start() ## Roda duas funções ao mesmo tempo      
    threading.Thread(target=x).start() ## Roda duas funções ao mesmo tempo
