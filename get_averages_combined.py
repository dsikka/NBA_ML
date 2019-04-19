#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:44:03 2019

@author: scalazar
"""

import os
import pandas as pd


averages_dir = 'averages'
files = os.listdir(averages_dir)

csv_files = []
for file in files:
    if file.lower().endswith('.csv'): #to avoid errors with hidden files
        csv_files.append(file)
    
combined_df = pd.concat( \
    [pd.read_csv(os.path.join(averages_dir, file)) for file in csv_files])
combined_df.to_csv(averages_dir + '/averages_combined.csv', index = False)