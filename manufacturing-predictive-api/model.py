import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score

class Model:
    def __init__(self):
        # Initialize the Decision Tree Classifier
        self.model = DecisionTreeClassifier(max_depth=5)
        self.data = None  # Placeholder for the dataset

    def load_data(self, df):
        # Load the DataFrame into the model
        self.data = df

    def train(self):
        # Check if data has been loaded
        if self.data is None:
            raise ValueError("No data loaded")
        
        # Define features (X) and target variable (y)
        X = self.data[['Temperature', 'Run_Time']]
        y = self.data['Downtime_Flag']
        
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train the model using the training data
        self.model.fit(X_train, y_train)
        
        # Make predictions on the test set
        predictions = self.model.predict(X_test)
        
        # Calculate performance metrics
        accuracy = accuracy_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)
        
        return accuracy, f1  # Return accuracy and F1 score

    def predict(self, input_data):
        # Convert input data to a DataFrame for prediction
        input_df = pd.DataFrame([input_data])
        
        # Make a prediction using the trained model
        prediction = self.model.predict(input_df)
        
        # Get the confidence score for the prediction
        confidence = self.model.predict_proba(input_df).max()
        
        # Return the prediction and confidence
        return ("Yes" if prediction[0] == 1 else "No"), confidence