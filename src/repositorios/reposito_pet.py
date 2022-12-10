import copy

from src.entidades import Pet
from src.database.database_utils import create_session


class RepositorioPet:
    def __init__(self) -> None:
        self.session = create_session()

    def selecionar(self):
        data = self.session.query(Pet).all()
        return data

    def selecionar_especifico(self, id):
        data = self.session.query(Pet).filter(Pet.id == id)
        return data

    def adicionar(self, pet: Pet):
        self.session.add(pet)
        self.session.commit()
        return copy.deepcopy(pet)

    def deletar(self, id):
        self.session.query(Pet).filter(Pet.id == id).delete()
        self.session.commit()

    def atualizar(self, id, idade, peso):
        self.session.query(Pet).filter(Pet.id == id).update(
            {"idade": idade, "peso": peso}
        )
        self.session.commit()
        return RepositorioPet().selecionar_especifico(id)


# NOTA: Por enquanto o PET vai usar um valor de idade fixo, realizar uma mudaça posteriormente
