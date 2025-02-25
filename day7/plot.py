import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

sns.set(style="whitegrid")
x = np.linspace(0, 10, 100)
y = np.sin(x)
df = pd.DataFrame({'x': x, 'y': y})
plt.figure(figsize=(8, 6))
plt.plot(df['x'], df['y'], label='sin(x)', color='blue', linewidth=2)
plt.xlabel('X-axis (radians)')
plt.ylabel('Y-axis (sin(x))')
plt.title('Plot of sin(x)')
plt.legend()
plt.show()
