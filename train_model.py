import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("spam.csv", encoding="latin-1")

# Keep only required columns
df = df[['v1', 'v2']]

# Convert labels
df['v1'] = df['v1'].map({
    'ham': 0,
    'spam': 1
})

# Features and target
X = df['v2']
y = df['v1']

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    stop_words='english'
)

X = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = LogisticRegression(max_iter=1000)

# Train
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("app/model.pkl", "wb"))

# Save vectorizer
pickle.dump(vectorizer, open("app/vectorizer.pkl", "wb"))

print("Model trained successfully!")