<?php
include_once __DIR__ . '/../includes/db.php';

$id = $_POST['id'];
$username = $_POST['username'];
$password = $_POST['password'];
$konfirmasi_password = $_POST['konfirmasi_password'];

if ($password === $konfirmasi_password) {
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    $stmt = $conn->prepare(
        "UPDATE admin SET username = ?, password = ? WHERE id = ?"
    );
    $stmt->bind_param('ssi', $username, $hashedPassword, $id);
    $stmt->execute();
    $stmt->close();
    header("Location: ../admin");
} else {
    echo "Password dan konfirmasi password tidak cocok.";
}
header("Location: ../admin");
