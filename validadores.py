from excessoes import OpcaoInvalida, NomeInvalido, ErroDeIntervalo

def valida_opcoes(variavel,opcoes,categoria):
    assert isinstance(variavel, str), f"Erro na categoria \"{categoria}\": Esperado tipo 'str', mas foi recebido '{type(variavel).__name__}'"
    variavel_minuscula = variavel.lower()
    if variavel_minuscula not in opcoes:
        raise OpcaoInvalida(opcao=variavel, opcoes_validas=opcoes, categoria=categoria)
    return variavel_minuscula

def valida_nome(nome):
    assert isinstance(nome, str), f"Erro na categoria \"nome\": Esperado tipo 'str', mas foi recebido '{type(nome).__name__}'"
    tamanho_nome = len(nome)
    if tamanho_nome < 3:
        raise NomeInvalido(tamanho=tamanho_nome,categoria="nome")
    return nome

def valida_intervalo(variavel,minimo,maximo,categoria):
    assert isinstance(variavel, float), f"Erro na categoria \"{categoria}\": Esperado tipo 'float', mas foi recebido '{type(variavel).__name__}'"
    if variavel < minimo or variavel > maximo:
        raise ErroDeIntervalo(variavel=variavel,
                              minimo=minimo,
                              maximo=maximo,
                              categoria=categoria)
    return variavel
    
def valida_id(_id):
    assert isinstance(_id, int), f"Erro na categoria \"id\": Esperado tipo 'int', mas foi recebido '{type(_id).__name__}'"
    return _id

def valida_leito(leito, minimo, maximo):
    assert isinstance(leito,int), f"Erro na categoria \"leito\": Esperado tipo 'int', mas foi recebido '{type(leito).__name__}'"
    if leito < minimo or leito > maximo:
        raise ErroDeIntervalo(variavel=leito,
                              minimo=minimo,
                              maximo=maximo,
                              categoria="Leito")
    return leito