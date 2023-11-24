import os
from receive_data import *

def ImprimeOpcoes():
    print("1 - Cadastrar novo usuário.")
    print("2 - Remover usuário.")
    print("3 - Listar usuários cadastrados.")
    print("4 - Sair.")

# abre um arquivo .json, onde tem as informações sobre os usuários cadastrados
with open("data_base.json") as file_json:
    data_base = json.load(file_json) # ususario recebe um dicionário correspondente ao conteúdo do .json

while True:
    #limpando o terminal para estética
    os.system('cls' if os.name == 'nt' else 'clear')
    #lendo o que o usuário deseja fazer
    ImprimeOpcoes()
    acao = input("Digite um número:\n")
    
    if acao == 1:
        new_user = Get_user(data_base["users"])
        if new_user:
            Add_user_data(new_user)
            sleep(2)
        else:
            #limpando o terminal para estética
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\033[0;31mNão foi possível realizar o cadastro\033[m\n")
            sleep(2)

    elif acao == 2:
        email_remove = input("Digite o email do usuário a ser removido:\n")
        Remove_user_data(email_remove)

    elif acao == 3:
        for c in range(data_base["quantity"]):
            nome = data_base["users"][c]["nome"]
            email = data_base["users"][c]["email"]
            print(f"{nome}:{email}")

    elif acao == 4:
        break
    
    else:
        print("\n\033[0;31mOpcao invalida\033[m\n")
        sleep(2)