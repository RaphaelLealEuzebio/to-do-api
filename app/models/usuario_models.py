from app.core.database_core import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy.types import String

class UsuarioModel(Base):
    
    __tablename__ = 'Usuario'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[String]
    senha: Mapped[String]
    