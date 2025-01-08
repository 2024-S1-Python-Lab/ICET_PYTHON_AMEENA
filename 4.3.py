class Rectangle:
    def __init__(self,l,b):
        self.__length=l
        self.__breadth=b
    def getDimension(self):
        return self.__length,self.__breadth
    def getArea(self):
        return self.__length*self.__breadth
    def __lt__ (self,other):
        if self.getArea()< other.getArea():
            return "1st rectangle is smaller"
        else:
            return "2nd rectangle is smaller"

length1=int(input("Enter 1st rectangle length:"))
breadth1=int(input("Enter 1st rectangle breadth:"))
a1=Rectangle(length1,breadth1)

length2=int(input("Enter 2nd rectangle length:"))
breadth2=int(input("Enter 2nd rectangle breadth:"))
a2=Rectangle(length2,breadth2)

print(f"Area of 1st rectangle {a1.getArea()} and Area of 2nd rectangle {a2.getArea()} ")
print(a1 < a2)



        