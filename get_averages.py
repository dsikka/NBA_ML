#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:10:06 2019

@author: scalazar
"""

import csv
import time
from basketball_reference_web_scraper import client
import pandas as pd
import pytz


#script parameters
season_end_year = 2018


start_time = time.time() #for timing how this takes

df = pd.read_csv('season_combined.csv')
df = df.sort_values(by = ['Season', 'team', 'date'])

averages_file = open('averages/averages' + str(season_end_year - 1) + 'to' + \
                     str(season_end_year) + '.csv', 'w')

str_to_write = 'season,date,home_team'
for i in range(3, len(df.columns)):
    str_to_write += ',' + df.columns[i] + '_home'
for i in range(3, len(df.columns)):
    str_to_write += ',' + df.columns[i] + '_away'
str_to_write += ',home_won\n'
averages_file.write(str_to_write)


games = client.season_schedule(season_end_year=season_end_year)
season = str(season_end_year - 1) + '-' + str(season_end_year)
est = pytz.timezone("US/Eastern")
for game in games:
    
    #can't calculate average from last 6 games if 6 games haven't been played yet
    date = game['start_time'].astimezone(est).strftime('%Y-%m-%d')
    home_prev_games = df.loc[(df['Season'] == season) & \
                             (df['team'] == game['home_team'].value) & \
                             (df['date'] < date)]
    away_prev_games = df.loc[(df['Season'] == season) & \
                             (df['team'] == game['away_team'].value) & \
                             (df['date'] < date)]
    if home_prev_games.shape[0] < 6 or away_prev_games.shape[0] < 6:
        continue
    
    
    #get averages from last 6 games and winner
    home_averages = home_prev_games.iloc[-6:].mean()
    away_averages = away_prev_games.iloc[-6:].mean()
    
    home_won = 0
    if game['home_team_score'] > game['away_team_score']:
        home_won = 1
    

    str_to_write = season + ',' + date + ',' + game['home_team'].value
    for i in range(len(home_averages)):
        str_to_write += ',' + str(home_averages[i])
    for i in range(len(away_averages)):
        str_to_write += ',' + str(away_averages[i])
    str_to_write += ',' + str(home_won) + '\n'
    averages_file.write(str_to_write)
    
    
    print(date + ': ' + game['away_team'].value + ' at ' + game['home_team'].value)
    
    
averages_file.close()

end_time = time.time() #for timing how this takes
print('Time required = %d s.' % round(end_time - start_time))