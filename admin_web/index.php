<?php
require_once __DIR__ . '/includes/db.php';
require_once __DIR__ . '/includes/auth.php';

$page = $_GET['page'] ?? 'home';

$segments = explode('/', $page);
$route = $segments[0];
$param = $segments[1] ?? null;

if (!isLoggedIn() && $page !== 'login') {
    header("Location: ?page=login");
    exit;
}

$viewFile = __DIR__ . "/views/{$route}.php";

if (file_exists($viewFile)) {
    if ($param !== null) {
        $_GET['id'] = $param;
    }
    include $viewFile;
} else {
    http_response_code(404);
    echo "404 - Halaman tidak ditemukan.";
}
