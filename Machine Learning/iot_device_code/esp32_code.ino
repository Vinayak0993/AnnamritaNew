#include <MQUnifiedsensor.h>
#include <WiFi.h>
#include <HTTPClient.h>

// WiFi credentials
const char* ssid = "your-ssid";
const char* password = "your-password";

// API endpoint to send the data
const char* serverName = "http://your-server-endpoint/predict";

// Sensor thresholds for spoilage detection
const float tempThreshold = 25.0;  // Temperature threshold in Celsius
const float humidityThreshold = 65.0;  // Humidity threshold in %
const float gasThreshold = 0.4;  // Gas level threshold (example: ppm)

// Initialize variables for sensors
float temperature, humidity, gasLevel;
bool isSpoiled = false;

void setup() {
    Serial.begin(115200);

    // Connect to WiFi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");
}

void loop() {
    // Simulate reading sensor data (replace these with actual sensor readings)
    temperature = random(200, 300) / 10.0;  // Random temp between 20°C and 30°C
    humidity = random(500, 700) / 10.0;     // Random humidity between 50% and 70%
    gasLevel = random(100, 500) / 1000.0;   // Random gas level between 0.1 and 0.5

    // Print sensor readings to the Serial Monitor
    Serial.println("Temperature: " + String(temperature) + " °C");
    Serial.println("Humidity: " + String(humidity) + " %");
    Serial.println("Gas Level: " + String(gasLevel) + " ppm");

    // Determine if food is spoiled based on thresholds
    if (temperature > tempThreshold || humidity > humidityThreshold || gasLevel > gasThreshold) {
        isSpoiled = true;
        Serial.println("Food is spoiled!");
    } else {
        isSpoiled = false;
        Serial.println("Food is not spoiled.");
    }

    // Send the data to the server (e.g., using HTTP POST)
    sendData(temperature, humidity, gasLevel, isSpoiled);

    // Wait for 10 seconds before the next reading
    delay(10000);
}

// Function to send sensor data and spoilage status to a server
void sendData(float temperature, float humidity, float gasLevel, bool isSpoiled) {
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;

        // Construct server URL
        http.begin(serverName);
        http.addHeader("Content-Type", "application/x-www-form-urlencoded");

        // Prepare the payload
        String payload = "temperature=" + String(temperature)
                       + "&humidity=" + String(humidity)
                       + "&gasLevel=" + String(gasLevel)
                       + "&isSpoiled=" + String(isSpoiled ? 1 : 0);

        // Send HTTP POST request
        int httpResponseCode = http.POST(payload);

        if (httpResponseCode > 0) {
            String response = http.getString();
            Serial.println("Server Response: " + response);
        } else {
            Serial.println("Error sending POST request. HTTP Response code: " + String(httpResponseCode));
        }

        // End the HTTP request
        http.end();
    } else {
        Serial.println("WiFi is not connected.");
    }
}