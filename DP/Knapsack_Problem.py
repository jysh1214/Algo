# coding:utf-8

def knapsack(item, w):
    for i in item:
        # item[i](value/weight, weight)
        i[0] = float(i[0]/i[1])
    item = sorted(item, key = lambda x: x[0])
    item.reverse()
    get_value = 0
    for i in item:
        if w == 0:
            break
        if i[1] <= w:
            get_value += i[0] * i[1]
            w -= i[1]
            continue
        if 0 < w < i[1]:
            get_value += i[0] * w
            break

    return get_value

def main():
    # item[i](value, weight)
    item = [[6,1],[10,2],[12,3]]
    w = 5 # max weight
    result = knapsack(item, w)
    print(result)

if __name__ == "__main__":
    main()
