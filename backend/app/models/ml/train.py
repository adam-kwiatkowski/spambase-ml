import json
import re

import numpy as np
from joblib import dump
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def get_feature_names(path):
    names = []
    regex = re.compile(r'^(.+)\:\s+(.+)\.$')

    with open(path) as file:
        for line in file:
            match = regex.match(line)
            if match:
                names.append(match.group(1))

    return names


dataset_dir = '../../../../spambase/'
feature_names = get_feature_names(dataset_dir + 'spambase.names')
with open("feature_names.json", "w") as f:
    json.dump(feature_names, f)

data = np.genfromtxt(dataset_dir + 'spambase.data', delimiter=',')

X, y = data[:, :-1], data[:, -1]

pipeline = Pipeline([
    ('feature_selection', SelectKBest(chi2, k=45)),
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(n_estimators=300, max_features='log2'))
])

pipeline.fit(X, y)

dump(pipeline, 'model.joblib')
