import os
import random
from tabulate import tabulate
import time

def clear_screen():
    os.system('cls')

mobs_list = ["Sárkány",  "Anyád", "Apád", "Anyós", "Kutya", "Zombie", "Medve", "Orbán"]
class Mobs:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg

mobs = {"Sárkány": Mobs(100, random.randrange(25, 50)),
        "Anyád": Mobs(150, random.randrange(25, 50)),
        "Apád": Mobs(200, random.randrange(25, 50)),
        "Anyós": Mobs(1000, random.randrange(25, 50)),
        "Kutya": Mobs(250, random.randrange(25, 50)),
        "Zombie": Mobs(200, random.randrange(25, 50)),
        "Medve": Mobs(250, random.randrange(25, 50)),
        "Orbán": Mobs(230, random.randrange(25, 50))
        }
class Player:
    def __init__(self, hp ,dmg, kepesseg_1, kepesseg_2, money):
        self.hp = hp
        self.dmg = dmg
        self.kepesseg_1 = kepesseg_1
        self.kepesseg_2 = kepesseg_2
        self.money = money
        self.damage_start = player_damage_start
        self.damage_end = player_damage_end

player_damage_start = 200
player_damage_end = 300

player = Player(100, random.randrange(player_damage_start, player_damage_end), 1, 1, 50000000)

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total:
        print()

def fighting():
    os.system('cls')
    if len(mobs_list) == 0:
        print("Megöltél minden ellenfelet!")
        time.sleep(2)
        clear_screen()
        return
    choice = random.choice(mobs_list)
    potions = 1
    back = 1
    while True:
        enemy = [["Ellenfeled", "Életereje", "Életerőd"],
                  [choice, mobs[choice].hp, player.hp]]
        print(tabulate(enemy, headers='firstrow', tablefmt='grid'))
        lehetosegek = [["Sima támadáshoz", "Képesség használatához", "Healeléshez", ],
                       ["0", "1", "+"]]
        print(tabulate(lehetosegek, headers='firstrow', tablefmt='grid'))
        console = input("Console >")
        player_turn = True
        if player_turn:
            if console == "0":
                mobs[choice].hp -= player.dmg
                print(f"Damageltél a mobra {player.dmg}-t!")
                for i in range(8):
                    printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                    time.sleep(0.25)
                player_turn = False
                clear_screen()
                if mobs[choice].hp <= 0:
                    mobs_list.remove(choice)
                    print("A mob meghalt!")
                    time.sleep(2)
                    clear_screen()
                    break
            elif console == "+":
                if potions == 1:
                    player.hp = player.hp + 50
                    print("Kaptál 50 életerőt!")
                    for i in range(8):
                        printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                        time.sleep(0.25)
                elif potions == 0:
                    print("Sajnos elfogyott a potionod!")
                    time.sleep(3)
                player_turn = False
                clear_screen()
            elif console == "1":
                all_data = [["Képességeid", "Leírás", "Felhasználhatóság", "Száma"],
                            ["Ezüstszelídítés", "Erősebb sebzést ad le az ellenfélnek!", player.kepesseg_1, 1],
                            ["Armor", "A Warrior életerejéhez ad hozzá + 40 armort!", player.kepesseg_2, 2]]

                print(tabulate(all_data, headers='firstrow', tablefmt='grid'))

                console = input("Console >")
                if console == "1":
                    if player.kepesseg_1 == 1:
                        damage = random.randrange(player_damage_start + 20, player_damage_end + 20)
                        mobs[choice].hp -= damage
                        print(f"Damageltél a mobra az Ezüstszelidítés képesség használatával {player.dmg}-t!")

                        for i in range(8):
                            printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                            time.sleep(0.25)

                        player.kepesseg_1 -= 1
                        player_turn = False
                        clear_screen()
                    elif player.kepesseg_1 == 0:
                        print("Sajnos ez a képességed elfogyott!")
                        time.sleep(1.5)
                        clear_screen()
                elif console == "2":
                    if player.kepesseg_2 == 1:
                        player.hp += 40
                        print("Az Armor képesség felhasználásával kaptál + 40 armort!")
                        time.sleep(2)
                        player.kepesseg_2 -= 1
                        player_turn = False
                        clear_screen()
                    elif player.kepesseg_2 == 0:
                        print("Sajnos ez a képességed elfogyott!")
                        time.sleep(1.5)
                        clear_screen()
                elif player.kepesseg_2 == 0:
                    print("Sajnos ez a képességed elfogyott!")
                    clear_screen()
                elif console == "exit":
                    clear_screen()
                    exit()
            elif console == "exit":
                clear_screen()
                exit()
            elif console == "back":
                if back == 1:
                    number = random.randrange(1, 10)
                    if number == 1:

                        print("Sikeresen meghátráltál a csatától!")
                        time.sleep(2)
                        clear_screen()
                        break
                    else:
                        print("Nem sikerült elfutnod a szörny elől! A harc folytatódik!")
                        back = back - 1
                        time.sleep(2)
                        clear_screen()
                else:
                    print("Nem tudsz meghátrálni a harcból!")
                    time.sleep(2)
                    clear_screen()
            else:
                print("Ez nem választás volt!")
                time.sleep(1.5)
                clear_screen()

        if player_turn == False:
            player.hp -= mobs[choice].dmg
            print(f"Az ellenség damagelt rád {mobs[choice].dmg}-t")
            for i in range(8):
                printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                time.sleep(0.25)
            clear_screen()
            player_turn = True
            if player.hp <= 0:
                print("Meghaltál! A játéknak vége!")
                time.sleep(2)
                clear_screen()
                exit()




