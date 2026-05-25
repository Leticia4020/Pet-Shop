from cadastro import Cadastrar_cliente, listar_clientes
from cadastro_pet import cadastrar_pet, listar_pets
from trabalho3 import registrar_servico, relatorios, relatorio_clientes, servicos_realizados

clientes = []
pets = []
opcao = ""

while opcao != "9":
    print("\n===== BEM VINDO AO PET MANIA =====")
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar pet")
    print("3 - Registrar serviço")
    print("4 - Listar clientes")
    print("5 - Listar pets")
    print("6 - Exibir relatório geral")
    print("7 - Buscar pet")
    print("8 - Listar serviços realizados")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        Cadastrar_cliente(clientes)

    elif opcao == "2":
        cadastrar_pet(clientes, pets)

    elif opcao == "3":
        registrar_servico(clientes, pets)

    elif opcao == "4":
        listar_clientes(clientes, pets)

    elif opcao == "5":
        listar_pets(pets)

    elif opcao == "6":
        relatorios(clientes, pets)

    elif opcao == "7":
        nome_pet = input("Digite o nome do pet para buscar: ").strip()
        pet_encontrado = None

        for pet in pets:
            if pet["nome"].lower().strip() == nome_pet.lower().strip():
                pet_encontrado = pet
                break

        if pet_encontrado:
            print("\n=== PET ENCONTRADO ===")
            print(f"Nome: {pet_encontrado['nome']}")
            print(f"Animal: {pet_encontrado['animal']}")
            print(f"Espécie: {pet_encontrado['especie']}")
            print(f"CPF do dono: {pet_encontrado['cpf_dono']}")
            print(f"Total de serviços: {pet_encontrado['total_servicos']}")
        else:
            print("Pet não encontrado.")

    elif opcao == "8":
        print("\n=== SERVIÇOS REALIZADOS ===")

        if not servicos_realizados:
            print("Nenhum serviço realizado ainda.")
        else:
            for s in servicos_realizados:
                print(f"Pet: {s['pet']}")
                print(f"CPF dono: {s['cpf_dono']}")
                print(f"Serviço: {s['servico']}")
                print(f"Valor: R$ {s['valor']:.2f}")
                print("----------------------")

    elif opcao == "9":
        print("Saindo do programa. Até mais!")

    else:
        print("Opção inválida. Tente novamente.")
