from funcoes import vali
def cadastrar_pet(clientes, pets):
    print("=== CADASTRO DE PETS ===")

    nome = input("Informe o nome do seu pet: ").strip()
    animal = input("Informe o tipo do seu pet (cachorro, gato, etc): ").strip()
    raca = input("Informe a raça ou espécie: ").strip()
    cpf = input("Informe o CPF do dono: ").replace(".", "").replace("-", "").strip()
    
    if not vali(cpf):
        print("Erro: CPF deve conter exatamente 11 dígitos numéricos: ")
        return
    dono_encontrado = False
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            dono_encontrado = True
            break

    if not dono_encontrado:
        print("CPF não cadastrado. Cadastre o cliente primeiro!")
        return

    pet = {
        "nome": nome,
        "animal": animal,
        "especie": raca,
        "cpf_dono": cpf,
        "total_servicos": 0
    }

    pets.append(pet)

    print("\n=== PET CADASTRADO COM SUCESSO ===")
    print(f"Nome: {pet['nome']}")
    print(f"Animal: {pet['animal']}")
    print(f"Raça/Espécie: {pet['especie']}")
    print(f"CPF do dono: {pet['cpf_dono']}")
    print(f"Total de serviços: {pet['total_servicos']}")


def listar_pets(pets):
    print("\n=== LISTA DE PETS ===")

    if len(pets) == 0:
        print("Nenhum pet cadastrado.")
        return

    for pet in pets:
        print("----------------------------")
        print(f"Nome: {pet['nome']}")
        print(f"Animal: {pet['animal']}")
        print(f"Raça/Espécie: {pet['especie']}")
        print(f"CPF do dono: {pet['cpf_dono']}")
        print(f"Total de serviços: {pet['total_servicos']}")
