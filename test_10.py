import itertools
def number_from_set(a,b):
    mass= []
    if a > b:
        temp = b
        b = a
        a = temp
    for i in range(1,len(str(b))):
        for j in itertools.combinations_with_replacement("1389",i):
            if int("".join(j)) > a:
                print(int("".join(j)))
a,b = map(int, input().split())
number_from_set(a,b)

