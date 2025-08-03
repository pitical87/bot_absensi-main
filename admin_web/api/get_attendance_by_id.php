<?php
include_once __DIR__ . '/../includes/db.php';

$id = $_GET['id'];
$sql = "SELECT a.*, e.name
          FROM attendance a
          JOIN employees e ON a.employee_id = e.id
          WHERE a.id = ?
          ORDER BY a.tanggal DESC";
$result = $conn->prepare($sql);
$result->bind_param('i', $id);
$result->execute();
$result = $result->get_result();

$data = [];
while ($row = $result->fetch_assoc()) {
    $data[] = $row;
}
echo json_encode($data);
