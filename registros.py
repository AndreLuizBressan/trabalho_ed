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
    
    def carga_de_dados(self):
        dados_iniciais = [
            Paciente(id=1, nome="João Silva", sexo="masculino", tipo_sanguineo="o+", altura=1.75, peso=70.5, leito=95),
            Paciente(id=2, nome="Maria Oliveira", sexo="feminino", tipo_sanguineo="a-", altura=1.65, peso=60.0, leito=22),
            Paciente(id=3, nome="Pedro Santos", sexo="outro", tipo_sanguineo="b+", altura=1.80, peso=85.0, leito=33),
            Paciente(id=4, nome="Ana Lima", sexo="feminino", tipo_sanguineo="ab+", altura=1.60, peso=55.0, leito=78),
            Paciente(id=5, nome="Carlos Mendes", sexo="masculino", tipo_sanguineo="a+", altura=1.90, peso=90.0, leito=6),
            Paciente(id=6, nome="Beatriz Silva", sexo="feminino", tipo_sanguineo="o-", altura=1.55, peso=50.0, leito=23),
            Paciente(id=7, nome="Ricardo Souza", sexo="outro", tipo_sanguineo="b-", altura=1.85, peso=95.0, leito=84),
            Paciente(id=8, nome="Fernanda Costa", sexo="feminino", tipo_sanguineo="ab-", altura=1.70, peso=68.0, leito=15),
            Paciente(id=9, nome="Gustavo Rocha", sexo="masculino", tipo_sanguineo="o+", altura=1.78, peso=72.0, leito=96),
            Paciente(id=10, nome="Luciana Alves", sexo="feminino", tipo_sanguineo="a-", altura=1.63, peso=59.0, leito=4),
        ]

        for paciente in dados_iniciais:
            self.inserir(paciente)