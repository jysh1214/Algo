# coding:utf-8

import random
import math

def select(A, k):
    temp_list = []
    length = len(A)
    count = 0

    # stop recursion
    if length <= 5:
        return sorted(A)[k-1]

    # Devide A into 5 heap
    while count < length:
        temp_list.append(A[0])
        A.remove(A[0])
        if len(temp_list) == 5:
            A.append(temp_list)
            temp_list = []
        count += 1

    # < 5 heap fill with infinity
    try: # check not inf
        int(temp_list[0]) 
        while len(temp_list) < 5:
            temp_list.append(math.inf)
        A.append(temp_list)
    except:
        pass
        
    # Now, A have A//5(+1, if A%5 >0) heap
    # sort all heap
    length = len(A)
    for i in range(length):
        A[i] = sorted(A[i])

    # shorted by medians
    A = sorted(A, key = lambda x: x[len(x)//2])

    # Now, we got the median of medians(MoM)
    MoM_i = len(A[len(A)//2])//2

    if len(A) % 2 == 0:
        MoM_j = (len(A)//2) - 1
    else:
        MoM_j = (len(A)//2)

    MoM = A[MoM_j][MoM_i]

    # left part
    S1 = []
    temp_list = []    
    for j in range(0, MoM_j+1):
        temp_list = list(x for x in A[j] if A[j].index(x) <= MoM_i)
        for i in temp_list:
            S1.append(i)
    S1.pop() # pop MoM

    # right part
    S2 = []
    temp_list = []    
    for j in range(MoM_j, len(A)):
        temp_list = list(x for x in A[j] if A[j].index(x) >= MoM_i)
        for i in temp_list:
            S2.append(i)
    S2.remove(S2[0]) # remove MoM 

    # find the kth number
    MoM_rank = len(S1) + 1
    if MoM_rank == k:
        return MoM

    new_part = []
    for x in flattern(A):
        try: # filter infinity
            int(x)
            new_part.append(x)
        except:
            pass

    # kth number impossibly in the S2, remove it
    if MoM_rank > k:
        for i in S2:
            if i in new_part:
                new_part.remove(i)

        return select(new_part, k)

    # kth number impossibly in the S1, remove it
    if MoM_rank < k:
        for i in S1:
            if i in new_part:
                new_part.remove(i)

        return select(new_part, k-len(S1))

def flattern(l):
    for i in l:
        if isinstance(i, list):
            yield from flattern(i)
        else:
            yield i

def main():
    length = 30
    A = [random.randint(0, 100) for i in range(length)]
    B = sorted(A)
    print(A)
    print(B)
    # find kth elements in array
    k = 15
    brute = B[k-1]
    
    result = select(A, k)
    print("{}'th number:{}". format(k, result))
    print("By bruteforce:{}". format(brute))

if __name__ == "__main__":
    main()
