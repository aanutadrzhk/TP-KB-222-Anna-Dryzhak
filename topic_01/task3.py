a = int(input("Please enter value a: "))
b = int(input("Please enter value b: "))
c = int(input("Please enter value c: "))

def findD(a, b ,c):
    
    result = b**2 - 4*a*c
    return result

print(findD(a, b ,c))
