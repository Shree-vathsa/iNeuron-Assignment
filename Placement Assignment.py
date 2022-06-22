#!/usr/bin/env python
# coding: utf-8

# 1. Create a function in python to read the text file and replace specific content
#    of the file.
# 
#    File name example.txt
#    Origin file content This is a placement assignment
#    Replace string Placement should be replaced by screening.
# 
#    Replaced file content This is a screening assignment

# In[94]:


def assignment1(file_path):
    search_text, replace_text = "placement", "screening"
    f = open(file_path, 'r')
    data = f.read()
    data = data.replace(search_text, replace_text)
    f = open(file_path, 'w')
    f.write(data)


# In[93]:


assignment1("C:\\Users\Shreevatsa\Desktop\example.txt")


# 2. Demonstrate use of abstract class, multiple inheritance and decorator in
#    python using examples.

# In[ ]:


# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

#vehicle.stop()
car.stop()
motorcycle.stop()



##When a class is derived from more than one base class it is called multiple Inheritance. 
##The derived class inherits all the features of the base case.
Class Base1:
       Body of the class

Class Base2:
     Body of the class

Class Derived(Base1, Base2):
     Body of the class
        
#Decorators allow us to modify the behaviour of a function or class.

def talk(text):
    return text.upper()
 
print(talk('Hello'))
 
speak = talk
 
print(speak('Hello'))

