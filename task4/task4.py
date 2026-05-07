import sys

file = sys.argv[1]

numbers = []
f = open(file, 'r')
for n in f:
    if n.strip():
        numbers.append(int(n.strip()))

f.close()

min_steps = 21
unique_numbers = set(numbers)
for num in unique_numbers:
    total_steps = 0
    for x in numbers:
        total_steps += abs(num-x)
    if total_steps <= min_steps:
        min_steps = total_steps
            
if min_steps == 21:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
else: 
    print(min_steps)