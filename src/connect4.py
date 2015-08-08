#Connect 4 Game
#By Ross Meikleham 2011
from Canvas import*
from random import*

#creates 6*7 board using 2 dimensional list
board=['0']*7
for i in range(7):
   board[i]=[0]*6

#stores locations for circles later on
circleProp=['x','y']*7
for i in range(7):
   circleProp[i]=['x','y']*6


   
def create_circle(X,Y,R,fill='white',width=1): #create circle centre X,Y radius R, optional colour
    create_oval(X-R,Y-R,X+R,Y+R,fill=fill,width=2)


def drawboard(startx,starty,endx,endy):
   create_rectangle(startx,starty,endx,endy,fill='cyan',outline='black') 

   #define height and length of board
   length=endx-startx
   height=endy-starty
   
   radius=height*(1.0/14) #radius of each board circle is 1/14 of the height
   spaceY=(height*1.0/7)/7  #space between each board circle as 1-(2*(6/14))=1/7 of the board left for spaces, 7 spaces on a column so 1/49 of the height 
   spaceX=(length*1.0/7)/7
   
   moveX=spaceX+2*radius #get distance to move along each time
   moveY=spaceY+2*radius
   
    #set starting positions to draw circles
   currenty=starty+spaceY+radius
   currentx=startx+spaceX+radius

   #create white circles for blank board
   for i in range(6):
       if i != 0: #not wanting to go 'down' on first ittiration of loop
          currenty+=moveY 
       currentx=startx+spaceX+radius #reset x co-ordinate when going down
       for j in range(7):
           wait(0.05)  
           create_circle(currentx,currenty,radius,width=3)
           circleProp[j][i]=[currentx,currenty] #save location of circle for later use
           currentx+=moveX
           
   return radius


def Update_Score(player,PlayerCount,prevValue,i,j):
    if (board[i][j]==player) and (player!=0):   #if the value in current position is that of the current player
       if prevValue==player:  #if the value in the previous position was the same as one in current then increment players score
          PlayerCount[player]+=1 
       else:
          PlayerCount[player]=1 #if previous position was different score is set to 1, as needs to be 4 in a row
       prevValue=player
    if (board[i][j]==player) and (player==0):
      prevValue=0
    return prevValue


                
def CheckWin():
   PlayerCount=[0,0,0] #position 0 for board, 1 and 2 for players respectively
   i=0;j=0
   prevValue=0 #value of previous position
   #Horizontal Check of rows
   for j in range(6):
      prevValue=0
      for i in range(7):
         if 4 not in PlayerCount: #if a player has won then no point continuing checking
            for player in range(0,3): #check for all players, empty spaces included as a 'player' 
               prevValue=Update_Score(player,PlayerCount,prevValue,i,j)
               
   #Vertical check of columns
                
   prevValue=0
   for i in range(7):
      prevValue=0
      for j in range(6):
         if 4 not in PlayerCount: #if a player has won then no point continuing checking
            for player in range(0,3): #check for all players
               prevValue=Update_Score(player,PlayerCount,prevValue,i,j)
   
   #checking 'left half' of diagonals from bottom left to top right
   i=0
   j=0
   while j<=5:
         k=0
         l=0 #temp variables k and l are needed to move diagonals without losing original place
         prevValue=0
         l=j
         
         while l>=0: #dont want to try access value that's non existant  
               for player in range(0,3): #check for all players
                  if 4 not in PlayerCount: #if a player has won then no point continuing checking    
                     prevValue=Update_Score(player,PlayerCount,prevValue,k,l)
     
            
               k=k+1  #increment k and decrement l to check next diagonal
               l=l-1
         j+=1 #move starting position down
         
   #checking 'right half' of diagonals from bottom left to top right
   i=0
   j=5
   while i<=6:
         k=0
         l=0 #temp variables k and l are needed to move diagonals without losing original place
         prevValue=0
         k=i
         while l>=0: #dont want to try access value that's non existant
                  for player in range(0,3): #check for all players
                      if 4 not in PlayerCount: #if a player has won then no point continuing checking
                         prevValue=Update_Score(player,PlayerCount,prevValue,k,l)
                  k=k+1  #increment both to check next diagonal
                  l=l-1
         i+=1 #move starting position to the right


   #checking 'right half' of diagonals from bottom right to top left
   i=6
   j=0
   while j<=5:
         k=6
         l=j
         prevValue=0
         while l>=0:
               for player in range(0,3): #check for all players
                  if 4 not in PlayerCount: #if a player has won then no point continuing checking
                     prevValue=Update_Score(player,PlayerCount,prevValue,k,l)
               k=k-1
               l=l-1
         j+=1 #move starting position down
         
   #checking 'left half' of diagonals from bottom right to top left
   i=6
   j=5
   while i>=0:
         k=6
         l=0
         prevValue=0
         while l>=0:
            for player in range(0,3):
                    if 4 not in PlayerCount:   
                       prevValue=Update_Score(player,PlayerCount,prevValue,k,l)
            k=k-1
            l=l-1
         i-=1 # move starting position left

   if 4 in PlayerCount: #if score of 4 is calculated then current player who made a move has won
      Win=True
   else:
      Win=False
   return Win      
   

   
def UpdateBoard(i,j): #update the canvas
   global radius,Player,colour,currentplayer
   

   if CheckWin() == False:
      board [i][j] =Player #set the position on board as taken by current playe
      create_circle(circleProp[i][j][0],circleProp[i][j][1],radius,fill=colour)
      if CheckWin() == False:
   
         if Player ==1:      #change the current state of the player
            Player=2
            colour='yellow'     #as well as the colour to use
         else:
            Player=1
            colour='red'
         
         delete(currentplayer)   
         currentplayer=create_text(300,40,text=("Player "+str(Player)+"'s turn"),fill=colour,font="Courier")
   return CheckWin()
   

def Check_Valid_Move(i,j):

   Valid=False
   if board [i][0]==0: #if on top row is empty the move is valid
      Valid=True
      j=5
      while board[i][j] != 0: #obtain the first space in the column (from bottom up) and return row value
         j-=1
         
   return Valid,j


def find(x,y,button):
    global radius,Win
    Found=False
    end=False
    i=-1
    j=0
    while (not end) and (not Found): #while all circles not checked and circle not found
       i+=1
       if i==columns+1: #if end of column, increment row
          i=0
          j+=1
        #testing circle equation of every circle in the board in sequential order with the click location
        #to see if the click satisifes the inequality, if it does then the click is in that circle   
       if (x-circleProp[i][j][0])**2 +(y-circleProp[i][j][1])**2 <=(radius**2):
          Found=True
          Valid,j=Check_Valid_Move(i,j)
          if Valid:
             Win=UpdateBoard(i,j)
             if Win==True:
                print 'Player',Player,'wins'
                unset_mousedown_handler(find)
       if i==columns and j==rows: #all values in board have been checked
          end=True
    return Win
   
 
Player=randint(1,2) #obtain player to start with
if Player==1:
   colour='red'
else:
   colour='yellow'

rows=5
columns=6

create_rectangle(0,0,650,600,fill='black')
create_text(90,20,text='Player 1: Red',fill='red',font="Courier")
create_text(500,20,text='Player 2: Yellow',fill='yellow',font="Courier")
currentplayer=create_text(300,40,text='Player'+str(Player)+"'s turn",fill=colour,font="Courier")
Win=False   
set_size(650,600)
set_title('Connect 4 by Ross Meikleham')
startx=50;starty=100
endy=570 ;endx=(endy-starty+startx)*(7.0/6) #end x is based on proportional size of other dimensions
radius=drawboard(startx,starty,endx,endy) #create the 'board'
set_mousedown_handler(find) #set the mouse handler ready


run()


   
   
   
