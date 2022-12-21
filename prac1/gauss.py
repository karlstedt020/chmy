def process_row(row):
    for i in range(0, n):
        A[row][i] -= cf * C[i]

def pretty_print():
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=" ")
        print(B[i])
        #print(end="\n")

def check(x1, x2, eps, n):
    for i in range(n):
        if abs(x1[i] - x2[i]) >= eps:
            return 1
    return 0

#n = int(input())
n = 25
A = list()
B = list()
for i in range(n):
    """
    now = input().split()
    now = list(map(int, now))
    B.append(now[-1])
    now = now[:-1]
    A.append(now)
    """
    m = 10
    A.append([])
    for j in range(n):
        if i != j:
            A[i].append((i + j) / (m + n))
        else:
            A[i].append(n + m * m + j / m + i / n)
    B.append(i * i - n)

SAVED_A = []
for x in A:
    SAVED_A.append(x.copy())
SAVED_B = B.copy()

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
    
    #pretty_print()

ans = list([0] * n)

for i in range(n - 1, -1, -1):
    x = B[i]
    for j in range(i + 1, n):
        x -= ans[j] * A[i][j]
    ans[i] = x / A[i][i]

print(ans)

A = SAVED_A
B = SAVED_B

x1 = []
for i in range(n):
    for j in range(i, n):
        try:
            x1.append(B[i] / A[i][i])
            k = B[j]
            B[j] = B[i]
            B[i] = k
            k = A[j].copy()
            A[j] = A[i].copy()
            A[i] = k.copy()
        except ZeroDivisionError:
            continue
#print(x1)
x2 = []
for i in range(n):
    curr = B[i] / A[i][i]
    for j in range(i):
        curr -= x2[j] * (A[i][j] / A[i][i])
    for j in range(i + 1, n):
        curr -= x1[j] * (A[i][j] / A[i][i])
    x2.append(curr)
#print(x2)
while check(x1, x2, 0.0001, n):
    x1 = x2.copy()
    x2 = []
    for i in range(0, n):
        curr = B[i] / A[i][i]
        for j in range(0, i):
            #print(j, ' ', i)
            curr -= x2[j] * (A[i][j] / A[i][i])
        for j in range(i + 1, n):
            curr -= x1[j] * (A[i][j] / A[i][i])
        x2.append(curr)
    #print(x2)
print(x2)