import requests

# Chave da API do OpenWeatherMap (substitua pela sua chave)
API_KEY = "6918387c371072deef7f2841b086f590"

# Função para obter a previsão do tempo
def obter_previsao_tempo(cidade):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temperatura = data["main"]["temp"]
            descricao = data["weather"][0]["description"]
            cidade_nome = data["name"]
            pais = data["sys"]["country"]

            previsao = f"Previsão do tempo em {cidade_nome}, {pais}:\nTemperatura: {temperatura}°C\nDescrição: {descricao}"
            return previsao
        else:
            return "Cidade não encontrada. Verifique o nome da cidade."
    except Exception as e:
        return f"Ocorreu um erro: {e}"

# Função principal do aplicativo
def aplicativo_previsao_tempo():
    cidade = input("Digite o nome da cidade para consultar a previsão do tempo: ")
    previsao = obter_previsao_tempo(cidade)
    print(previsao)

# Iniciar o aplicativo de consulta de previsão do tempo
if __name__ == "__main__":
    aplicativo_previsao_tempo()