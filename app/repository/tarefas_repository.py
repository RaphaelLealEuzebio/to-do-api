from sqlalchemy import select

from app.models.tarefas_models import TarefaModel
from sqlalchemy.orm import Session


class TarefaRepository:
    def __init__(self, database: Session):
        self.database = database

    def criar_tarefa(self, tarefa: TarefaModel) -> TarefaModel:
        self.database.add(tarefa)
        self.database.commit()
        self.database.refresh(tarefa)
        return tarefa

    def autualizar_tarefa(self, tarefa_id: int, dados:dict) -> TarefaModel | None:
        tarefa = self.database.get(TarefaModel, tarefa_id)
        if tarefa is None:
            return None

        for campo, valor in dados.items():
            setattr(tarefa, campo, valor)

        self.database.commit()
        self.database.refresh(tarefa)
        
        return tarefa

    def listar_todas_tarefas(self) -> list:
        return list(self.database.scalars(select(TarefaModel)).all())

    def deletar_tarefa(self, tarefa_id: int)-> TarefaModel | None:
        tarefa = self.database.get(TarefaModel, tarefa_id)
        if tarefa is None:
            return None

        self.database.delete(tarefa)
        self.database.commit()
        self.database.refresh(tarefa)

        return tarefa