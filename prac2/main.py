import math
import matplotlib.pyplot as plt

def f1(x, y1 = 0, y2 = 0):
    return math.cos(x + 1.1 * y2) + y1
def f2(x, y1, y2):
    return -y2 * y2 + 2.1 * y1 + 1.1

def iterate(x, y, dx, f1, f2):
    try:
        k1 = f1(x, y[0], y[1]) * dx
    except Exception as e:
        print(y[0], y[1])
        raise
    k2 = f1(x + 0.5 * dx, y[0] + 0.5 * k1, y[1] + 0.5 * k1) * dx
    k3 = f1(x + 0.5 * dx, y[0] + 0.5 * k2, y[1] + 0.5 * k2) * dx
    k4 = f1(x + 0.5 * dx, y[0] + 0.5 * k3, y[1] + 0.5 * k3) * dx
    k5 = f2(x, y[0], y[1]) * dx
    k6 = f2(x + 0.5 * dx, y[0] + 0.5 * k5, y[1] + 0.5 * k5) * dx
    k7 = f2(x + 0.5 * dx, y[0] + 0.5 * k6, y[1] + 0.5 * k6) * dx
    k8 = f2(x + 0.5 * dx, y[0] + 0.5 * k7, y[1] + 0.5 * k7) * dx
    new_y = [y[0] + (k1 + 2 * k2 + 2 * k3 + k4) / 6, y[1] + (k5 + 2 * k6 + 2 * k7 + k8) / 6]
    return new_y

x = 0
y = [0.25, 1]
ans_x, ans_y = [], []
dx = 0.01
while (x <= 3):
    x += dx
    y = iterate(x, y, dx, f1, f2)
    ans_x.append(x)
    ans_y.append(y)
    print(x)
plt.plot(ans_x, ans_y, label='runge_kutta')
#plt.plot(ans_x, [-0.5 * math.sin(t[0]) + 0.5 * math.cos(t[0]) + 21/2 * math.exp(-t[0]) for t in ans_x], label='exact')
plt.legend()
plt.show()