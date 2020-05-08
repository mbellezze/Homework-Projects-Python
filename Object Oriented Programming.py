#Homework Assignment

#Problem 1

#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance 
#of the line.

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1_x1, self.coor1_y1 = coor1 #Otra forma es: x1,y1 = self.coor1
        self.coor2_x2, self.coor2_y2 = coor2 #Lo mismo acá: x2,y2 = self.coor2
    
    def distance(self):
        return ((self.coor2_x2 - self.coor1_x1)**2 + (self.coor2_y2 - self.coor1_y1)**2)**0.5
    
    def slope(self):
        return ((self.coor2_y2 - self.coor1_y1)/(self.coor2_x2 - self.coor1_x1))


# EXAMPLE OUTPUT
#coordinate1 = (3(x1),2(y1))
#coordinate2 = (8(x2),10(y2))

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
#li.distance()
#9.433981132056603

print(li.slope())
#li.slope()
#1.6



#Problem 2

#Fill in the class

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return (3.14)*((self.radius)**2)*(self.height)
    
    def surface_area(self):
        return ((2*3.14*self.radius*self.height) + (2*3.14*(self.radius)**2))


# EXAMPLE OUTPUT
c = Cylinder(2,3)

print(c.volume())
#c.volume()
#56.52

print(c.surface_area())
#c.surface_area()
#94.2
