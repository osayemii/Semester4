from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the saved model
model = joblib.load('iris_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    features = [[
        float(data['sepal_length']),
        float(data['sepal_width']),
        float(data['petal_length']),
        float(data['petal_width'])
    ]]
    
    prediction = int(model.predict(features)[0])
    
    species = {
        0: 'Setosa',
        1: 'Versicolor',
        2: 'Virginica'
    }
    
    return jsonify({
        'predicted_species': species[prediction]
    })
    
    
if __name__ == '__main__':
    app.run(debug=True)