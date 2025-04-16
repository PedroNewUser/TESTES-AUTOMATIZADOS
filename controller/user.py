usariosLista = [{"nome":"pedro", "email":"cpf", "senha":"1232141", "CPF":"12292813432"},
               {"nome": "Chico", "email": "teste@teste.com", "senha": "1234567", "CPF":"471987563"}]

def criarUsuario(usariosLista):
        bancoDeDados=[]    
        bancoDeDados.append(usariosLista)
        print(bancoDeDados)
        return True
        
#criarUsuario(usariosLista)

def listarUsuarios():
     return usariosLista    
    
#print(listarUsuarios())

def listarApenasUmUsuario(cpf):
   for usuario in usariosLista:
        try:
            if usuario['CPF'] == cpf:
                return usuario
        except KeyError:
            continue  

#print(listarApenasUmUsuario("471987563"))

def deletar(cpf):
    bancoDeDados=usariosLista 
    for usuario in bancoDeDados:
        try:
            if usuario['CPF'] == cpf:
                bancoDeDados.remove(usuario)
                print(bancoDeDados)
                return True
        except KeyError:
            continue
    return False

print(deletar("471987563"))