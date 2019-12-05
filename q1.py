# Hunter Nyenhuis
# 27 November 2019
# Extra Credit Assignment

import file_handler
players = {}

print('\n------------------------------\nWelcome to the rank calculator\n------------------------------')
menu = ['','Enter a value (1 - 8)','1. Create player','2. Remove player',
		'3. Update wins and losses', '4. Display player statistics',
		'5. Save player data to csv file','6. Load player data from csv file', 
		'7. View plot of individual player', '8. View plot of every player', '9. Exit']
for x in menu:
	print(x)
input1 = input()
while not input1.isdigit():
	print('Please enter an integer from the menu.')
	for x in menu:
		print(x)
	input1 = input()
choice = int(input1)
		
while choice != 9:	

	if choice == 1: # add player name
		
		# Get user input for player info
		player_name = input('Enter player name to add: ')
		new_player = {} # new dict of players

		# set wins and losses for new player
		wins_input = input('Enter number of wins: \n')
		while not wins_input.isdigit() or int(wins_input) < 0:
			wins_input = input('Error: Please enter a valid number of wins: \n')

		losses_input = input('Enter number of losses:\n')
		while not losses_input.isdigit() or int(losses_input) < 0:
			losses_input = input('Error: Please enter a valid number of wins: \n')

		# convert digits to int
		wins = int(wins_input)
		losses = int(losses_input)
		
		# base case -> undefeated
		if losses == 0 and wins != 0: 
			rank_value = 6
		else:
			if wins/losses > 6: # set cut-off to be top rank
					rank_value = 6
			else:
				rank_value = wins/losses

		new_player['wins'] = wins
		new_player['losses'] = losses
		new_player['rank'] = 'unranked'
		new_player['rank_value'] = rank_value # for plotting
		new_player['progression_list'] = [rank_value] # for individual progression plotting
		# add student info to dictionary of students
		players[player_name] = new_player

	elif choice == 2: # remove player
		if players:
			name = input('Enter player to remove: ')
			while name not in players:
				name = input('Error: Player entry does not exist. Enter valid name: ')
			del players[name]
		else:
			print('No player entries exist.')

	elif choice == 3: # update wins and losses
		if players:
			
			user_input = input('Enter a player name to update wins and losses: \n')

			while user_input not in players:
				user_input = input('Player entry does not exist. Please enter valid name: ')

			wins_input = input('Enter number of new wins: \n')
			while not wins_input.isdigit() or int(wins_input) < 0:
				wins_input = input('Error: Please enter a valid number of new wins: \n')

			losses_input = input('Enter number of new losses:\n')
			while not losses_input.isdigit() or int(losses_input) < 0:
				losses_input = input('Error: Please enter a valid number of new losses: \n')

			wins = int(wins_input) + players[user_input]['wins'] # cumulative wins
			losses = int(losses_input) + players[user_input]['losses'] # cumulative losses

			# base case -> undefeated
			if losses == 0 and wins != 0: 
				rank_value = 6
			else:
				if wins/losses > 6: # set cut-off to be top rank
					rank_value = 6
				else:
					rank_value = wins/losses

			# update player's dictionary
			players[user_input]['wins'] = wins
			players[user_input]['losses'] = losses
			players[user_input]['rank_value'] = rank_value
			players[user_input]['progression_list'].append(rank_value)

		else:
			print('No player entries exist.')

	elif choice == 4: # Display player statistics
		if players: 				
			user_input = input('Enter player name, or enter \"all\"\n')
			categories = ['wins','losses','rank']	

			# highest and lowest ranked players
			max_rank = 0
			min_rank = 1000 # extreme outlier because there is no win percentage cap
			max_rank_name = ''
			min_rank_name = ''

			# calculate rank for each player
			for player_key in players: # for each player
		
				rank_value = players[player_key]['rank_value']

				if rank_value >= max_rank:
					max_rank_name = player_key # update name holding max rank
					max_rank = rank_value # update max rank value
				if rank_value <= min_rank:
					min_rank_name = player_key
					min_rank = rank_value

				rank = ''
				if rank_value >= 6: # winning 6x as many games as losing earns Grand Champion
					rank = 'Grand Champion'
				elif rank_value >= 5 and rank_value < 6:
					rank = 'Champion'
				elif rank_value >= 4 and rank_value < 5:
					rank = 'Diamond'
				elif rank_value >= 3 and rank_value < 4:
					rank = 'Platinum'
				elif rank_value >= 2 and rank_value < 3:
					rank = 'Gold'
				elif rank_value >= 1 and rank_value < 2:
					rank = 'Silver'
				elif rank_value >= 0 and rank_value < 1:
					rank = 'Bronze'
				else:
					rank = 'Error: Invalid rank value'
				players[player_key]['rank'] = rank
			
			# Option 1: dispaly all students
			if user_input == 'all':

				print('')
				for player_key in players: # for each student
					print(player_key)
					for x in categories:
						print('{}: {}'.format(x,players[player_key][x])) # print category with its info				
					print('**********************')

				print('Highest and lowest ranks')
				print('Max: %s : %s'%(max_rank_name,players[max_rank_name]['rank']))
				print('Min: %s : %s'%(min_rank_name,players[min_rank_name]['rank']))

			# Option 2: display specific student
			else:
				while user_input not in players:
					user_input = input('Player entry does not exist. Please enter valid name:\n')
					
				for x in categories:
					print('{}: {}'.format(x,players[user_input][x])) # print category with its info
		else:
			print('No player entries exist.')

	elif choice == 5: # Save player data to a csv file
		if players:
			file_handler.write(players)	
		else:
			print('No player entries exist.')

	elif choice == 6: # Load students’ data from file
		players = file_handler.read(players)

	elif choice == 7: # View plot of rank progression for individual player
		if players:
			name = input('Enter player name to view a plot of their rank progression: ')
			while name not in players:
				name = input('Error: Player entry does not exist. Enter valid name: ')
			file_handler.plotPlayerProgression(name, players[name]['progression_list'])
		else:
			print('No player entries exist.')

	elif choice == 8: # View plot of all players
		if players:
			file_handler.plotAllPlayers(players)
		else:
			print('No player entries exist.')

	else:
		print('Invalid input. Please enter an integer value 1 through 8')

	# restart loop
	for x in menu:
		print(x)
	input1 = input()
	while not input1.isdigit():
		print('Please enter an integer from the menu.')
		for x in menu:
			print(x)
		input1 = input()
	choice = int(input1)