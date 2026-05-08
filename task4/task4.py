import sys


if len(sys.argv) != 2:
    print("Использование: python task4.py <file>")
    sys.exit(1)
    

file = sys.argv[1]


numbers = []

try: 
    f = open(file, 'r')
    for n in f:
        if n.strip():
            numbers.append(int(n.strip()))
    
    f.close()
    if len(numbers) == 0:
        print("Файл пустой")
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

min_steps = 21
unique_numbers = set(numbers)
for num in unique_numbers:
    total_steps = 0
    for x in numbers:
        total_steps += abs(num-x)
    if total_steps < min_steps:
        min_steps = total_steps
            
if min_steps == 21:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
else: 
    print(min_steps)