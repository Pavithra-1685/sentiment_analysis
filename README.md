# 🌟 Sentiment Analysis Web App  

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B)](https://streamlit.io/)  
[![Scikit-learn](https://img.shields.io/badge/ML-ScikitLearn-F7931E)](https://scikit-learn.org/)  
[![NLTK](https://img.shields.io/badge/NLP-NLTK-00A86B)](https://www.nltk.org/)  

A machine learning–based **Sentiment Analysis Web Application** built with **Python, Scikit-learn, NLTK, and Streamlit**.  
The app takes user text input, preprocesses it with lemmatization, and predicts sentiment into one of four categories:  

✅ **Irrelevant**  
😠 **Negative**  
😐 **Neutral**  
😊 **Positive**  

---

## 📊 Model Performance  

**Overall Accuracy:** `94.02%`  

**Classification Report:**



```
          precision    recall  f1-score   support
```

Irrelevant       0.95      0.92      0.94      2624
Negative         0.96      0.94      0.95      4463
Neutral          0.92      0.95      0.93      3589
Positive         0.93      0.94      0.94      4123

accuracy                             0.94     14799
macro avg        0.94      0.94      0.94     14799
weighted avg     0.94      0.94      0.94     14799

````

---

## 🚀 Features  

- 🔮 **Real-time sentiment prediction** from user input  
- 🎭 **Four-class classification** (Irrelevant, Negative, Neutral, Positive)  
- 🖥️ **Streamlit-based web interface**  
- 🧹 **Text preprocessing with NLTK WordNet Lemmatizer**  
- ⚡ **Fast model loading** with Joblib  

---

## 🛠️ Tech Stack  

- **Python 3**  
- **Scikit-learn** → Model training & evaluation  
- **NLTK** → NLP preprocessing (lemmatization)  
- **Streamlit** → Interactive UI  
- **Joblib** → Model persistence  

---

## ⚙️ Installation & Setup  

1️⃣ Clone the repository  
```bash
git clone <repo_link>
cd sentiment-analysis
````

2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

3️⃣ Run the Streamlit app

```bash
streamlit run sentiment_app_model.py
```

4️⃣ First-time NLTK setup (if needed)

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

## 🎯 Example Usage

**Input:**

```
I love using this product, it makes my life easier!
```

**Output:**

```
Predicted Sentiment: Positive ✅
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

## 👩‍💻 Author

**Pavithra H** ✨

