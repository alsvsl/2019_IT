import numpy as np 
import math

n = int(input())
batch = int(input())
k = float(input())
global_n=n
test_size = n / (k * batch + 1)
t = math.floor(test_size)
t_1 = math.ceil(test_size)

kt = math.floor(t*k)
kt_1 = math.ceil(t_1*k)

index_lst = []
it = 0
for i in range(batch - 1):
    if n > 0:
        if (n - kt_1 > batch * kt) :
            index_lst.append((it, it + kt_1 - 1, it + (k+1)*t_1 - 1))
            it += kt_1
            n -= kt_1
        else:
            index_lst.append((it, it + kt - 1, it + (k+1)*t - 1))
            it += kt
            n -= kt
index_lst.append((it, it + kt - 1, global_n - 1))
print(index_lst) 





 