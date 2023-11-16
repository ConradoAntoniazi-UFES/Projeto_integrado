from ufesRU import *

cardapio_do_dia = retorna_cardapio_ru()
if cardapio_do_dia:
        print("\n\033[0;32mCARDÁPIO DO RU:\033[m\n")
        print(cardapio_do_dia)
else:
    print("\n\033[0;31mNão foi possível encontrar o cardápio desse dia!\nTente mais tarde e certifique-se que o dia informado é válido.\033[m\n")

