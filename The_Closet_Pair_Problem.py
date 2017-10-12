# coding:utf-8

import math
import random

def closet_pair(p_x, p_y):
    if len(p_x) <= 3:
        return brute(p_x)

    mid = len(p_x)//2 # mid must be int
    L_x = p_x[:mid]
    R_x = p_x[mid:]

    L_set = set(L_x)
    L_y = []
    R_y = []
    for point in p_y:
        if point in L_set:
            L_y.append(point)
        else:
            R_y.append(point)

    (x_l, y_l, d_l) = closet_pair(L_x, L_y)
    (x_r, y_r, d_r) = closet_pair(R_x, R_y)

    if d_l <= d_r:
        d_min = d_l
        pair = (x_l, y_l)
    else:
        d_min = d_r
        pair = (x_r, y_r)

    # closet pair maybe on the split line
    (x_s, y_s, d_s) = closet_split_pair(p_x, p_y, d_min, pair)

    if d_min <= d_s:
        return pair[0], pair[1], d_min
    else:
        return x_s, y_s, d_s

def closet_split_pair(p_x, p_y, d, best_pair):
    mid_x = p_x[len(p_x)//2][0]

    # create a subarray of points not further than delta from
    # midpoint on x-sorted array
    s_y = [x for x in p_y if (mid_x-d) <= x[0] <= (mid_x+d)]

    d_min = d
    for i in range(len(s_y)-1):
        for j in range(i+1, len(s_y)):
            d_new = dist(s_y[i], s_y[j])
            if d_new <= d_min:
                d_min = d_new
                best_pair = s_y[i], s_y[j]

    return best_pair[0], best_pair[1], d_min

def brute(p_x):
    p1, p2 = p_x[0], p_x[1]
    d_min = dist(p_x[0], p_x[1])

    if len(p_x) == 2:
        return p_x[0], p_x[1], d_min

    for i in range(len(p_x)-1):
        for j in range(i+1, len(p_x)):
            d_new = dist(p_x[i], p_x[j])
            if d_new <= d_min:
                d_min = d_new
                p1, p2 = p_x[i], p_x[j]

    return p1, p2, d_min

def main():
    # test
    points = random_create(20) # length = 20
    print(points)
    
    p_x = sorted(points, key = lambda x: x[0]) # preshorting X_wise
    p_y = sorted(points, key = lambda x: x[1]) # preshorting Y_wise
    (p1, p2, d_min) = closet_pair(p_x, p_y)
    print("Closet pair:",p1, p2)
    print("Distance:", d_min)

def random_create(length):
    points = []
    temp_pair = (0,0)
    x_list = [random.randint(-20, 20) for i in range(length)]
    y_list = [random.randint(-20, 20) for i in range(length)]

    for i in range(length):
        temp_pair = x_list[i], y_list[i]
        points.append(temp_pair)

    return points

def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

if __name__ == "__main__":
    main()
