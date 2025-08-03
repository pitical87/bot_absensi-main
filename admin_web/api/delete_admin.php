<?php
include_once __DIR__ . '/../includes/db.php';

$id = $_GET['id'];
$sql = "DELETE FROM admin WHERE id = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param('i', $id);
$stmt->execute();
$stmt->close();

header("Location: ../admin");
