#!/usr/bin/env python3

import random

n = random.randint(2, 2*(10**5))

print(str(n))
flag = True
with open("inp.txt", 'w') as out:
    out.write(str(n) + '\n')
    for i in range(n):
        if flag:
            t = 1
            flag = False
        else:
            t = random.randint(1, 2)
        num = random.randint(0, 10**6)
        out.write(str(t) + " " + str(num) + '\n')
        print(str(t) + " " + str(num))


