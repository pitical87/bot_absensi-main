<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="/bot_absensi-main/admin_web/assets/css/bootstrap.min.css">
    <title>Document</title>
</head>

<body>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link <?= $page === 'home' ? 'active' : '' ?>" aria-current="page"
                            href="/bot_absensi-main/admin_web/home">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link <?= $page === 'employees' ? 'active' : '' ?>"
                            href="/bot_absensi-main/admin_web/employees">Employees</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link <?= $page === 'admin' ? 'active' : '' ?>"
                            href="/bot_absensi-main/admin_web/admin">Admin</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link <?= $page === 'rekap' ? 'active' : '' ?>"
                            href="/bot_absensi-main/admin_web/rekap">Rekap</a>
                    </li>

                </ul>
                <ul class="navbar-nav mb-2 mb-lg-0">
                    <a class="nav-link" href="logout">Logout</a>
                </ul>
            </div>
        </div>
    </nav>
    <main class="container mt-1">
</body>
