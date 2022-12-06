from sqlalchemy.orm import sessionmaker
from criar_banco_sqlite import Tutor, engine

Session = sessionmaker(bind=engine)
session = Session()


class ComandosTutor:

    def selecionar(self):
        data = session.query(Tutor).all()  # esse "db" tá pegando tudo que tem "self"
        return data

    def selecionar_especifico(self, id):
        data = session.query(Tutor).filter(Tutor.id == id)
        return data

    def adicionar(self, nome, endereco, telefone):
        data_isert = Tutor(nome=nome, endereco=endereco, telefone=telefone)
        session.add(data_isert)
        session.commit()

    def deletar(self, id):
        session.query(Tutor).filter(Tutor.id == id).delete()
        session.commit()

    def atualizar(self, id, endereco, telefone):
        session.query(Tutor).filter(Tutor.id == id).update({'endereco': endereco, 'telefone': telefone})
        session.commit()


# tutor = ComandosTutor().adicionar('thiago', 'rua castelo branco', '(85) 9 9990-5675')
# tutor = ComandosTutor().deletar(3)

tutor = ComandosTutor().selecionar()
print(tutor)



