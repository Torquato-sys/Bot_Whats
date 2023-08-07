# 1. Importar bibliotecas necessárias
import pywhatkit
import keyboard
import time
from datetime import datetime

# 2. Definir para quais contatos iremos enviar as mensagens
contatos = ['+5511960444066']
# 3. Definir intervalo de envio
while len(contatos) >= 1:
    # enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0], 'Você pode tudo!', datetime.now().hour,datetime.now().minute + 2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
# 4. Testar!
