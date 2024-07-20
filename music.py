import pygame
import random

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()

musics = ['C:/Users/Bácsi Péter/PycharmProjects/Game2.0/Hurts - Some Kind of Heaven (Audio).mp3',
          'C:/Users/Bácsi Péter/PycharmProjects/Game2.0/Hurts - Nothing Will Be Bigger Than Us (Audio).mp3',
          'C:/Users/Bácsi Péter/PycharmProjects/Game2.0/Hurts - Slow (Audio).mp3',
          'C:/Users/Bácsi Péter/PycharmProjects/Game2.0/Hurts - Wish (Official Video).mp3'
          ]

def play_music():
    first_choice = random.choice(musics)
    pygame.mixer.music.load(first_choice)
    pygame.mixer.music.play()
    musics.remove(first_choice)
    pygame.mixer.music.set_volume(0.1)
    if pygame.mixer.music.get_busy() == False:
        second_choice = random.choice(musics)
        pygame.mixer.music.load(second_choice)
        pygame.mixer.music.play()
        musics.remove(second_choice)
        pygame.mixer.music.set_volume(0.1)
        if pygame.mixer.music.get_busy() == False:
            third_choice = random.choice(musics)
            pygame.mixer.music.load(third_choice)
            pygame.mixer.music.play()
            musics.remove(third_choice)
            pygame.mixer.music.set_volume(0.1)
            if pygame.mixer.music.get_busy() == False:
                forth_choice = random.choice(musics)
                pygame.mixer.music.load(forth_choice)
                pygame.mixer.music.play()
                musics.remove(forth_choice)
                pygame.mixer.music.set_volume(0.1)


def skip():
    musics_len = len(musics)
    if musics_len == 3:
        pygame.mixer.music.stop()
        random_choice_1 = random.choice(musics)
        pygame.mixer.music.load(random_choice_1)
        pygame.mixer.music.play()
        musics.remove(random_choice_1)
        pygame.mixer.music.set_volume(0.2)
        if pygame.mixer.music.get_busy() == False:
            random_choice_2 = random.choice(musics)
            pygame.mixer.music.load(random_choice_2)
            pygame.mixer.music.play()
            musics.remove(random_choice_2)
            pygame.mixer.music.set_volume(0.2)
            if pygame.mixer.music.get_busy() == False:
                random_choice_3 = random.choice(musics)
                pygame.mixer.music.load(random_choice_3)
                pygame.mixer.music.play()
                musics.remove(random_choice_3)
                pygame.mixer.music.set_volume(0.2)
    if musics_len == 2:
        pygame.mixer.music.stop()
        random_choice_1 = random.choice(musics)
        pygame.mixer.music.load(random_choice_1)
        pygame.mixer.music.play()
        musics.remove(random_choice_1)
        pygame.mixer.music.set_volume(0.2)
        if pygame.mixer.music.get_busy() == False:
            random_choice_2 = random.choice(musics)
            pygame.mixer.music.load(random_choice_2)
            pygame.mixer.music.play()
            musics.remove(random_choice_2)
            pygame.mixer.music.set_volume(0.2)
    if musics_len == 1:
        pygame.mixer.music.stop()
        random_choice_1 = random.choice(musics)
        pygame.mixer.music.load(random_choice_1)
        pygame.mixer.music.play()
        musics.remove(random_choice_1)
        pygame.mixer.music.set_volume(0.2)
    if musics_len == 0:
        pygame.mixer.music.stop()
        musics.append('C:/Users/Bácsi Péter/PycharmProjects/Game2.0/Hurts - Some Kind of Heaven (Audio).mp3')
        musics.append('C:/Users/Bácsi Péter/PycharmProjects/Game2.0/Hurts - Nothing Will Be Bigger Than Us (Audio).mp3')
        musics.append('C:/Users/Bácsi Péter/PycharmProjects/Game2.0/Hurts - Slow (Audio).mp3')
        musics.append('C:/Users/Bácsi Péter/PycharmProjects/Game2.0/Hurts - Wish (Official Video).mp3')
        random_choice_1 = random.choice(musics)
        pygame.mixer.music.load(random_choice_1)
        pygame.mixer.music.play()
        musics.remove(random_choice_1)
        pygame.mixer.music.set_volume(0.2)
        if pygame.mixer.music.get_busy() == False:
            random_choice_2 = random.choice(musics)
            pygame.mixer.music.load(random_choice_2)
            pygame.mixer.music.play()
            musics.remove(random_choice_2)
            pygame.mixer.music.set_volume(0.2)
            if pygame.mixer.music.get_busy() == False:
                random_choice_3 = random.choice(musics)
                pygame.mixer.music.load(random_choice_3)
                pygame.mixer.music.play()
                musics.remove(random_choice_3)
                pygame.mixer.music.set_volume(0.2)
                if pygame.mixer.music.get_busy() == False:
                    random_choice_4 = random.choice(musics)
                    pygame.mixer.music.load(random_choice_4)
                    pygame.mixer.music.play()
                    musics.remove(random_choice_4)
                    pygame.mixer.music.set_volume(0.2)
def turn_off():
    pygame.mixer.music.stop()
