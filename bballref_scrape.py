
"""
@author: dsikka
- Script written to extract advanced and basic statistics for one season
- Makes used of basketball_reference_web_scraper module, which has been modified 
for this specific project 

"""

import numpy as np
import pandas as pd

from basketball_reference_web_scraper import client
from basketball_reference_web_scraper import output


year_month = {'first_half': {'year': 2012, 'months': np.linspace(10, 12, num=3)},
'second_half': {'year': 2013, 'months': np.linspace(1, 6, num=6)}}
days = np.linspace(1, 31, num=31)

boxscores_1 = {}
boxscores_2 = {}


for k,v in year_month.items():
    for month in v['months']:
        for day in days:
            date_list = [str(int(v['year'])), str(int(month)).zfill(2), str(int(day)).zfill(2)]
            s = '-'
            date_formatted =s.join(date_list)
            box_score_1 = client.team_box_scores(day=int(day), month=int(month), year=int(v['year']), adv=False)
            box_score_2 = client.team_box_scores(day=int(day), month=int(month), year=int(v['year']), adv=True)
            if len(box_score_2) is not 0:
                boxscores_1.update({date_formatted: box_score_1})
                boxscores_2.update({date_formatted: box_score_2})

output.team_box_scores_to_csv_adv(boxscores_2, '2012to2013adv.csv', 'w')
output.team_box_scores_to_csv(boxscores_1, '2012to2013basic.csv', 'w')

df1 = pd.read_csv('2012to2013adv.csv')
df2 = pd.read_csv('2012to2013basic.csv')
result = pd.concat([df2, df1], axis=1)
result.to_csv("2012to2013combined.csv", index=False, encoding='utf-8-sig')