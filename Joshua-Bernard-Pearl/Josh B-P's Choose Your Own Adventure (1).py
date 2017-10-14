'''import random
health = 100
items = []
print (items)
print("health = " + str(health))
print("You walk into a forest")

q = "do you like cheese: A) Yes B) No C) Maybe D) So"
o = ["yes","no","maybe","so"]

def play(question,option):
	answer = input(question)
	if answer == "A" or "a":
		return options[0]
play(q,o)'''



'''def  add(x,y):
	return x + y
def subtract(x,y):
	return x - y
def multiply(x,y):
	return x * y
def divide(x,y):
	return x / y
def calc(function,x,y):
	return function(x,y)
print(calc(add,1,2))

number = 4

def thing():
	global number
	number = number + 1
	return number ** 2
print(thing())'''




# 	"""answer = input("A wild boar appears what will you do:\nA)Run\nB)Climb A Tree\nC)Fight With A Stick\nD)Hide And Hope It Doesn't Notice You\n\nPress I for items")
# 	if answer == "A" or "a":
# 		print("You Try To Run")
# 		chance = random.randrange(1, 10)
# 		if chance <= 3:
# 			print("You Escape")
# 		else:	
# 			print("You Fail And The Boar Charges Into You")
# 			health -= 10
# 			print("health = " + str(health))
# 	elif answer == "B" or "b":
# 		print("You Try To Climb The Tree But Fail")
# 	elif answer == "C" or "c":
# 		print("You Try To Fight It With A Stick")
# 	elif answer == "D" or "d":
# 		print("You Try To Hide")
# 	elif answer == "I" or "i":
# 		print(items)
# 		play()

# play()



# i = 0
# while i > -1:
# 	i += 1

import random
class Question():
	def __init__(self,question,choices):
		self.question = question
	def get_question(self):
		return self.question

def probability(x):
	def chance():
		if random.randint(1,100) <= x:
			return True
		else:
		return False
	return chance

query = Question("You wake up in a forest and see a wiled boar charging toward you\n a)run\n b)fight\nwhat will you do:")		
print(query.get_question())


# health = 100
# for i in range(50):
# 	print()


# def rand_function(gain,loss,succeed,fail,probability):
# 	global health
# 	if random.randint(1,100) <= probability:
# 		health += gain
# 		print(succeed)
# 		return questionrunW
# 	else:
# 		health -= loss
# 		print(fail)
# 		return questionrunL


# questionrunL = ["you are now on the ground again and the boar is standing over you"]
# questionrunW = ["you escape from the boar and stop at a river\n a)follow the river upstream\n b)follow the river downstream\n c)cross the river tand keep exploring\nwhat will you do:",{"a":"option 1","b":"option 2","c":"option 3"}]
# question1 = ["You wake up in a forest and see a wiled boar charging toward you\n a)run\n b)climb a tree\n c)pick up a branch and try to fight\n d)stay still and hope it doesn't notice you\nwhat will you do:",{"a":rand_function(0,10,"you outran the boar","the caught up to you and trampled you",70),"b":"option 2","c":"option 3","d":"option 4"}]

# gameon = True
# question = question1
# while gameon:
# 	answer = input(question[0])
# 	question = question[1][answer]
# 	print("\nhealth=" + str(health))
# 	print()

# blob = []
# blob.append("tree")