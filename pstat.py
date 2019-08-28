'''
Player stats - pstat.py

This is a test script to create a dictionary
including RPG like stats for a text game.

Of course, this game needs to have magic in it.
So here we go.
'''

status = {
'name':'Hero'
,'Class':'None'
,'LVL': 1
,'HP':100
,'ST':100
,'MP':100
,'EXP':0
,'NLV':100
,'STR':1
,'DXT':1
,'END':1
,'INT':1 
,'WIS':1
,'CHA':1
,'LCK':1
,'ATR':0
}

def rstatus():
	print("================Status======================")
	print("| Name: " + str(status['name']))
	print("| Class: " + str(status['Class']))
	print("| LVL: " + str(status['LVL']))
	print("| EXP: " + str(status['EXP'])+"/"+str(status['NLV']))
	print("|  HP: " + str(status['HP']))
	print("|  MP: " + str(status['MP']))
	print("|  ST: " + str(status['ST']))
	print("============================================")

'''
rstatus()
'''




'''
print("Welcome, adventurer!")
time.sleep(1)
print("I am Kagemoto, the god of this realm.")
time.sleep(1)
print("You have been summoned here from another world, because"\
	" the demon lord is about to be born.")
time.sleep(3)
print("You must go to the land of demons to put a stop to it before it becomes too late.")
time.sleep(1)

ans = 0

while ans != "y":
	print("\n\nNow then, hero, what is your name?")
	time.sleep(1)
	print("Name: ",end="")
	a = str(input())
	status['Name'] = a
	print("Aha, I see! So your name is " + status['Name'] + "?")
	time.sleep(1)
	print("\nYes(y) No(n)")
	ans = str(input())
	if ans == "y":
		time.sleep(1)
		print("Welcome, " + status['Name'] + ", Traveller of Worlds!")
		time.sleep(1)
		print("Your adventure has only just begun!")
	else:
		print("Aha, I see, I was mistaken then.")
'''

