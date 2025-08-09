import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, accuracy_score
from loan_ml_pipeline import get_pipeline

df = pd.read_csv('../data/prepared_loan_data.csv')

X = df.drop(['Loan_Status', 'Loan_ID'], axis=1)
y = df['Loan_Status']

numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()
categorical_features = [col for col in X.columns if col not in numeric_features]

pipeline, preprocessor = get_pipeline(numeric_features, categorical_features)

param_grid = {
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [5, 10, None],
    'classifier__min_samples_split': [2, 5]
}

gs = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
gs.fit(X, y)

print("Best params:", gs.best_params_)
print("Best score:", gs.best_score_)

joblib.dump(gs.best_estimator_, 'model.pkl')
joblib.dump(gs.best_estimator_.named_steps['preprocessor'], 'preprocessors.pkl')

importances = gs.best_estimator_.named_steps['classifier'].feature_importances_
importances_file = '../predictor/static/predictor/plots/feature_importance.png'

import matplotlib.pyplot as plt
feat_names = (
    numeric_features +
    list(gs.best_estimator_.named_steps['preprocessor']
         .transformers_[1][1]
         .get_feature_names_out(categorical_features))
)
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(12,6))
plt.title("Feature importances")
plt.bar(range(len(importances)), importances[indices], align="center")
plt.xticks(range(len(importances)), [feat_names[i] for i in indices], rotation=90)
plt.tight_layout()
plt.savefig(importances_file)
plt.close()