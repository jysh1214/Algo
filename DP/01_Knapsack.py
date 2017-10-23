# coding:utf-8

def knapsack(item, w):
    value = [[0 for j in range(w+1)]for i in range(len(item)+1)]
    for i in range(1, len(item)+1):
        for j in range(1, w+1):
            vi, wi = item[i-1][0], item[i-1][1]
            if wi <= j:
                # max(take ith, don't take ith)
                value[i][j] = max(vi+value[i-1][j-wi], value[i-1][j])
            else:
                value[i][j] = value[i-1][j]
    return value[len(item)][w]

def main():
    # item[i](value, weight)
    item = [[6,1],[10,2],[12,3]]
    w = 5 # max weight
    result = knapsack(item, w)
    print(result)

if __name__ == "__main__":
    main()
