import copy

from src.database.database_utils import create_session
from src.entidades import Pet


class RepositorioPet:
    def __init__(self, session=None) -> None:
        self.session = session or create_session()

    def selecionar(self):
        data = self.session.query(Pet).all()
        return data

    def selecionar_especifico(self, id):
        data = self.session.query(Pet).filter(Pet.id == id).one()
        return data

    def adicionar(self, pet: Pet):
        self.session.add(pet)
        self.session.commit()
        pet_adicionado = self.selecionar_especifico(pet.id)
        return pet_adicionado
        # copy.deepcopy(pet)

    def deletar(self, id):
        self.session.query(Pet).filter(Pet.id == id).delete()
        self.session.commit()

    def atualizar(self, id, nome_pet, idade, peso, tutor_id):
        self.session.query(Pet).filter(Pet.id == id).update(
            {"nome_pet": nome_pet, "idade": idade, "peso": peso, "tutor_id": tutor_id}
        )
        self.session.commit()
        return RepositorioPet().selecionar_especifico(id)


# NOTA: Por enquanto o PET vai usar um valor de idade fixo, realizar uma mudaça posteriormente
