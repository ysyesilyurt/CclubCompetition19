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
    sinan = {}
    sinanDct = set()
    # stuff = {}
    n = int(input())
    for _ in range(n):
        inp = list(map(int, input().split(" ")))
        binN = bin(inp[1])[2:]
        binN = binN[::-1]
        lenN = len(binN)
        binN += (20 - lenN) * '0'
        if inp[0] == 1:
            for digit in range(20):
                try:
                    if binN[digit] == '0':
                        if inp[1] not in sinan[digit][0]:
                            sinan[digit][0].add(inp[1])
                    else:
                        if inp[1] not in sinan[digit][0]:
                            sinan[digit][1].add(inp[1])
                except KeyError:
                    if binN[digit] == '0':
                        sinan[digit] = [{inp[1]}, set()]
                    else:
                        sinan[digit] = [set(), {inp[1]}]
            sinanDct.add(inp[1])
        else:
            if inp[1] in sinanDct:
                print(0)
            else:
                st = {}
                for digit in range(20):
                    if binN[digit] == '0':
                        for num in sinan[digit][0]:
                            try:
                                st[num] += 1
                            except KeyError:
                                st[num] = 1
                    else:
                        for num in sinan[digit][1]:
                            try:
                                st[num] += 1
                            except KeyError:
                                st[num] = 1
                if st == {}:
                    print(20)
                else:
                    print(len(binN) - max(st.values()))

"""
if __name__ == '__main__':
    sinan = []
    sinanDct = set()
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
                minCount = 20
                for numS in sinan:
                    binaryRep = bin(numS ^ inp[1])
                    ones = [ones for ones in binaryRep[2:] if ones == '1']
                    leno = len(ones)
                    if leno < minCount:
                        minCount = leno
                print(minCount)
"""
