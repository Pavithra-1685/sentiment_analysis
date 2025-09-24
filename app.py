# sentiment_app_model.py
import streamlit as st
import pickle
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()

def lemmatize_nltk(text):
    """Lemmatize each word in the text."""
    return ' '.join([lemmatizer.lemmatize(word) for word in text.split()])

# Load your trained model
import joblib
model = joblib.load("/Users/yuvashankarnarayana/Desktop/senti/text_clf.pkl")
print("Model loaded successfully!")


# Streamlit App
st.title("Sentiment Analysis ")
st.write("Enter text below ")
# User input
user_input = st.text_area("Enter Text Here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        # Preprocess text
        lemmatized_text = lemmatize_nltk(user_input)

        # Predict sentiment
        prediction = model.predict([lemmatized_text])[0]

        # Optional: if model has predict_proba
        try:
            proba = model.predict_proba([lemmatized_text])[0]
            st.write(f"Prediction Probabilities: {proba}")
        except:
            pass

        st.write(f"**Predicted Sentiment:** {prediction}")
