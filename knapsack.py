m=4
cap=9
peso=[4,2,3,4]
profitto=[10,7,8,6]

def print_mat(mat,n):
    for i in range(0,n+1):
        print(mat[i])
    print('\n')

def knapsack(n,capacity,w,p):

    matrix=[]
    for i in range(0,n+1):
        matrix.append([])
        for j in range(0,capacity+1):
            matrix[i].append(0)


    for i in range(1,n+1):
        for c in range(1,capacity+1):

            if (w[i-1] <= c):
                matrix[i][c] = max(matrix[i-1][c], matrix[i-1][c-w[i-1]] + p[i-1])

            else:
                matrix[i][c] = matrix[i-1][c]

            print_mat(matrix,n)

    print('\n')
    for i in range(0,n+1):
        print (matrix[i])
    return (matrix[n][capacity])


print ('\nThe result is: ',knapsack(m,cap,peso,profitto))
