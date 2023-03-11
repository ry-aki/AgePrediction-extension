from flask import Flask, request, render_template, jsonify
from agepredictor import AgePrediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict-age')
def predict_age():
    name = request.args.get('name')
    filename = 'cs_profiles/' + name + '.json'
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