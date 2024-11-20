import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif

# Load dataset
data = pd.read_csv('extracted_features.csv')

# Separate features and labels
X = data.drop('label', axis=1)
y = data['label']

# Drop constant features
X = X.loc[:, (X != X.iloc[0]).any()]
print("Remaining features after dropping constants:", X.columns.tolist())

# If we have more than 3 features remaining, apply SelectKBest; otherwise, use remaining features
if X.shape[1] > 3:
    k = min(3, X.shape[1])  # Set k to a smaller value or to the total number of features
    selector = SelectKBest(f_classif, k=k)
    X_selected = selector.fit_transform(X, y)
    selected_features = X.columns[selector.get_support(indices=True)]
else:
    X_selected = X.values
    selected_features = X.columns.tolist()

# Save selected features for use in model training
X_selected_df = pd.DataFrame(X_selected, columns=selected_features)
X_selected_df['label'] = y
X_selected_df.to_csv('selected_features.csv', index=False)

print("Feature engineering completed. Selected features saved in 'selected_features.csv'")
