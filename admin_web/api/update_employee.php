<?php
include_once __DIR__ . '/../includes/db.php';

$id = $_POST['id'];
$name = $_POST['name'];
$telegram_id = $_POST['telegram_id'];

$stmt = $conn->prepare(
    "UPDATE employees SET 
    name = ?, 
    telegram_id = ?
    WHERE id = ?"
);
$stmt->bind_param('ssi', $name, $telegram_id, $id);
$stmt->execute();
$stmt->close();

header("Location: ../employees");
