import json
import re

import numpy as np
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


def get_feature_names(path):
    names = []
    regex = re.compile(r'^(.+)\:\s+(.+)\.$')

    with open(path) as file:
        for line in file:
            match = regex.match(line)
            if match:
                names.append(match.group(1))

    return names


feature_names = get_feature_names('../../../../spambase/spambase.names')
with open("feature_names.json", "w") as f:
    json.dump(feature_names, f)

data = np.genfromtxt('../../../../spambase/spambase.data', delimiter=',')

X, y = data[:, :-1], data[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

clf = SVC(gamma=0.0001, C=10000)
clf.fit(X_train, y_train)

dump(clf, 'model.joblib')
dump(scaler, 'scaler.joblib')

y_pred = clf.predict(X_test)
accuracy = 1 - (np.sum(y_pred != y_test) / y_test.shape[0])
print(f'Accuracy: {accuracy * 100:.{4}}%')
