#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172

from pikachu import Pikachu
from dragon import Dragon
from kehwany import Kehwany
from keswani import Keswani

import random

#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

	#first reset everyone's health!
	m1.resetHealth()
	m2.resetHealth()

	#next print out who is battling
	print("\n-----------------------------------------------------\nStarting Battle Between")
	print('\t' + m1.getName()+": "+m1.getDescription())
	print('\t' + m2.getName()+": "+m2.getDescription())
	
	#Whose turn is it?
	attacker = None
	defender = None
	
	#Select Randomly whether m1 or m2 is the initial attacker
	#to other is the initial definder
	randNum = random.randint(0, 1)
	if(randNum == 0):
		attacker = m1
		defender = m2
	elif(randNum == 1):
		attacker = m2
		defender = m1
	
	
	print('\n' + attacker.getName()+" goes first.\n")
	#Loop until either 1 is unconscious or timeout
	while( m1.getHealth() > 0 and m2.getHealth() > 0):
		#Determine what move the monster makes
		#Probabilities:
		#	60% chance of standard attack
		#	20% chance of defense move
		#	20% chance of special attack move

		#Pick a number between 1 and 100
		move = random.randint(1,100)
		#It will be nice for output to record the damage done
		#before_health = defender.getHealth()
		
		#for each of these options, apply the appropriate attack and 
		#print out who did what attack on whom
		if( move >=1 and move <= 60):
			#Attacker uses basic attack on defender
			print('\nBASIC ATTACK: ' + attacker.getName() + ' used a basic attack: ' + attacker.basicName() + ' on ' + defender.getName())
			attacker.basicAttack(defender)
		elif move>=61 and move <= 80:
			#Defend!
			print('\nDEFEND: ' + attacker.getName() + ' used a used a defense attack: ' + attacker.defenseName() + ' on ' + defender.getName())
			attacker.defenseAttack(defender)
		else:
			#Special Attack!
			print('\nSPECIAL ATTACK: ' + attacker.getName() + ' used a used a special attack: ' + attacker.specialName() + ' on ' + defender.getName())
			attacker.specialAttack(defender)
		
		#Swap attacker and defender
		temp = attacker
		attacker = defender
		defender = temp
		
		#Print the names and healths after this round
		print(m1.getName() + "'s health (" + str(m1.getHealth()) + ")")
		print(m2.getName() + "'s health (" + str(m2.getHealth()) + ")")
		
	#Return who won
	
	if(m1.getHealth() > 0):
		print('\nRound Winner: ' + m1.getName())
		return m1
	else:
		print('\nRound Winner: ' + m2.getName())
		return m2

#----------------------------------------------------
if __name__=="__main__":
	#Every battle should be different, so we need to
	#start the random number generator somewhere "random".
	#With no input Python will set the seed
	
	random.seed(1)
	
	first = Pikachu()
	second = Dragon()

	third = Keswani()
	fourth = Kehwany()
	
	round1_winner = monster_battle(first,second)
	round2_winner = monster_battle(third, fourth)

	final_winner = monster_battle(round1_winner, round2_winner)
	
	print(final_winner.getName() + ' won all of the monster battles!!')

	