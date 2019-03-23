#!/usr/bin/env python3

"""
Sample Input
4
2 4
2 3
3 5
6 7

Sample Output
4
"""


def springFestival(points):
    lenp = len(points)
    points = sorted(points)
    coordCount = {}
    for i in range(lenp):
        for j in range(points[i][0]-points[i][1], points[i][0]+points[i][1]+1):
            try:
                coordCount[j] += 1
            except KeyError:
                coordCount[j] = 1
    print(max(coordCount.values()))


if __name__ == '__main__':
    points = []
    n = int(input())
    for _ in range(n):
        lst = input().split(" ")
        points.append((int(lst[0]), int(lst[1])))
    springFestival(points)
