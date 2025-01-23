5. README.md

# Manufacturing Predictive API

This project provides a RESTful API for predicting machine downtime in manufacturing operations using a simple decision tree model.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd manufacturing-predictive-api
2.Install the required packages:
  pip install -r requirements.txt
Running the API
Run the application:

python app.py
The API will be available at http://127.0.0.1:5000.

## Testing the API

The API endpoints have been tested using Postman to ensure they function as expected. Below are some  requests that can be used to test the API:

###  Requests

1. **Upload Data**:
   - **Method**: POST
   - **URL**: `/upload`
   - **Body**: Form-data with a CSV file.

2. **Train the Model**:
   - **Method**: POST
   - **URL**: `/train`

3. **Make a Prediction**:
   - **Method**: POST
   - **URL**: `/predict`
   - **Body**: JSON with input data (e.g., `{
    "Temperature" : 80,
    "Run_Time" : 189
}`).

Feel free to use Postman or any other API testing tool to interact with the endpoints.