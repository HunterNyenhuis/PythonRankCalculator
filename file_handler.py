# Hunter Nyenhuis
# 27 November 2019
# Extra Credit Assignment

import csv
from matplotlib import pyplot as plt
import numpy as np

def write(players):

	filename = input('Enter a name for the file you want to save. Make sure to add .csv to the end.\nFile name: ')
	while filename[-4:] != '.csv' or len(filename) < 5:
		filename = input('Please add a name and \".csv\" to the end of the filename.\nFile name: ')

	categories = ['name','wins','losses','rank', 'rank_value','progression_list']
	with open(filename, "w") as csvfile:

		player_writer = csv.DictWriter(csvfile, categories)
		player_writer.writeheader()

		#player_names = [player for player in players]

		player_progression_lists = []
		i = 0
		for name in players:
			# add delimiter to combine progression list for writing to file
			progression = players[name]['progression_list']
			player_progression_lists.append(progression) # add to list of lists of player progressions
			combined_rank_values = '-'.join(str(val) for val in progression) #.75-1.5-2.0-1.8-4.25
			# update progression_list key with combined rank_values string
			players[name]['progression_list'] = combined_rank_values
			# write to csv
			player_writer.writerow({category: players[name].get(category) or name for category in categories})
			# revert back to original value for additional entries
			players[name]['progression_list'] = player_progression_lists[i]
			i += 1
		print('{} was saved successfully'.format(filename))

def read(players):

	players = {}
	filename = input('Enter the name of a file to load.\nFile name: ')
	
	file_exists = False
	while file_exists is False:
		try:
			with open(filename) as csvfile:
				player_reader = csv.reader(csvfile, delimiter=',')
				first_row = True
				for row in player_reader:
					#skip first row
					if first_row:
						first_row = False
						continue
					
					rank_splitter_list = row[5].split('-') # [.75,1.5,2.0,1.8,4.25]
					for i in range(0,len(rank_splitter_list)):
						rank_splitter_list[i] = float(rank_splitter_list[i])

					players[row[0]] = {'wins':float(row[1]),'losses':float(row[2]),'rank':row[3],'rank_value':float(row[4]),'progression_list':rank_splitter_list}
			file_exists = True
		except IOError:
			filename = input('Please enter a valid file name or file path. Be sure to add \".csv\" to the end of the filename.\nFile name: ')
	print('{} was loaded successfully'.format(filename))
	return players

def plotPlayerProgression(name, progression_list):

	ranks_list = ['Bronze','Silver','Gold','Platinum','Diamond','Champion','Grand\nChampion']
	num_values = range(0,len(progression_list))
	# plot
	plt.plot(num_values, progression_list,'ro:', label="Rank Value")

	# plot customizations
	plt.legend(loc="upper left", fancybox=True, framealpha=.5)
	plt.title('{}\'s Rank Progression'.format(name))
	plt.xlabel('Player Win/Loss Entries')
	plt.ylabel('Rank')
	plt.xlim(0, len(num_values) - 1)
	plt.ylim(0, 7)

	y = np.array([0,1,2,3,4,5,6])
	plt.yticks(y, ranks_list)

	plot_file = input('Enter a name for the plot file. Make sure to add .png to the end.\nFile name: ')
	while plot_file[-4:] != '.png' or len(plot_file) < 5:
		plot_file = input('Please add a name and \".png\" to the end of the filename.\nFile name: ')
	plt.savefig(plot_file)		
	print('{} has been successfully saved in the assingment folder.'.format(plot_file))	
	plt.clf()

def plotAllPlayers(players):
	
	ranks_list = ['Bronze','Silver','Gold','Platinum','Diamond','Champion','Grand\nChampion']

	# find x-axis range
	max_entries = 0
	for name in players:
		if len(players[name]['progression_list']) > max_entries:
			max_entries = len(players[name]['progression_list'])
			
	num_values = range(0,max_entries)
	# plot
	line_type = ['bo:','go:','ro:','ko:','yo:','mo:','co:','bo--','go--','ro--','ko--','yo--','mo--','co--']
	i = 0
	for name in players:
		x_range = num_values[:len(players[name]['progression_list'])] # from 0 to the varied list length
		plt.plot(x_range, players[name]['progression_list'],line_type[i],label=name)
		i += 1

	# plot customizations
	plt.legend(loc="upper left", fancybox=True, framealpha=.5)
	plt.title('All Player Rank Progressions')
	plt.xlabel('Player Win/Loss Entries')
	plt.ylabel('Rank')
	plt.xlim(0, len(num_values) - 1)
	plt.ylim(0, 7)

	y = np.array([0,1,2,3,4,5,6])
	plt.yticks(y, ranks_list)

	plot_file = input('Enter a name for the plot file. Make sure to add .png to the end.\nFile name: ')
	while plot_file[-4:] != '.png' or len(plot_file) < 5:
		plot_file = input('Please add a name and \".png\" to the end of the filename.\nFile name: ')
	plt.savefig(plot_file)		
	print('{} has been successfully saved in the assingment folder.'.format(plot_file))	
	plt.clf()

