class OpcaoInvalida(AssertionError):
    """Exceção personalizada para opções inválidas."""
    def __init__(self, opcao, opcoes_validas, categoria):
        self.opcao = opcao
        self.opcoes_validas = opcoes_validas
        message = (f"erro ao validar categoria \"{categoria}\": "
                   f"\"{opcao}\" não é uma opção válida. "
                   f"As opções válidas são: {', '.join(opcoes_validas)}.")
        super().__init__(message)

class NomeInvalido(AssertionError):
    """Exceção personalizada para strings muito curtas."""
    def __init__(self, tamanho, categoria):
        self.tamanho = tamanho
        message = (f"erro ao validar categoria \"{categoria}\": "
                   f"A string fornecida tem apenas {tamanho} caracteres. "
                   f"O tamanho mínimo permitido é 3.")
        super().__init__(message)

class ErroDeIntervalo(AssertionError):
    """
    Exceção personalizada para indicar que um número está fora do intervalo permitido.
    """
    def __init__(self, variavel, minimo, maximo, categoria):
        super().__init__(f"O valor \"{variavel}\" está fora do intervalo de \"{categoria}\" ({minimo} a {maximo}).")
