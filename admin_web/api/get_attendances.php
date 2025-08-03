<?php
include_once __DIR__ . '/../includes/db.php';

$sql = "SELECT a.*, e.name
          FROM attendance a
          JOIN employees e ON a.employee_id = e.id
          ORDER BY a.tanggal DESC";
$result = $conn->query($sql);

$data = [];
while ($row = $result->fetch_assoc()) {
    $data[] = $row;
}
echo json_encode($data);
