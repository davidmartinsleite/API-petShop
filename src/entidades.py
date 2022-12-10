from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Agora vamos criar uma classe para representar nossos usuários
Base = declarative_base()


# Cada um destes atributos será uma coluna na tabela gerada
class Tutor(Base):  # modelo de dados
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    endereco = Column(String, nullable=False)
    telefone = Column(String(16), nullable=False)
    pet = relationship("Pet", backref="pets")


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    nome_pet = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=True)
    peso = Column(Integer, nullable=True)
    tutor_id = Column(Integer, ForeignKey("tutores.id"))

    def __repr__(self):
        return f"pet = {self.nome_pet} tutor id = {self.tutor_id}"
