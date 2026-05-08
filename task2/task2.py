import sys
import os

def inEllipse(x,y,x0,y0,a,b):
    distance = ((x-x0)**2)/(a**2)+((y-y0)**2)/(b**2)
    
    if abs(distance - 1) < 1e-10:
        return 0
    if distance < 1:
        return 1
    else: 
        return 2


if len(sys.argv) != 3:
    print("Использование: python task2.py <file> <file> ")
    sys.exit(1)

ellipse = sys.argv[1]
points = sys.argv[2]

if os.path.getsize(ellipse) == 0:
    print("Файл пуст")
    sys.exit(1)
    
if os.path.getsize(points) == 0:
    print("Файл пуст")
    sys.exit(1)
try:
    f = open(ellipse, 'r')
    x0, y0 = map(float, f.readline().split())
    a, b = map(float, f.readline().split())
    f.close()
    
    if a <= 0 or b<= 0:
        print("a, b должны быть положительными")
        sys.exit(1)

except FileNotFoundError:
    print("Файл не найден")
    sys.exit(1)
except ValueError:
    print("В файле должны быть числа")
    sys.exit(1)
except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")  
        sys.exit(1)
try:
    f = open(points, 'r')
    for line in f:
        if line.strip():
            x, y = map(float, line.split())
            print(inEllipse(x, y, x0, y0, a, b))
    f.close()
    
except FileNotFoundError:
    print("Файл не найден")
    sys.exit(1)
except ValueError:
    print("В файле должны быть числа") 
    sys.exit(1)
except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        sys.exit(1)
