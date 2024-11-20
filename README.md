# Phishing URL Detection System

### Overview
The **Phishing URL Detection System** is an advanced machine learning-based project designed to detect phishing websites in real-time. By leveraging modern techniques such as feature extraction, ensemble modeling, and dynamic blacklist management, this system ensures accurate and adaptive classification of URLs as "Phishing" or "Legitimate." A user-friendly CLI or Streamlit interface enhances usability, making it a robust solution for cybersecurity applications.

---

### Features
1. **Feature Extraction**: 
   - Extracts meaningful characteristics of URLs, such as length, HTTPS presence, special characters, and IP address usage.

2. **Machine Learning Models**:
   - Implements a **stacking ensemble** with Multi-Layer Perceptron (MLP) and XGBoost models for precise predictions.
   - Utilizes logistic regression as a meta-model to combine the strengths of base models.

3. **Dynamic Blacklist Management**:
   - Allows users to **blacklist phishing URLs** or whitelist legitimate ones dynamically.
   - Updates the dataset (`urls.csv`) in real-time for better adaptability.

4. **User-Friendly Interface**:
   - Command-line interaction for direct terminal use.
   - Optional Streamlit-based front-end for real-time URL analysis and management.

5. **Customizability**:
   - Supports hyperparameter tuning for optimizing model performance.
   - Modular codebase for easy integration into larger systems.

---

### Technologies Used
- **Languages**:
  - Python
- **Python Libraries**:
  - `pandas`: Data handling and manipulation.
  - `scikit-learn`: Building MLP, stacking, and logistic regression models.
  - `xgboost`: Implementing gradient boosting for enhanced prediction accuracy.
  - `streamlit`: Interactive front-end for URL analysis.
  - `pickle`: Saving and loading trained models.

---

### How It Works
1. **Feature Extraction**:
   - Key features of URLs are extracted and pre-processed using Python scripts.

2. **Model Training**:
   - A stacking ensemble (MLP + XGBoost) is trained on labeled URL datasets with selected features.
   - The trained model is saved and used for prediction.

3. **URL Prediction**:
   - The system checks the URL against the blacklist first. If not blacklisted, it analyzes features using the trained model to classify the URL.

4. **Blacklist/Whitelist Management**:
   - Users can dynamically update the blacklist and whitelist for improved accuracy and adaptive detection.

5. **Interface**:
   - Use the CLI for terminal-based interaction or Streamlit for a graphical interface.

---

### How to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/phishing-url-detection.git
   cd phishing-url-detection
   ```

2. **Set Up the Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On macOS/Linux
   .\venv\Scripts\activate       # On Windows
   pip install -r requirements.txt
   ```

3. **Run Feature Engineering**:
   ```bash
   python feature_engineering.py
   ```

4. **Train the Model**:
   ```bash
   python model_training.py
   ```

5. **(Optional) Tune the Model**:
   ```bash
   python tuning.py
   ```

6. **Run the Application**:
   - **CLI Version**:
     ```bash
     python updated_app.py
     ```
   - **Streamlit Version**:
     ```bash
     streamlit run updated_app.py
     ```

---

### Use Cases
- **Cybersecurity**: Detect phishing websites in real-time to prevent fraud.
- **Web Monitoring**: Analyze URLs for suspicious patterns.
- **Personal Use**: Verify the safety of URLs before visiting them.

---

### Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to suggest improvements or report bugs.

---

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This description highlights the project's goals, functionality, and setup, presenting it professionally for a GitHub repository.
