import pandas as pd


data = pd.read_csv("./histogram.csv")
data.plot(kind='bar', legend=False)
plt.savefig('hist1.svg', bbox_inches='tight', dpi=300)
