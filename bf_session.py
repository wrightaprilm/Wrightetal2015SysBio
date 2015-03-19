import pandas as pd
import os
import re
import dendropy
from dendropy.utility.fileutils import find_files
import matplotlib.pyplot as plt
plt.style.use('ggplot')

exp = pd.read_csv('m8ee_SS')
exp = exp.dropna()
uniform = pd.read_csv('m8e1_SS')
uniform = uniform.dropna()
default = pd.read_csv('m8ed_SS')
default = default.dropna()
fixed = pd.read_csv('m8e2_SS')
fixed = fixed.dropna()

uniform.columns = ['a','uniform']
default.columns = ['a','default']
exp.columns = ['a','exp']
fixed.columns = ['a','fixed']
uniform = uniform.drop('a',axis=1)
fixed =fixed.drop('a',axis=1)
exp =exp.drop('a',axis=1)
default =default.drop('a',axis=1)



merged_inner = pd.merge(left=default, right=exp, left_index=True, right_index = True)
merged_inner = pd.merge(left=merged_inner, right=fixed, left_index=True, right_index = True)
merged_inner = pd.merge(left=merged_inner, right=uniform, left_index=True, right_index = True)
merged_inner['maxdex'] = merged_inner.idxmax(axis=1)
a = mi.values
a.sort(axis=1)
a = a[:, ::-1]
a = pd.DataFrame(a, mi.index, mi.columns)
a['bf'] = a['exp']-a['fixed']
pref_df = pd.DataFrame(a['bf'])
pref_df['max'] = merged_inner['maxdex']
pref_df.to_csv('preferences.csv')
b = merged_inner.groupby('maxdex').count()

