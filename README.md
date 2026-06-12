# 📧 Spam Email Classifier

A Machine Learning-based Email/SMS Spam Classifier built using FastAPI and Scikit-Learn. The application predicts whether a message is Spam or Safe and displays confidence scores with a modern UI.

---

## 🚀 Features

- Detects Spam and Safe emails/messages
- Confidence score prediction
- Spam and Ham probability bars
- Modern responsive UI
- FastAPI backend
- Machine Learning using Logistic Regression
- TF-IDF vectorization
- Custom spam and safe icons
- Real-time predictions
- Ready for deployment with Render

---

## 🛠 Technologies Used

### Backend
- Python
- FastAPI
- Uvicorn

### Machine Learning
- Scikit-Learn
- Logistic Regression
- TF-IDF Vectorizer
- Pandas
- NumPy

### Frontend
- HTML
- CSS
- Jinja2 Templates

---

## 📂 Project Structure

```
SpamClassifier
│
├── app
│   ├── __pycache__
│   ├── static
│   │   ├── safe.png
│   │   ├── spam.png
│   │   └── style.css
│   │
│   ├── templates
│   │   ├── index.html
│   │   └── result.html
│   │
│   ├── main.py
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── requirements.txt
├── spam.csv
├── train_model.py
├── runtime.txt         
├── .gitignore          
├── README.md           
├── render.yaml      
└── LICENSE             
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/SpamClassifier.git
```

Move into the project:

```bash
cd SpamClassifier
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🏃 Running the Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

## 🧠 Machine Learning Pipeline

1. Load dataset (`spam.csv`)
2. Preprocess text
3. TF-IDF Vectorization
4. Train Logistic Regression model
5. Save model using Pickle
6. Predict Spam or Safe messages
7. Display confidence scores and probability bars

---

## 📈 Example Predictions

### Spam

```
USPS: Your package is waiting for delivery. Confirm your address and pay a $1.95 customs fee.
```

```
Your PayPal account is locked. Sign in now.
```

```
Netflix payment failed. Update your billing information.
```

### Safe

```
Hi, are we meeting tomorrow at 10 AM?
```

```
Can you send me the notes after class?
```

---

## 🌐 Deployment

This project can be deployed on:

- Render
- Railway
- Azure
- AWS
- Google Cloud

---

## 👨‍💻 Author

**B. Thriveni**

B.Tech Computer Science and Engineering

---

## ⭐ Future Enhancements

- Dark Mode
- Pie Charts
- BERT-based Spam Detection
- Email Attachment Analysis
- Multilingual Support
- User Authentication
- Database Integration

---

## 📄 License

This project is created for educational and portfolio purposes.