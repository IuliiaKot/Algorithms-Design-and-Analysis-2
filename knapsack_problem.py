import random
def knapsack(W, value_weigth):
    N = len(value_weigth)
    A = [[0 for _ in xrange(W)] for _ in xrange(N)]
    for i in xrange(1,N):
        v , w = value_weigth[i]
        for x in xrange(W):
            if (w > x):
                A[i][x] = A[i-1][x]
            else:
                A[i][x] = max(A[i-1][x], A[i-1][x-w] + v)
    return A[N-1][W-1]


def knapsack_op(W, value_weight):
    N = len(value_weight)
    #A = [[0 for _ in xrange(W)] for _ in xrange(N)]
    A = [[0]*W]
    for i in xrange(1,N):
        v , w = value_weight[i]
        #A[0][:w-1] = A[i-1][:w-1]
        for x in xrange(w,W):
            A[0][x] = max(A[0][x], A[0][x-w] + v)
    return A[N-1][W-1]


def read_file():
    f = open('knapsack_problem.txt')
    
    V, W = [int(x) for x in f.readline().split()]
    value_weight = []
    for line in range(W):
        a, b = [int(x) for x in f.readline().split()]
        value_weight.append([a,b])
        #value_weight[0][0].append(a)
       # value_weight[0][1].append(b)

    return V,value_weight

def main():
    W, value_weigth = read_file()
    # Inizialisation A
    result = knapsack(W, value_weigth)
    print("result", result)

main()
