from random import choice, randint
import time

def baucua():
    list_game = ["Bau", "Cua", "Tom", "Ca", "Ga", "Nai", "Huou"]

    # choice group of 3
    return choice(list_game), choice(list_game), choice(list_game)


def create_dice():
    print("Bắt đầu sốc")
    
    for(i, value) in enumerate(baucua()):
        time.sleep(1)
        print(i, value)

if __name__ == '__main__':
    create_dice()