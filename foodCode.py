#!/usr/bin/env python3

"""
Sample Input
aaaa aaa
3
a b
b c
c a

Sample Output
aaaa aaa
"""


def foodCode(s, rules):
    lens = len(s)
    res = []
    for j in range(lens):
        letter = s[j]
        for i in range(len(rules)-1,-1,-1):
            #print(i)
            if(rules[i][1] == letter):
                letter = rules[i][0]
        res.append(letter)
    print("".join(res))


if __name__ == '__main__':
    rules = []
    s = input()
    n = int(input())
    for _ in range(n):
        lst = input().split(" ")
        rules.append(lst)
    foodCode(s, rules)

