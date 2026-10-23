from pydantic import BaseModel, Field
from pydantic.types import Enum, datetime

class Status_Task(str, Enum):
    concluida = 'Concluida'
    progresso = 'Progresso'
    falha = 'Falha'

class TarefaRequest(BaseModel):
    nome: str = Field(max_length=30)
    descricao: str = Field(max_length=150)
    criado_em: datetime
    status: Status_Task
    
class TarefaResponse(BaseModel):
    nome: str
    status: Status_Task