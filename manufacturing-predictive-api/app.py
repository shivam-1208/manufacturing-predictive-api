from flask import Flask, request, jsonify
import pandas as pd
from model import Model

# Initialize the Flask application
app = Flask(__name__)

# Create an instance of the Model class
model = Model()

@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file is part of the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    # Get the uploaded file
    file = request.files['file']
    
    # Check if the filename is empty
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # If a file is provided, read it into a DataFrame
    if file:
        df = pd.read_csv(file)  # Load the CSV file into a DataFrame
        model.load_data(df)     # Load the data into the model
        return jsonify({"message": "File uploaded successfully"}), 200

@app.route('/train', methods=['POST'])
def train():
    # Train the model on the uploaded dataset and get performance metrics
    accuracy, f1_score = model.train()
    return jsonify({"accuracy": accuracy, "f1_score": f1_score}), 200

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON input from the request
    data = request.json
    
    # Make a prediction using the model
    prediction, confidence = model.predict(data)
    
    # Return the prediction and confidence in JSON format
    return jsonify({"Downtime": prediction, "Confidence": confidence}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development