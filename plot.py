import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('plotdata.csv')

df.plot()

plt.show()