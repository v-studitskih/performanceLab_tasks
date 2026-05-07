import sys

def inEllipse(x,y,x0,y0,a,b):
    distance = ((x-x0)**2)/(a**2)+((y-y0)**2)/(b**2)
    
    if abs(distance - 1) < 1e-10:
        return 0
    if distance < 1:
        return 1
    else: 
        return 2


ellipse = sys.argv[1]
points = sys.argv[2]

f = open(ellipse, 'r')
x0, y0 = map(float, f.readline().split())
a, b = map(float, f.readline().split())
f.close()

f = open(points, 'r')
for line in f:
    x, y = map(float, line.split())
    print(inEllipse(x, y, x0, y0, a, b))
f.close()
