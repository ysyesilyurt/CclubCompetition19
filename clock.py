#!/usr/bin/env python3

"""
Sample Input
10 4
1
2
-1
-2
2

Sample Output
0.7696
"""


def strangeClock(L, T, speeds):
    if not speeds or L == 0:
        print(0)
    elif T == 0:
        failProb = ((L-1)/L) ** len(speeds)
        print(1 - failProb)
    else:
        failProb = .0
        flag = False
        lens = len(speeds)
        for i in range(lens):
            if speeds[i] == 0:
                if not flag:
                    flag = True
                    failProb = (L-1)/L
                else:
                    failProb *= (L-1)/L
            else:
                x = abs(T * speeds[i])
                if x < L:
                    if not flag:
                        flag = True
                        failProb = (L - x) / L
                    else:
                        failProb *= (L - x) / L
        print(1 - failProb)


if __name__ == '__main__':
    speeds = []
    inp = list(map(int, input().split(" ")))
    for i in range(inp[1]):
        speeds.append(int(input()))
    T = int(input())
    strangeClock(inp[0], T, speeds)

