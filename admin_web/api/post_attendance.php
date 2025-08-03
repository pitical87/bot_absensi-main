<?php
include_once __DIR__ . '/../includes/db.php';

$employee_id = $_POST['employee_id'];
$shift = $_POST['shift'];
$masuk = $_POST['masuk'];
$pulang = $_POST['pulang'];
$tanggal = $_POST['tanggal'];
$logbook = $_POST['logbook'];

$stmt = $conn->prepare(
    "INSERT INTO attendance (employee_id, shift, masuk, pulang, tanggal, logbook) VALUES (?, ?, ?, ?, ?, ?)"
);
$stmt->bind_param('isssss', $employee_id, $shift, $masuk, $pulang, $tanggal, $logbook);
$stmt->execute();
$stmt->close();

header("Location: ../home");
?>

