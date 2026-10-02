x = float(input("Enter x: "))
y = float(input("Enter y: "))

def f1(xWar, yWar):
    if xWar*yWar >= 0:
        if xWar < yWar: return xWar ** 2
        else: return yWar ** 2 
    
    elif xWar*yWar < 0:
        if xWar**2 > yWar**2: return xWar**2
        else: return yWar**2

print(f1(x,y))