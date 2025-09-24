

#  Sentiment Analysis Web App  

A machine learning–based **Sentiment Analysis Web Application** built with **Python, Scikit-learn, NLTK, and Streamlit**.  
The app allows users to input text, applies preprocessing (lemmatization), and predicts sentiment into one of four categories:  
- Irrelevant  
- Negative  
- Neutral  
- Positive  

---

## 📊 Model Performance  

Accuracy: 94.02%  

Classification Report:
```

```
           precision    recall  f1-score   support
```

Irrelevant       0.95      0.92      0.94      2624
Negative       0.96      0.94      0.95      4463
Neutral       0.92      0.95      0.93      3589
Positive       0.93      0.94      0.94      4123

```
accuracy                           0.94     14799
```

macro avg       0.94      0.94      0.94     14799
weighted avg       0.94      0.94      0.94     14799

````

---

## 🚀 Features  

- Real-time sentiment prediction from user input.  
- Multi-class classification with **four sentiment labels**.  
- Interactive **Streamlit web interface**.  
- Text preprocessing with **NLTK WordNet Lemmatizer**.  
- Trained model stored with **Joblib** for fast loading.  

---

## 🛠️ Tech Stack  

- **Python 3**  
- **Scikit-learn** → Model training & evaluation  
- **NLTK** → Text preprocessing (lemmatization)  
- **Streamlit** → Web app interface  
- **Joblib** → Model persistence  

---

## ⚙️ Installation & Setup  

1. **Clone the repository**  
   ```bash
   git clone <repo_link>
   cd sentiment-analysis
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**

   ```bash
   streamlit run sentiment_app_model.py
   ```

4. **First-time NLTK setup**
   The app will download required resources (`wordnet`, `omw-1.4`) automatically.
   Alternatively, you can run this manually before starting the app:

   ```python
   import nltk
   nltk.download('wordnet')
   nltk.download('omw-1.4')
   ```

---

## 📂 Project Structure

```
sentiment-analysis/
│
├── sentiment_app_model.py   # Streamlit application
├── text_clf.pkl             # Trained ML model
├── requirements.txt         # Dependencies
└── README.md                # Documentation
```

---

## 📊 Example Usage

**Input:**

```
I love using this product, it makes my life easier!
```

**Output:**

```
Predicted Sentiment: Positive
```

---

## 📦 Requirements

`requirements.txt`

```txt
streamlit==1.39.0
scikit-learn==1.5.2
nltk==3.9.1
joblib==1.4.2
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🙌 Acknowledgments

* [Scikit-learn](https://scikit-learn.org/stable/)
* [NLTK](https://www.nltk.org/)
* [Streamlit](https://streamlit.io/)

---
## Author
  Pavithra H
