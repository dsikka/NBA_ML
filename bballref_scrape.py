import numpy as np

from basketball_reference_web_scraper import client
from basketball_reference_web_scraper import output

# HAVE TO UPDATE YEAR VALUES AND CSV FILE NAMES FOR EACH SEASON

year_month = {'first_half': {'year': 2014, 'months': np.linspace(10, 12, num=3)},
'second_half': {'year': 2015, 'months': np.linspace(1, 6, num=6)}}
days = np.linspace(1, 31, num=31)

box_scores = {}

# k gives first_half, second_half
# v gives all the stored values
for k,v in year_month.items():
    for month in v['months']:
        for day in days:
            date_list = [str(v['year']), str(month), str(day)]
            s = '-'
            date_formatted =s.join(date_list)
            box_score = client.team_box_scores(day=int(day), month=int(month),year=int(v['year']))
            if len(box_score) is not 0:
                box_scores.update({date_formatted: box_score})
                
output.team_box_scores_to_csv(box_scores, '2014to2015.csv', 'w')