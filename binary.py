import itertools as iter

def zbits(n,k):
    s=set()
    array0='0'*(n-k)
    array1='1'*k
    array=array0+array1
    for item in iter.permutations(array,n):
        s.add(''.join(item))
    return s
