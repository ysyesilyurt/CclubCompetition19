inp = input()
ret = ""
temp = ""
flag = 1
home_flag = 0
for i in range(len(inp)):
    if (inp[i]=='['):
        if(home_flag):
            ret = temp + ret
            temp = ""
            continue
        flag = 0
        home_flag = 1
        continue
    elif (inp[i]==']'):
        flag = 1
        home_flag = 0
        ret = temp + ret
        temp = ""
        continue
    else:
        if(flag):
            ret = ret + inp[i]
        else:
            temp = temp + inp[i]
if(len(temp) != 0):
    ret = temp +ret

print(ret)