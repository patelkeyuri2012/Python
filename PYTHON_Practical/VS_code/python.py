''' 
what is function?
what is module?
what is packages?

arithmetic - sum, sub, div, mul
dmath - mean, midean, mode
interset - simple, compond

'''

from interest import *

p = 20000
r = 10
n = 3

print("\nSimple interest for given P R N is :",simple_interest(p,r,n))
print("\nCompound interest for given P R N is :",compound_interest(p,r,n))


from arithmetic import *

a = 45
b = 34

print("\nAddition of both number is :",add(a,b))
print("\nSubstraction of both number is :",sub(a,b))
print("\nMultiplication of both number is :",mul(a,b))
print("\nDivision of both number is :",div(a,b))


from dmath import *

data = [45,24,23,56,45,24,36,78]

print("\nMean of given numbers is :", mean(data))
print("\nMedian of given numbers is :", median(data))
print("\nMode of given numbers is :", mode(data))