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
        visited = set()
        while letter in rules:
            if letter in visited:
                res.append(letter)
                break
            elif rules[letter] in rules:
                visited.add(letter)
                letter = rules[letter]
            else:
                res.append(rules[letter])
                break
        else:
            res.append(s[j])
    print("".join(res))


if __name__ == '__main__':
    rules = {}
    s = input()
    n = int(input())
    for i in range(n):
        lst = input().split(" ")
        rules[lst[1]] = lst[0]
    foodCode(s, rules)

