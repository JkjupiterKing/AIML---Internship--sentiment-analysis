import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. Load dataset
df = pd.read_csv("product_reviews.csv")

# 2. Features and labels
X = df["review"]
y = df["sentiment"]

# 3. Convert text to numbers
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# 4. Train a simple model
model = LogisticRegression()
model.fit(X_vec, y)

# 5. Save the model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved!")