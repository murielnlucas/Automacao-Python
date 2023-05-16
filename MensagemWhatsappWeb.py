#importando as 
import pyautogui as auto
import time 
import pyperclip

#Definindo uma constante de tempo 
auto.PAUSE=2

#Acesso ao navegador pela barra de tarefas
auto.click(x=557, y=737)
#Acesso ao site
auto.click(x=266, y=48)
auto.write("https://web.whatsapp.com")
auto.press("Enter")
#Tempo para o carregamento
time.sleep(15)
#Selecionando a conversa que esta fixada (justamente para teste)
auto.click(x=223, y=299)
auto.click(x=678, y=697)
mensagem = "Oi! Esse é o meu primeiro robô"
pyperclip.copy(mensagem)
auto.hotkey("ctrl", "v")
auto.press("Enter")
