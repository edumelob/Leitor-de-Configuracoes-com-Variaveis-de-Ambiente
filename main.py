from config import Config

def main():
    print("🔧 CARREGANDO CONFIGURAÇÕES 🔧\n")

    try:
        Config.check_required()
        print(f"Nome da aplicação: {Config.APP_NAME}")
        print(f"Versão: {Config.VERSION}")
        print(f"Modo debug: {Config.DEBUG}")
        print(f"Chave de API carregada com sucesso? {'Sim' if Config.API_KEY else 'Não'}")

    except ValueError as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main()
