from ufesRU import *
from send_email import *
from receive_data import *

# abre um arquivo .json, onde tem as informações sobre os usuários cadastrados
with open("data_base.json") as file_json:
    data_base = json.load(file_json) # ususario recebe um dicionário correspondente ao conteúdo do .json

while True:
    #limpando o terminal para estética
    os.system('cls' if os.name == 'nt' else 'clear')
    #lendo o que o usuário deseja fazer
    acao = input("Deseja cadastrar novo usuario? (y/n):\n")
    
    if acao == 'y':
        new_user = Get_user(data_base["users"])
        if new_user:
            Add_user_data(new_user)
            print(f"Usuário cadastrado.")
        else:
            #limpando o terminal para estética
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Não foi possível realizar o cadastro.")
            print("Usuário não salvou a foto do rosto conforme solicitado.")
        sleep(2)
        
    elif acao == 'n':
        break
    
    else:
        print("\n\033[0;31mOpcao invalida\033[m\n")
        sleep(2)

cardapio_do_dia = retorna_cardapio_ru()

if cardapio_do_dia:
    # abre um arquivo .json, onde tem as informações sobre os usuários cadastrados
    with open("data_base.json") as file_json:
        data_base = json.load(file_json) # ususario recebe um dicionário correspondente ao conteúdo do .json

    for c in range(len(data_base["users"])):
        send_email(data_base["users"][c]["name"], data_base["users"][c]["email"],cardapio_do_dia)
    
    print("\n\033[0;32mCARDÁPIO DO RU:\033[m\n")
    print(cardapio_do_dia)
        
else:
    print("\n\033[0;31mNão foi possível encontrar o cardápio desse dia!\nTente mais tarde e certifique-se que o dia informado é válido.\033[m\n")
