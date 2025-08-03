<?php
include_once __DIR__ . '/../includes/template/header.php';
?>
<h2>Edit Data Admin</h2>

<form action="/bot_absensi-main/admin_web/api/update_admin.php" method="POST">
    <input type="hidden" name="id" id="id" value="<?= $_GET['id'] ?>">
    <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" name="username" class="form-control" id="username" required>
    </div>

    <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <div class="input-group">
            <input type="password" class="form-control" id="password" name="password" required>
            <button class="btn btn-outline-primary" id="showPassword">Tampilkan</button>
        </div>
    </div>
    <div class="mb-3">
        <label for="konfirmasi_password" class="form-label">Konfirmasi Password</label>
        <div class="input-group">
            <input type="password" class="form-control" id="konfirmasi_password" name="konfirmasi_password" required>
            <button class="btn btn-outline-primary" id="showKonfirmasiPassword">Tampilkan</button>
        </div>
    </div>
    <button type="submit" class="btn btn-primary">Simpan</button>
    <a href="/bot_absensi-main/admin_web/admin" class="btn btn-secondary">Kembali</a>
</form>
<script>
    const passwordInput = document.getElementById('password');
    const konfirmasiPasswordInput = document.getElementById('konfirmasi_password');

    document.getElementById("showPassword").addEventListener("click", function (e) {
        e.preventDefault();
        if (passwordInput.type === "password") {
            passwordInput.type = "text";
        } else {
            passwordInput.type = "password";
        }
    });

    document.getElementById("showKonfirmasiPassword").addEventListener("click", function (e) {
        e.preventDefault();
        if (konfirmasiPasswordInput.type === "password") {
            konfirmasiPasswordInput.type = "text";
        } else {
            konfirmasiPasswordInput.type = "password";
        }
    });

    fetch('/bot_absensi-main/admin_web/api/get_admin_by_id.php?id=<?= $_GET['id'] ?>')
        .then(response => response.json())
        .then(data => {
            document.getElementById('username').value = data.username;
        })
</script>
<?php
include_once __DIR__ . '/../includes/template/footer.php';

?>

