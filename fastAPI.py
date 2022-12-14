from fastapi import FastAPI
from src.entidades import Tutor
from src.repositorios.repositorio_tutor import RepositorioTutor

app = FastAPI()
# uvicorn fastAPI:app --reload


@app.get('/tutores/seleciona')  # criar um endpoint para verificar todos os objetos criados
def pega_todos_os_tutores():
    return RepositorioTutor().selecionar()


@app.get('/tutores/seleciona/{id}')
def pega_tutor_especifico(id: int):
    return RepositorioTutor().selecionar_especifico(id)


@app.post('/tutores/tutor')
def adiona_novo_tutor(nome, endereco, telefone):
    tutor = Tutor(nome=nome, endereco=endereco, telefone=telefone)
    tutor_adicionado = RepositorioTutor().adicionar(tutor)
    return tutor_adicionado
