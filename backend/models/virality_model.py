import lightgbm as lgb  # Import LightGBM for efficient model creation
import joblib  # For saving and loading the model

class ViralityModel:
    def __init__(self):
        # Initialize a LightGBM classifier
        # LightGBM is chosen here for its speed and efficiency, especially for large-scale datasets.
        # chosen for its speed and ability to handle large datasets
        # It performs well with high-dimensional data, making it suitable for virality prediction.
        self.model = lgb.LGBMClassifier()

    def fit(self, X, y):
        # Train the model using features (X) and target (y)
        self.model.fit(X, y)

    def predict(self, X):
        # Predict labels for given features (X)
        return self.model.predict(X)

    def save(self, path):
        # Save the trained model to the specified path
        joblib.dump(self.model, path)

    def load(self, path):
        # Load a saved model from the specified path
        self.model = joblib.load(path)
