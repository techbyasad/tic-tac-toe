def askAboutPlay(repeat):
    playgame = input(f"would you like to play the tiktak game {repeat}? 'yes' or 'no':")
    playgame = playgame.lower()
    while(playgame != 'yes' and playgame != 'no'):
        playgame = askAboutPlay(repeat)
    return playgame


def printTable(gameTable):
    print(' '+ gameTable[0][0]+' '+'|'+' '+ gameTable[0][1]+' '+'|'' '+ gameTable[0][2]+' ')
    print('------------')
    print(' '+ gameTable[1][0]+' '+'|'+' '+ gameTable[1][1]+' '+'|'' '+ gameTable[1][2]+' ')    
    print('------------')
    print(' '+ gameTable[2][0]+' '+'|'+' '+ gameTable[2][1]+' '+'|'' '+ gameTable[2][2]+' ')    


def checkWinner(gameTable,player1,player2):
    if(
        (gameTable[0][0] == player1 == gameTable[0][1] == gameTable[0][2]) 
       or (gameTable[1][0] == player1 == gameTable[1][1] == gameTable[1][2])
       or (gameTable[2][0] == player1 == gameTable[2][1] == gameTable[2][2])
       or (gameTable[0][0] == player1 == gameTable[1][0] == gameTable[2][0])
       or (gameTable[0][2] == player1 == gameTable[1][2] == gameTable[2][2])
       or (gameTable[0][2] == player1 == gameTable[1][1] == gameTable[2][0])
       or (gameTable[0][0] == player1 == gameTable[1][1] == gameTable[2][2])
       ):
            print('Winner is player 1')
            return player1;
    elif(
        (gameTable[0][0] == player2 == gameTable[0][1] == gameTable[0][2]) 
       or (gameTable[1][0] == player2 == gameTable[1][1] == gameTable[1][2])
       or (gameTable[2][0] == player2 == gameTable[2][1] == gameTable[2][2])
       or (gameTable[0][0] == player2 == gameTable[1][0] == gameTable[2][0])
       or (gameTable[0][2] == player2 == gameTable[1][2] == gameTable[2][2])
       or (gameTable[0][2] == player2 == gameTable[1][2] == gameTable[2][0])
       or (gameTable[0][0] == player2 == gameTable[1][2] == gameTable[2][2])
       ):
            print('Winner is player 2')
            return player2
    return -1;


def takeInput(gameTable,playerSign,playerNumber):
    notgoodInput = True
    while(notgoodInput):
        index = input(f"Player {playerNumber}, please choose the box where you would like to place your {playerSign}, press q if you quit:")
        if(index == 'q' or index == 'Q'):
            print('quiting..')
            return -1;
        if(index.isdigit()):
            index = int(index)
            if(index in range(1,10)):
                if(index <= 3 and gameTable[0][index -1] == ' '):
                    gameTable[0][index -1] = playerSign;
                    return index
                elif(index > 3 and index <= 6 and gameTable[1][index -4] == ' '):
                    gameTable[1][index -4] = playerSign;
                    return index
                elif(index > 6 and index <= 9 and gameTable[2][index -7] == ' '):
                    gameTable[2][index -7] = playerSign;                    
                    return index
                else:
                    print('Already Filled, try again');
            else:
                print('out of range')
        else:
            print('wrong input, please try again.')


repeat = '' 
playgame = askAboutPlay(repeat)

while(playgame == 'yes'):
    
    player1 = ''
    player2 = ''
    gameOn = True
    gameTable = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    printTable(gameTable)
    #choose sign for game

    while(player1 != 'X' and player1 != 'O'):
        player1 = input("please choose a sign for player 1... X or O:")
        player1 = player1.upper()
    
    player2 = 'O' if player1 == 'X' else 'X'
    print(f"Great, player 1 is {player1} and player2 is {player2}")

    printTable(gameTable)

    whoseTurn = player1;
    playerNumber = 1;
    while (gameOn):
        output = takeInput(gameTable,whoseTurn,playerNumber)
        if(output == -1):
            gameOn = False
            break
        
        printTable(gameTable)        
        winner = checkWinner(gameTable,player1,player2)
        if(winner != -1):
            gameOn = False
            break;
        whoseTurn = player2 if(whoseTurn == player1) else player1
        playerNumber = 2 if(playerNumber == 1) else 1

    #ask for the game again
    repeat = 'again'
    playgame = askAboutPlay(repeat)