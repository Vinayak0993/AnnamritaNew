<?php
// Replace with your ESP32 device's IP address
$esp32IpAddress = "192.168.1.100";

$data = json_decode(file_get_contents("http://".$esp32IpAddress."/data.json"), true);

if ($data) {
    $temperature = floatval($data['temperature']);
    $moisture = floatval($data['moisture']);
    $gasValue = floatval($data['gasValue']);
    
    echo json_encode($data);
} else {
    echo json_encode(array("error" => "Failed to fetch data from ESP32"));
}
?>