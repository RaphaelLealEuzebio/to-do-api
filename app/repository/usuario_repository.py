from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.usuario_models import UsuarioModel

class UsuarioRepository:
    def __init__(self,database: Session):
        self.database = database
        pass
        
    def criar_usuario(self, usuario: UsuarioModel)-> UsuarioModel:
        self.database.add(usuario)
        self.database.commit()
        self.database.refresh(usuario)
        
        return usuario

    def atualizar_usuario(self, usuario_id: int, dicionario: dict) -> UsuarioModel | None:
        usuario = self.database.get(UsuarioModel, usuario_id)

        if usuario is None:
            return None

        for campo, valor in dicionario.items():
            setattr(usuario, campo, valor)
            
        return usuario

    def listar_usuario(self) -> list:
        return list(self.database.scalars(select(UsuarioModel)).all())

    def deletar_usuario(self, usuario_id: int) -> UsuarioModel | None:
        usuario = self.database.get(UsuarioModel, usuario_id)
        if usuario is None:
            return None
        
        self.database.delete(usuario)
        self.database.commit()
        self.database.refresh(usuario)

        return usuario