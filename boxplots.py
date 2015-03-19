import pandas as pd
import os
import re
import dendropy
from dendropy.utility.fileutils import find_files
import matplotlib.pyplot as plt
plt.style.use('ggplot')

default = pd.read_csv('./d.csv')
uniform = pd.read_csv('./1.csv')
exp = pd.read_csv('./e.csv')
fixed = pd.read_csv('./2.csv')

uniform.columns = ['a','uni', 'b','c','d']
default.columns = ['a','def', 'b','c','d']
exp.columns = ['a','exp', 'b','c','d']
fixed.columns = ['a','fix', 'b','c','d']


uniform = uniform.drop(['b','c','d'],axis=1)
fixed =fixed.drop(['b','c','d'],axis=1)
exp =exp.drop(['b','c','d'],axis=1)
default =default.drop(['b','c','d'],axis=1)



merged_inner = pd.merge(left=default, right=exp, left_on='a', right_on = 'a')
merged_inner = pd.merge(left=merged_inner, right=fixed,left_on='a', right_on = 'a')
merged_inner = pd.merge(left=merged_inner, right=uniform, left_on='a', right_on = 'a')


merged_inner['default'] = merged_inner['def']/10
merged_inner['expo'] = merged_inner['exp']/10
merged_inner['fixed'] = merged_inner['fix']/10
merged_inner['uniform'] = merged_inner['uni']/10
merged_inner = merged_inner.drop(['def','exp','fix','uni','a'],axis=1)
merged_inner.plot(kind='box').set_ylim(-.2,1)
plt.show()
