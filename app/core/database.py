import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# A URL do banco de dados será lida de uma variável de ambiente
# Usamos um valor padrão para desenvolvimento local, mas o ideal é sempre usar variáveis de ambiente
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

# Cria a engine do SQLAlchemy. `echo=True` é útil para debug, mostrando as queries SQL geradas.
engine = create_engine(DATABASE_URL)

# Cria uma SessionLocal class. Cada instância de SessionLocal será uma sessão de banco de dados.
# O `autocommit=False` garante que você precise commitar suas transações explicitamente.
# O `autoflush=False` evita que as operações sejam automaticamente enviadas ao banco de dados.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos do SQLAlchemy. Seus modelos herdarão desta base.
Base = declarative_base()


# Função para obter uma sessão de banco de dados. Usada como dependência no FastAPI.
# Garante que a sessão seja fechada após a requisição.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
