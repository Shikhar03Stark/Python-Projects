#A matrix can be defined as a combined list in python
def showMatrix(x):
    if isinstance(x, str) == False: #checking if return value is a string
        for i in range(0, len(x)):
            for j in range(0, len(x[0])):
                print(x[i][j], end = ' ')

            print('\n')
    else:
        print(x)

def addMatrix(x, y):
    if(len(x) == len(y) and len(x[0]) == len(y[0])):
        sum = [[0 for j in range(0,len(x[0]))] for i in range(0,len(x))]
        for i in range(0, len(x)):
            for j in range(0, len(x[0])):
                sum[i][j] = x[i][j] + y[i][j]
        return sum

    else:
        error = "Matrices of different order"
        return error

def subtractMatrix(x, y):
    if(len(x) == len(y) and len(x[0]) == len(y[0])):
        sum = [[0 for j in range(0,len(x[0]))] for i in range(0,len(x))]
        for i in range(0, len(x)):
            for j in range(0, len(x[0])):
                sum[i][j] = x[i][j] - y[i][j]
        return sum

    else:
        error = "Matrices of different order"
        return error

def multiplyMatrix(x, y):
    if(isinstance(x,(int, float)) == False):
        if(len(x[1]) == len(y)):
            mult = [[0 for j in range(len(y[0]))] for i in range(len(x))]
            for p in range(0, len(mult)):
                for q in range(0, len(mult[0])):
                    for i in range(0, len(x[0])):
                        mult[p][q] += x[p][i]*y[i][q]
            return mult

        else:
            error = "Invalid Order of Matrices"
            return error
    else:
        for i in range(len(y)):
            for j in range(len(y[0])):
                y[i][j] = x*y[i][j]
        return y
def transposeMatrix(x):
    transpose = [[0 for a in range(0, len(x))] for b in range(0, len(x[0]))]
    for i in range(0, len(x)):
        for j in range(0, len(x[0])):
            transpose[j][i] = x[i][j]
    return transpose

def detMatrix(x):
    if(len(x) != len(x[0])):
        error = "Matrix is not square"
        return error
    det = 0
    order = len(x)

    if(order == 2):
        det = x[0][0]*x[1][1] - x[0][1]*x[1][0]
        return det
    else: #optimization required
        for j in range(0, len(x[0])):
            det += ((-1)**j)*x[0][j]*detMatrix(cofactor(x,0,j)) #Recursive call
        return det
#extracting Co-factors and adjoint of addMatrix
def cofactor(x,r,c):
    if(len(x) != len(x[0])):
        error = "Matrix is not square"
        return error
    order = len(x)
    cof = [[0 for x in range(0,order-1)] for y in range(0,order-1)]
    a , b = 0, 0
    for i in range(0,len(x)):
        if(i == r):
            continue
        b = 0
        for j in range(0, len(x[0])):
            if(j == c):
                continue
            cof[a][b] = x[i][j]
            b = b + 1
        a = a +1
    return cof

def adjMatrix(x):
    if(len(x) != len(x[0])):
        error = "Matrix is not square"
        return error
    adj = [[0 for a in range(0,len(x))] for b in range(0,len(x))]
    for i in range(0,len(x)):
        for j in range(0,len(x)):
            adj[i][j] = ((-1)**(i+j))*detMatrix(cofactor(x,i,j))
    adj = transposeMatrix(adj)
    return adj

def inverseMatrix(x):
    det = detMatrix(x)
    inv = multiplyMatrix(1/det,adjMatrix(x))
    return inv


m1 = [[0,3,6],[1,2,4],[6,18,27]]
m2 = [[-1,8, 7],[4,-5,6],[1,9,1]]
m3 = [[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]]
m4 = [[2,6],[1,-1]]
m5 = [[3,0,5,2],[2,9,-1,0],[3,11,0,1],[5,6,2,1]]

#Prob1
T = [[1/3,-2/3,-2/3],[-2/3,1/3,-2/3],[-2/3,-2/3,1/3]]
a = [[1],[2],[3]]
#showMatrix(multiplyMatrix(T,a))
showMatrix(m1)
showMatrix(inverseMatrix(m1))
