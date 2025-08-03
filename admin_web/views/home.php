<?php
include_once __DIR__ . '/../includes/template/header.php';
?>
<h2 class="mb-3">Daftar Absensi</h2>

<a class="btn btn-primary mb-3" href="tambah_absensi">Tambah Absensi</a>
<table id="attendanceTable" class="table table-bordered table-striped table-hover">
    <thead class="table-dark">
        <tr>
            <th>Nama</th>
            <th>Tanggal</th>
            <th>Shift</th>
            <th>Jam Masuk</th>
            <th>Jam Pulang</th>
            <th>Logbook</th>
            <th>Aksi</th>
        </tr>
    </thead>
    <tbody></tbody>
</table>

<script>
    fetch('/bot_absensi-main/admin_web/api/get_attendances.php')
        .then(response => response.json())
        .then(data => {
            const tBody = document.querySelector('#attendanceTable tbody');
            data.forEach(row => {
                const tr = document.createElement('tr');
                tr.innerHTML =
                    `
            <td>${row.name}</td>
            <td>${row.tanggal}</td>
            <td>${row.shift}</td>
            <td>${row.masuk}</td>
            <td>${row.pulang}</td>
            <td>${row.logbook}</td>
            <td> <a class="btn btn-primary" href="/bot_absensi-main/admin_web/edit_absensi/${row.id}">edit</a> 
             <a class="btn btn-danger" href="/bot_absensi-main/admin_web/delete_absensi/${row.id}">hapus</a></td>
            `
                tBody.appendChild(tr);
            });
        })
        .catch(err => {
            console.error("gagal memuat data:", err);
        })
</script>
<?php
include_once __DIR__ . '/../includes/template/footer.php';
?>

