<?php
include_once __DIR__ . '/../includes/template/header.php';
?>
<h2>Tambah Data Staf IT</h2>

<form action="/bot_absensi-main/admin_web/api/post_employee.php" method="POST">
    <div class="mb-3">
        <label for="name" class="form-label">Nama</label>
        <input type="text" class="form-control" id="name" name="name" required>
    </div>
    <div class="mb-3">
        <label for="telegram_id" class="form-label">ID Telegram</label>
        <input type="text" class="form-control" id="telegram_id" name="telegram_id" required>
    </div>

    <button type="submit" class="btn btn-primary">Simpan</button>
    <a href="/bot_absensi-main/admin_web/employees" class="btn btn-secondary">Kembali</a>
</form>
<?php
include_once __DIR__ . '/../includes/template/footer.php';

?>

