#!/usr/bin/env python3

"""
Sample Input
4
1 2
2 1
1 1
2 3

Sample Output
2
1
"""

# 1000 < n < 10000

if __name__ == '__main__':
    sinan = []
    sinanDct = set()
    usedIndexes = {}
    stuff = {}
    n = int(input())
    for _ in range(n):
        inp = list(map(int, input().split(" ")))
        if inp[0] == 1:
            sinan.append(inp[1])
            sinanDct.add(inp[1])
        else:
            if inp[1] in sinanDct:
                print(0)
            else:
                minCount = 32
                for numS in sinan:
                    if numS % inp[1] > inp[1]:
                        continue
                    res = numS ^ inp[1]
                    if res in stuff:
                        leno = stuff[res]
                    else:
                        binaryRep = bin(res)
                        leno = 0
                        for ones in binaryRep[2:]:
                            if ones == '1':
                                leno += 1
                        stuff[res] = leno
                    if leno < minCount:
                        minCount = leno
                print(minCount)
