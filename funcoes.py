
    
def vali (cpf):
    cpf = str(cpf).strip()
    return len(cpf) == 11 and cpf.isdigit()