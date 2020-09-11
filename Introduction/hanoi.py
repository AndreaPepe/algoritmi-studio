def moveTower(n,source,dest,temp):
    if n==1:
        print("Move disk from ",source,"--> to ", dest)
    else:
        moveTower(n-1,source,temp,dest)
        moveTower(1,source,dest,temp)
        moveTower(n-1,temp,dest,source)

def hanoi(n):
    moveTower(n,"A","C","B")


hanoi(20)
