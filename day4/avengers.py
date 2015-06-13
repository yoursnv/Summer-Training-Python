class Avenger:
	avengersCount = 0

	def __init__(self, name, power):
		Avenger.avengersCount += 1
		self.name = name
		self.power = power

	def howMany():
		print("Total  Avengers %d" % Avenger.avengersCount)

	def getName(self):
		print("Avengers name: " + self.name+ " have power " + self.power)


hulk = Avenger("Hulk","Angry")
print(hulk.name)
print(hulk.power)

print("AvengersCount: ", Avenger.avengersCount)
Avenger.howMany()
hulk.getName()

print("****************************************")

Ironman = Avenger("Ironman","jarvis")
print(Ironman.name)
print(Ironman.power)

print("AvengersCount: ", Avenger.avengersCount)
Avenger.howMany()
Ironman.getName()

print("****************************************")

Thor = Avenger("Thor","Thunder Hammer")
print(Thor.name)
print(Thor.power)

print("AvengersCount: ", Avenger.avengersCount)
Avenger.howMany()
Thor.getName()

del hulk.power

print(hulk.name)

x = getattr(hulk, 'name')
print(x)
print(setattr(hulk,"name", "BigHulk"))
print(hulk.name)