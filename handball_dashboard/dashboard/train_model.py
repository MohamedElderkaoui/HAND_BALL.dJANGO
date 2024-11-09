from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd
import os

# Example data preparation (this could be player stats from the database)
data = {
    'goals': [5, 3, 7, 2, 4],  # Example goals scored
    'assists': [3, 2, 5, 1, 3],  # Example assists
    'blocks': [1, 0, 3, 2, 1],  # Example blocks
    'saves': [0, 1, 2, 1, 0],   # Example saves
    'performance': [1, 0, 1, 0, 1]  # 1 = Good performance, 0 = Poor performance (target)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[['goals', 'assists', 'blocks', 'saves']]
y = df['performance']

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a random forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Create directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Save the model
joblib.dump(model, './models/model.pkl')
