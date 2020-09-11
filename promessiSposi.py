def sottostringaRec(T,P,n,m):
    if (n==0 and m==0) or m==0:         # Pattern finito ( +1 occorrenza )
        return 1
    if n==0:                            # Nessuna occorrenza trovata
        return 0
    if T[n-1]==P[n-1]:                  # scartare o no T[n-1]
        return sottostringaRec(T,P,n-1,m-1) + sottostringaRec(T,P,n-1,m)
    else:                               #scartare T[n-1]
        return sottostringaRec(T,P,n-1,m)



# PROGRAMMAZIONE DINAMICA (MEMOIZATION)
def sottostringa(T,P,n,m):
    DP = [0] * (m+1)                    # create a row
    DP[0] = 1                           # pattern finito ( +1 occorrenza )

    for i in range(0,n):
        DP1 = DP.copy()                 # la nuova riga dipende solo dalla precedente, cioè da DP1
        for j in range (1,m+1):
            if T[i]==P[j-1]:            # Aggiusto gli indici
                DP[j] = DP1[j-1] + DP1[j]
            else:
                DP[j] = DP1[j]
    return DP[m]
