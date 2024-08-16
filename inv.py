import os
from tabulate import tabulate
from fighting import player

def clear_screen():
    os.system('cls')

def inventory():
    clear_screen()
    inv = [["Életerőd", "Sebzésed", "1-es képesség felhasználhazóság", "2-es képesség felhasználhazóság", "Potijaid száma", "Pénzed"],
                   [player.hp, f"{player.damage_start} - {player.damage_end}", player.kepesseg_1, player.kepesseg_2, player.poti, f"{player.money} Lumin"]]
    print(tabulate(inv, headers='firstrow', tablefmt='grid'))
    console = input("Console >")
    while True:
        if console == "exit":
            clear_screen()
            exit()
        if console == "back":
            clear_screen()
            break