def process_row(row, cf):
    for i in range(0, n):
        A[row][i] -= cf * C[i]

def pretty_print():
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=" ")
        print(end="\n")

n = int(input())
A = list()
B = list()
for i in range(n):
    now = input().split()
    now = list(map(int, now))
    B.append(now[-1])
    now = now[:-1]
    A.append(now)

for i in range(n):
    C = list()
    s = -1
    for j in range(i, n):
        if A[j][i] != 0:
            s = j
            break
    if s == -1:
        continue
    C = A[s].copy()
    for j in range(i + 1, n):
        process_row(j, A[j][i] / C[i])
        B[j] -= B[s] * (A[j][i] / C[i])
    #pretty_print()

