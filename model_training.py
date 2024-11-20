import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
import pickle

# Load engineered features
data = pd.read_csv('selected_features.csv')
X = data.drop('label', axis=1)
y = data['label']

# Ensure data is numeric
X = X.astype(float)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define base and meta-models for stacking
mlp = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=1000, random_state=42)  # Increased max_iter
xgb = XGBClassifier(eval_metric='logloss', random_state=42)
meta_model = LogisticRegression()

# Create and train the stacking model
stacking_model = StackingClassifier(
    estimators=[('mlp', mlp), ('xgb', xgb)],
    final_estimator=meta_model,
    cv=3
)
stacking_model.fit(X_train, y_train)

# Save the trained model
with open('stacked_model.pkl', 'wb') as model_file:
    pickle.dump(stacking_model, model_file)

print("Stacked model trained and saved as 'stacked_model.pkl'")
