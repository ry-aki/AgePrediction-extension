from flask import Flask, request, render_template, jsonify
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
    return render_template('popup.html')

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
    #return json.dumps(response), 200 
    return jsonify({'predicted_age': predicted_age})
    #return f"The approximate age of {name} is {predicted_age} years old."

if __name__ == '__main__':
    app.run(debug=True)