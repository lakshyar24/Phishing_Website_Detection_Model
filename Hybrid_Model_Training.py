import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
import pickle

# Load the dataset
data = pd.read_csv('extracted_features.csv')
X = data[['length', 'has_https', 'num_digits', 'num_special_chars', 'Have_IP', 'Have_At']]  # Specify features used
y = data['label']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the MLP model
mlp_model = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)
mlp_model.fit(X_train, y_train)

# Train the XGBoost model
xgb_model = XGBClassifier(eval_metric='logloss', random_state=42)
xgb_model.fit(X_train, y_train)

# Save the models
with open('mlp_model.pkl', 'wb') as mlp_file:
    pickle.dump(mlp_model, mlp_file)
xgb_model.save_model('XGBoostClassifier.json')
print("Models trained and saved successfully.")
