#Script for plotting three ways in which I looked at the empirical data
import pandas as pd
from ggplot import *
big_df = pd.read_csv('big_df')
ggplot(aes(x=big_df['NTax'],y=big_df['Best Score'], color='Rejected Default'), data=big_df) + geom_point() + stat_smooth()
ggplot(aes(x=big_df['NChar'],y=big_df['Best Score'], color='Rejected Default'), data=big_df) + geom_point() + stat_smooth()
ggplot(aes(x=divisor,y=big_df['Best Score'], color='Rejected Default'), data=big_df) + geom_point() + stat_smooth()
ggplot(aes(x=big_df.NChar,y=big_df.NTax, color='Rejected Default'), data=big_df) + geom_point() + stat_smooth()

