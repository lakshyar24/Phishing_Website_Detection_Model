from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform, randint
import pickle
import pandas as pd

# Load data
data = pd.read_csv('selected_features.csv')
X = data.drop('label', axis=1).astype(float)  # Ensure data is numeric
y = data['label']

# Parameter grid with reduced `n_iter`
param_grid = {
    'mlp__hidden_layer_sizes': [(64,), (64, 32), (128, 64)],
    'mlp__alpha': uniform(0.0001, 0.1),
    'mlp__learning_rate_init': uniform(0.0001, 0.01),
    'xgb__max_depth': randint(3, 10),
    'xgb__learning_rate': uniform(0.01, 0.3),
    'xgb__n_estimators': randint(50, 100)  # Reduced to speed up tuning
}

# Load initial model
with open('stacked_model.pkl', 'rb') as model_file:
    stacking_model = pickle.load(model_file)

# Run randomized search with reduced n_iter
random_search = RandomizedSearchCV(
    estimator=stacking_model,
    param_distributions=param_grid,
    n_iter=10,  # Reduced iterations to make tuning faster
    scoring='accuracy',
    cv=3,
    random_state=42,
    n_jobs=-1
)

# Fit random search
random_search.fit(X, y)
best_model = random_search.best_estimator_

# Save tuned model
with open('stacked_model_tuned.pkl', 'wb') as model_file:
    pickle.dump(best_model, model_file)

print("Tuned stacked model saved as 'stacked_model_tuned.pkl'")
