""" 
Gonzalo Guerra
lab 6, classes, object, and methods

"""
import math as plt

print("\n ---- example 1: classes ---- ")
# a class is like a blueprint of something
# using the class, we can create different instance of an object 
# data attributes (properties) are valuese that represents an object 
# methods are functions of an object

class Circle(object):
    def __init__(self, radius, color):
        self.r = radius
        self.c = color

    # method to add value to the radius
    def add_radius(self, plusradius):
        self.r += plusradius
        return self.r 
    
    # method to add value to the color
    def add_color(self, add_color):
        self.c += add_color
        return self.c


class Rectangle(object):
    def __init__(self, height, width, color):
        self.h = height
        self.w = width
        self.c = color

    # method to calculate and return the area of the rectangle
    def area(self):
        return self.h * self.w
    
    # method to calculate the perimeter of a rectangle
    def perimter(self):
        return 2*self.h + 2*self.w
    
    # method to draw the rectangle
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.w, self.h, fc=self.c))
        plt.axis("Scaled")
        plt.show()


# create an instance of an object
circle1 = Circle(5, "yellow")
circle2 = Circle(2, "red")

rectangle1 = Rectangle(2, 3, "green")
rectangle2 = Rectangle(5, 4, "blue")

# accessing to data in an object
print(f"color of circle 2 = {circle2.c}")
print(f"The are of rectangle 1 = {rectangle1.h * rectangle1.w} and the color is {rectangle1.c}")
print(f"The are of rectangle 2 = {rectangle2.h * rectangle2.w} and the color is {rectangle2.c}")

# modify data of an object
circle2.c = "orange"
print(f"color of circle 2 after modification = {circle2.c}")




print(f"radius of circle 2 = {circle2.r}")
# call method add_radius in circle 2 and pass 6
circle2.add_radius(6)
print(f"radius of circle 2 after method add_radius = {circle2.r}")

print(f"The color of circle 2 = {circle2.c}")
# call method add_color in circle 2 and pass 'lime'
circle2.add_color(" lime")
print(f"The color of circle 2 after method add_color = {circle2.c}")

# call methods in class Rectangle
print(f"The area of rectangle 1 = {rectangle1.area()}")
print(f"The preimeter of rectangle 2 = {rectangle2.perimter()}")


# draw rectangle 
# rectangle2.drawRectangle()


print("\n ---- Exercise ---- ")


class BankAccount(object):
    def __init__(self, account_number, account_holder, balance):
        self.num = account_number
        self.h = account_holder
        self.b = balance

    def deposit(self, adding):
        self.b += adding
        return self.b
    
    def withdraw(self, subtract):
        self.b -= subtract
        return self.b
        

#     # def add_radius(self, plusradius):
#     #     self.r += plusradius
#     #     return self.r 


useraccount = BankAccount(123456789, "Gonzalo Guerra", 250)

print(f"Account number {useraccount.num} and the name is {useraccount.h}. and he have {useraccount.b}")

useraccount.deposit(500)

print(f"Account number {useraccount.num} and the name is {useraccount.h}. and he have {useraccount.b} added more")

useraccount.withdraw(700)

print(f"Account number {useraccount.num} and the name is {useraccount.h}. and he have {useraccount.b}  substracted after ")
        



# class Triangle(object):
#     def __init__(self, lengths, angles, area):
#         self.l   = lengths
#         self.ang = angles
#         self.a   = area


        
        

        
