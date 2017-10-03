#NAME: AMAN REHMAN
#SECTION A
#ROLL NO.: 2017278
#Assignment-2, Game Tic-tac-toe
#State: Tiles are numbered 1 to 9
"""
Tick-Tac-Toe game state is defined as follows: 

tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______
A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.

We will estimate probability of winning for a player for different scenarios.
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
"""
import random
from math import *
# There are 9 tiles numbered tile0 to tile9
tile1= 0
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0
tile9= 0
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2

def validmove(move):
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9

	""" Checks whether a move played by a player is valid or invalid.
		Return True if move is valid. 
		A move is valid if the corresponding tile for the move is not ticked.
	"""
	#move is an int value, 1<=move<=9 denoting which tile is being marked.
	if move==1:
		if(tile1!=0):
			return False

		else:
			return True

	elif move==2:
		if(tile2!=0):
			return False

		else:
			return True

	elif move==3:
		if(tile3!=0):
			return False

		else:
			return True

	elif move==4:
		if(tile4!=0):
			return False

		else:
			return True

	elif move==5:
		if(tile5!=0):
			return False

		else:
			return True

	elif move==6:
		if(tile6!=0):
			return False

		else:
			return True

	elif move==7:
		if(tile7!=0):
			return False

		else:
			return True

	elif move==8:
		if(tile8!=0):
			return False

		else:
			return True

	elif move==9:
		if(tile9!=0):
			return False

		else:
			return True

def win():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9
	""" 
	Returns True if the board state specifies a winning state for some player.
 		A player wins if ticks made by the player are present either
 		i) in a row
 		ii) in a column
 		iii) in a diagonal
	"""
	# checks for 3 1s in a row anywhere in the grid. All combinations are present.
	if((tile1==tile2==tile3==1) or (tile4==tile5==tile6==1) or (tile7==tile8==tile9==1) or (tile1==tile4==tile7==1) or (tile2==tile5==tile8==1) or (tile3==tile6==tile9==1) or (tile1==tile5==tile9==1) or (tile3==tile5==tile7==1)):
		return True					#returns true is p1 wins

	else:
		return False

def P2win():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9

	# checks for 3 2s in a row anywhere in the grid. All combinations are present.
	if((tile1==tile2==tile3==2) or (tile4==tile5==tile6==2) or (tile7==tile8==tile9==2) or (tile1==tile4==tile7==2) or (tile2==tile5==tile8==2) or (tile3==tile6==tile9==2) or (tile1==tile5==tile9==2) or (tile3==tile5==tile7==2)):
		return True					#returns true is p2 wins

	else:
		return False

def takeNaiveMove():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9

	""" Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.    
	"""
	valid=False
	while(valid==False):
		tile=random.randint(1,9)
		valid=validmove(tile)		#check if the move naive player is about to take is valid or not,i.e, if that tile is marked already

		if(valid==True):			#if tile is unmarked
			return tile
			break

def takeStrategicMove():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9

	""" Returns a tile number from the set of unchecked tilescusing some rules.
	"""
	if((tile1==tile2==1 or tile1==tile2==2) and validmove(3)==True):	#check if p1/p2 have 2 consecutive tiles,one may win,block winning mark	
		return 3														#blocks winning move after checking if third tile is a valid move.

	if((tile2==tile3==1 or tile2==tile3==2) and validmove(1)==True):
		return 1

	if((tile1==tile3==1 or tile1==tile3==2) and validmove(2)==True):
		return 2

	if((tile4==tile5==1 or tile4==tile5==2) and validmove(6)==True):
		return 6

	if((tile5==tile6==1 or tile5==tile6==2) and validmove(4)==True):
		return 4

	if((tile4==tile6==1 or tile4==tile6==2) and validmove(5)==True):
		return 5

	if((tile7==tile8==1 or tile7==tile8==2) and validmove(9)==True):
		return 9

	if((tile8==tile9==1 or tile8==tile9==2) and validmove(7)==True):
		return 7

	if((tile7==tile9==1 or tile7==tile9==2) and validmove(8)==True):
		return 8

	if((tile1==tile7==1 or tile1==tile7==2) and validmove(4)==True):
		return 4
	
	if((tile4==tile7==1 or tile4==tile7==2) and validmove(1)==True):
		return 1

	if((tile1==tile4==1 or tile1==tile4==2) and validmove(7)==True):
		return 7

	if((tile3==tile9==1 or tile3==tile9==2) and validmove(6)==True):
		return 6

	if((tile3==tile6==1 or tile3==tile6==2) and validmove(9)==True):
		return 9

	if((tile6==tile9==1 or tile6==tile9==2) and validmove(3)==True):
		return 3

	if((tile2==tile8==1 or tile2==tile8==2) and validmove(5)==True):
		return 5

	if((tile2==tile5==1 or tile2==tile5==2) and validmove(8)==True):
		return 8

	if((tile5==tile8==1 or tile5==tile8==2) and validmove(2)==True):
		return 2	

	if((tile1==tile5==1 or tile1==tile5==2) and validmove(9)==True):							#diagonal check for consecutive 1s/2s
		return 9

	if((tile1==tile9==1 or tile1==tile9==2) and validmove(5)==True):							#diagonal check for consecutive 1s/2s
		return 5

	if((tile9==tile5==1 or tile9==tile5==2) and validmove(1)==True):							#diagonal check for consecutive 1s/2s
		return 1			

	if((tile3==tile5==1 or tile3==tile5==2) and validmove(7)==True):							#diagonal check for consecutive 1s/2s
		return 7

	if((tile3==tile7==1 or tile3==tile7==2) and validmove(5)==True):							#diagonal check for consecutive 1s/2s
		return 5

	if((tile5==tile7==1 or tile5==tile7==2) and validmove(3)==True):							#diagonal check for consecutive 1s/2s
		return 3

								#here the intelligent one now thinks about his own moves
	if(validmove(5)==True):
		return 5

	if(validmove(5)==False):
		#marking the tile according to the random returned
		next=random.choice('1379')										#returns random - 1 or 3 or 7 or 9,corners
		if(next=='1' and validmove(1)):
			return 1

		if(next=='3' and validmove(3)):
			return 3

		if(next=='7'  and validmove(7)):
			return 7

		if(next=='9' and validmove(9)):
			return 9

		next=random.choice('2468')										#returns random - 2 or 4 or 6 or 8,corners
		if(next=='2' and validmove(2)):
			return 2

		if(next=='4' and validmove(4)):
			return 4

		if(next=='6' and validmove(4)):
			return 6

		if(next=='8' and validmove(8)):
			return 8		

	if(tile1==2 or tile3==2 or tile7==2 or tile9==2):					#third move(making L shape)
		if(tile1==2):
			next=random.choice('24')
			if(next=='2' and validmove(2)):
				return 2

			if((next=='4') and validmove(4)):
				return 4

		if(tile3==2): 
			next=random.choice('26')
			if(next=='2' and validmove(2)):
				return 2

			if((next=='6') and validmove(6)):
				return 6

		if(tile7==2):
			next=random.choice('48')
			if(next=='4' and validmove(4)):
				return 4

			if((next=='8') and validmove(8)):
				return 8

		if(tile9==2):
			next=random.choice('68')
			if(next=='6' and validmove(6)):
				return 6

			if((next=='8') and validmove(8)):
				return 8

	if(tile1==1 or tile3==1 or tile7==1 or tile9==1):			#second move(after the corners are marked)
		if(tile1==1):
			next=random.choice('24')
			if(next=='2' and validmove(2)):
				return 2

			if((next=='4') and validmove(4)):
				return 4

		if(tile3==1):
			next=random.choice('26')
			if(next=='2' and validmove(2)):
				return 2

			if((next=='6') and validmove(6)):
				return 6

		if(tile7==1):
			next=random.choice('48')
			if(next=='4' and validmove(4)):
				return 4

			if((next=='8') and validmove(8)):
				return 8

		if(tile9==1):
			next=random.choice('68')
			if(next=='6' and validmove(6)):
				return 6

			if((next=='8') and validmove(8)):
				return 8

def validBoard():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9
	""" Return True if board state is valid.
		A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
	"""
	states=''
	states=str(tile1)+str(tile2)+str(tile3)+str(tile4)+str(tile5)+str(tile6)+str(tile7)+str(tile8)+str(tile9) #store all tile states in a string
	p1=states.count('1')
	p2=states.count('2')

	if(abs(p1-p2)>=2):				#moves of both of them should be equal or one can be exactly one move ahead, difference will be 0 or 1
		return False

	else:
		return True

def game(gametype=1):
	""" Returns 1 if player1 wins and 2 if player2 wins
		and 0 if it is a draw.
		gametype defines three types of games discussed above.
		i.e., game1, game2, game3
	"""
	pass

def checkfullboard():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9

	record=str(tile1)+str(tile2)+str(tile3)+str(tile4)+str(tile5)+str(tile6)+str(tile7)+str(tile8)+str(tile9)
	if('0' in record):
		return False

	else:
		return True

def resetboard():
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9

	tile1=0
	tile2=0
	tile3=0
	tile4=0
	tile5=0
	tile6=0
	tile7=0
	tile8=0
	tile9=0

def game1(n):
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9

	""" Returns the winning probability for player1.
	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	count_win=0
	for i in range(n):
		while(checkfullboard()==False or win()==False):
			P1=takeNaiveMove()
			if(P1==1):
				tile1=1

			elif(P1==2):
				tile2=1

			elif(P1==3):
				tile3=1

			elif(P1==4):
				tile4=1

			elif(P1==5):
				tile5=1

			elif(P1==6):
				tile6=1

			elif(P1==7):
				tile7=1

			elif(P1==8):
				tile8=1

			else:
				tile9=1

			if(win()==True or checkfullboard()==True):
				break

			P2=takeNaiveMove()
			if(P2==1):
				tile1=2

			elif(P2==2):
				tile2=2

			elif(P2==3):
				tile3=2

			elif(P2==4):
				tile4=2

			elif(P2==5):
				tile5=2

			elif(P2==6):
				tile6=2

			elif(P2==7):
				tile7=2

			elif(P2==8):
				tile8=2

			else:
				tile9=2

			if(P2win()==True or checkfullboard()==True):
				break

		P1win=win()
		if(P1win==True):
			count_win+=1

		resetboard()
	probability=count_win/n
	return probability

def game2(n):
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9
	"""Returns the winning probability for player1.
	n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
	"""
	count_win=0
	for i in range(n):
		while(checkfullboard()==False or win()==False):
			P1=takeNaiveMove()
			if(P1==1):
				tile1=1

			elif(P1==2):
				tile2=1

			elif(P1==3):
				tile3=1

			elif(P1==4):
				tile4=1

			elif(P1==5):
				tile5=1

			elif(P1==6):
				tile6=1

			elif(P1==7):
				tile7=1

			elif(P1==8):
				tile8=1

			else:
				tile9=1

			if(win()==True or checkfullboard()==True):
				break

			P2=takeStrategicMove()
			if(P2==1):
				tile1=2

			elif(P2==2):
				tile2=2

			elif(P2==3):
				tile3=2

			elif(P2==4):
				tile4=2

			elif(P2==5):
				tile5=2

			elif(P2==6):
				tile6=2

			elif(P2==7):
				tile7=2

			elif(P2==8):
				tile8=2

			else:
				tile9=2

			if(P2win()==True or checkfullboard()==True):
				break

		P1win=win()
		if(P1win==True):
			count_win+=1

		resetboard()
	probability=count_win/n
	return probability

def game3(n):
	global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9
	"""Returns the winning probability for player1. 
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	count_win=0
	for i in range(n):
		while (checkfullboard()==False or win()==False):
			P1=None
			while(P1==None):
				P1=takeStrategicMove()

			if(P1==1):
				tile1=1

			elif(P1==2):
				tile2=1

			elif(P1==3):
				tile3=1

			elif(P1==4):
				tile4=1

			elif(P1==5):
				tile5=1

			elif(P1==6):
				tile6=1

			elif(P1==7):
				tile7=1

			elif(P1==8):
				tile8=1

			elif(P1==9):
				tile9=1

			if(win()==True or checkfullboard()==True):
				break

			P2=None
			while(P2==None):
				P2=takeStrategicMove()

			if(P2==1):
				tile1=2

			elif(P2==2):
				tile2=2

			elif(P2==3):
				tile3=2

			elif(P2==4):
				tile4=2

			elif(P2==5):
				tile5=2

			elif(P2==6):
				tile6=2

			elif(P2==7):
				tile7=2

			elif(P2==8):
				tile8=2

			elif(P2==9):
				tile9=2

			if(P2win()==True or checkfullboard()==True):
				break

		P1win=win()
		if(P1win==True):
			count_win+=1

		resetboard()
	probability=count_win/n
	return probability