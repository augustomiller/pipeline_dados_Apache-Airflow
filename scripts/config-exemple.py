import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Obtém os valores das variáveis
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
secret_key = os.getenv("SECRET_KEY")

# Exemplo de uso
print(f"Usuário do banco de dados: {db_user}")
print(f"Senha: {db_password}")  # Evite expor isso em produção!
