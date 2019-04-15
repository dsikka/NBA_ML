import os
import pandas as pd 

files = ['2013to2014combined.csv', '2014to2015combined.csv', '2015to2016combined.csv', 
'2016to2017combined.csv', '2017to2018combined.csv']

combined_csv = pd.concat([pd.read_csv(f) for f in files], axis=0)
combined_csv.to_csv("season_combined.csv", index=False, encoding='utf-8-sig')
