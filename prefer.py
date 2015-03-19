import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df = pd.read_csv('prefs.csv')
df.pivot(index='prior',columns='missing',values='prop').plot(kind='bar')
plt.show()
