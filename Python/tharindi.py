N_T=(input()).split(" ")
N=int (N_T[0])
T=int (N_T[1])
print(N_T)
q=[0]*N
for i in range(0,T):
    abc=(input()).split(" ")
    N1=int (abc[0])
    T1=int (abc[1])
    Y=int(abc[2])
    for j in range(N1-1,T1):
        q[j]+=Y
       
k=input()
k1=int(k)
count=0
for p in q:
    if p<k1:
        count+=1
print (count)

        
