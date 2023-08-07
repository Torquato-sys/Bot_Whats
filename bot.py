# 1. Importar bibliotecas necessárias
import pywhatkit
import keyboard
import time
from datetime import datetime

# 2. Definir para quais contatos iremos enviar as mensagens
contatos = ['+5511999999999', '+5511999999999'] # aqui estamos com uma lista criada armazenada na variavel contatos, lembre de informar o codigo do pais(+55) e o DDD da sua região;

# 3. Definir intervalo de envio
while len(contatos) >= 1: # enquanto o tamanho da lista que esta na variavel contatos for maior ou igual a 1, execute tal função;
    # enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0], 'Você pode tudo!', datetime.now().hour,datetime.now().minute + 2) # estamos chamando a biblioteca pywhatkit para acessar (whatmsg) acessando a variavel contatos começando  as mensagens a partir do primeiro item [0], definindo hora atual, e 2 minuto para todo o processamento, abrir navegador acessar whats_web e abrir a mensagem;
    del contatos[0] # para evitar mensagens repetidas para os contatos estamos excluind eles conforme for enviando começa a partir do primeiro item[0]
    time.sleep(60) # tempo de 60 segundos de uma conversa para a outra;
    keyboard.press_and_release('ctrl + w') # estamos pedindo para realizar a ação control + w(fecha abas do navegador), assim evitando abrir uma pagina para cada conversa;

# 4. Testar!
# Importante "se você tem 2 telas deixa o mouse na tela que ira abrir o navegador, apos executar o codigo com sua IDE", "evitar esta mechendo no mouse pois a ferramenta trabalha com o sensor do mesmo mechendo podera interromper o funcionamento da ferramenta"