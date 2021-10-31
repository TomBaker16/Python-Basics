import itertools


def win(y):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0: 
            return True
        else:
            return False

    #Horizontal check
    for row in game:
        if all_same(row):  
            print(f"Player {row[0]} is the winner horizontally! (---)")
            return True

    #Diagonal check
    diags_u = []  
    for col, row in enumerate(reversed(range(len(game)))):
        diags_u.append(game[row][col])
    if all_same(diags_u):   
        print(f"Player {diags_u[0]} is the winner diagonally! (/)")
        return True

    diags_d = []
    for i in range(len(game)):  
        diags_d.append(game[i][i])
    if all_same(diags_d):   
        print(f"Player {diags_d[0]} is the winner diagonally! (\\)")
        return True


    #vertical check
    for col in range(len(game)):
        x = []  
        for row in game:   
            x.append(row[col])         
        if all_same(x):
            print(f"Player {x[0]} is the winner vertically! (|)")
            return True
    return False 


def game_board(game_map, choice=0, row=0, column=0, just_display=False): #the function that controls game inputs
    try:
        if game_map[row][column] != 0:  #if the location on the game map does not equal 0 
            print("no can do, choose another")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = choice 
        for i, row in enumerate (game_map): 
            print (i, row)
        return game_map, True

    except IndexError as error:
        print ('choose a different number', error)
        return game_map, False

    except Exception as error:
        print ('whoops', error)
        return game_map, False

play = True
players = [1,2]
while play:
    game = [[0, 0, 0], 
            [0, 0, 0], 
            [0, 0, 0]]

    game_won = False
    game, _ = game_board(game, just_display = True)
    player_choice = itertools.cycle(players)
    while not game_won:
        current_player = next(player_choice)
        print(f"Player {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column? (0, 1, 2): "))
            row_choice = int(input("What row? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("Game over, play again? (y/n) ")
            if again.lower() == "y":
                print('restarting')
            elif again.lower() == "n":
                print("byyyyye")
                play = False
            else:
                print("not valid answer, bye")
                play = False








