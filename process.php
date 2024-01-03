<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Получаем данные из формы
    $username = $_POST["username"];
    $balance = $_POST["balance"];

    // Генерируем уникальный ключ
    $key = uniqid();

    // Сохраняем данные в файл (вместо этого лучше использовать базу данных)
    $data = "$balance|$username";
    file_put_contents("keys/$key.txt", $data);

    // Перенаправляем обратно на страницу с балансом и ключом
    header("Location: show_balance.php?key=$key");
    exit;
}
?>
