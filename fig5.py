import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')


data = pd.read_csv("./RFhistogram.csv", index=True)
data.plot(kind='hist', alpha=0.5, legend=False)
plt.savefig('hist1.svg', bbox_inches='tight', dpi=300)
