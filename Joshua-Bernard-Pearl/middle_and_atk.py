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

class Player:
	def __init__(self):
		self.name = Jose
		self.stre = 5
		self.weapn_name = "sword"
		self.weapon = 5
		self.defe = 5
		self.spd = 4
		self.hp = 10
class Blob:
	def __init__(self):
		self.name = "Blob"
		self.stre = random.randint(3,5)
		self.weapon_name = "body"
		self.weapon = 1
		self.defe = random.randint(3,5)
		self.spd = random.randint(1,2)
		self.hp = 10
class Custom_Enemy:
	def __init__(self,name,level,stre,weapon_name,weapon,defe,spd,hp):
		self.name = name
		self.level = level
		self.stre = stre
		self.weapon_name = weapon_name
		self.weapon = weapon
		self.defe = defe
		self.spd = spd
		self.hp = hp


# def dam_value(x,y):
# 	print()
# 	return y.hp-(x.stre*x.weapon//y.defe)


def combat(x,y):
	print(x.name+":\nStrength: "+x.stre+"\nWeapon: "+x.weapon_name+"("+x.weapon+")\nDefence: "+x.defe+"\nSpeed: "+x.spd+"HP: "+x.hp)
	print(y.name+":\nStrength: "+y.stre+"\nWeapon: "+y.weapon_name+"("+y.weapon+")\nDefence: "+y.defe+"\nSpeed: "+y.spd+"HP: "+y.hp)
	answer = input("Type atk to atack\nType run to try and run away")
	if answer == "atk":
		if x.spd > y.spd:
		print("oponent HP = "+str(y.hp-(x.stre*x.weapon//y.defe))
		print("Your HP = "+str(x.hp-(y.stre*y.weapon//x.defe))
		else:
		print("Your HP = "+str(x.hp-(y.stre*y.weapon//x.defe))
		print("oponent HP = "+str(y.hp-(x.stre*x.weapon//y.defe))


jose = Player()

blob = Blob()

combat(jose,blob)

