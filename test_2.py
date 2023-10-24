def fibonacci(n):
    mass_fibonacci = [1,1]
    for i in range(1, n-1):
        mass_fibonacci.append(mass_fibonacci[i]+mass_fibonacci[i-1])
    print(mass_fibonacci)

n = int(input())
fibonacci(n)