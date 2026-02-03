def ab(a,b):
    global S
    a = int(a)
    b = int(b)
    S[a-1], S[b-1] = S[b-1], S[a-1]
    return S

def xy(x,y):
    global S
    S = [y if i  == x else i for i in S]
    return S

S,Q = input().split()
S=list(S)
Q = int(Q)

for _ in range(Q):
    q,a,b = input().split()
    q = int(q)
    if q == 1:
        S = ab(a,b)
        print(*S, sep="")
    else:
        S = xy(a,b)
        print(*S, sep="")
    
    