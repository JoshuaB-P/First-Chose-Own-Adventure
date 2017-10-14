
# def middle(x,y,z):
# 	nums = [x,y,z]
# 	list.sort(nums)
# 	return nums.pop(1)



# print(middle(4,7882634,904))


# def cows(a,b,c):
# 	if b >= a and b <= c:
# 		return b
# 	if c >= a and c <= b:
# 		return c
# 	if c >= b and c <= a:
# 		return c
# 	if a >= b and a <= c:
# 		return a
# 	if a >= c and a <= b:
# 		return a
# 	if b >= c and b <= a:
# 		return b


# print(cows(345,23145237,76769))

# def tim(x,y,z):
# 	return x + y + z -min(x,y,z) -max(x,y,z)
# print(tim(342,9,47))

import random

class otha:
	stre = 5
	weapon = 5
	defe = 5
	spd = 4
	hp = 10
class blob:
	__init__():
		self.stre = random.randint(3,5)
		self.weapon = 1
		self.defe = random.randint(3,5)
		self.spd = random.randint(1,2)
		self.hp = 10



# def dam_value(x,y):
# 	print()
# 	return y.hp-(x.stre*x.weapon//y.defe)


def combat(x,y):
	answer = input("Type atk to atack\nType run to try and run away")
	if answer == "atk":
		print("oponent HP = "hp-(x.stre*x.weapon//y.defe)

