<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="5" >
    <link rel="stylesheet" type="text/css" href="style.css" media="screen"/>
    <link rel="stylesheet" href="home.css">
    <link rel="stylesheet" href="sensed data.css">
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
                <li><a href="profile.php"  class="active">Profile</a></li>
                <li ><a href="fooddonateform.php"  >Donate</a></li>
                <li ><a href="sensed data.php"  >Sensor data</a></li>
            </ul>
        </nav>
    </header>

</head>

<body>

    <h1>SENSOR DATA</h1>
<?php
$servername = "localhost";
$username = "root";
$password = " ";
$dbname = "foodonate";

// Create connection
$connection=mysqli_connect("localhost","root","");
$db=mysqli_select_db($connection,'foodonate');
// Check connection
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

$sql = "SELECT id, Temperature, Humidity, Pressure, reading_time FROM sensordata ORDER BY id DESC"; /*select items to display from the sensordata table in the data base*/

echo '<table cellspacing="5" cellpadding="5">
      <tr> 
        <th>ID</th> 
        <th>Date $ Time</th> 
        <th>Temperature &deg;C</th> 
        <th>Humidity &#37;</th>
        <th>Pressure</th>       
      </tr>';
 
if ($result = $connection->query($sql)) {
    while ($row = $result->fetch_assoc()) {
        $row_id = $row["id"];
        $row_reading_time = $row["reading_time"];
        $row_value1 = $row["Temperature"];
        $row_value2 = $row["Humidity"]; 
        $row_value3 = $row["Pressure"]; 
        
        // Uncomment to set timezone to - 1 hour (you can change 1 to any number)
       // $row_reading_time = date("Y-m-d H:i:s", strtotime("$row_reading_time - 1 hours"));
      
        // Uncomment to set timezone to + 4 hours (you can change 4 to any number)
        //$row_reading_time = date("Y-m-d H:i:s", strtotime("$row_reading_time + 4 hours"));
      
        echo '<tr> 
                <td>' . $row_id . '</td> 
                <td>' . $row_reading_time . '</td> 
                <td>' . $row_value1 . '</td> 
                <td>' . $row_value2 . '</td>
                <td>' . $row_value3 . '</td> 
                
              </tr>';
    }
    $result->free();
}

$connection->close();
?> 
</table>

</body>
</html>

	</body>
</html>