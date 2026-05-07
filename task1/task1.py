import sys

def path(n, m):
    positions = []
    startPosition = 1
    
    while True:
        positions.append(startPosition)
        endPosition = (startPosition + m - 1) % n
        if endPosition == 0:
            endPosition = n 
            
        startPosition = endPosition
        if startPosition == 1:
            break
    
    return ''.join(map(str,positions))


n1 = int(sys.argv[1])
m1 = int(sys.argv[2])
n2 = int(sys.argv[3])
m2 = int(sys.argv[4])

print(path(n1,m1) + path(n2,m2))