/*import axios from 'axios';

const predictAge = async () => {
    const name = document.getElementById('name-select').value;
    if (!name) {
        console.log('Please select a name.');
        return "0";
    }
    try {
        const response = await axios.get(`/predict-age?name=${name}`);
        const predictedAge = response.data.predicted_age;
        document.getElementById('prediction-result').textContent = `The approximate age of ${name} is ${predictedAge} years old.`;
    } catch (error) {
        console.log('Failed to predict age. Please try again later.');
    }
};*/
const predictAge = () => {
    const name = document.getElementById('name-select').value;
    if (!name) {
        alert('Please select a name.');
    }
    //const response = await axios.get(`/predict-age?name=${name}`);
    
};
document.getElementById('predict-button').addEventListener('click', predictAge);
/*
const predictButton = document.getElementById("predict-button");
predictButton.addEventListener("click", () => {
    chrome.tabs.create({ url: "https://example.com" });
})*/