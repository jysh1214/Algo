# coding:utf-8

def rod_cutting(n, p):
    p.insert(0, 0)
    best_price = [0] # best_price[i]:best price of i length
    first_part = [0] # first_part[i]:first length of i legth

    for i in range(1, n+1):
        best_price.append(0)
        first_part.append(0)
        for j in range(1, i+1):
            if best_price[i] < p[j] + best_price[i-j]:
                best_price[i] = p[j] + best_price[i-j]
                first_part[i] = j

    return best_price, first_part

def main():
    n = 10
    p = [1,3,8,8,9,10,18,18,23,25]
    (r, c) = rod_cutting(n, p)
    # show result
    print("   i|", end="")
    for i in range(1, 11):
       print("{0:2d}|".format(i), end="")
    print()
    print("p[i]|", end="")
    for i in range(1, 11):
        print("{0:2d}|".format(p[i]), end="")
    print()
    print("r[i]|", end="")
    for i in range(1, 11):
        print("{0:2d}|".format(r[i]), end="")
    print()
    print("c[i]|", end="")
    for i in range(1, 11):
        print("{0:2d}|".format(c[i]), end="")
    print()

if __name__ == "__main__":
    main()
