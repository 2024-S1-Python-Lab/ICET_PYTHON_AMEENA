class Rect:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        a=self.l*self.b 
        return a
    def perimeter(self):
        p=2*(self.l+self.b)
        return p
x1=int(input("Enter length of 1st rectangle:"))
y1=int(input("Enter breadth of 1st rectangle:"))
r1=Rect(x1,y1)
print(f"\nArea of Rectangle 1:{r1.area()}")
print(f"Perimeter of Rectangle 1:{r1.perimeter()}")

x2=int(input("Enter length of 2nd rectangle:"))
y2=int(input("Enter breadth of 2nd rectangle:"))
r2=Rect(x2,y2)
print(f"\nArea of Rectangle 2:{r2.area()}")
print(f"Perimeter of Rectangle 1:{r2.perimeter()}")

if r1.area()==r2.area():
    print('\n Areas of both rectangles are equal.')
else:
    print('\n Areas of both rectangles are  not equal.')


