import random

for i in range(10,50,10):
    with open(str(i)+'.txt', 'w') as f:
        for j in range(i):
            a = random.randint(0,3)
            if a == 0:
                f.write('A')
            elif a == 1:
                f.write('C')
            elif a == 2:
                f.write('G')
            elif a == 3:
                f.write('T')
        f.write('\n')
        for j in range(i):
            a = random.randint(0,3)
            if a == 0:
                f.write('A')
            elif a == 1:
                f.write('C')
            elif a == 2:
                f.write('G')
            elif a == 3:
                f.write('T')
        f.write('\n')
    