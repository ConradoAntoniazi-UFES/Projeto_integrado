# Importar o módulo
import json
from time import sleep
import os

# Verificando se o email ja foi cadastrado
def verify_email(email, users):
    for i in range(len(users)):
        if email == users[i]["email"]:
            return False
    return True

# Recebe um email pelo terminal (entrada padrão)
def get_email(users):
    email = input("Digite o email para cadastro: ")
    while True:
        if verify_email(email, users):
            return email
        #limpando o terminal e imprimindo mensagem caso ja exista o email
        os.system('cls' if os.name == 'nt' else 'clear')
        email = input(f"O email {email} já existe.\nDigite outro email para cadastro: ")

# Recebendo dados de cadastro do usuário pelo terminal
def Get_user (users):
    nome = input("Digite o nome para cadastro: ")
    email = get_email(users)
    
    print("Cadastro feito com sucesso.")
    user = {
        "name": nome,
        "email": email
    }

    return user

#converte o dicionário com os dados do usuário em uma string JSON já identada
def Convert_user_to_JSON (user):
    user_json = json.dumps(user, indent=3)

    return user_json

#adicionar usuário no dataBase.json
def Add_user_data (new_user):
    arq = "data_base.json"
    try:
        # Tenta abrir o arquivo no modo de leitura e escrita
        with open(arq, 'r') as file_json:
            # Tenta carregar o conteúdo do arquivo JSON
            data_base_json = json.load(file_json)

            # Adicionando o novo usuário à lista existente
            data_base_json["users"].append(new_user)

            # Abre o arquivo novamente no modo de escrita
            with open(arq, 'w') as file_json:
                # Escreve de volta ao arquivo JSON
                json.dump(data_base_json, file_json, indent=2)
        
    except FileNotFoundError:
        # Se o arquivo não existe, cria um novo
        with open(arq, 'w') as file_json:
            # Cria um novo dicionário com o novo usuário
            data_base_json = {
                "users": [new_user]
            }

            # Escreve o dicionário no arquivo JSON
            json.dump(data_base_json, file_json, indent=2)