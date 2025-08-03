<?php
include_once __DIR__ . '/../includes/template/header.php';
?>
<h2>Edit Data Staf IT</h2>

<form action="/bot_absensi-main/admin_web/api/update_employee.php" method="POST">
    <input type="hidden" name="id" id="id" value="<?= $_GET['id'] ?>">
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
<script>
    fetch('/bot_absensi-main/admin_web/api/get_employee_by_id.php?id=<?= $_GET['id'] ?>')
        .then(response => response.json())
        .then(data => {
            document.getElementById('name').value = data[0].name;
            document.getElementById('telegram_id').value = data[0].telegram_id;
        })
</script>
<?php
include_once __DIR__ . '/../includes/template/footer.php';

?>

