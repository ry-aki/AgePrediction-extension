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
/*const predictAge = async () => {
    const name = document.getElementById('name-select').value;
    if (!name) {
        alert('Please select a name.');
    }
    else {
        try {
            const data = {'name': name};
            const put_data_response = await axios.put('/predict-age', data);
            const result = put_data_response.data;
            console.log(result);
            return result;   
        } catch (error) {
            console.error(error);
            throw error;
        }    
    }


};
//const response = axios.get('')
//const predictedAge = response.data.predicted_age;
//document.getElementById('prediction-result').textContent = `The approximate age of ${name} is ${predictedAge} years old.`;
document.getElementById('predict-button').addEventListener('click', predictAge);
*/

document.addEventListener('DOMContentLoaded', () => {
    const predictAge = async () => {
        const name = document.getElementById('name-select').value;

        if (!name) {
            alert('Please select a name.');
            console.log('Please select a name.');
        }
        else{
            try{
                const data = {'name': name};
                const response = await axios.put(`/predict-age?name=${name}`, data);
                console.log(response);
                

                const predictedAge = response.data.predicted_age;
                console.log(predictedAge);
        
                document.getElementById('prediction-result').textContent = `The approximate age of ${name} is ${predictedAge} years old.` ;
                }
            catch(error){
                console.log('Failed to predict age. Please try again later.');
                }

            }
        };
        document.getElementById('predict-button').addEventListener('click', predictAge);
});
