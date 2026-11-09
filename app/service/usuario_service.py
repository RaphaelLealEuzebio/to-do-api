from app.repository.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, usuario_repository: UsuarioRepository):
        self.usuario_repository = usuario_repository

    def login(self, payload):
        nome_usuario = payload['username']
        senha = payload['password']

        usuario = self.usuario_repository.procurar_usuario_por_nome(nome_usuario)

        if usuario is None:
            raise ValueError ("Usuario informado nao existe")

        