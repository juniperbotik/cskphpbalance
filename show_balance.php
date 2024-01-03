<?php
if ($_SERVER["REQUEST_METHOD"] == "GET") {
    $key = $_GET["key"];
    $data = @file_get_contents("keys/$key.txt");

    if ($data !== false) {
        list($balance, $username) = explode('|', $data);
        echo "Username: $username<br>";
        echo "Balance: $balance";
    } else {
        echo "Invalid key";
    }
}
?>
