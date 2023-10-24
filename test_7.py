def common_multiples(a,b,n):
    for i in range(1,n+1):
        if a%i == 0 and b%i == 0:
            print(i)

a,b,n = map(int,input().split())
common_multiples(a,b,n)