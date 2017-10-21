# coding:utf-8

def fab(n):
    F = [0, 1] # F[0] = 0, F[1] = 1
    if n == 0:
        return F[0]
    if n == 1:
        return F[1]
    for i in range(2, n+1):
        F.append(0)
        F[i] = F[i-1] + F[i-2]
    return F

def main():
    n = 20
    result = fab(n)
    print(result)

if __name__ == "__main__":
    main()
