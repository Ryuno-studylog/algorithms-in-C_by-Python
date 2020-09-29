def eratos():
    n = 100
    i,j,a = 0,0,[1]*(n+1)
    ans = []
    a[0],a[1] = 0,0

    for i in range(2,n,2):
        a[i] = 0
    for i in range(2,int(n/2),1):
        j = 2
        while j <= n/i:
            a[i*j] = 0
            j += 1
    for l in range(n+1):
        if a[l] == 1:
             ans.append(l)
    print(ans)



def main():
    eratos()

main()