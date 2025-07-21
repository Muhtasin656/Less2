def factoriol(x):
    '''this is doc string'''
    if x==0 or x==1:
        return 1
    else:
        return x*factoriol(x-1)
print(factoriol.__doc__)
print(factoriol(3))
print(factoriol(23))
print(factoriol(8))
print(factoriol(64))