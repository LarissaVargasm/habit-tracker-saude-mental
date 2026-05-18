from flask import Flask
from api.motivacional_api import get_motivational_quote
import os

app = Flask(__name__)


@app.route("/")
def home():
    quote = get_motivational_quote()

    return f"""
    <h1>🌿 HabitTracker - Saúde Mental</h1>

    <p><strong>Motivação do dia:</strong></p>

    <p>{quote}</p>

    <p>Projeto desenvolvido por Larissa Vargas Moreira.</p>
    """


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)