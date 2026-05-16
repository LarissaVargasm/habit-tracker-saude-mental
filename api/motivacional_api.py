import requests
from deep_translator import GoogleTranslator


def get_motivational_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")

        if response.status_code == 200:
            data = response.json()

            quote = data[0]['q']
            author = data[0]['a']

            translated_quote = GoogleTranslator(
                 source= 'auto',
                 target='pt'
            ).translate(quote)

            return f'"{translated_quote}" -{author}'
        
        else:
            return "Não foi possível buscar a frase motivacional."
        
    except Exception as error:
        return f"Erro ao acessar a API: {error}"


