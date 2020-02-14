def SeqOutput(x):
    a = 1
    sequence = []
    isGreaterThan = False
    while True:
        for i in range(a):
            sequence.append(a)
            if len(sequence) >= x:
                isGreaterThan = True
                break
        a += 1
        if isGreaterThan == True:
            break

    print(*sequence)

def PositionsOfNumber(list, x):
    positions = []
    for i in range(len(list)):
        if list[i] == x:
            positions.append(i)

    if len(positions) == 0:
        print("Отсутствует")
    else:
        print(*positions, sep = "\t")

def Matrix(strArr):
    startMatrix = []
    for i in range(len(strArr)):
        if strArr[i] != "end":
            startMatrix.append([])
            row = strArr[i].split()
            for j in range(len(row)):
                startMatrix[i].append(row[j])

    print("До:")
    for row in startMatrix:
        print(*row, sep = " ", end = "\n")
    print("\n")

    returnMatrix = []
    for i in range(len(strArr)):
        if strArr[i] != "end":
            returnMatrix.append([])

    for i in range(len(startMatrix)):
        for j in range(len(startMatrix[i])):
            a = int(startMatrix[(i - 1)%len(startMatrix)][j])
            b = int(startMatrix[(i + 1)%len(startMatrix)][j])
            c = int(startMatrix[i][(j - 1)%len(startMatrix[i])])
            d = int(startMatrix[i][(j + 1)%len(startMatrix[i])])
            returnMatrix[i].append(a + b + c + d)

    print("После: ")
    for i in returnMatrix:
        print(*i, sep = " ", end = "\n")
    print("\n\n")

def Spiral(a):
    mat = [[0]*a for i in range(a)]
    st, m = 1, 0

    mat[a//2][a//2]=a*a
    for v in range(a//2):
    
        for i in range(a-m):
            mat[v][i+v] = st
            st+=1
        for i in range(v+1, a-v):
            mat[i][-v-1] = st
            st+=1
        for i in range(v+1, a-v):
            mat[-v-1][-i-1] =st
            st+=1
        for i in range(v+1, a-(v+1)):
            mat[-i-1][v]=st
            st+=1
        m+=2

    for i in mat:
        print(*i)
        

    



SeqOutput(7)
print("-------------------------")
PositionsOfNumber([1, 2, 3, 4, 5, 5, 4, 3, 2, 1], 1)
print("-------------------------")
Matrix(["1 2 3 4 5 5 4 3", "5 4 3 2 1 0 1 2", "1 3 5 7 9 3 4 5", "2 4 6 8 0 2 1 3", "3 7 1 1 1 8 9 0 ", "end"])
Matrix(["1 2 3 4 5 5 4 3", "end"])
Matrix(["3", "7", "1", "1", "1", "8", "9", "0", "end"])
print("-------------------------")
Spiral(10)
print("-------------------------")