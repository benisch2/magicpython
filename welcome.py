'''
Welcome.py
Start of the game
'''
#standard libraries
import time

#custom library
import pstat


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
	status['name'] = a
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

rstatus()
