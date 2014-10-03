import pandas as pd
import os

default = pd.read_csv('../default/deafult_aggregate.csv')
uniform = pd.read_csv('aggregate_uniform.csv')
exp = pd.read_csv('../exp1/aggregate_exp.csv')
fixed = pd.read_csv('../fixed2/agregate_fixed2.csv')

merged_inner = pd.merge(left=default, right=uniform, left_on='Data Set', right_on='Data Set')
troi = pd.merge(left=merged_inner, right=exp, left_on='Data Set', right_on='Data Set')
agg = pd.merge(left=troi, right=fixed, left_on='Data Set', right_on='Data Set')
agg.columns = ['Data Set','Default Score','Uniform score','Exp score','fixed score']

dname = [os.path.split(item)[1] for item in dlist]
ename = [os.path.split(item)[1] for item in elist]
fname = [os.path.split(item)[1] for item in flist]
uname = [os.path.split(item)[1] for item in ulist]

dstrings = [re.sub('.nex.con.tre', '', file) for file in dname]
estrings = [re.sub('.nex.con.tre', '', file) for file in ename]
fstrings = [re.sub('.nex.con.tre', '', file) for file in fname]
ustrings = [re.sub('.nex.con.tre', '', file) for file in uname]

dstrings = [re.sub('_', ' ', file) for file in dstrings]
estrings = [re.sub('_', ' ', file) for file in estrings]
fstrings = [re.sub('_', ' ', file) for file in fstrings]
ustrings = [re.sub('_', ' ', file) for file in ustrings]

suffix = '.nex.con.tre'
d_set = agg['Data Set']
for x in agg['Index']:
    if x == 'Exp score':
        e_set = agg[agg['Index'] == 'Exp score']['Data Set']
    elif x == 'fixed score':
        f_set = agg[agg['Index'] == 'fixed score']['Data Set']
    else:
        u_set = agg[agg['Index'] == 'Uniform score']['Data Set']

set_list = ['e_set', 'f_set', 'u_set']

def find_files(sets, lists):
    se_ls = [re.sub(' ', '_', data) for data in sets]
    d_path = [os.path.split(item)[0] for item in lists]
    zipped = zip(d_path, se_ls)
    d_paths = [os.path.join(i[0], i[1]) for i in zipped]
    d_paths = [path + suffix for path in d_paths]
    return(d_paths)

def read_t(defs, paths, name):
    rfs = []
    for path in paths:
        tree2 = dendropy.Tree.get_from_path(path, 'nexus')
        path = [re.sub(name, 'default', path)]
        for p in path: 
            if p in defs:
                tree = dendropy.Tree.get_from_path(p, 'nexus')
                rfs.append(tree.symmetric_difference(tree2))
    return(rfs)


defs = find_files(d_set, dlist)
e_paths = find_files(e_set, dlist)
f_paths = find_files(f_set, dlist)
u_paths = find_files(u_set, dlist)

s = agg.groupby('Index')
subset_e = agg[agg['Index'] == 'Exp score']
e_rf = read_t(defs, e_paths, 'exp1')
subset_e['RF'] = e_rf

subset_f = agg[agg['Index'] == 'fixed score']
f_rf = read_t(defs, f_paths, 'fixed2')
subset_f['RF'] = f_rf

subset_u = agg[agg['Index'] == 'Uniform score']
u_rf = read_t(defs, u_paths, 'uniform')
subset_u['RF'] = u_rf

subset_d = agg[agg['Index'] == 'Default Score']
subset_d['RF'] = 'NaN'


catted = pd.concat([subset_d, subset_e, subset_f, subset_u])

