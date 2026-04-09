import requests
import time
import random

# URL da sua API Flask definida no documento [cite: 165]
URL = 'http://localhost:5000/leituras'

def simular_dados():
    print("Iniciando Simulação de Estação Meteorológica...")
    print("Pressione Ctrl+C para parar.")
    
    while True:
        try:
            # Gerando valores aleatórios realistas 
            temp = round(random.uniform(20.0, 32.0), 2)
            umid = round(random.uniform(40.0, 80.0), 2)
            pres = round(random.uniform(1000.0, 1020.0), 2)
            
            # Montando o JSON que o Arduino enviaria [cite: 78, 93, 94]
            dados = {
                "temperatura": temp,
                "umidade": umid,
                "pressao": pres
            }
            
            # Enviando para a rota POST /leituras [cite: 141, 144]
            response = requests.post(URL, json=dados)
            
            if response.status_code == 201:
                print(f"Dado Simulado Enviado: {dados}")
            else:
                print(f"Erro ao enviar: {response.status_code}")
                
        except Exception as e:
            print(f"Erro na conexão: {e}")
            
        # O documento sugere envio a cada 5 segundos [cite: 78, 96]
        time.sleep(5)

if __name__ == '__main__':
    simular_dados()