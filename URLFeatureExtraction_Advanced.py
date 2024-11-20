import os
import pandas as pd
import re
import tldextract  # Ensure this is installed with `pip install tldextract`

def extract_features(url):
    features = {}

    # Extract features with names that match the training data
    features['length'] = len(url)
    features['has_https'] = int('https' in url.lower())
    features['num_digits'] = sum(c.isdigit() for c in url)
    features['num_special_chars'] = sum(not c.isalnum() for c in url)
    features['Have_IP'] = int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url)))  # Ensure correct feature name
    features['Have_At'] = int('@' in url)  # Ensure correct feature name

    return features

def main():
    # Load URLs and extract features
    if not os.path.exists('urls.csv'):
        print("Error: 'urls.csv' file not found. Please provide a file with URLs and labels.")
        return
    
    url_data = pd.read_csv('urls.csv')
    url_data['features'] = url_data['url'].apply(extract_features)
    url_features_df = pd.json_normalize(url_data['features'])
    url_features_df['label'] = url_data['label']
    url_features_df.to_csv('extracted_features.csv', index=False)
    print("Feature extraction complete. Saved to extracted_features.csv")

if __name__ == '__main__':
    main()
