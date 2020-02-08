"""Primera linea de comandos"""
bicycles=['trek', 'cannondale', 'redline', 'specialized'] 
print(bicycles)
"""Segunda linea de comandos"""
print('Imprimiendo solo un objeto de la lista: ')
print(bicycles[1])
"""tercera linea de comandos"""
print('usando metodo title en el comando print.')
print(bicycles[0].title())
"""1.2 Ejercicio de Tarea 1 """
names=['Alejandro','Rodolfo','Carlos','Armando','Jafet']
print('Ejercicio 1.2')
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
"""Mensaje por cada persona"""
for name in names:
	print('hola amigo, '+str(name)+'!!!')
"""Lista de deseos"""
wishes=['Terminar mi carrera','Conseguir novia','alcanzar todas mis metas',
	'Mejorar mis calificaciones', 'Conseguir un buen trabajo','Mejorar mi nivel de programacion',
	'Ser el orgullo de mis padres','aprender a andar mejor en moto', 'mejorar mi nivel de ingles',
	'enamorarme de nuevo','ser feliz','viajar por el mundo','comprarme una moto mas grande',
	'ganar un campeonato de Videojuegos','Regresarle todo lo que me han dado mis padres a mis hijos']
print(wishes[4].title())
print(wishes[7].title())
print(wishes[5].title())
'''2 Modificando, Agregando y Removiendo elementos de la lista'''
'''2.1	Modificando los elementos de una lista'''
print('\nParte 1 del ejercicio 2')
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
motorcycles[0] = 'ducati' 
print(motorcycles)
'''2.2	Agregando elementos a la lista'''
print('\nParte 2 del ejercicio 2')
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
motorcycles.append('ducati') 
print(motorcycles)
'''2.3	Insertando elementos a una lista'''
print('\nParte 3 del ejercicio 2')
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
motorcycles.insert(0, 'ducati') 
print(motorcycles)
'''2.4	Removing Elements from a List'''
print('\nParte 4 del ejercicio 2')
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
del motorcycles[0] 
print(motorcycles)
'''3	Funciones'''
'''3.1	Passing Information to a Function'''
print('\nParte 1 del ejercicio 3')
def greet_user():
	"""Dipaly a simple greeting""" 
	print("Hello!")

greet_user()

'''3.1	Passing Information to a Function'''
print('\nParte 2 del ejercicio 3')
def greet_user(username): 
	"""Display a simple greeting.""" 
	print("Hello, " + username.title() + "!") 

greet_user('jessie')
'''3.2	Paso de argumentos'''
print('\nParte 3 del ejercicio 3')
def describe_pet(animal_type, pet_name): 
	"""Display information about a pet.""" 
	print("\nI have a " + animal_type + ".") 
	print("My " + animal_type + "s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry') 
describe_pet('dog', 'willie')
'''En comparacion con el codigo'''
print('\nParte 4 del ejercicio 3')
def describe_pet(animal_type, pet_name): 
	"""Display information about a pet.""" 
	print("\nI have a " + animal_type + ".") 
	print("My " + animal_type + "s name is " + pet_name.title() + ".")
describe_pet('harry', 'hamster')
'''3.2.2	Keword Arguments'''
print('\nParte 5 del ejercicio 3')
def describe_pet(animal_type, pet_name):
	"""Display information about a pet.""" 
	print("\nI have a " + animal_type + ".") 
	print("My " + animal_type + "s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')
'''3.3	Default Values'''
print('\nParte 6 del ejercicio 3')
def describe_pet(pet_name, animal_type='dog'):
 """Display information about a pet.""" 
 print("\nI have a " + animal_type + ".") 
 print("My " + animal_type + "s name is " + pet_name.title() + ".") 
describe_pet(pet_name='willie')
'''3.4	Tarea'''
print('\nTarea 3.4.1')
def make_shirt(size_shirt,message_shirt):
	print("\nhis shirt is: " + size_shirt + ".")
	print('This is the text that will appear on your shirt: '+'"'+message_shirt+'"')
make_shirt(size_shirt='big',message_shirt='IPN')
'''3.4	Tarea'''
print('\nTarea 3.4.2')
def make_shirt(size_shirt='big',message_shirt='I <3 Python'):
	print("\nhis shirt is: " + size_shirt + ".")
	print('This is the text that will appear on your shirt: '+'"'+message_shirt+'"')
make_shirt()
make_shirt(size_shirt='medium')
make_shirt(size_shirt='small',message_shirt='it Works !!!')	
'''3.4 Tarea'''
print('\nTarea 3.4.3')
def describe_city(city,country='Rusia'):
	print('\nthe '+city+' is in '+country)
describe_city(city='moscow')
describe_city(city='paris',country='France')
describe_city(city='toronto',country='Canada') 

'''4	Clases'''
print('\nParte 1 del ejercicio 4')
class Dog():
	"""Clase que ayuda a describir un perro""" 
	def __init__(self, name, age):
		"""Inicializa los atributos name y age""" 
		self.name = name 
		self.age = age
def sit(self):
	"""Simula el comportamiento de un perro al sentarse""" 
	print(self.name.title() + " is now sitting")
def roll_over(self):
	"""Simula el comportamiento de un perro al girar""" 
	print(self.name.title() + " ha dado una vuelta")
my_dog = Dog('willie',6) 
print("My dogs name is " + my_dog.name.title() + ".") 
print("My dog is " + str(my_dog.age) + " years old.")
class Restaurant():
	'''Clase del Restaurante'''
	def __init__(self,restaurant_name,restaurant_type,restaurant_OC):
		self.restaurant_name=restaurant_name
		self.restaurant_type=restaurant_type
		self.restaurant_OC=restaurant_OC
def describe_restaurant(self):
	print(self.restaurant_name+'It is the best restaurant in the world.')
	print('This restaurant specializes in:'+self.restaurant_type)
def open_restaurant(self):
	print(self.restaurant_OC)
my_restaurant=Restaurant('Don Martin','Mexican food','open')
print("\nMy restaurant name is " + my_restaurant.restaurant_name.title() + ".") 
print("\nThis restaurant specializes in: " + my_restaurant.restaurant_type)
print("\nThis restaurant is now: " + my_restaurant.restaurant_OC)
my_restaurant=Restaurant('moshi moshi ','japanesse food','close')
print("\nMy restaurant name is " + my_restaurant.restaurant_name.title() + ".") 
print("\nThis restaurant specializes in: " + my_restaurant.restaurant_type)
print("\nThis restaurant is now: " + my_restaurant.restaurant_OC)
my_restaurant=Restaurant('Italianis','italian food','open')
print("\nMy restaurant name is " + my_restaurant.restaurant_name.title() + ".") 
print("\nThis restaurant specializes in: " + my_restaurant.restaurant_type)
print("\nThis restaurant is now: " + my_restaurant.restaurant_OC)

class user():
	def __init__(self,first_name,last_name,type_blood,allergies,age):
		self.first_name=first_name
		self.last_name=last_name
		self.type_blood=type_blood
		self.allergies=allergies
		self.age=age
	def describe_user(self):
		print('\nName of user: '+self.first_name)
		print('\nlast name of user: '+self.last_name)
		print('\nType of blood: '+self.type_blood)
		print('\ntype of allergy: '+self.allergies)
		print('\nAge: '+str(self.age))
	def greet_user(self):
		print('Hola, '+self.first_name+', welcome to the program.')
my_user=user('Eduardo','Mendez','0+','penisilina',18)
print(my_user.greet_user())
print(my_user.describe_user())
my_user=user('Miguel','Espinoza','AB-','none',23)
print(my_user.greet_user())
print(my_user.describe_user())
my_user=user('Jose','Estrada','A-','Cetirizina',24)
print(my_user.greet_user())
print(my_user.describe_user())
my_user=user('Romario','Ramirez','b-','Cetirizina',24)
print(my_user.greet_user())
print(my_user.describe_user())
my_user=user('Angelica','Andamio','o+','Cetirizina',24)
print(my_user.greet_user())
print(my_user.describe_user())
my_user=user('Brenda','Blandin','0-','Cetirizina',24)
print(my_user.greet_user())
print(my_user.describe_user())
my_user=user('Carmen','Cruz','0-','Cetirizina',24)
print(my_user.greet_user())
print(my_user.describe_user())
my_user=user('David','Damazo','A-','Cetirizina',24)
print(my_user.greet_user())
print(my_user.describe_user())
my_user=user('Frida','Fernandez','A-','Cetirizina',24)
print(my_user.greet_user())
print(my_user.describe_user())
my_user=user('Gerardo','Gomez','A-','Cetirizina',24)
print(my_user.greet_user())
print(my_user.describe_user())