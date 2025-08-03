<?php
include_once __DIR__ . '/../includes/template/header.php';
?>
<h2>Edit Data Absensi</h2>

<form action="/bot_absensi-main/admin_web/api/update_attendance.php" method="POST">
    <input type="hidden" name="id" id="id" value="<?= $_GET['id'] ?>">
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
    const id = document.getElementById('id').value;
    fetch('/bot_absensi-main/admin_web/api/get_attendance_by_id.php?id=' + id)
        .then(response => response.json())
        .then(data => {
            const tanggalInput = document.getElementById('tanggal');
            tanggalInput.value = data[0].tanggal;
            const shiftSelect = document.getElementById('shift');
            shiftSelect.value = data[0].shift;
            const masukInput = document.getElementById('masuk');
            masukInput.value = data[0].masuk;
            const pulangInput = document.getElementById('pulang');
            pulangInput.value = data[0].pulang;
            const logbookInput = document.getElementById('logbook');
            logbookInput.value = data[0].logbook;

            fetch('/bot_absensi-main/admin_web/api/get_employees.php')
                .then(response => response.json())
                .then(employees => {
                    const employeeSelect = document.getElementById('employee_id');
                    employees.forEach(employee => {
                        const option = document.createElement('option');
                        option.value = employee.id;
                        option.textContent = employee.name;
                        if (employee.id == data[0].employee_id) {
                            option.selected = true;
                        }
                        employeeSelect.appendChild(option);
                    });
                })
        })
</script>
<?php
include_once __DIR__ . '/../includes/template/footer.php';

?>

