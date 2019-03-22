inp = input()
ret = ""
temp = ""
flag = 1
for i in range(len(inp)):
    if (inp[i]=='['):
        flag = 0
        continue
    elif (inp[i]==']'):
        flag = 1
        ret = temp + ret
        temp = ""
        continue
    else:
        if(flag):
            ret = ret + inp[i]
        else:
            temp = temp + inp[i]

print(ret)