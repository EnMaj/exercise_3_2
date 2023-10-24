from math import sqrt

def prime(number):
    for i in range(2,sqrt(number)):
        if number%i == 0:
            return False
    return True
def write_prime(n):
    lst=[2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i%10 == 5):
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            elif (i % j == 0):
                break
        else:
            lst.append(i)
    print(lst)

n = int(input())