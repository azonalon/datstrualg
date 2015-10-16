# Cell
def Binomial(n,k):
    if k == 0 or n == k:
        return 1
    elif n<k:
        raise Exception('Value Error')
    else:
        return Binomial(n-1, k-1) + Binomial(n-1, k)

print(Binomial(5,3))
# Cell
