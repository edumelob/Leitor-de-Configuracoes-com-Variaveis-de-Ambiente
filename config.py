import os
from dotenv import load_dotenv

# Carrega o arquivo .env, se existir
load_dotenv()

class Config:
    """Classe que carrega configurações a partir de variáveis de ambiente."""

    APP_NAME = os.getenv("APP_NAME", "Meu Aplicativo")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    API_KEY = os.getenv("API_KEY")  # sem default, pois é sensível
    VERSION = os.getenv("VERSION", "1.0.0")

    @staticmethod
    def check_required():
        """Verifica se variáveis obrigatórias estão preenchidas."""
        if Config.API_KEY is None:
            raise ValueError("A variável de ambiente API_KEY é obrigatória!")
