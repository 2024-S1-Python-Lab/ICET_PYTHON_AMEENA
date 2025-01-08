from graphics.rectangle import area as rect_area,perimeter as rect_perimeter
l=int(input('Enter length of rectangle:'))
b=int(input('Enter breadth of rectangle:'))
print('Rectangle Area:',rect_area(l,b))
print('Rectangle Perimeter:',rect_perimeter(l,b))

from graphics.circle import area as circ_area,perimeter as circ_perimeter
r=float(input('Enter radius ofa circle:'))
print('Circle Area:',circ_area(r))
print('Circle Perimeter:',circ_perimeter(r))

from graphics.graphics3d.cuboid import area as cuboid_area,perimeter as cuboid_perimeter
l=int(input('Enter length of cuboid:'))
b=int(input('Enter breadth of cuboid:'))
h=int(input('Enter height of cuboid:'))
print('Cuboid Area:',cuboid_area(l,b,h))
print('Cuboid Perimeter:',cuboid_perimeter(l,b,h))

from graphics.graphics3d.sphere import area as sphere_area,perimeter as sphere_perimater
r=float(input('Enter radius ofa Sphere:'))
print('Sphere Area:',sphere_area(r))
print('Sphere Perimeter:',sphere_perimater(r))
