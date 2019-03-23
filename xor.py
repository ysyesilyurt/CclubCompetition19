def findOnes(a,b):
    temp = a ^ b
    ret = 0
    while(temp):
        if(temp%2 == 1):
            ret += 1
        temp = int(temp/2)
    return ret

if __name__ == "__main__":
    n = int(input())
    sinan = []
    tempDict = {}
    for i in range(n):
        line = list(map(int, input().split(" ")))
        minNumber = 100
        if(line[0] == 1):
            newNumber = line[1]
            sinan.append(newNumber)
            for b in tempDict: #önceden eklenmiş numaralar için mini güncelle
                bVal = tempDict.get(b)
                if(bVal == 0):
                    continue
                minNumber = findOnes(b,newNumber)
                #print("a:" + str(newNumber) + "-b:"+ str(b)+"->"+str(minNumber))
                if(bVal > minNumber):
                    tempDict[b] = minNumber       
        else:
            a = line[1]
            if (a in tempDict):
                minNumber = tempDict.get(a)
            else:
                if(a in sinan):
                    minNumber = 0
                else:
                    lenSinan = len(sinan)
                    for j in range(lenSinan):
                        b = sinan[j]
                        tempMin = findOnes(a,b)
                        if (tempMin < minNumber):
                            minNumber = tempMin
                tempDict[a] = minNumber
            print(minNumber)