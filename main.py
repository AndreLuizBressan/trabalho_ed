from diretorios import Diretorio
from lista_invertida import ListaInvertida
from paciente import Paciente

def main():
    lista_invertida = ListaInvertida()
    diretorio_sexo = Diretorio()
    diretorio_tipo_sanguineo = Diretorio()

    while True:
        print("\nMenu:")
        print("1. Inserir Paciente")
        print("2. Consulta simples")
        print("3. Consulta composta")
        print("4. Inclusão de novo elemento")
        print("5. Busca de elemento por ID")
        print("6. carga de dados")
        print("7. Exibir todos os dados")
        print("8. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            sucesso = False
            try:
                print()
                _id = int(input("ID: "))
                nome = input("Nome: ")
                sexo = input("Sexo: ")
                tipo_sanguineo = input("Tipo Sanguíneo: ")
                altura = float(input("Altura: "))
                peso = float(input("Peso: "))
                leito = int(input("Leito: "))
                sucesso = True
                print()
            except ValueError as e:
                print(f"Falha de dados: {e}")
            if sucesso:
                try:
                    paciente = Paciente(_id=_id,
                                        nome=nome,
                                        sexo=sexo,
                                        tipo_sanguineo=tipo_sanguineo,
                                        altura=altura,
                                        peso=peso,
                                        leito=leito)
                    lista_invertida.inserir(paciente)
                    diretorio_sexo.adicionar(sexo, paciente)
                    diretorio_tipo_sanguineo.adicionar(tipo_sanguineo, paciente)
                    print("Paciente adicionado com sucesso!!!")
                except AssertionError as e:
                    print(e)
        
        elif escolha == "2":
            campo = input("Escolha o campo (sexo/tipo_sanguineo/altura): ")
            valor = input("Especifique o valor para busca: ")
            if campo == 'sexo':
                results = diretorio_sexo.buscar(valor)
            elif campo == 'tipo_sanguineo':
                results = diretorio_tipo_sanguineo.buscar(valor)
            # elif campo == 'height':
            #     min_value, max_value = map(int, valor.split())
            #     results = height_directory.search_range(min_value, max_value)
            else:
                print("Coluna inválida.")
                continue
    
            print(f"resultados para valor {valor} no campo {campo}: ")
            for patient in results:
                print()
                print(vars(patient))


        elif escolha == "6":
            lista_invertida.carga_de_dados()
            for registro in lista_invertida.registros.values():
                diretorio_sexo.adicionar(registro.sexo, registro)
                diretorio_tipo_sanguineo.adicionar(registro.tipo_sanguineo, registro)
            print()
            print("carga de dados finalizada com sucesso!!!")

if __name__ == "__main__":
    main()