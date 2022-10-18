# slicing lists
players = ['charles','martina','micheal','florence','eli']
print(players)

# indexing
print(players[0])
print(players[1])
print(players[2])
print(players[3])
print(players[4])

# Slicing 
print(players[0:3])
# prints the llist includes the first three players
# players[0] charles
# players[1] martina
# players[2] micheal
# To find second third fourth items in list
print(players[1:4])
# slicing starts at index1 and ends at index4
print(players[:4]) 
# without starting index the remaining elements are
print(players[2:]) 
# slice that includes the ewnd of the list

# looping trogh slice
# printing the first three names 
for player in players[:3]:
    print("Players are "+player.title()) 
# printing the last three names
for player in players[3:]:
    print("Players are "+player.title())  

# Copying the lists
my_games = ['cds','cds2','cgs']
my_games.append('wwe')
friends_games = my_games[:]
print(my_games) 
print(friends_games) 