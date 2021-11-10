N = [2,4,8,16,32,64]
from itertools import compress
res = list(zip(N,N[1:]+N[:1]))
print(res)
a= (map(lambda:res,res))
print(a)