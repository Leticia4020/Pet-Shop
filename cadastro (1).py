from funcoes import vali
def Cadastrar_cliente(clientes):
    print("\n==== CADASTRO DE CLIENTE =====")

    nome = input("Digite o nome do cliente: ").strip()
    cpf = input("CPF: ").replace(".", "").replace("-", "").strip()
    while not vali(cpf):
        cpf = input("Erro: CPF deve conter exatamente 11 dígitos numéricos.")
      
    if not vali(cpf):
        print("Erro: CPF deve conter exatamente 11 dígitos numéricos: ")
        return
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("Erro: já existe um cliente cadastrado com esse CPF.")
            return
        
    telefone = input("Digite o telefone do cliente: ").strip()

    email = ""
    while "@" not in email:
        email = input("Digite o email do cliente (deve conter '@'): ").strip()
        if "@" not in email:
            print("Email inválido. Por favor, tente novamente.")

    rua = input("Rua: ").strip()
    numero = input("Número: ").strip()
    bairro = input("Bairro: ").strip()
    cidade = input("Cidade: ").strip()
    estado = input("Estado: ").strip()

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email,
        "endereco": {
            "rua": rua,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado
        }
    }

    clientes.append(cliente)

    print("\n=== CLIENTE CADASTRADO COM SUCESSO ===")
    print(f"Nome: {cliente['nome']}")
    print(f"CPF: {cliente['cpf']}")
    print(f"Telefone: {cliente['telefone']}")
    print(f"Email: {cliente['email']}")


def listar_clientes(clientes, pets):
    print("\n=== LISTA DE CLIENTES ===")

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print("----------------------------")
        print(f"Nome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")
        print("Pets do cliente:")

        encontrou_pet = False

        for pet in pets:
            if pet["cpf_dono"] == cliente["cpf"]:
                print(f" - {pet['nome']} ({pet['animal']})")
                encontrou_pet = True

        if not encontrou_pet:
            print(" Nenhum pet cadastrado")
