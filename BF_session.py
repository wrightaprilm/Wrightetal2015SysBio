# coding: utf-8

import pandas

default = pandas.read_csv("out", header = False)
default.columns = ['Data Set', 'Score']
default.groupby('Data Set')
s = df.groupby('Data Set')
s.sum()
t = s.sum()
t.to_csv("ugh")

uniform = pandas.read_csv("out", header = False)
uniform.columns = ['Data Set', 'Score']
s = uniform.groupby('Data Set')
t = s.sum()
t.to_csv("aggregate_uniform.csv")

exp = pd.read_csv('../exp1/aggregate_exp.csv')
fixed = pd.read_csv('../fixed2/agregate_fixed2.csv')
merged_inner = pd.merge(left=default, right=uniform, left_on='Data Set', right_on='Data Set')
troi = pd.merge(left=merged_inner, right=exp, left_on='Data Set', right_on='Data Set')
agg = pd.merge(left=troi, right=fixed, left_on='Data Set', right_on='Data Set')
agg.columns = ['Data Set','Default Score','Uniform score','Exp score','fixed score']

values = agg['Default Score'] / agg['Uniform scores']
agg['bfDU'] = values
values = agg['Default Score'] / agg['Fixed scores']
agg['bfDF'] = values
values = agg['Default Score'] / agg['Exp scores']
agg['bfDE'] = values
