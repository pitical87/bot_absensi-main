<?php
include_once __DIR__ . '/../includes/template/header.php';
?>
<h2>Tambah Data Absensi</h2>

<form action="/bot_absensi-main/admin_web/api/post_attendance.php" method="POST">
    <div class="mb-3">
        <label for="employee_id" class="form-label">Nama Karyawan</label>
        <select name="employee_id" id="employee_id" class="form-select" required>
            <option value="">Pilih Karyawan</option>
        </select>
    </div>

    <div class="mb-3">
        <label for="tanggal" class="form-label">Tanggal</label>
        <input type="date" class="form-control" id="tanggal" name="tanggal" required>
    </div>

    <div class="mb-3">
        <label for="shift" class="form-label">Shift</label>
        <select name="shift" id="shift" class="form-select" required>
            <option value="">Pilih Shift</option>
            <option value="Pagi">Pagi</option>
            <option value="Sore">Sore</option>
            <option value="Malam">Malam</option>
        </select>
    </div>

    <div class="mb-3">
        <label for="masuk" class="form-label">Jam Masuk</label>
        <input type="time" class="form-control" id="masuk" name="masuk">
    </div>

    <div class="mb-3">
        <label for="pulang" class="form-label">Jam Pulang</label>
        <input type="time" class="form-control" id="pulang" name="pulang">
    </div>

    <div class="mb-3">
        <label for="logbook" class="form-label">Logbook</label>
        <textarea name="logbook" id="logbook" class="form-control" rows="3"></textarea>
    </div>

    <button type="submit" class="btn btn-primary">Simpan</button>
    <a href="/bot_absensi-main/admin_web/home" class="btn btn-secondary">Kembali</a>
</form>
<script>
    fetch('/bot_absensi-main/admin_web/api/get_employees.php')
        .then(response => response.json())
        .then(data => {
            const employeeSelect = document.getElementById('employee_id');
            data.forEach(employee => {
                const option = document.createElement('option');
                option.value = employee.id;
                option.textContent = employee.name;
                employeeSelect.appendChild(option);
            });
        })
</script>
<?php
include_once __DIR__ . '/../includes/template/footer.php';

?>

