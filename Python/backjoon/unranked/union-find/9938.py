import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

N, L = map(int, input().split(' '))

ladica = [i for i in range(L + 1)]

drink = [0 for i in range(L + 1)]


def find(parent, x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent, parent[x])
        return parent[x]

def union(parent, x, y, drink):
    x = find(parent, x)
    y = find(parent, y)

    # print(x, y)
    parent[x] = y
    print("LADICA")
for i in range(1, N + 1):
    a, b = map(int, input().rstrip().split(' '))

    flag = 1
    if drink[a] == 0:
        drink[a] = i
        union(ladica, a, b, drink)
    else:
        if drink[b] == 0:
            drink[b] = i
            union(ladica, b, a, drink)
        else:
            if drink[find(ladica, a)] == 0:
                drink[find(ladica, a)] = i
                union(ladica, a, b, drink)
            elif drink[find(ladica, b)] == 0:
                drink[find(ladica, b)] = i
                union(ladica, b, a, drink) 
            else:
                print("SMECE")

# print(drink, ladica)