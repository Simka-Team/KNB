import random



start_my_turn = input("Chouse your turn(stone(0),scissors(1), paper(2)")
start_en_turn = str(random.randint(0,2))
if start_en_turn == "0":
	if start_my_turn == "0":
		end = 'Ничья'
		
	elif start_my_turn == '1':
	 	end = 'Defeat'
	 	
	elif start_my_turn == '2':
	 	end = "Win"
	 	
	 
elif start_en_turn == '1':
	 if start_my_turn == '0':
	 	end = 'Win'
	 	
	 elif start_my_turn == '1':
	 	end = 'Ничья'
	 	
	 elif start_my_turn == '2':
	 	end = 'Defeat'
	 	
	 
elif start_en_turn == "2":
	 if start_my_turn == '0':
	 	end = "Defeat"
	 	
	 elif start_my_turn == '1':
	 	end = 'Win'
	 	
	 elif start_my_turn == '2':
	 	end = 'Ничья'
	 	
	 
	 		
print(end)
