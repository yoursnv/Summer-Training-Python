class Food:
	dishCount = 0

	def __init__(self, name, flavor):
		Food.dishCount += 1
		self.name = name
		self.flavor = flavor

	def howMany():
		print("Total Dishes %d" % Food.dishCount)

	def getName(self):
		print("Dish name: " + self.name+ " have flavors of " + self.flavor)


burgur = Food("Burgur","Chicken")
print(burgur.name)
print(burgur.flavor)

print("dishCount: ", Food.dishCount)
burgur.getName()

print("****************************************")
pizza = Food("Burgur","Vegetables")
print(pizza.name)
print(pizza.flavor)

print("dishCount: ", Food.dishCount)
pizza.getName()

print("****************************************")
