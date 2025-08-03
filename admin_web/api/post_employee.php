<?php
include_once __DIR__ . '/../includes/db.php';

$name = $_POST['name'];
$telegram_id = $_POST['telegram_id'];

$stmt = $conn->prepare(
    "INSERT INTO employees (name,telegram_id) VALUES (?, ?)"
);
$stmt->bind_param('si', $name, $telegram_id);
$stmt->execute();
$stmt->close();

header("Location: ../employees");
?>

