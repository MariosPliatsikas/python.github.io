#author:Marios Pliatsikas

print('Distance between two points on the ground!!!\n')

print('Point Α')
p1=float(input('Give Latitude, (a real number from 0 to 90: \n'))
m1=float(input('Give Longitude, (a real number from 0 to 90: \n'))
print('Point Β')
p2=float(input('Give Latitude, (a real number from 0 to 90: \n'))
m2=float(input('Give Longitude, (a real number from 0 to 90: \n'))

from math import sin, cos, sqrt, atan2, radians

# radius of the earth to km 
R = 6373.0

p1 = radians(p1)
m1 = radians(m1)
p2 = radians(p2)
m2 = radians(m2)

Dm = m2 - m1
Dp = p2 - p1

a = sin(Dp / 2)**2 + cos(p1) * cos(p2) * sin(Dm / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print('\nDistance A-->B :',distance,'km')
