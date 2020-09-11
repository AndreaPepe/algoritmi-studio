array=[1,3,4,-8,2,3,-1,3,4,-3,10,-3,2]

def maxsum(array):
    maxSoFar=0
    maxHere=0       # max subarray sum ending in A[i]
    start=end=0
    last=0          # beginning of the last max subarray sum found so far

    for i in range(0,len(array)):
        maxHere += array[i]
        if maxHere<=0:      # se la somma fino a questo momento è minore o uguale a 0 si può trascurare e ripartire da 0
            maxHere = 0
            last = i+1
        if maxHere > maxSoFar:
            maxSoFar = maxHere
            start,end = last, i
                            # se maxHere < maxSoFar non si fa nulla, semplicemente si va avanti aggiornando maxHere


        print('maxHere:' + str(maxHere) + '\nmaxSoFar:' + str(maxSoFar) +
         '\nlast:' + str(last) + '\nstart:' + str(start) + '\nend:' + str(end) + "\n")

    print('Max subarray sum start at position '+ str(start) +
    ' and end at position ' + str(end) + ' with sum ' + str(maxSoFar))

    return(start,end)


maxsum(array)
