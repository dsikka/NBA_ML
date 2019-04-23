#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:06:15 2019

@author: scalazar
"""

from basketball_reference_web_scraper import client
import pandas as pd
import pytz
import time


def add_points(season_end_year = 2018):

	start_time = time.time() #for timing how this takes
	
	
	path = 'scraped_data_combined/' + str(season_end_year - 1) + 'to' + \
	                     str(season_end_year) + 'combined.csv'
	df = pd.read_csv(path)
	df.insert(df.shape[1] - 1, 'points', 0)
	
	
	games = client.season_schedule(season_end_year=season_end_year)
	est = pytz.timezone("US/Eastern")
	for game in games:
	    
	    date = game['start_time'].astimezone(est).strftime('%Y-%m-%d')
	    home_row_num = df.loc[(df['team'] == game['home_team'].value) & \
	                             (df['date'] == date)].index[0]
	    away_row_num = df.loc[(df['team'] == game['away_team'].value) & \
	                             (df['date'] == date)].index[0]
	    
	    df['points'][home_row_num] = game['home_team_score']
	    df['points'][away_row_num] = game['away_team_score']
	    
	    
	    print(date + ': ' + game['away_team'].value + ' at ' + game['home_team'].value)
	    
	
	df.to_csv(path, index=False, encoding='utf-8-sig')
	
	
	end_time = time.time() #for timing how this takes
	print('Time required = %d s.' % round(end_time - start_time))
    

for i in range(2008, 2019):
    add_points(i)