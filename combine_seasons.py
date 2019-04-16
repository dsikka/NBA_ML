import os
import pandas as pd 
import re

from os import path

data_path = 'scraped_data_combined'
files = os.listdir(data_path)

# Add season column to each combined data file

for file in files:
	fullPath = os.path.join(data_path, file)
	df = pd.read_csv(fullPath)
	s = re.match("(\w+)combined.csv", file).group(1)
	s = s.replace("to", '-')
	df.insert(0, 'Season', s)
	df.to_csv(fullPath, index=False, encoding='utf-8-sig')


# Combine all the seasons together
combined_csv = pd.concat([pd.read_csv(os.path.join(data_path, file)) for file in files], axis=0)
combined_csv.to_csv("season_combined.csv", index=False, encoding='utf-8-sig')
