document.addEventListener("DOMContentLoaded", function() {
    fetch('/api/sensor-data')
        .then(response => response.json())
        .then(data => {
            const sensorDiv = document.getElementById('sensorData');
            sensorDiv.innerHTML = JSON.stringify(data);
        });
});
