from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Estamos criando uma instância de Engine com o sqlite
engine = create_engine("sqlite:///petshop.db")

# Agora vamos criar uma classe para representar nossos usuários
Base = declarative_base()

# Podemos agora gerar toda a estrutura do banco usando um método
# utilitário da classe Base que criamos.
Base.metadata.create_all(engine)


# Cada um destes atributos será uma coluna na tabela gerada
class User(Base):
    __tablename__ = 'tutores'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    endereco = Column(String, nullable=False)
    telefone = Column(String, nullable=False)


