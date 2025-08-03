<?php
include_once __DIR__ . '/../includes/db.php';

$sql = "SELECT * FROM employees";
$result = $conn->query($sql);

$data = [];
while ($row = $result->fetch_assoc()) {
    $data[] = $row;
}
echo json_encode($data);
