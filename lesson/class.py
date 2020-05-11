"""
Class definition

You don't have to write [object]

"""


#class Person(object):
#    def __init__(self, name):
#        self.name = name
#        print(self.name)

#    def say_something(self):
#        print('I am {}. hello'.format(self.name))
#        self.run(3)
          
#    def run(self, num):
#        print('run' * num)

#person = Person('Mike')
#person.say_something()

#---------------------------------
#　I am Mike. hello
# runrunrun


"""
Destructor

Run del when the class is no longer used
"""

#class Person(object):
#    def __init__(self, name):
#        self.name = name
#        print(self.name)

#    def say_something(self):
#        print('I am {}. hello'.format(self.name))
#        self.run(3)
          
#    def run(self, num):
#        print('run' * num)

#    def __del__(self):
#        print('good bye')

#person = Person('Mike')
#person.say_something()

#del person

#print('##############')


"""
Class inheritance
"""

#class Car(object):
#    def run(self):
#        print('run')

#class ToyotaCar(Car):
#    pass

#class TeslaCar(Car):
#    def auto_run(self):
#        print('auto run')

#car = Car()
#car.run()

#print('###########')
#toyota_car = ToyotaCar()
#toyota_car.run()
#toyota_car.auto_run()
#print('###########')
#tesla_car = TeslaCar()
#taesla_car.run()
#tesla_car.auto_run()

#-----------------------------

#run
###########
#run
###########
#run
#auto run


"""
override
"""


#class Car(object):
#    def __init__(self, model=None):
#        self.model = model
#    def run(self):
#        print('run')

#class ToyotaCar(Car):
#    def run(self):
#        print('fast')

#class TeslaCar(Car):
#    def run(self):
#        print('super fast')
#    def auto_run(self):
#        print('auto run')

#car = Car()
#car.run()

#print('###########')
#toyota_car = ToyotaCar('Lexus')
#print(toyota_car.model)
#toyota_car.run()
#toyota_car.auto_run()
#print('###########')
#tesla_car = TeslaCar('Model S')
#print(tesla_car.model)
#tesla_car.run()
#tesla_car.auto_run()

#-----------------------------

#run
###########
#Lexus
#fast
###########
#Model S
#super fast
#auto run


"""
super : Can inherit the functionality of the parent class
"""

#class Car(object):
#    def __init__(self, model=None):
#        self.model = model
#    def run(self):
#        print('run')

#class ToyotaCar(Car):
#    def run(self):
#        print('fast')

#class TeslaCar(Car):
#    def __init__(self, model='Model S', enable_auto_run=False):
#        #self.model = model
#        super().__init__(model)
#        self.enable_auto_run = enable_auto_run

#    def run(self):
#        print('super fast')
#    def auto_run(self):
#        print('auto run')

#car = Car()
#car.run()

#print('###########')
#toyota_car = ToyotaCar('Lexus')
#print(toyota_car.model)
#toyota_car.run()
#toyota_car.auto_run()
#print('###########')
#tesla_car = TeslaCar('Model S')
#print(tesla_car.model)
#tesla_car.run()
#tesla_car.auto_run()

#-----------------------------

#run
###########
#Lexus
#fast
###########
#Model S
#super fast
#auto run

