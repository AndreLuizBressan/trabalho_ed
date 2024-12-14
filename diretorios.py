class Diretorio:
    def __init__(self):
        self.indice = dict()

    def adicionar(self, chave, id):
        if chave not in self.indice:
            self.indice[chave] = {id}
        else:
            self.indice[chave].add(id)

    def buscar(self, chave):
        return self.indice.get(chave, set())