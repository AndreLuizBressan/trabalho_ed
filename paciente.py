from validadores import valida_opcoes, valida_nome, valida_intervalo

class Paciente:

    tipos_sanguineos = ("a+", "a-", "b+", "b-", "ab+", "ab-", "o+", "o-")
    sexos = ("masculino", "feminino", "outro")
    altura_minima = 0.45
    altura_maxima = 2.20
    peso_minimo = 1.0
    peso_maximo = 500.0

    def __init__(self, nome, sexo, tipo_sanguineo, altura, peso, leito):
        self.nome = valida_nome(nome),
        self.sexo = valida_opcoes(variavel=sexo,
                                  opcoes=self.sexos,
                                  categoria="sexo")
        self.tipo_sanguineo = valida_opcoes(variavel=tipo_sanguineo,
                                  opcoes=self.tipos_sanguineos,
                                  categoria="Tipo sanguíneo")
        self.altura = valida_intervalo(variavel=altura,
                                       minimo=self.altura_minima,
                                       maximo=self.altura_maxima,
                                       categoria="Altura")
        self.peso = valida_intervalo(variavel=peso,
                                     minimo=self.peso_minimo,
                                     maximo=self.peso_maximo,
                                     categoria="Peso")
        self.leito = leito
