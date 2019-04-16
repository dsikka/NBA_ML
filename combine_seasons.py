import os
import pandas as pd 

#files = ['2013to2014combined.csv', '2014to2015combined.csv', '2015to2016combined.csv', 
#'2016to2017combined.csv', '2017to2018combined.csv']
#
#combined_csv = pd.concat([pd.read_csv(f) for f in files], axis=0)
#combined_csv.to_csv("season_combined.csv", index=False, encoding='utf-8-sig')

df2014 = pd.read_csv('./scraped_data_combined/2013to2014combined.csv')
df2014['season'] = '2013-2014'

df2015 = pd.read_csv('./scraped_data_combined/2014to2015combined.csv')
df2015['season'] = '2014-2015'

df2016 = pd.read_csv('./scraped_data_combined/2015to2016combined.csv')
df2016['season'] = '2015-2016'

df2017 = pd.read_csv('./scraped_data_combined/2016to2017combined.csv')
df2017['season'] = '2016-2017'

df2018 = pd.read_csv('./scraped_data_combined/2017to2018combined.csv')
df2018['season'] = '2017-2018'

combined_csv = pd.concat([df2014, df2015, df2016, df2017, df2018], axis=0)
combined_csv.to_csv('seasons_combined.csv', index=False, encoding='utf-8-sig')