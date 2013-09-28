import math

def checkNumber(a,b,c):
    if (type(a) not in [float, int, long]) or (type(b) not in [float, int, long]) or (type(c) not in [float, int, long]):
        return 0
    elif (a <= 0) or (a > (2**32 - 1)) or (b <= 0) or (b > (2**32 - 1)) or (c <= 0) or (c > (2**32 - 1)):
        return 0
    else: 
        return 1
                
def checkScaleneTriangle(a,b,c):
    if ((a + b) > c and abs(a-b) < c) and ((a + c) > b and abs(a-c) < b) and ((b + c) > a and abs(b-c) < a):
            return 1
    else:
            return 0

def checkEquilateralTriangle(a,b,c):
    if a == b == c:
        return 1
    else:
        return 0
    
def checkIsoscelesTriangle(a,b,c):
    if ((a == b and a != c) or (a == c and a != b) or (c == b and c != a)) and checkScaleneTriangle(a, b, c):
        return 1
    else:
        return 0
    
def checkRightTriangle(a,b,c):
    if abs(a**2 + b**2 - c**2)<10**(-9) or abs(b**2 + c**2 - a**2)<10**(-9) or abs(a**2 + c**2 - b**2)<10**(-9):
        return 1
    else:
        return 0
    
def checkRightIsoscelesTriangle(a,b,c):
    if checkRightTriangle(a, b, c) and checkIsoscelesTriangle(a, b, c):
            return 1
    else:
            return 0
    
def detect_triangle(a,b,c):
        if checkNumber(a, b, c):
            if checkEquilateralTriangle(a, b, c):
                print "This is a Equilateral Triangle."
                return "This is a Equilateral Triangle."
            elif checkRightIsoscelesTriangle(a, b, c):
                print "This is a Right Isosceles Triangle."
                return "This is a Right Isosceles Triangle." 
            elif checkRightTriangle(a, b, c):
                print "This is a Right Triangle."
                return "This is a Right Triangle."
            elif checkIsoscelesTriangle(a, b, c):
                print "This is a Isosceles Triangle."
                return "This is a Isosceles Triangle."
            elif checkScaleneTriangle(a, b, c):
                print "This is a Scalene Triangle."
                return "This is a Scalene Triangle."
            else:
                print "This is not a triangle!"
                return "This is not a triangle!"
        else:
            print "The input is invalid! Please enter 3 integers from 0 to 2^32-1."
            return "The input is invalid! Please enter 3 integers from 0 to 2^32-1."      
if __name__ == "__main__":
    detect_triangle(1, 1, math.sqrt(2))
