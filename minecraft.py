def getInputs():
    inpLine = list(map(int, input().split(" ")))
    rows = inpLine[0]
    columns = inpLine[1]
    foods = inpLine[2]
    matrix = x = [[0 for i in range(columns)] for j in range(rows)]
    for i in range(rows):
        tempInp = input()
        for j in range(len(tempInp)):
            if(tempInp[j] == "-"):
                matrix[i][j] = -9999
            elif(tempInp[j] == "^"):
                matrix[i][j] = -9999
            elif(tempInp[j] == "*"):
                matrix[i][j] = 0
            elif(tempInp[j] == "B"):
                start = (i,j)
            elif(tempInp[j] == "E"):
                end = (i,j)
            else:
                matrix[i][j] = int(tempInp[j])
    return (matrix,start,end)

if __name__ == "__main__":
    nodes = getInputs()