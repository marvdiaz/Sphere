# Marvin Diaz
# maerdiaz@ucsc.edu
# programming assignment 1
# This program recieves an input radius from the user and outputs the volume and surface area of that sphere.

from math import pi as p

# Obtains radius from user
r = float(input("Enter the radius of the sphere: "))
# Caluclates volume of the sphere
v = (4/3)*p*r**3
# Calculates surface area of sphere 
sa = 4*p*r**2

# Prints out the volume and surface area
print("The volume is: "+str(v))
print("The surface area is: "+str(sa))
