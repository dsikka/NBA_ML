import os
import pandas as pd 
import sklearn.feature_selection

import matplotlib.pyplot as plt
import numpy as np

from os import path
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFECV
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
from sklearn.model_selection import StratifiedKFold
from sklearn.svm import SVC

data_path = 'averages/averages_combined.csv'
df = pd.read_csv(data_path)

# Include home won/loss data
y = df['home_won']
# Include all other training data apart from specific ones
X = df.drop(['season', 'date', 'home_team', 'home_won'], axis=1)

# Univariate feature selection
# Different methods SelectKBest, SelectPercentile
# using chi2 or f_classif results in slightly 
# different answers

# Should set max_depth and min_samples_leaf
clf = RandomForestClassifier(n_estimators=10, random_state=0, n_jobs=-1)
# Train model

# Importance are "gini importance" or "mean decrease impurity" and is the "total decrease in node impurity weighted
# by the probability of reaching the node"

model = clf.fit(X, y)
importances = model.feature_importances_
# Sort feature importances in descending order
indices = np.argsort(importances)[::-1]
# Rearrange feature names so they match the sorted feature importances
names = [X.columns.values[i] for  i in indices]
print(names[:5])
plt.figure()
plt.title("Feature Importance")
plt.barh(range(X.shape[1]), importances[indices], align='center')
plt.gca().invert_yaxis()
plt.yticks(range(X.shape[1]), names, rotation=0)
plt.show()

# Feature selection using scores
# Recursive feature elimination 
# SelectFromModel
rfecv = RFECV(estimator=clf, step=1, cv=StratifiedKFold(5),
              scoring='accuracy')
selector = rfecv.fit(X, y)
print("Optimal number of features : %d" % rfecv.n_features_)
column_names_3 = X.columns[selector.get_support()]
print(rfecv.ranking_)
print(column_names_3)
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()



'''K = 10
percentage = 18
method = chi2
X_indices = np.arange(X.shape[-1])


selected_vals = SelectKBest(method, k=K)
X_new_K = selected_vals.fit(X, y)
column_names = X.columns[selected_vals.get_support()]

selected_vals_2 = SelectPercentile(method, percentage)
X_new_K_2 = selected_vals_2.fit_transform(X, y)
column_names_2 = X.columns[selected_vals_2.get_support()]

# Print the selected top 5 features
print(column_names)
print(column_names_2)
'''
