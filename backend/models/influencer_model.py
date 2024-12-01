import xgboost as xgb  # Import XGBoost for robust model creation
import joblib  # For saving and loading the model

class InfluencerModel:
    def __init__(self):
        # Initialize an XGBoost classifier
        # XGBoost is chosen here for its ability to handle complex data and nonlinear relationships effectively.
        # Baiscallly to chosen for its robustness in capturing complex relationships 
        # Influencer scoring requires robust feature interaction modeling, which XGBoost handles well.
        self.model = xgb.XGBClassifier()

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
