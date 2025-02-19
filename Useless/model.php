<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="5" >
    <link rel="stylesheet" type="text/css" href="style.css" media="screen"/>
    <link rel="stylesheet" href="home.css">
    <link rel="stylesheet" href="model.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

	<title> Sensor Data </title>
    <header>
        <div class="logo">Food <b style="color: #06C167;">Donate</b></div>
        <div class="hamburger">
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
        </div>
        <nav class="nav-bar">
            <ul>
                <li><a href="home.html">Home</a></li>
                <li><a href="about.html" >About</a></li>
                <li><a href="contact.html"  >Contact</a></li>
                <li><a href="profile.php">Profile</a></li>
                <li ><a href="fooddonateform.php"  >Donate</a></li>
                <li ><a href="model.php" class="active" >Sensor data</a></li>
            </ul>
        </nav>
    </header>

</head>

<body>

    <h1>SENSOR DATA</h1>

    <?php
$hostname = "localhost";
$username = "root";
$password = "";
$database = "foodonate";

$conn = mysqli_connect($hostname, $username, $password, $database);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Receive the entire data string from ESP32
    $data = isset($_POST["data"]) ? $_POST["data"] : null;

    if ($data !== null) {
        // Split the structured data string into individual values
        list($Methane, $temperature, $Moisture) = sscanf($data, "Methane:%f Temperature:%f Moisture:%f");

        // Insert data into the "sensordata" table with prepared statements
        $sql = "INSERT INTO sensordata (Methane, Temaperature, Moisture) VALUES (?, ?, ?)";
        $stmt = mysqli_prepare($conn, $sql);

        if ($stmt) {
            mysqli_stmt_bind_param($stmt, "dddd", $Methane, $temperature, $Moisture);

            if (mysqli_stmt_execute($stmt)) {
                echo "Data inserted successfully\n";
            } else {
                echo "Error inserting data: " . mysqli_error($conn) . "\n";
            }

            mysqli_stmt_close($stmt);
        } else {
            echo "Error preparing statement: " . mysqli_error($conn) . "\n";
        }
    } else {
        echo "Invalid data received.";
    }
} else {
    echo "Invalid request method.";
}

$sql = "SELECT id, Methane, Temperature, Moisture FROM sensordata ORDER BY id DESC"; /*select items to display from the sensordata table in the data base*/

echo '<table cellspacing="5" cellpadding="5">
      <tr> 
        <th>ID</th> 
        <th>Date $ Time</th> 
        <th>Temperature &deg;C</th> 
        <th>Humidity &#37;</th>
        <th>Pressure</th>       
      </tr>';
 
// if ($result = $connection->query($sql)) {
//     while ($row = $result->fetch_assoc()) {
//         $row_value1 = $row["Methane"];
//         $row_value2 = $row["Temperature"]; 
//         $row_value3 = $row["Moisture"]; 
        
//         // Uncomment to set timezone to - 1 hour (you can change 1 to any number)
//        // $row_reading_time = date("Y-m-d H:i:s", strtotime("$row_reading_time - 1 hours"));
      
//         // Uncomment to set timezone to + 4 hours (you can change 4 to any number)
//         //$row_reading_time = date("Y-m-d H:i:s", strtotime("$row_reading_time + 4 hours"));
      
//         echo '<tr> 
//                 <td>' . $row_value1 . '</td> 
//                 <td>' . $row_value2 . '</td>
//                 <td>' . $row_value3 . '</td> 
                
//               </tr>';
//     }
//     $result->free();
// }

mysqli_close($conn);
?>

</table>

</body>
</html>

	</body>
</html>
