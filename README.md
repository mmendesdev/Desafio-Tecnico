# API de Formulários Dinâmicos

Uma API desenvolvida com FastAPI e SQLAlchemy para gerenciar formulários e perguntas dinâmicas.

## Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido para construção de APIs
- **SQLAlchemy**: ORM para Python
- **PostgreSQL**: Sistema de gerenciamento de banco de dados
- **Pydantic**: Validação de dados usando type hints do Python
- **Uvicorn**: Servidor ASGI para aplicações Python


### Pré-requisitos

•
Python 3.8+

•
PostgreSQL 12+

•
pip (gerenciador de pacotes do Python)

Instalação e Configuração

### 1. Clone o repositório

Bash


git clone <url-do-repositorio>
cd backend


### 2. Crie um ambiente virtual

Bash


python -m venv venv

# No Windows
venc\Scripts\activate

# No Linux/Mac
source venv/bin/activate


### 3. Instale as dependências

Bash


pip install -r requirements.txt


### 4. Configure o banco de dados

##### 1.
Crie um banco de dados PostgreSQL:

SQL


CREATE DATABASE formularios_db;
CREATE USER formularios_user WITH PASSWORD \'sua_senha\';
GRANT ALL PRIVILEGES ON DATABASE formularios_db TO formularios_user;


1.
Copie o arquivo de exemplo de variáveis de ambiente:

Bash


cp .env.example .env


1.
Edite o arquivo .env com suas configurações:

Plain Text


DATABASE_URL=postgresql://formularios_user:sua_senha@localhost:5432/formularios_db


### 5. Execute a aplicação

Bash


uvicorn main:app --reload --host 0.0.0.0 --port 8000


A API estará disponível em: http://localhost:8000


### Executando com Docker

Para facilitar o desenvolvimento e deployment, o projeto inclui configuração Docker.

Pré-requisitos para Docker

•
Docker

•
Docker Compose

Executar com Docker Compose

### 1.
Clone o repositório:

Bash


git clone <url-do-repositorio>
cd backend


### 1.
Execute com Docker Compose:

Bash


docker-compose up --build


### Isso irá:

•
Criar um container PostgreSQL

•
Criar um container para a API

•
Configurar automaticamente a conexão entre eles

•
Expor a API na porta 8000

A API estará disponível em: http://localhost:8000

Comandos Docker úteis

Bash


# Parar os containers
docker-compose down

# Executar em background
docker-compose up -d

# Ver logs
docker-compose logs -f

# Reconstruir containers
docker-compose up --build





....


