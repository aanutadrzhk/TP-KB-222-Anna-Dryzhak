a = int(input("Будь ласка, введіть значення a: "))
b = int(input("Будь ласка, введіть значення b: "))
c = int(input("Будь ласка, введіть значення c: "))

def findD(a, b ,c):
    
    D = b**2 - 4*a*c
    return D


def FindRoots(a, b, c):
    D = findD(a, b, c)
    if D > 0:
        x1 = (-b + D**0.5) / 2*a
        x2 = (-b - D**0.5) / 2*a
        return x1, x2
    elif D == 0:
        x1 = -b / 2*a
        return x1
    else:
        return None

roots = FindRoots(a, b, c)

if roots is not None:
    if isinstance(roots, tuple):
        x1, x2 = roots
        print("Рівняння має два корені:")
        print("x1 =", x1)
        print("x2 =", x2)
    else:
        x1 = roots
        print("Рівняння має один корінь:")
        print("x1 =", x1)
else:
    print("Рівняння не має коренів.")
