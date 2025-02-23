from flask import Flask, render_template, request
import joblib
import numpy as np
import os

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model (ensure the pickle file is in your project folder)
model = joblib.load("flight_price_model.pkl")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the input values from the form
        var_1 = float(request.form['class'])
        var_2 = float(request.form['airline'])
        var_3 = float(request.form['duration'])
        var_4 = float(request.form['stops'])

        # Create an array of input data
        input_data = np.array([[var_1, var_2, var_3, var_4]])

        # Make a prediction using the model
        prediction = model.predict(input_data)

        # Map prediction result to human-readable text
        result = prediction[0]

        return render_template('index.html', prediction=result)

    return render_template('index.html')


if __name__ == '__main__':
    # Get the PORT environment variable, default to 5001 if not provided
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)

