from flask import Flask, request, render_template, jsonify, send_file
from flask_cors import CORS
from agepredictor import AgePrediction

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})
@app.route('/', methods=['GET'])
def index():
    return send_file('popup.html')

@app.route('/predict-age', methods=['PUT', 'GET'])
def predict_age():
    name = request.get_json('name')
    filename = 'cs_profiles/' + name['name'] + '.json'
    prediction_obj = AgePrediction(filename)
    predicted_age = prediction_obj.predict_age()
    response = {
        'name': name,
        'predicted_age': predicted_age
    }
    return jsonify({'predicted_age': predicted_age})
    
if __name__ == '__main__':
    app.run(debug=True)