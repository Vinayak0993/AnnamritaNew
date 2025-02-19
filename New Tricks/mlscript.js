$('#predictionForm').on('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting traditionally
    
    const foodType = $('#food_type').val();
    const methaneGasLevel = $('#methane_gas_level').val();
    const humidity = $('#humidity').val();
    const temperature = $('#temperature').val();

    $.ajax({
        url: 'http://127.0.0.1:5000/predict',  // API endpoint
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            food_type: foodType,
            methane_gas_level: methaneGasLevel,
            humidity: humidity,
            temperature: temperature
        }),
        success: function(response) {
            // Check if the prediction is available
            if (response.prediction !== undefined) {
                $('#predictionResult').text('Prediction: ' + (response.prediction === 1 ? 'Spoiled' : 'Not Spoiled'));
            } else {
                $('#predictionResult').text('Error: Prediction is undefined');
            }
        },
        error: function(error) {
            $('#predictionResult').text('Error: Could not get prediction.');
        }
    });
});
