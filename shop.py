import os
from tabulate import tabulate

def shop():
    os.system('cls')
    shop_1 = [["Páncélokhoz", "Kardokhoz", "Potikhoz"],
             ["1", "2", "3"]]
    print(tabulate(shop_1, headers='firstrow', tablefmt='grid'))
    console = input("Console >")
    while True:
        if console == "1":
            os.system('cls')
            shop_armor = [["Páncélok", "Árak", "Vásárlási cimke"],
                      ["Sárkánybőr Páncélzat", "50 Lumin", "1"],
                      ["Holdfény Vért", "100 Lumin", "2"],
                      ["Szellemharcos Lemez", "150 Lumin", "3"],
                      ["Viharkovácsolt Páncél", "200 Lumin", "4"],
                      ["Fagyisten Páncél", "250 Lumin", "5"],
                      ["Égkék Lemezvért", "300 Lumin", "6"],
                      ["Kőóriás Páncélzat", "350 Lumin", "7"],
                      ["Fényláng Páncélzat", "400 Lumin", "8"],
                          ]
            print(tabulate(shop_armor, headers='firstrow', tablefmt='grid'))
            console = input("Console >")
            if console == "exit":
                os.system('cls')
                exit()
            if console == "break":
                os.system('cls')
                break

        if console == "2":
            os.system('cls')
            shop_weapon = [["Kardok", "Árak", "Vásárlási cimke"],
                      ["Lángoló Végzet", "50 Lumin", "1"],
                      ["Éjfél Pengéje", "100 Lumin", "2"],
                      ["Sárkányölő Szablya", "150 Lumin", "3"],
                      ["Hajnalfény Kardja", "200 Lumin", "4"],
                      ["Fényhozó Penge", "250 Lumin", "5"],
                      ["Erdeifény Penge", "300 Lumin", "6"],
                      ["Végső Ítélet", "350 Lumin", "7"],
                      ["Holdfény Kasza", "400 Lumin", "8"],
                          ]
            print(tabulate(shop_weapon, headers='firstrow', tablefmt='grid'))
            console = input("Console >")
            if console == "exit":
                os.system('cls')
                exit()
            if console == "break":
                os.system('cls')
                break

        if console == "3":
            os.system('cls')
            shop_potions = [["Poti", "Árak", "Vásárlási cimke"],
                      ["Heal Potion", "50 Lumin", "1"],
                          ]
            print(tabulate(shop_potions, headers='firstrow', tablefmt='grid'))
            console = input("Console >")
            if console == "exit":
                os.system('cls')
                exit()
            if console == "break":
                os.system('cls')
                break
