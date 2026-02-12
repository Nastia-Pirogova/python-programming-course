import matplotlib.pyplot as plt

import numpy as np

#Y(x)=2^x*sin(10x), x=[-3...3]

x = np.linspace(-3, 3, 500)

y = 2**x * np.sin(10 * x)

plt.plot(x, y, label='y = 2^x · sin(10x)', linewidth=3)

plt.title('Графік функції y = 2^x · sin(10x)', fontsize=14)

plt.xlabel('t', fontsize=12, color='blue')
plt.ylabel('y', fontsize=12, color='blue')
plt.legend()
plt.grid(True)

plt.show()