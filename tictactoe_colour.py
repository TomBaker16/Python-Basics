import itertools

from colorama import Fore, Back, Style

def win(y): #defines the function to determine if a win has occured

    def all_same(l):  #function within the win function that checks for the win
        if l.count(l[0]) == len(l) and l[0] != 0: 
            return True
        else:                 #the True/False logic here relates to the "all_same" function. If the 'if' statement is correct
            return False    #then True is returned and the function execute and passes the code. If not then it returns false
                            #and the code isn't passed
    #Horizontal look
    for row in game:
        if all_same(row):  #apply the "all_same" function and use row as the parameter. if the function returns True, the next
            print(f"Player {row[0]} is the winner horizontally! (---)")    #code is executed.
            return True   #this makes the win function True, a win has happened

    #Diagonal look
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


    #vertical look
    for col in range(len(game)):
        x = []  
        for row in game:   
            x.append(row[col])         
        if all_same(x):
            print(f"Player {x[0]} is the winner vertically! (|)")
            return True
    return False #win function is False if none of the above for loops returns a true


def game_board(game_map, choice=0, row=0, column=0, just_display=False): #the function that controls game inputs
           #the game_map parameter is where the function will display the board
           #choice parameter is for what object you want to place on the board (eg a 1 or 2)
           #row and column parameters are for where choice will be placed on the board
           #just display parameter is to print out the game board
    try:
        if game_map[row][column] != 0:  #if the location on the game map does not equal 0, then: 
            print("no can do, choose another") #(row and column parameters are defined in the function)
            return game_map, False  #by returning game_map and false, the loop runs again until the location chosen DOES  
                                    #equal zero, then this loop isn't run and it goes onto the next loop
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))   #this line is to print the column labels
                                                                        
        if not just_display:               #this loop says if just_display=False (the default) then execute the code below.                               
            game_map[row][column] = choice  #statement says that game_map location at indexes row and column  
                                                #equal whatever 'choice' is. Puts a 1 or 2 at the location.
        for i, row in enumerate (game_map): #enumerate gives the index followed by the item for the list "game_map"
            coloured_row = ""
            for item in row:
                if item == 0:
                    coloured_row += "   "
                elif item == 1:
                    coloured_row += Fore.GREEN + " X " + Style.RESET_ALL
                elif item == 2:
                    coloured_row += Fore.MAGENTA + " O " + Style.RESET_ALL
            print (i, coloured_row)   #this allows the rows of the game to be labelled alongside the game board


        return game_map, True  #this return command is outside of the loops above. So this happens once the above is done 
                                #and satisfies the try: command

    except IndexError as error:
        print ('choose a different number', error)
        return game_map, False

    except ValueError:
        print ('whoops')
        return game_map, False

play = True        #statement. Allows us to be able to end the game later
players = [1,2]   #defining a variable, players
while play:      #while play is True do all of the following
    game = [[0, 0, 0], 
            [0, 0, 0],     #defines the game board which will later be edited by game_board function
            [0, 0, 0]]

    game_won = False    #statement. Allows us to have 'game won' and 'game not yet won' scenarios
    game_board(game, just_display=True) # game, _ = 
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
