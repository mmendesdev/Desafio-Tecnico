import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class Settings:
    # Define a URL do banco de dados. Tenta ler da variável de ambiente DATABASE_URL.
    # Se não encontrar, usa um valor padrão (útil para desenvolvimento local, mas deve ser configurado).
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/formularios_db")
    PROJECT_NAME: str = "API de Formulários Dinâmicos"
    PROJECT_VERSION: str = "0.0.1"

# Cria uma instância das configurações para ser importada em outros módulos
settings = Settings()
