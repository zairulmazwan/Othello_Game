import os


menu = ":::Welcome to Othello Game:::\n=============================\n1. New Game\n2. Store a game\n3. Quit\n\n"

player1 = "  "
player2 = "@@"
player1Name=""
player2Name=""

def drawBoard():
  size = 8
  board =[]
  counter=1
  for i in range (size):
    row=[]
    for j in range (size):
      if counter<10:
        number="0"+str(counter)
      else:
        number = str(counter)
      row.append(number)
      counter+=1
    board.append(row)
  return board


def setOthello(board):
  for i in range(len(board)):
    for j in range(len(board)):
      if (i==3 and j == 3):
        board[i][j]=str(player1)
      elif (i==3 and j == 4):
       board[i][j]=str(player2)
      elif (i==4 and j == 3):
       board[i][j]=str(player2)
      elif (i==4 and j == 4):
       board[i][j]=str(player1)
  return board


def printBoard(board):
  for i in range(len(board)):
    print(" ----"*len(board))
    print("|", end=" ")
    for j in range(len(board)):
      print(board[i][j], "|", end = " ")
    print()
  print(" ----"*len(board))


def checkSpaceToMove(board):
  canMove = False
  for row in board:
    for col in row:
      if (col != "  " or col != "@@"):
        canMove=True
  return canMove

def makeMove(board, userChoice, player):
 if (userChoice%len(board)==0):
      row = (userChoice//len(board))-1
      col = (userChoice%len(board))-1
      board[row][col] = player
 else:
      row = userChoice//len(board)
      col = (userChoice%len(board))-1
      board[row][col] = player


def checkValidSpace(board, userChoice):
  valid=True
  row=-1
  col=-1
  if (userChoice%len(board)==0):
      row = (userChoice//len(board))-1
      col = (userChoice%len(board))-1
  else:
      row = userChoice//len(board)
      col = (userChoice%len(board))-1
  if (board[row][col]=="  " or board[row][col]=="@@"):
    valid=False
  return valid


def Move(board, userChoice, player):
 #print("Player pattern : ", player)
 valid = False
 row=-1
 col=-1

 #check whether the place has been chosen
 if (board[row][col]=="  " or board[row][col]=="@@"):
    valid=False

 if (userChoice%8==0):
   row = (userChoice//8)-1
   col = 7
 else:
   row = (userChoice//8)
   col = userChoice-(row*len(board))-1

 playerOpposite=""
 if (player=="@@"):
   playerOpposite="  "
 else:
    playerOpposite="@@"

 #print("player opposite pattern : ", playerOpposite)
 #west
 #print("west")
 #print(col)
 if (col>0):
  if (board[row][col-1]==playerOpposite):
    board[row][col]=player
    #print("west")
    #print(row, col)
    indexCol=(col-1)
    while(indexCol>-1):
      indexCol-=1
      if (board[row][indexCol]==player):
        valid=True
    #print(valid)
    indexCol=(col-1)
    if(valid):
      while(indexCol>1):
        #print(indexCol)
        if (board[row][indexCol]==playerOpposite):
          #print("Flip")
          board[row][indexCol]=player
        else:
          break
        indexCol-=1

 valid = False
 #northwest
 if(col>0 and row>0):
  if (board[row-1][col-1]==playerOpposite):
    board[row][col]=player
    #print("northwest")
    #print(row, col)
    indexRow=(row-1)
    indexCol=(col-1)
    while(indexRow>1 or indexCol>1):
      indexRow-=1
      indexCol-=1
      if (board[indexRow][indexCol]==player):
        valid=True
    #print(valid)
    indexRow=(row-1)
    indexCol=(col-1)
    if(valid):
      while(indexRow>1 or indexCol>1):
        if (board[indexRow][indexCol]==playerOpposite):
          board[indexRow][indexCol]=player
        else:
          break
        indexRow-=1
        indexCol-=1

 valid = False
 #north
 if(row>0):
  if (board[row-1][col]==playerOpposite):
    #print("north")
    board[row][col]=player
    #print(row, col)
    indexRow=(row-1)
    while(indexRow>0):
      indexRow-=1
      if (board[indexRow][col]==player):
        valid=True
    #print(valid)
    indexRow=(row-1)
    if(valid):
      while(indexRow>1):
        print(indexRow)
        if (board[indexRow][col]==playerOpposite):
          board[indexRow][col]=player
        else:
          break
        indexRow-=1

 valid = False
 #northeast
 if(row>0 and col<7):
  if (board[row-1][col+1]==playerOpposite):
    #print("northeast")
    board[row][col]=player
    #print(row, col)
    indexRow=(row-1)
    indexCol=(col+1)
    while(indexRow>1 and indexCol<len(board)-2):
      indexRow-=1
      indexCol+=1
      if (board[indexRow][indexCol]==player):
        valid=True
    #print(valid)
    indexRow=(row-1)
    indexCol=(col+1)
    if(valid):
      while(indexRow>1 and indexCol<len(board)-2):
        #print(indexRow)
        if (board[indexRow][indexCol]==playerOpposite):
          board[indexRow][indexCol]=player
        else:
          break
        indexRow-=1
        indexCol+=1

 valid = False
 #east
 if(col<7):
  if (board[row][col+1]==playerOpposite):
    #print("east")
    board[row][col]=player
    #print(row, col)
    indexCol=(col+1)
    while(indexCol<len(board)-2):
      indexCol+=1
      #print(row, indexCol)
      if (board[row][indexCol]==player):
        valid=True
    #print(valid)
    indexCol=(col+1)
    if(valid):
      while(indexCol<len(board)-2):
        if (board[row][indexCol]==playerOpposite):
          board[row][indexCol]=player
        else:
          break
        indexCol+=1

 valid = False
 #southeast
 if(row<7 and col<7):
  #print("southeast")
  #print(row, col)
  if (board[row+1][col+1]==playerOpposite):
      board[row][col]=player
      #print(row, col)
      indexRow=(row+1)
      indexCol=(col+1)
      while(indexRow<len(board)-2 and indexCol<len(board)-2):
        indexRow+=1
        indexCol+=1
        #print(indexRow, indexCol)
        if (board[indexRow][indexCol]==player):
          valid=True
      #print(valid)
      indexRow=(row+1)
      indexCol=(col+1)
      if(valid):
        while(indexRow<len(board)-2 or indexCol<len(board)-2):
          if (board[indexRow][indexCol]==playerOpposite):
            board[indexRow][indexCol]=player
          else:
            break
          indexRow+=1
          indexCol+=1

 valid = False
 #south
 if(row<7):
  if (board[row+1][col]==playerOpposite):
    board[row][col]=player
    #print("south")
    #print(row, col)
    indexRow=(row+1)
    while(indexRow<len(board)-1):
      indexRow+=1
      if (board[indexRow][col]==player):
        valid=True
    #print(valid)
    indexRow=(row+1)
    if(valid):
      while(indexRow<len(board)-2):
        if (board[indexRow][col]==playerOpposite):
          board[indexRow][col]=player
        else:
          break
        indexRow+=1

 valid = False
  #southwest
 if(row<7 and col>0):
  if (board[row+1][col-1]==playerOpposite):
      board[row][col]=player
      #print("southwest")
      #print(row, col)
      indexRow=(row+1)
      indexCol=(col-1)
      while(indexRow<len(board)-2 and indexCol>0):
        indexRow+=1
        indexCol-=1
        #print(indexRow, indexCol)
        if (board[indexRow][indexCol]==player):
          valid=True
      #print(valid)
      indexRow=(row+1)
      indexCol=(col-1)
      if(valid):
        while(indexRow<len(board)-3 and indexCol>1):
          if (board[indexRow][indexCol]==playerOpposite):
            board[indexRow][indexCol]=player
          else:
            break
          indexRow+=1
          indexCol+=1

 return valid

def checkSpaceBalance(board):
  spaceBal = 0;
  for row in range(len(board)):
    for col in range(len(board[row])):
      if ((board[row][col]!="@@") and (board[row][col]!="  ") and (board[row][col]!="\n")):
        #print(board[row][col])
        spaceBal+=1
  return spaceBal


def countToken(board, player):
  count=0
  for row in board:
    for col in row:
      if (col==player):
        count+=1
  return count


def displayTokenInfo (board, player1Name, player2Name):
     print("Number of tokens for player ", player1Name," ","'",player1,"'"," : ", countToken(board, player1))
     print("Number of tokens for player ", player2Name," ","'",player2,"'", " : ",countToken(board, player2))

def saveGame(board):
  fileName = input("Give the name for the game to save : ")
  fileName +=".txt"
  fileOpen = open(fileName, 'w')

  for row in range(len(board)):
    for col in range(len(board[row])):
      if(board[row][col]!="\n"):
        fileOpen.write(board[row][col])
        fileOpen.write(",")
    fileOpen.write("\n")
  fileOpen.close()

def restoreGame():
  fileName = input("Type the file name of the game to restore : ")
  fileName +=".txt"
  fileOpen = open(fileName, 'r')
  read = fileOpen.readlines()
  board=[]
  for i in read:
    x=i.split(',')
    board.append(x)
  return board


def checkWinner(board, player1, player2, player1Name, player2Name):
  won=False
  x = checkSpaceBalance(board)
  #print(x)
  p1=0
  p2=0
  if (x<8):
    p1= countToken(board, player1)
    p2= countToken(board, player2)
    #print(p1)
    #print(p2)
    if (p1>p2):
      print(player1Name, " won\n\n")
    else:
      print(player2Name, " won\n\n")
    won=True
  return won


def playGameMenu (board,cont,won):
        player1Name = input("Insert the first player name : ")
        player2Name = input("Insert the second player name : ")
        print("Hi ", player1Name, " your are ", "'",player1, "'")
        print("Hi ", player2Name, " your are ", player2)
        print("\nLet's play!\n")
        printBoard(board)
        print()

        move = checkSpaceToMove(board) #return true or false
        turn = 1 #1 or 2 : player 1 or player 2
        while (move):
          if (turn%2!=0):
            print(player1Name," turn, please select one number from the board : ")
            select = input()

            if (not select.isdigit()):
              move=False
              cont=False
              save=input("Do you want to save the current game? ('Y' or 'N')")
              if (save=="Y" or save=="y"):
                os.system('clear')
                saveGame(board)
                print("The game has been saved into a txt file\n\n")
                cont=False
              break
            else:
              select = int(select)

            print(player1Name, " has selected ", select)
            os.system('clear')

            validMove = checkValidSpace(board, select)
            while(not validMove):
              print(select, " is not a valid space to move!")
              printBoard(board)
              select = int(input("Select again : "))
              validMove = checkValidSpace(board, select)
            Move(board, select, player1)
            displayTokenInfo (board,player1Name, player2Name)

          else:
            print(player2Name," turn, please select one number from the board : ")
            select = input()

            if (not select.isdigit()):
              move=False
              cont=False
              save=input("Do you want to save the current game? ('Y' or 'N')")
              if (save=="Y" or save=="y"):
                os.system('clear')
                saveGame(board)
                print("The game has been saved into a txt file\n\n")
                cont=False
              break
            else:
              select = int(select)
              os.system('clear')

            print(player2Name, " has selected ", select)
            validMove = checkValidSpace(board, select)
            while(not validMove):
              print(select, " is not a valid space to move!")
              printBoard(board)
              select = int(input("Select again : "))
              validMove = checkValidSpace(board, select)
            Move(board, select, player2)
            displayTokenInfo (board, player1Name, player2Name)


          printBoard(board)
          turn+=1
          move = checkSpaceToMove(board)
          print("No of space balance : ", checkSpaceBalance(board))
          print("Press q or Q to quit from the current game")
          won = checkWinner(board, player1, player2, player1Name, player2Name)
          if(won):
            break


def main():
  game = True
  won = False
  while (game):
    print(menu)
    cont = True
    userMenu = (input("Select a number from the menu : "))
    while(not userMenu.isdigit()):
      os.system('clear')
      print("Invalid number!\n\n")
      print(menu)
      userMenu = (input("Select a number from the menu : "))
    userMenu = int(userMenu)
    board = drawBoard()
    setOthello(board)

    while (cont):

      if (userMenu==2):
        os.system('clear')
        print("::You have selected storing a game to play::\n\n")
        board=restoreGame()
        playGameMenu (board, cont,won)
        break
      elif(userMenu==1):
        os.system('clear')
        print("::A new Game::")
        player1Name = input("Insert the first player name : ")
        player2Name = input("Insert the second player name : ")
        print("Hi ", player1Name, " your are ", "'",player1, "'")
        print("Hi ", player2Name, " your are ", player2)
        print("\nLet's play!\n")
        printBoard(board)
        print()

        move = checkSpaceToMove(board) #return true or false
        turn = 1 #1 or 2 : player 1 or player 2
        while (move):
          if (turn%2!=0):
            print(player1Name," turn, please select one number from the board : ")
            select = input()

            if (not select.isdigit()):
              move=False
              cont=False
              save=input("Do you want to save the current game? ('Y' or 'N')")
              if (save=="Y" or save=="y"):
                os.system('clear')
                saveGame(board)
                print("The game has been saved into a txt file\n\n")
              break
            else:
              select = int(select)

            print(player1Name, " has selected ", select)
            os.system('clear')

            validMove = checkValidSpace(board, select)
            while(not validMove):
              print(select, " is not a valid space to move!")
              printBoard(board)
              select = int(input("Select again : "))
              validMove = checkValidSpace(board, select)
            Move(board, select, player1)
            displayTokenInfo (board,player1Name, player2Name)

          else:
            print(player2Name," turn, please select one number from the board : ")
            select = input()

            if (not select.isdigit()):
              move=False
              cont=False
              save=input("Do you want to save the current game? ('Y' or 'N')")
              if (save=="Y" or save=="y"):
                os.system('clear')
                saveGame(board)
                print("The game has been saved into a txt file\n\n")

              break
            else:
              select = int(select)
              os.system('clear')

            print(player2Name, " has selected ", select)
            validMove = checkValidSpace(board, select)
            while(not validMove):
              print(select, " is not a valid space to move!")
              printBoard(board)
              select = int(input("Select again : "))
              validMove = checkValidSpace(board, select)
            Move(board, select, player2)
            displayTokenInfo (board, player1Name, player2Name)

          printBoard(board)
          turn+=1
          move = checkSpaceToMove(board)
          print("No of space balance : ", checkSpaceBalance(board))
          print("Press q or Q to quit from the current game")
          won = checkWinner(board, player1, player2, player1Name, player2Name)
          if(won):
            break

      elif(userMenu==3):
        print("Bye! See you again.")
        cont=False
        game = False
      else:
        userMenu = int(input("Invalid range! Select a number from the menu : "))

main()
