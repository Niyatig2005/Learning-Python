# Key notes for future me
Originally written on obsidian, so excuse any formatting errors!
### Classes:
- Encapsulate functionality to be used as complete modules
```
class Vehicle():
	def __init__(self, bodystyle): #to initialise, self is to refer to itself
		`sel.bodystyle = bodystyle`
class Car(Vehicle):
	def __init__(self, enginetype):
		super().__init__("Car")
		self.wheels = 4
		self.doors = 4
		self.enginetype = enginetype
class Motercycle(Vehicle):
	def __init__(self, enginetype, hassidecar):
		super().__init__("Motercycle")
		if (hassidecar):
			self.wheels = 3
		else:
			self.wheels = 2
		self.doors = 0
		self.enginetype = enginetype
  ```
- Now to create the things:
```
car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)
```
- So now
```
print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)
```
- The outputs would be:
	- 3
	- gas
	- 4
- Classes don't only told data, they can also hold functions (attributes and methods):
```
class Vehicle():
	def __init__(self, bodystyle): #to initialise, self is to refer to itself
		self.bodystyle = bodystyle
	def drive(self, speed):
		self.mode = "driving"
		self.speed = speed
  class Car(Vehicle):
	def __init__(self, enginetype):
		super().__init__("Car")
		self.wheels = 4
		self.doors = 4
		self.enginetype = enginetype
	def drive(self, speed):
		super().drive(speed)
		print("driving my", self.enginetype, "car at", self.speed)
		
class Motercycle(Vehicle):
	def __init__(self, enginetype, hassidecar):
		super().__init__("Motercycle")
		if (hassidecar):
			self.wheels = 3
		else:
			`self.wheels = 2
		self.doors = 0
		self.enginetype = enginetype
	def drive(self, speed):
		super().drive(speed)
		print("driving my", self.enginetype, "Motorcycle at", self.speed)
car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)
```
- then if we add:
```
car1.drive(30)
car2.drive(40)
mc1.drive(50)
```
- We get:
	- 3
	- gas
	- 4
	- Driving my gas car at 30
	- Driving my electric car at 40
	- Driving my gas motorcycle at 50

### Exceptions:
- in general
```
	try:
		x = 10/0 #where potential trouble making code goes
	except:
		print("Well that didn't work") #togo instrction in case "try" fails
```
- `finally` for code that always runs when tried at all
### Working with Files:
- To open/create: `myfile = open("textfile.txt", "w+")`
- To write: `myfile.write("Text")`
- To close: `myfile.close()`
- To append text at end of file: `myfile = open("textfile.txt", "a+")`
- To read: `myfile = open("textfile.txt", "r")`
		` if myfile.mode = 'r':`
			`contents = myfile.read()`
			`print(contents)`
