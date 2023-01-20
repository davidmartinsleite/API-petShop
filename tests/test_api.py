from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_ler_raiz():
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert resposta.json() == {"msg": "API Petshop"}


def test_ver_todos_os_tutores():
    resposta = client.get('/tutores/seleciona')
    conteudo = resposta.json()
    assert resposta.status_code == 200
    assert len(conteudo) == 5


def test_criar_novo_tutor():
    resposta = client.post('/tutores/adcionar', json={"endereco": "endereco", "nome": "nome", "telefone": "88 9 9933-1122"})
    assert resposta.status_code == 200
