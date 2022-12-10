import copy

from sqlalchemy.orm import sessionmaker
from criar_banco_sqlite import Pet, engine

Session = sessionmaker(bind=engine)
session = Session()


class RepositorioPet:

    def selecionar(self):
        data = session.query(Pet).all()
        return data

    def selecionar_especifico(self, id):
        data = session.query(Pet).filter(Pet.id == id)
        return data

    def adicionar(self, pet: Pet):
        session.add(pet)
        session.commit()
        return copy.deepcopy(pet)

    def deletar(self, id):
        session.query(Pet).filter(Pet.id == id).delete()
        session.commit()

    def atualizar(self, id, idade, peso):
        session.query(Pet).filter(Pet.id == id).update({'idade': idade, 'peso': peso})
        session.commit()
        return RepositorioPet().selecionar_especifico(id)


# NOTA: Por enquanto o PET vai usar um valor de idade fixo, realizar uma mudaça posteriormente
