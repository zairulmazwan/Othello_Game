menu = ":::Welcome to Othello Game:::\n=============================\n1. New Game - Play with computer\n2. New Game - 2 Players\n3. Quit\n\n"


print(menu)
player1 = "  "
player2 = "@@"


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
        board[i][j]=str("  ")
      elif (i==3 and j == 4):
       board[i][j]=str("@@")
      elif (i==4 and j == 3):
       board[i][j]=str("@@")
      elif (i==4 and j == 4):
       board[i][j]=str("  ")
  return board


def printBoard(board):
  for i in range(len(board)):
    print(" ----"*len(board))
    print("|", end=" ")
    for j in range(len(board)):
      print(board[i][j], "|", end = " ")
    print()
  print(" ----"*len(board))


def validNumber(board, row, col):
  valid=True

  if (board[row][col]=="  " or board[row][col]=="@@"):
    valid=False
  return valid


def validateMove(board, userChoice, player):
 print("Player pattern : ", player)
 valid = False
 row=-1
 col=-1

 #check whether the place has been chosen
 if (board[row][col]=="  " or board[row][col]=="@@"):
    valid=False

 if (userChoice%len(board)==0):
   row = (userChoice//len(board))-1
   col = (userChoice%len(board))-1
   board[row][col] = player
 else:
   row = userChoice//len(board)
   col = (userChoice%len(board))-1
   board[row][col] = player

 playerOpposite=""
 if (player=="@@"):
   playerOpposite="  "
   print("this")
 else:
    playerOpposite="@@"
    print("this b")

 print("player opposite pattern : ", playerOpposite)
 #west
 if (board[row][col-1]==playerOpposite):
   print("west")
   index=(col-1)
   while(index>0):
     index-=1
     if (board[row][index]==player):
       valid=True

   if(valid):
     while(col>0):
      col-=1
      if (board[row][col]==playerOpposite):
        board[row][col]=player


 #northwest
 if (board[row-1][col-1]==playerOpposite):
   print("northwest")
   indexRow=(row-1)
   indexCol=(col-1)
   while(indexRow>1 or indexCol>1):
     indexRow-=1
     indexCol-=1
     if (board[indexRow][indexCol]==player):
       valid=True

   if(valid):
     while(row>1 or col>1):
      row-=1
      col-=1
      if (board[row][col]==playerOpposite):
        board[row][col]=player

 #north
 if (board[row-1][col]==playerOpposite):
   print("north")
   indexRow=(row-1)
   while(indexRow>0):
     indexRow-=1
     if (board[indexRow][col]==player):
       valid=True

   if(valid):
     while(row>0):
      row-=1
      if (board[row][col]==playerOpposite):
        board[row][col]=player


 #northeast
 if (board[row-1][col+1]==playerOpposite):
   print("northeast")
   indexRow=(row-1)
   indexCol=(col+1)
   while(indexRow!=1 or indexCol!=len(board)-2):
     indexRow-=1
     indexCol+=1
     if (board[indexRow][indexCol]==player):
       valid=True

   if(valid):
     while(row!=0 or col!=len(board)-1):
      row-=1
      col+=1
      if (board[row][col]==playerOpposite):
        board[row][col]=player

 #east
 if (board[row][col+1]==playerOpposite):
   print("east")
   indexCol=(col+1)
   while(indexCol<len(board)-2):
     indexCol+=1
     print(row, indexCol)
     if (board[row][indexCol]==player):
       valid=True

   if(valid):
     while(col<len(board)-2):
      col+=1
      if (board[row][col]==playerOpposite):
        board[row][col]=player

 #southeast
 if (board[row+1][col+1]==playerOpposite):
    print("southeast")
    indexRow=(row+1)
    indexCol=(col+1)
    while(indexRow<len(board)-2 or indexCol<len(board)-2):
      indexRow+=1
      indexCol+=1
      print(indexRow, indexCol)
      if (board[indexRow][indexCol]==player):
        valid=True

    if(valid):
     while(row<len(board)-2 or col<len(board)-2):
      row+=1
      col+=1
      if (board[row][col]==playerOpposite):
        board[row][col]=player

 #south
 if (board[row+1][col]==playerOpposite):
   print("south")
   indexRow=(row+1)
   while(indexRow<len(board)-1):
     indexRow+=1
     if (board[indexRow][col]==player):
       valid=True

   if(valid):
     while(row<len(board)-2):
      row+=1
      if (board[row][col]==playerOpposite):
        board[row][col]=player

  #southwest
 if (board[row+1][col-1]==playerOpposite):
    print("southwest")
    indexRow=(row+1)
    indexCol=(col-1)
    while(indexRow<len(board)-2 or indexCol>1):
      indexRow+=1
      indexCol-=1
      print(indexRow, indexCol)
      if (board[indexRow][indexCol]==player):
        valid=True

    if(valid):
     while(row<len(board)-2 or col!=0):
      row+=1
      col+=1
      if (board[row][col]==playerOpposite):
        board[row][col]=player

 return valid





def userChoice(board, player):
 usernumber = int(input("Select your choice between 1 and 64:\n"))

 while (usernumber<1 or usernumber>64):
   usernumber = int(input("Outside the range!\nSelect your choice between 1 and 64"))

 validateMove(board, usernumber, player2)
 return board


def flip(board, row, col, player, playerOpposite):
   while(row<len(board)-2 or col!=0):
      row+=1
      col-=1
      if (board[row][col]==playerOpposite):
        board[row][col]=player



board=drawBoard()
#printBoard(board)
setOthello(board)
print()
printBoard(board)

#valid = validateMove(board, 27, player2)
#print(valid)
#printBoard(board)




'''
print("\n\n")
cont = True
userMenu = int(input("Select a number from the menu : "))

while (cont):
  while (userMenu<1 or userMenu>3):
    userMenu = int(input("Invalid range! Select a number from the menu : "))

  if (userMenu==1):
    print("Playing with computer")
  elif(userMenu==2):
    player1Name = input("Insert the first player name : ")
    player2Name = input("Insert the second player name : ")
    print("Hi ", player1Name, " your are ", "'",player1, "'")
    print("Hi ", player2Name, " your are ", player2)
    print("\nLet's play!\n")
    printBoard(board)
    print()



  elif(userMenu==3):
    print("Bye!")
    cont=False
  
  print(menu)
  userMenu = int(input("Select a number from the menu : "))


'''
