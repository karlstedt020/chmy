import math
import matplotlib.pyplot as plt

def p(x):
    return 1

def q(x):
    return -2

def f(x):
    return 0

x1, x2 = 0, 1
n = 5
h = (x2 - x1) / n
sgm1, gmm1, dlt1 = 1, -1, 0
sgm2, gmm2, dlt2 = 1, 1, 2 * math.exp(1)
arr = []
arr.append([0, sgm1 - gmm1 / h, gmm1 / h, dlt1])
x = x1
for i in range(1, n):
    x += h
    arr.append([1 - p(x) * h / 2, q(x) * h * h - 2, 1 + p(x) * h / 2, f(x) * h * h])
arr.append([gmm2 / h, sgm2 - gmm2 / h, 0, dlt2])
#получилась готовая матрица, к которой необходимо применить метод прогонки

alpha, beta = 0, 0
y_s = []
x_s = []
cfs = []
y = 0
for i in range(n + 1):
    [a, b, c, d]  = arr[i]
    if i == 0:
        y = b
    else:
        y = b + a * alpha
    if i == 0:
        alpha = -c / y
        beta = d / y
    elif i != n:
        alpha = -c / y
        beta = (d - a * beta) / y
    else:
        alpha = 0
        beta = (d - a * beta) / y
    cfs.append([alpha, beta])
x = x2
for i in range(n, -1, -1):
    [alpha, beta] = cfs[i]
    if i == n:
        y = beta
    else:
        y = alpha * y + beta
    y_s.append(y)
    x_s.append(x)
    x -= h

plt.plot(x_s, y_s, label='runge_kutta')
plt.legend()
plt.show()