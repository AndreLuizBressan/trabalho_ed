from diretorios import Diretorio, DiretorioContinuo
from lista_invertida import ListaInvertida
from paciente import Paciente

def main():
    lista_invertida = ListaInvertida()
    diretorio_sexo = Diretorio()
    diretorio_tipo_sanguineo = Diretorio()
    diretorio_altura = DiretorioContinuo()

    while True:
        print("\nMenu:")
        print("1. Inserir Paciente")
        print("2. Consulta simples")
        print("3. Consulta composta")
        print("4. Remoção de elemento por ID")
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
                    diretorio_altura.adicionar(altura, paciente)
                    print("Paciente adicionado com sucesso!!!")
                except AssertionError as e:
                    print(e)
        
        elif escolha == "2":
            campo = input("Escolha o campo (sexo/tipo_sanguineo/altura): ")
            valor = input("Especifique o valor para busca: ")
            if campo == 'sexo':
                pacientes = diretorio_sexo.buscar(valor)
            elif campo == 'tipo_sanguineo':
                pacientes = diretorio_tipo_sanguineo.buscar(valor)
            elif campo == 'altura':
                min_value, max_value = map(float, valor.split())
                pacientes = diretorio_altura.buscar_por_intervalo(min_value, max_value)
            else:
                print("Coluna inválida.")
                continue
    
            print()
            print(f"resultados para valor {valor} no campo {campo}: ")
            for paciente in pacientes:
                print()
                print(vars(paciente))

        elif escolha == "3":
            print()
            campo1 = input("Escolha o primeiro campo (sexo/tipo_sanguineo/altura): ")
            valor1 = input("Especifique o valor para busca no primeiro campo: ")
            campo2 = input("Escolha o segundo campo (sexo/tipo_sanguineo/altura): ")
            valor2 = input("Especifique o valor para busca no segundo campo: ")
            if campo1 == 'sexo':
                resultados1 = diretorio_sexo.buscar(valor1)
            elif campo1 == 'tipo_sanguineo':
                resultados1 = diretorio_tipo_sanguineo.buscar(valor1)
            elif campo1 == 'altura':
                minimo, maximo = map(float, valor1.split())
                resultados1 = diretorio_altura.buscar_por_intervalo(minimo, maximo)
            else:
                print("Primeira coluna inválida.")
                continue
            if campo2 == 'sexo':
                resultados2 = diretorio_sexo.buscar(valor2)
            elif campo2 == 'tipo_sanguineo':
                resultados2 = diretorio_tipo_sanguineo.buscar(valor2)
            elif campo2 == 'altura':
                minimo, maximo = map(float, valor2.split())
                resultados2 = diretorio_altura.buscar_por_intervalo(minimo, maximo)
            else:
                print("Segunda coluna inválida.")
                continue
            pacientes = resultados1.intersection(resultados2)
            print()
            print(f"resultados para valor {valor1} no campo {campo1} e valor {valor2} no campo {campo2}: ")
            for paciente in pacientes:
                print()
                print(vars(paciente))

        elif escolha == "4":
            try:
                id = int(input("ID do paciente a ser removido: "))
                paciente = lista_invertida.procura_por_id(id)
                if paciente:
                    lista_invertida.deleta_por_id(id)
                    diretorio_sexo.remover(paciente.sexo, paciente)
                    diretorio_tipo_sanguineo.remover(paciente.tipo_sanguineo, paciente)
                    diretorio_altura.remover(paciente.altura, paciente)
                    print()
                    print("Paciente removido com sucesso!")
                else:
                    print()
                    print("Paciente com o ID especificado não encontrado.")
            except ValueError:
                print("Por favor, insira um ID válido.")

        elif escolha == "5":
            try:
                id = int(input("ID do paciente a ser buscado: "))
                paciente = lista_invertida.procura_por_id(id)
                if paciente:
                    print("Paciente encontrado:")
                    print(vars(paciente))
                else:
                    print("Paciente com o ID especificado não encontrado.")
            except ValueError:
                print("Por favor, insira um ID válido.")

        elif escolha == "6":
            lista_invertida.carga_de_dados()
            for registro in lista_invertida.registros.values():
                diretorio_sexo.adicionar(registro.sexo, registro)
                diretorio_tipo_sanguineo.adicionar(registro.tipo_sanguineo, registro)
                diretorio_altura.adicionar(registro.altura, registro)
            print()
            print("carga de dados finalizada com sucesso!!!")


        elif escolha == "7":
            lista_invertida.mostra_todos()

        elif escolha == "8":
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()