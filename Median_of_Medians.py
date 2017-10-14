# coding:utf-8

import random

def select(A, k):
    temp_list = []
    length = len(A)
    count = 0

    # stop recursion
    if length <= 10:
        return sorted(A)[k-1]

    # Devide A into 5 heap
    while count < length:
        temp_list.append(A[0])
        A.remove(A[0])
        if len(temp_list) == 5:
            A.append(temp_list)
            temp_list = []
        count += 1

    if len(temp_list) != 0:
        A.append(temp_list)
        
    # Now, A have A//5(+1, if A%5 >0) heap
    # sort all heap
    length = len(A)
    for i in range(length):
        A[i] = sorted(A[i])

    # shorted by medians
    A = sorted(A, key = lambda x: x[len(x)//2])
    # Now, we got median of medians
    MoM_i = len(A[len(A)//2])//2
    MoM_j = len(A)//2
    MoM = A[MoM_j][MoM_i]

    # left part
    S1 = []
    temp_list = []    
    for j in range(0, (len(A)//2)+1):
        temp_list = list(x for x in A[j] if A[j].index(x) <= MoM_i)
        for i in temp_list:
            S1.append(i)
    S1.pop() # pop MoM

    # right part
    S2 = []
    temp_list = []    
    for j in range((len(A)//2), len(A)):
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
        new_part.append(x)

    # kth number impossibly in the S2, remove it
    if MoM_rank > k:
        for i in S2:
            if i in new_part:
                new_part.remove(i)
        # MoM is the smallest number, and not our target
        if len(S2) == 0:
            new_part.remove(MoM)  

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
    length = 150
    A = [random.randint(0, 100) for i in range(length)]
    B = sorted(A)
    print(A)
    print(B)
    #k = len(A)//2+1 # find kth elements in array
    k = 8
    brute = B[k-1]
    
    result = select(A, k)
    print("{}'th number:{}". format(k, result))
    print("By bruteforce:{}". format(brute))

if __name__ == "__main__":
    main()
