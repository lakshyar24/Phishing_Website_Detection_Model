import streamlit as st
import numpy as np
import pickle
from URLFeatureExtraction import featureExtraction  # Import the feature extraction function from URLFeatureExtraction.py

# Load the pre-trained model
def load_model():
    with open('mlp_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Predict if a URL is phishing based on extracted features
def predict_phishing(features):
    model = load_model()
    try:
        prediction = model.predict(np.array([features]))
        return prediction
    except Exception as e:
        st.write(f"Error in predict_phishing: {e}")
        return None

# Main function for Streamlit app
def main():
    st.title('Phishing URL Detector')
    st.write("Enter a URL to check if it's phishing or not.")
    
    url = st.text_input("Enter URL:")
    
    if st.button("Check"):
        st.write("Extracting features...")
        features = featureExtraction(url)

        # Heuristic Checks
        if features[5] == 1:  # URL shortener detected (assuming `tinyURL` is at index 5)
            st.error("Phishing Alert! This URL is classified as phishing due to the use of a URL shortener.")
            return
        
        if features[12] == 1:  # Suspicious keywords in the domain (assuming `suspiciousKeywords` is at index 12)
            st.error("Phishing Alert! This URL is classified as phishing due to suspicious keywords in the domain.")
            return
        
        # Use heuristic check on the `dnsRecord` feature to indicate potential issues
        if features[8] == 1:  # Assuming `dnsRecord` is at index 8
            st.write("Note: DNS record is missing. This could be a sign of phishing, but further analysis is needed.")
        
        st.write("Predicting...")
        prediction = predict_phishing(features)
        
        if prediction is not None:
            if prediction[0] == 0:
                st.error("Phishing Alert! This URL is classified as phishing.")
            else:
                st.success("No Phishing Detected. This URL seems safe.")
        else:
            st.error("Prediction could not be made due to an error.")

if __name__ == '__main__':
    main()
