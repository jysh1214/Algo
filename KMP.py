#usr/bin/env/ python3

def KMP(T, P):
    n = len(T)
    m = len(P)
    T = list(T)
    P = list(P)
    T.insert(0, " ")
    P.insert(0, " ")
    k = 0
    pi = Prefix_Function(P)
    for i in range(1, n):
        while k > 0 and P[k+1] != T[i]:
            k = pi[k]
        if P[k+1] == T[i]:
            k = k + 1
        if k == m:
            print("Valid shift:",i-m)
            k = pi[k]

def Prefix_Function(P):
    m = len(P)
    pi = []
    for i in range(0, m): # set pi = [0~m]
        pi.append(i)
    pi[1] = 0
    k = 0

    for i in range(2, m):
        while k > 0 and P[k+1] != P[i]:
            k = pi[k]
        if P[k+1] == P[i]:
            k = k + 1
        pi[i] = k
    
    print("pi:", end=" ")
    for i in range(1, len(pi)):
        print(pi[i], end=" ")
    print()
    return pi

def main():
    T = "ababababaaababa"
    P = "ababaa"
    KMP(T, P)

if __name__ == "__main__":
    main()
