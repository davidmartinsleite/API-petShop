from src.database.database_utils import create_session
from src.entidades import Tutor


class RepositorioTutor:
    def __init__(self, session=None) -> None:
        self.session = session or create_session()

    def selecionar(self):
        data = self.session.query(Tutor).all()
        return data

    def selecionar_especifico(self, id):
        data = self.session.query(Tutor).filter(Tutor.id == id).one()
        return data

    def adicionar(self, tutor: Tutor):
        self.session.add(tutor)
        self.session.commit()
        # tutor_adicionado = self.selecionar_especifico(tutor.id)
        return tutor

    def deletar(self, id):
        self.session.query(Tutor).filter(Tutor.id == id).delete()
        self.session.commit()

    def atualizar(self, id, nome, endereco, telefone):
        self.session.query(Tutor).filter(Tutor.id == id).update(
            {"nome": nome, "endereco": endereco, "telefone": telefone}
        )
        self.session.commit()
        return self.selecionar_especifico(id)
