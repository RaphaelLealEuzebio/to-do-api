from pydantic.type_adapter import BaseModel

class UsuarioRequest(BaseModel):
    nome: str
    senha: str
    
class UsuarioResponse(BaseModel):
    nome: str