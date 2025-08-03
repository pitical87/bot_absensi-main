<?php
include_once __DIR__ . '/../includes/db.php';

$id = $_POST['id'];
$employee_id = $_POST['employee_id'];
$shift = $_POST['shift'];
$masuk = $_POST['masuk'];
$pulang = $_POST['pulang'];
$tanggal = $_POST['tanggal'];
$logbook = $_POST['logbook'];

$stmt = $conn->prepare(
    "UPDATE attendance SET 
    employee_id = ?, 
    shift = ?, 
    masuk = ?, 
    pulang = ?, 
    tanggal = ?, 
    logbook = ?
    WHERE id = ?"
);
$stmt->bind_param('isssssi', $employee_id, $shift, $masuk, $pulang, $tanggal, $logbook, $id);
$stmt->execute();
$stmt->close();

header("Location: ../home");
?>

