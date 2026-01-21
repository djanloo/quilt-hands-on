import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("eeg_brainstorm_65.txt", delim_whitespace=True, header=None, names=["nome", "x", "y", "z"])

print(df)

names = df["nome"].values
x = df['x'].values
y = df['y'].values

plt.scatter(x, y)
for nn, xx, yy in zip(names,x,y):
    plt.annotate(nn, (xx, yy), va="center", ha="center")
plt.show()
