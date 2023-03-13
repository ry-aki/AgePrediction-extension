
#  Age Predictor Chrome Extension
This project is a simple chrome extension that fetches the approximate age of a person. It is supported by a Flask application that provides an endpoint for the extension to make requests to.  
The extension has a dropdown menu with 10 names, clicking on which displays the result.

### Technical Details:

* The directory cs_profiles has 10 json files of profiles.
* A Python class named AgePrediction is used to calculate the approximate age of a person based on their education and work experience details.
* The Flask application provides an API endpoint at /predict-age that takes in the name of a person and returns the approximate age by calling the AgePrediction class.
* The extension is built using HTML, CSS, and JavaScript.
* Axios is used to make HTTP requests from the extension to the Flask API endpoint.
* The extension is loaded using the manifest.json file that specifies the extension's properties.

### References:

Flask documentation: https://flask.palletsprojects.com/en/2.1.x/  
Chrome extension documentation



