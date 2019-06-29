def power(N,K):
    if(K==1):
        return(N)
    if(K!=1):
        return(N*power(N,K-1))
N=int(input())
K=int(input())
print(power(N,K))
