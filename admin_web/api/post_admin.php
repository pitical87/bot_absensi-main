<?php
include_once __DIR__ . '/../includes/db.php';

$username = $_POST['username'];
$password = $_POST['password'];
$konfirmasi_password = $_POST['konfirmasi_password'];

if ($password === $konfirmasi_password) {
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    $stmt = $conn->prepare(
        "INSERT INTO admin (username, password) VALUES (?, ?)"
    );
    $stmt->bind_param('ss', $username, $hashedPassword);
    $stmt->execute();
    $stmt->close();
    header("Location: ../admin");
} else {
    echo "Password dan konfirmasi password tidak cocok.";
}
header("Location: ../admin");
