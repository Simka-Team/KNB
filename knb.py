import random



start_my_turn = input("Chouse your turn(stone(0),scissors(1), paper(2)")
str(start_en_turn = random.randint(0,2))
if start_en_turn == "0":
	if start_my_turn == "0":
		end = 'Ничья'
		break
	elif start_my_turn == '1':
	 	end = 'Defeat'
	 	break
	elif start_my_turn == '2':
	 	end = "Win"
	 	break
	 
elif start_en_turn == '1':
	 if start_my_turn == '0':
	 	end = 'Win'
	 	break
	 elif start_my_turn == '1':
	 	end = 'Ничья'
	 	break
	 elif start_my_turn == '2':
	 	end = 'Defeat'
	 	break
	 
elif start_en_turn == "2":
	 if start_my_turn == '0':
	 	end = "Defeat"
	 	break
	 elif start_my_turn == '1':
	 	end = 'Win'
	 	break
	 elif start_my_turn == '2':
	 	end = 'Ничья'
	 	break
	 
	 		
print(f'{end}')
