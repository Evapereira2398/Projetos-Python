# Bibliotecas usadas no código
import requests
import json

# Função para receber as informações da API
def converter(valor, de, para):
    api = requests.get(f"https://economia.awesomeapi.com.br/{de}-{para}/")
    
    if api.status_code == 200:
        response = api.json()
        return float(response[0]['bid']) * valor
    else:
        return None

# Realizando a conversão
print("========================== Conversor de moedas ==============================")
print("Moedas disponíveis para conversão: USD, BRL, EUR, JPY, BTC, ETH, DOGE, ETC.\n")

valor = float(input("Digite o valor que deseja converter: "))
de = input("Valor em (código): ")
para = input("Converter para (código): ")

cotacao = converter(valor, de, para)

if cotacao is not None:
    print(f"{valor} {de} é equivalente a {cotacao} {para}")
else:
    print("Erro: moeda inválida.")