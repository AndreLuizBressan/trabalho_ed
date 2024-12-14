class Registros:
    def __init__(self):
        self.resgistros = {}

    def inserir(self, registro):
        self.resgistros[registro.id] = registro

    def procura_por_id(self, id):
        return self.resgistros.get(id, None)

    def deleta_por_id(self, id):
        if id in self.resgistros:
            del self.resgistros[id]

    def mostra_todos(self):
        for registro in self.resgistros.values():
            print(vars(registro))
            print()