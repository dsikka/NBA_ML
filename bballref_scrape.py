import numpy as np

import pandas as pd

from basketball_reference_web_scraper import client
from basketball_reference_web_scraper import output

# HAVE TO UPDATE YEAR VALUES AND CSV FILE NAMES FOR EACH SEASON

year_month = {'first_half': {'year': 2017, 'months': np.linspace(10, 12, num=3)},
'second_half': {'year': 2018, 'months': np.linspace(1, 6, num=6)}}
days = np.linspace(1, 31, num=31)

boxscores_1 = {}
boxscores_2 = {}

# k gives first_half, second_half
# v gives all the stored values

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

output.team_box_scores_to_csv_adv(boxscores_2, '2017to2018basic.csv', 'w')
output.team_box_scores_to_csv(boxscores_1, '2017to2018adv.csv', 'w')

df1 = pd.read_csv('2017to2018basic.csv')
df2 = pd.read_csv('2017to2018adv.csv')
result = pd.concat([df2, df1], axis=1)
result.to_csv("2017to2018combined.csv", index=False, encoding='utf-8-sig')