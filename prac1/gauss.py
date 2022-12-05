def process_row(row):
    for i in range(0, n):
        A[row][i] -= cf * C[i]

def pretty_print():
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=" ")
        print(B[i])
        #print(end="\n")

n = int(input())
A = list()
B = list()
SAVED_A = A.copy()
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
    for j in range(i, n):
        if j != s:
            cf = A[j][i] / C[i]
            process_row(j)
            B[j] -= B[s] * cf
    
    pretty_print()

ans = list([0] * n)

for i in range(n - 1, -1, -1):
    x = B[i]
    for j in range(i + 1, n):
        x -= ans[j] * A[i][j]
    ans[i] = x / A[i][i]

print(ans)
import numpy as np
A = np.matrix(SAVED_A)
print("Det: " + str(np.linalg.det(A)))
for i, j in range(n):
