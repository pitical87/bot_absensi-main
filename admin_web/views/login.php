<?php

if (isLoggedIn()) {
    header('Location: ?page=home');
    exit;
}
$error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';
    if (login($username, $password, $conn)) {
        header('Location: ?page=home');
        exit;
    } else {
        $error = "Username atau password salah!";
    }
}


?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
</head>

<body>

    <div class="container d-flex justify-content-center align-items-center vh-100">
        <div class="card shadow-sm p-4" style="width: 100%; max-width: 400px;">
            <h2 class="text-center mb-4">Login Admin</h2>
            <form method="post">
                <div class="form-floating mb-3">
                    <input type="text" name="username" id="username" class="form-control" placeholder="Username"
                        required>
                    <label for="username">Username</label>
                </div>
                <div class="form-floating mb-4">
                    <input type="password" name="password" id="password" class="form-control" placeholder="Password"
                        required>
                    <label for="password">Password</label>
                </div>
                <button type="submit" class="btn btn-primary w-100">Login</button>
            </form>
        </div>
    </div>
</body>

</html>
