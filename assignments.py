def Binomial(n,k):
    if k == 0 or n == k:
        return 1
    elif n<k:
        raise Exception('First argument must be bigger than second')
    else:
        return Binomial(n-1, k-1) + Binomial(n-1, k)

def Fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n <= 0:
        raise Exception('Number must be positive')
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

def Factorial(n):
    if n == 0:
        return 1
    return n*Factorial(n-1)


print('Pascal Triangle:')
for n in range(0,10):
    line=''
    for j in range(0,n+1):
        line += str(Binomial(n,j))+' '
    print(line.center(80))

print(Factorial(5))
print([Fibonacci(n) for n in range(0,10)])
