# coding:utf-8

def fac(n):
    f = [0, 1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, n+1):
        f.append(0)
        f[i] = f[i-1] * i
    return f[n]

def main():
    n = 10
    result = fac(n)
    print("{}!={}".format(n, result))

if __name__ == "__main__":
    main()
