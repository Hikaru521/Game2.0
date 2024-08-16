import os
from tabulate import tabulate
from fighting import player

def clear_screen():
    os.system('cls')

def inventory():
    clear_screen()
    inv = [["Életerőd", "Sebzésed", "Potijaid száma"],
                   [player.hp, f"{player.damage_start} - {player.damage_end}", player.poti,]]
    print(tabulate(inv, headers='firstrow', tablefmt='grid'))
    inv_abilites = [["1-es képesség felhasználhatóság", "2-es képesség felhasználhatóság"],
                   [player.kepesseg_1, player.kepesseg_2,]]
    print(tabulate(inv_abilites, headers='firstrow', tablefmt='grid'))
    inv_money = [["Pénzed"],
                   [f"{player.money} Lumin"]]
    print(tabulate(inv_money, headers='firstrow', tablefmt='grid'))
    console = input("Console >")
    while True:
        if console == "exit":
            clear_screen()
            exit()
        if console == "back":
            clear_screen()
            break