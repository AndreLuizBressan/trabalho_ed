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
    
class DiretorioContinuo(Diretorio):
    def buscar_por_intervalo(self, minimo, maximo):
        resultados = set()
        for chave in self.indice:
            if minimo <= chave <= maximo:
                resultados = resultados.union(self.indice[chave])
        return resultados
