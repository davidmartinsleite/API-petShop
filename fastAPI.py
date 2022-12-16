from fastapi import FastAPI
from src.entidades import Tutor, Pet
from src.repositorios.repositorio_tutor import RepositorioTutor
from src.repositorios.reposito_pet import RepositorioPet


app = FastAPI()
# uvicorn fastAPI:app --reload


@app.get('/tutores/seleciona')  # criar um endpoint para verificar todos os objetos criados
def pega_todos_os_tutores():
    return RepositorioTutor().selecionar()


@app.get('/tutores/seleciona/{id}')
def pega_tutor_especifico(id: int):
    return RepositorioTutor().selecionar_especifico(id)


@app.post('/tutores/adcionar')
def adiona_novo_tutor(nome: str, endereco: str, telefone: str):
    tutor = Tutor(nome=nome, endereco=endereco, telefone=telefone)
    tutor_adicionado = RepositorioTutor().adicionar(tutor)
    return tutor_adicionado


@app.delete('/tutores/deletar/{id}')
def deletar_tutor(id: int):
    confirmacao = RepositorioTutor().deletar(id)
    return confirmacao


@app.patch('/tutores/atualizar')
def atualizar_tutor(id: int, nome: str, endereco: str, telefone: str):
    tutor_atualizado = RepositorioTutor().atualizar(id=id, nome=nome, endereco=endereco, telefone=telefone)
    return tutor_atualizado


@app.get('/pets/seleciona')  # criar um endpoint para verificar todos os objetos criados
def pega_todos_os_pets():
    return RepositorioPet().selecionar()


@app.get('/pets/seleciona/{id}')
def pega_pet_especifico(id: int):
    return RepositorioPet().selecionar_especifico(id)


@app.post('/pets/adcionar')
def adiona_novo_pet(nome_pet: str, idade: int, peso: float, tutor_id: int):
    pet = Pet(nome_pet=nome_pet, idade=idade, peso=peso, tutor_id=tutor_id)
    pet_adicionado = RepositorioPet().adicionar(pet)
    return pet_adicionado


@app.delete('/pets/deletar/{id}')
def deletar_pet(id: int):
    confirmacao = RepositorioPet().deletar(id)
    return confirmacao


@app.patch('/pets/atualizar')
def atualizar_pet(id: int, nome_pet: str, idade: int, peso: float, tutor_id: int):
    pet_atualizado = RepositorioPet().atualizar(id=id, nome_pet=nome_pet, idade=idade, peso=peso, tutor_id=tutor_id)
    return pet_atualizado
