import os
import random
from tabulate import tabulate
import time

def clear_screen():
    os.system('cls')

mobs_list = ["Sárkány", "Anyád", "Apád", "Anyós", "Kutya", "Zombie", "Medve"]
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
        }

boss_list = ["Ramatra", "Reyna"]
class Boss:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg


boss = {"Ramatra": Boss(1000, random.randrange(250, 500)),
        "Reyna": Boss(1500, random.randrange(250, 500)),
        }

class Player:
    def __init__(self, hp ,dmg, kepesseg_1, kepesseg_2, money, poti):
        self.hp = hp
        self.dmg = dmg
        self.kepesseg_1 = kepesseg_1
        self.kepesseg_2 = kepesseg_2
        self.money = money
        self.damage_start = player_damage_start
        self.damage_end = player_damage_end
        self.poti = poti

player_damage_start = 2000
player_damage_end = 3000

player = Player(100, random.randrange(player_damage_start, player_damage_end), 1, 1, 50000000, 1)

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total:
        print()

def fighting():
    os.system('cls')
    back = 1
    while True:
        if len(mobs_list) > 0:
            choice = random.choice(mobs_list)
            choice_m_or_b = 0
        elif len(mobs_list) == 0:
            choice = random.choice(boss_list)
            choice_m_or_b = 1
        if choice_m_or_b == 0:
            enemy = [["Ellenfeled", "Életereje", "Életerőd"],
                    [choice, mobs[choice].hp, player.hp]]
            print(tabulate(enemy, headers='firstrow', tablefmt='grid'))
        elif choice_m_or_b == 1:
            enemy = [["Ellenfeled", "Életereje", "Életerőd"],
                    [choice, boss[choice].hp, player.hp]]
            print(tabulate(enemy, headers='firstrow', tablefmt='grid'))
        lehetosegek = [["Sima támadáshoz", "Képesség használatához", "Healeléshez", ],
                       ["0", "1", "+"]]
        print(tabulate(lehetosegek, headers='firstrow', tablefmt='grid'))
        console = input("Console >")
        player_turn = True
        if player_turn:
            if console == "0":
                if choice_m_or_b == 0:
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
                if choice_m_or_b == 1:
                    boss[choice].hp -= player.dmg
                    print(f"Damageltél a bossra {player.dmg}-t!")
                    for i in range(8):
                        printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                        time.sleep(0.25)
                    player_turn = False
                    clear_screen()
                    if boss[choice].hp <= 0:
                        boss_list.remove(choice)
                        print("A boss meghalt!")
                        time.sleep(2)
                        clear_screen()
                        break
            elif console == "+":
                if player.poti == 1:
                    player.hp = player.hp + 50
                    player.poti -= 1
                    print("Kaptál 50 életerőt!")
                    for i in range(8):
                        printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                        time.sleep(0.25)
                elif player.poti == 0:
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
                        if choice_m_or_b == 0:
                            damage = random.randrange(player_damage_start + 20, player_damage_end + 20)
                            mobs[choice].hp -= damage
                            print(f"Damageltél a mobra az Ezüstszelidítés képesség használatával {player.dmg}-t!")

                            for i in range(8):
                                printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                                time.sleep(0.25)

                            player.kepesseg_1 -= 1
                            player_turn = False
                            clear_screen()
                        if choice_m_or_b == 1:
                            damage = random.randrange(player_damage_start + 20, player_damage_end + 20)
                            boss[choice].hp -= damage
                            print(f"Damageltél a bossra az Ezüstszelidítés képesség használatával {player.dmg}-t!")

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
            if choice_m_or_b == 0:
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
            if choice_m_or_b == 1:
                player.hp -= boss[choice].dmg
                print(f"Az ellenség damagelt rád {boss[choice].dmg}-t")
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




