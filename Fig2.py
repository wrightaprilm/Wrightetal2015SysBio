import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

dat = pd.read_csv('../Data/empirical_prefs.csv')

dat['sets'].plot(kind='pie')

plt.show()

