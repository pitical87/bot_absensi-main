<?php
include_once __DIR__ . '/../includes/template/header.php';
?>
<h2 class="mb-3">Daftar Staf IT</h2>

<a class="btn btn-primary mb-3" href="tambah_employee">Tambah Staff</a>
<table id="employeeTable" class="table table-bordered table-striped table-hover">
    <thead class="table-dark">
        <tr>
            <th>Nama</th>
            <th>ID Telegram</th>
            <th>Aksi</th>
        </tr>
    </thead>
    <tbody></tbody>
</table>

<script>
    fetch('/bot_absensi-main/admin_web/api/get_employees.php')
        .then(response => response.json())
        .then(data => {
            const tBody = document.querySelector('#employeeTable tbody');
            data.forEach(row => {
                const tr = document.createElement('tr');
                tr.innerHTML =
                    `
                    <td>${row.name}</td>
                    <td>${row.telegram_id}</td>
                    <td>
                        <a class="btn btn-primary" href="edit_employee/${row.id}">Edit</a>
                        <a class="btn btn-danger" href="delete_employee/${row.id}">Hapus</a>
                    </td>
                `;
                tBody.appendChild(tr);
            });
        })
</script>
<?php
include_once __DIR__ . '/../includes/template/footer.php';

?>

