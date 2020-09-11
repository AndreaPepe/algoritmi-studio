def solve(n,i,a,b,c):
    if i<n:
        for j in range(0,n):
            if j not in a and (i+j) not in b and (i-j) not in c:    # b and c cover the diagonals
                for solution in solve(n,i+1, a+[j],b+[i+j],c+[i-j]):    # RECURSIVEEEE!!!
                    yield solution
    else:
        yield a                 # work endend when i==n



def erase(mat,n):
    for i in range(n):
        for j in range(n):
            mat[i][j]=0

def print_mat(mat,n):
    for i in range(0,n):
        print(mat[i])
    print('\n')


mat=[]
for i in range(8):
    mat.append([])
    for j in range(8):
        mat[i].append(0)

for solution in solve(8,0,[],[],[]):
    #print (solution)
    erase(mat,8)
    for i in range(len(solution)):
        mat[solution[i]][i]=1
    print_mat(mat,8)
