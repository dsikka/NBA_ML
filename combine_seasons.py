import os
import pandas as pd 
import re

from os import path

data_path = 'scraped_data_combined'
files = os.listdir(data_path)

"""
@author: dsikka
- Add a 'Season' label for each year
- Separate data between playoff and non-playoff data for each season
- Combine all the seasons together
- Allows one csv with features which are to be further investigated 

"""

playoff_start_dates = {'2007to2008' : '2008-04-19',
                      '2008to2009' : '2009-04-18',
                      '2009to2010' : '2010-04-17',
                      '2010to2011' : '2011-04-16',
                      '2011to2012' : '2012-04-28',
                      '2012to2013' : '2013-04-20',
                      '2013to2014' : '2014-04-19',
                      '2014to2015' : '2015-04-18',
                      '2015to2016' : '2016-04-16',
                      '2016to2017' : '2017-04-15',
                      '2017to2018' : '2018-04-14'}

for file in files:
   fullPath = os.path.join(data_path, file)
   df = pd.read_csv(fullPath)
   s = re.match("(\w+)combined.csv", file).group(1)
   s = s.replace("to", '-')
   df.insert(0, 'Season', s)
   df.columns.values[0] = 'season' #rename 'Season' to 'season'
   df.insert(df.shape[1], 'during_playoffs', df['date'] >= playoff_start_dates[s])
   df['during_playoffs'] = df['during_playoffs'].astype(int)
   df.to_csv(fullPath, index=False, encoding='utf-8-sig')
    

# Combine all the seasons together
combined_csv = pd.concat([pd.read_csv(os.path.join(data_path, file)) for file in files], axis=0)
combined_csv.to_csv("season_combined.csv", index=False, encoding='utf-8-sig')
