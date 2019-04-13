#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:10:06 2019

@author: scalazar
"""

import csv
import time
from basketball_reference_web_scraper import client


season_end_year = 2018


start_time = time.time() #for timing how this takes

#averages_file = open('averages.csv', 'w')
#
#averages_file.write('header1,' + \
#                    'header2' + \
#                    '\n')


games = client.season_schedule(season_end_year=season_end_year)
for game in games:
    
    home_team_won = 0
    if game['home_team_score'] > game['away_team_score']:
        home_team_won = 1
    
    print(game['start_time'].strftime('%m/%d/%Y') + ': ' + game['home_team'].value + ' vs. ' + game['away_team'].value)


#    data = [1, 2] #placeholder code
#
#    averages_str = str(data[0])
#    averages_str += ',' + str(data[1])
#    averages_str += '\n'
#    averages_file.write(averages_str)
    
    
    break #only look at one game when testing code
    
    
#averages_file.close()

end_time = time.time() #for timing how this takes
print('Time required = %d s.' % round(end_time - start_time))