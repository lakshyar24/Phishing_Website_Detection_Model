import pandas as pd
import pickle
from URLFeatureExtraction_Advanced import extract_features

# Load the tuned model
def load_model():
    with open('stacked_model_tuned.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

model = load_model()

# Load expected feature names from selected_features.csv
selected_features_df = pd.read_csv('selected_features.csv')
expected_features = selected_features_df.drop('label', axis=1).columns.tolist()

# Check if URL is blacklisted
def check_blacklist(url):
    try:
        urls_df = pd.read_csv('urls.csv')
        return url in urls_df[urls_df['Blacklisted'] == 1]['url'].values
    except FileNotFoundError:
        return False

# Predict phishing
def predict_phishing(url, model):
    if check_blacklist(url):
        return "Phishing (Blacklisted)"
    
    features = extract_features(url)
    features_df = pd.DataFrame([features])

    # Ensure features_df has the correct columns in the right order
    features_df = features_df.reindex(columns=expected_features, fill_value=0)

    # Predict using the loaded model
    prediction = model.predict(features_df)
    return "Phishing" if prediction == 1 else "Legitimate"

# Update blacklist
def update_blacklist_status(url, status=1):
    try:
        urls_df = pd.read_csv('urls.csv')
        if url in urls_df['url'].values:
            urls_df.loc[urls_df['url'] == url, 'Blacklisted'] = status
        else:
            new_entry = pd.DataFrame({'url': [url], 'label': [1], 'Blacklisted': [status]})
            urls_df = pd.concat([urls_df, new_entry], ignore_index=True)
        urls_df.to_csv('urls.csv', index=False)
    except FileNotFoundError:
        urls_df = pd.DataFrame({'url': [url], 'label': [1], 'Blacklisted': [status]})
        urls_df.to_csv('urls.csv', index=False)

def main():
    print("Phishing Website Detection CLI")

    while True:
        url = input("\nEnter a URL to check (or type 'exit' to quit): ").strip()
        if url.lower() == 'exit':
            print("Exiting...")
            break
        
        prediction = predict_phishing(url, model)
        print(f"The URL '{url}' is predicted to be: {prediction}")

        # Offer options based on prediction
        if prediction == "Legitimate":
            choice = input("Would you like to blacklist this URL as phishing? (y/n): ").strip().lower()
            if choice == 'y':
                update_blacklist_status(url, status=1)
                print(f"The URL '{url}' has been blacklisted.")
        elif prediction == "Phishing (Blacklisted)":
            choice = input("This URL is blacklisted as phishing. Would you like to whitelist it? (y/n): ").strip().lower()
            if choice == 'y':
                update_blacklist_status(url, status=0)
                print(f"The URL '{url}' has been whitelisted and marked as legitimate.")

if __name__ == "__main__":
    main()
