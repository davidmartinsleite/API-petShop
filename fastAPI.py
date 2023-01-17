from fastapi import FastAPI
from src.entidades import Tutor, Pet
from src.repositorios.repositorio_tutor import RepositorioTutor
from src.repositorios.repositorio_pet import RepositorioPet

app = FastAPI()


# uvicorn fastAPI:app --reload

class TutoresEndPoint:
    def __init__(self):
        self.repositorio = RepositorioTutor()

    @app.get('/tutores/seleciona')  # criar um endpoint para verificar todos os objetos criados
    def pega_todos_os_tutores(self):
        return self.repositorio.selecionar()

    @app.get('/tutores/seleciona/{id}')
    def pega_tutor_especifico(self, id: int):
        return self.repositorio.selecionar_especifico(id)

    @app.post('/tutores/adcionar')
    def adiona_novo_tutor(self, nome: str, endereco: str, telefone: str):
        tutor = Tutor(nome=nome, endereco=endereco, telefone=telefone)
        tutor_adicionado = self.repositorio.adicionar(tutor)
        return tutor_adicionado

    @app.delete('/tutores/deletar/{id}')
    def deletar_tutor(self, id: int):
        confirmacao = self.repositorio.deletar(id)
        return confirmacao

    @app.patch('/tutores/atualizar')
    def atualizar_tutor(self, id: int, nome: str, endereco: str, telefone: str):
        tutor_atualizado = self.repositorio.atualizar(id=id, nome=nome, endereco=endereco, telefone=telefone)
        return tutor_atualizado


class PetsEndpoint:
    def __init__(self):
        self.repositorio = RepositorioPet()

    @app.get('/pets/seleciona')  # criar um endpoint para verificar todos os objetos criados
    def pega_todos_os_pets(self):
        return self.repositorio.selecionar()

    @app.get('/pets/seleciona/{id}')
    def pega_pet_especifico(self, id: int):
        return self.repositorio.selecionar_especifico(id)

    @app.post('/pets/adcionar')
    def adiona_novo_pet(self, nome_pet: str, idade: int, peso: float, tutor_id: int):
        pet = Pet(nome_pet=nome_pet, idade=idade, peso=peso, tutor_id=tutor_id)
        pet_adicionado = self.repositorio.adicionar(pet)
        return pet_adicionado

    @app.delete('/pets/deletar/{id}')
    def deletar_pet(self, id: int):
        confirmacao = self.repositorio.deletar(id)
        return confirmacao

    @app.patch('/pets/atualizar')
    def atualizar_pet(self, id: int, nome_pet: str, idade: int, peso: float, tutor_id: int):
        pet_atualizado = self.repositorio.atualizar(id=id, nome_pet=nome_pet, idade=idade, peso=peso, tutor_id=tutor_id)
        return pet_atualizado
