import os
from tabulate import tabulate
from fighting import player
import time
from fighting import player_damage_end, player_damage_start

def clear_screen():
    os.system('cls')



def shop():
    clear_screen()
    shop_1 = [["Páncélokhoz", "Kardokhoz", "Potikhoz"],
             ["1", "2", "3"]]
    print(tabulate(shop_1, headers='firstrow', tablefmt='grid'))
    console = input("Console >")
    while True:
        if console == "1":
            clear_screen()
            shop_armor = [["Páncélok", "Árak", "Vásárlási cimke", "Pénzed"],
                      ["Sárkánybőr Páncélzat", "50 Lumin", "1", str(player.money) + " Lumin"],
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
                clear_screen()
                exit()
            elif console == "break":
                clear_screen()
                break
            elif console == "1":
                if player.money >= 50:
                    player.money = player.money - 50
                    player.hp += 50
                    print(f"Megvetted a Sárkánybőr Páncélzatot és így az életerőd {player.hp}-ra/re nőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "2":
                if player.money >= 100:
                    player.money = player.money - 100
                    player.hp += 100
                    print(f"Megvetted a Holdény vértet és így az életerőd {player.hp}-ra/re nőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "3":
                if player.money >= 150:
                    player.money = player.money - 150
                    player.hp += 150
                    print(f"Megvetted a Szellemharcos Lemezt és így az életerőd {player.hp}-ra/re nőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "4":
                if player.money >= 200:
                    player.money = player.money - 200
                    player.hp += 200
                    print(f"Megvetted a Viharkovácsolt páncélt és így az életerőd {player.hp}-ra/re nőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "5":
                if player.money >= 250:
                    player.money = player.money - 250
                    player.hp += 250
                    print(f"Megvetted a Fagyisten páncélt és így az életerőd {player.hp}-ra/re nőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "6":
                if player.money >= 300:
                    player.money = player.money - 300
                    player.hp += 300
                    print(f"Megvetted az Égkék Lemezvértet és így az életerőd {player.hp}-ra/re nőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "7":
                if player.money >= 350:
                    player.money = player.money - 350
                    player.hp += 350
                    print(f"Megvetted a Kőóriás Páncélzatát és így az életerőd {player.hp}-ra/re nőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "8":
                if player.money >= 400:
                    player.money = player.money - 400
                    player.hp += 400
                    print(f"Megvetted a Fényláng Páncélzatot és így az életerőd {player.hp}-ra/re nőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            else:
                print("Ez nem választás volt!")
                time.sleep(1.5)
                clear_screen()
                break
        if console == "2":
            clear_screen()
            shop_weapon = [["Kardok", "Árak", "Vásárlási cimke", "Pénzed"],
                      ["Lángoló Végzet", "50 Lumin", "1", str(player.money) + " Lumin"],
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
                clear_screen()
                exit()
            if console == "back":
                clear_screen()
                break
            elif console == "1":
                if player.money >= 50:
                    player.money = player.money - 50
                    player.damage_start += 10
                    player.damage_end += 10
                    print(f"Megvetted a Lángoló Végzetet és így az sebzésed 10-el megnőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "2":
                if player.money >= 100:
                    player.money = player.money - 100
                    player.damage_start += 20
                    player.damage_end += 20
                    print(f"Megvetted az Éjfél Pengéjét és így az sebzésed 20-al megnőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "3":
                if player.money >= 150:
                    player.money = player.money - 150
                    player.damage_start += 30
                    player.damage_end += 30
                    print(f"Megvetted a Sárkányölő Szablyát és így az sebzésed 30-al megnőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "4":
                if player.money >= 200:
                    player.money = player.money - 200
                    player.damage_start += 40
                    player.damage_end += 40
                    print(f"Megvetted a Hajnalfény Kardját és így az sebzésed 40-el megnőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "5":
                if player.money >= 250:
                    player.money = player.money - 250
                    player.damage_start += 50
                    player.damage_end += 50
                    print(f"Megvetted a Fényhozó Pengét és így az sebzésed 50-el megnőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "6":
                if player.money >= 300:
                    player.money = player.money - 300
                    player.damage_start += 60
                    player.damage_end += 60
                    print(f"Megvetted az Erdeifény Pengét és így az sebzésed 60-al megnőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "7":
                if player.money >= 350:
                    player.money = player.money - 350
                    player.damage_start += 70
                    player.damage_end += 70
                    print(f"Megvetted a Végső Ítéletet és így az sebzésed 70-el megnőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            elif console == "8":
                if player.money >= 400:
                    player.money = player.money - 400
                    player.damage_start += 80
                    player.damage_end += 80
                    print(f"Megvetted a Holdfény Kaszát és így az sebzésed 80-al megnőtt!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            else:
                print("Ez nem választás volt!")
                time.sleep(1.5)
                clear_screen()
                break

        if console == "3":
            clear_screen()
            shop_potions = [["Poti", "Árak", "Vásárlási cimke", "Pénzed"],
                      ["Heal Potion", "50 Lumin", "1", str(player.money) + " Lumin"],
                          ]
            print(tabulate(shop_potions, headers='firstrow', tablefmt='grid'))
            console = input("Console >")
            if console == "exit":
                clear_screen()
                exit()
            elif console == "break":
                clear_screen()
                break
            elif console == 1:
                if player.money >= 50:
                    player.money = player.money - 50
                    print(f"Vettél egy Heal Potiont!")
                    time.sleep(4)
                    clear_screen()
                    break
                else:
                    print("Nincs elegendő Luminod ennek a vásárlásnak a lefolytatásához!")
                    time.sleep(4)
                    clear_screen()
                    break
            else:
                print("Ez nem választás volt!")
                time.sleep(1.5)
                clear_screen()
                break
        if console == "exit":
            clear_screen()
            exit()
        else:
            print("Ez nem választás volt!")
            time.sleep(1.5)
            clear_screen()
            break
