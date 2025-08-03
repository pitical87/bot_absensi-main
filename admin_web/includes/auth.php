<?php
session_start();

function login($username, $password, $conn)
{
    $stmt = $conn->prepare("SELECT * FROM admin WHERE username=?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();
    if (!$row = $result->fetch_assoc()) {
        return false;
    }
    if (password_verify($password, $row['password'])) {
        $_SESSION['user'] = $row;
        return true;
    }

    return false;
}

function isLoggedIn()
{
    return isset($_SESSION['user']);
}

function logOut()
{
    session_destroy();
    unset($_SESSION['user']);
    header("Location: ?page=login");
    exit;
}
