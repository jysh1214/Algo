"""
matrix   | A1| A2| A3| A4|
dimension|2*3|3*5|5*4|4*2|

find the minimum numbers of scalar multiplications
"""

def matrix_chain(A):
    n = len(A)
    temp = [0 for i in range(n)]
    s = [temp for i in range(n)]

    for i in range(n):
        for j in range(n-1, -1, -1):
            if (i-j) == 1:
                s[j][i] = A[j][0]*A[j][1]*A[i][1]
            
            elif i > j:
                s[j][i] = min(s[j][i-1]+(A[j][0]*A[i-1][1]*A[i][1]),\
                              s[j+1][i]+(A[j+1][0]*A[i][1]*A[j][0]))
                
    return s[n-1][n-1]

def main():
    # A[i][0]*A[i][1] means Ai dimension, i = 1~4
    A = [[2,3],[3,5],[5,4],[4,2]]
    print(matrix_chain(A))

if __name__ == '__main__':
    main()
