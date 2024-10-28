import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0
b = 2
n_points = 10000
y_min = 0
y_max = f(b)

# Метод Монте-Карло
x_random = np.random.uniform(a, b, n_points)
y_random = np.random.uniform(y_min, y_max, n_points)
under_curve = y_random < f(x_random)
integral_mc = (under_curve.sum() / n_points) * (b - a) * y_max

print("Метод Монте-Карло: інтеграл ≈", integral_mc)

result, error = spi.quad(f, a, b)
print("Аналітичний результат (quad): інтеграл =", result, "±", error)

x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3, label='Область під кривою')

ax.scatter(x_random, y_random, c=under_curve, cmap='bwr', alpha=0.3, s=1)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([y_min, y_max + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Метод Монте-Карло для обчислення інтегралу f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.legend()
plt.grid()
plt.show()
