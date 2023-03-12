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
                const response = await axios.put(`http://localhost:5000/predict-age?name=${name}`, data);
                //alert(response);
                

                const predictedAge = response.data.predicted_age;
                //alert(predictedAge);
        
                document.getElementById('prediction-result').textContent = `The approximate age of ${name} is ${predictedAge} years old.` ;
                }
            catch(error){
                alert('Failed to predict age. Please try again later.');
                }

            }
        };
        document.getElementById('predict-button').addEventListener('click', predictAge);
});
