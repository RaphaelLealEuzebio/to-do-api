from app.core.database_core import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Integer, String
from app.schemas.tarefas_schemas import Status_Task

class TarefaModel(Base):
    __tablename__ = 'Tarefa'

    id: Mapped[Integer] = mapped_column(primary_key=True)
    nome: Mapped[String]
    descricao: Mapped[String]
    criado_em: Mapped[String]
    status: Mapped[Status_Task]