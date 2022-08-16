def solution(X, A):
    B = [0]*X
    S=0
    for i in range (0,len(A)):
        if (B[A[i]-1]==0 and A[i]<=X):
            s+=1
            B[A[i]-1]=1
        if (s==X):
            return i
    return -1
    