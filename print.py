import random


def sravn(first_turn, second_turn):
    """
    sravnenie dvuh znacheniy
    stone = 0 
    scissors = 1
    paper = 2 
    0<1<2
    """
    if first_turn == second_turn:
        sravn=0
    elif first_turn > second_turn:
        if first_turn - second_turn == 1:
            sravn = 2
        elif first_turn - second_turn > 1:
            sravn = 1
    elif first_turn < second_turn:
        if second_turn - first_turn == 1:
            sravn=1
        elif second_turn - first_turn > 1:
            sravn=2
    
    return sravn
    #pass

start_my_turn = int(input("Chouse your turn(stone(0),scissors(1), paper(2) :"))
start_en_turn = random.randint(0, 2)
if start_en_turn == 0:
    if start_my_turn == 0:
        end = 'Ничья'
    elif start_my_turn == 1:
        end = 'Defeat'
    elif start_my_turn == 2:
        end = "Win" 

elif start_en_turn == 1:
    if start_my_turn == 0:
        end = 'Win' 
    elif start_my_turn == 1:   
        end = 'Ничья' 
    elif start_my_turn == 2:
        end = 'Defeat'

elif start_en_turn == 2:
    if start_my_turn == 0:
        end = "Defeat" 
    elif start_my_turn == 1:
        end = 'Win' 
    elif start_my_turn == 2: 
        end = 'Ничья'

print(f'Робот загадал {start_en_turn}')
print(f'{end}')



print("new def")
print(sravn(start_my_turn,start_en_turn))
