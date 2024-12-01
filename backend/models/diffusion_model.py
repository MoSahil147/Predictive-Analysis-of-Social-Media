from sklearn.ensemble import RandomForestClassifier  # Import Random Forest model
import joblib  # For saving and loading the model

class DiffusionModel:
    def __init__(self):
        # Initialize a Random Forest classifier
        # Random Forest is chosen for its robustness and ability to handle noisy data effectively
        self.model = RandomForestClassifier()

    def fit(self, X, y):
        # Train the model using features (X) and target labels (y)
        self.model.fit(X, y)

    def predict(self, X):
        # Predict labels for the given test features (X)
        return self.model.predict(X)

    def save(self, path):
        # Save the trained model to a file for later use
        joblib.dump(self.model, path)

    def load(self, path):
        # Load a saved model from a file to make predictions
        self.model = joblib.load(path)
