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
    tutor = Tutor(id=id, nome=nome, endereco=endereco, telefone=telefone)
    tutor_atualizado = RepositorioTutor().atualizar(tutor)
    return tutor_atualizado
