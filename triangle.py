import math
def checkNumber(a,b,c):
    if (a <= 0) or (a > (2**32 - 1)) :
            return 0
    elif (b <= 0) or (b > (2**32 - 1)) :
            return 0
    elif (c <= 0) or (c > (2**32 - 1)) :
            return 0
    else: 
            return 1
                
def checkScaleneTriangle(a,b,c):
    if ((a + b) > c and abs(a-b) < c) or ((a + c) > b and abs(a-c) < b) or ((b + c) > a and abs(b-c) < a):
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
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
        return 1
    else:
        return 0
    
def checkRightIsoscelesTriangle(a,b,c):
    if checkRightTriangle(a, b, c) and checkIsoscelesTriangle(a, b, c):
        return 1
    else:
        return 0
    
def checkTypeOfTriangle(a,b,c):
    if checkNumber(a,b,c):
        if checkEquilateralTriangle(a, b, c):
            print "This is a Equilateral Triangle."
        elif checkRightIsoscelesTriangle(a, b, c):
            print "This is a Right Isosceles Triangle." 
        elif checkRightTriangle(a, b, c):
            print "This is a Right Triangle."
        elif checkIsoscelesTriangle(a, b, c):
            print "This is a Isosceles Triangle."
        elif checkScaleneTriangle(a, b, c):
            print "This is a Scalene Triangle."
        else:
            print "This is not a triangle!"
    else:
        print "The input is invalid! Please enter 3 numbers from 0 to 2^32-1."
        
checkTypeOfTriangle(2, 2, 2*math.sqrt(2))
