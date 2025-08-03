<?php
include_once __DIR__ . '/../includes/template/header.php';
?>
<h2 class="mb-3">Daftar Admin PIT</h2>

<a class="btn btn-primary mb-3" href="tambah_admin">Tambah Admin</a>
<table id="adminTable" class="table table-bordered table-striped table-hover">
    <thead class="table-dark">
        <tr>
            <th>No</th>
            <th>Username</th>
            <th>Aksi</th>
        </tr>
    </thead>
    <tbody></tbody>
</table>

<script>
    fetch('/bot_absensi-main/admin_web/api/get_admins.php')
        .then(response => response.json())
        .then(data => {
            const tBody = document.querySelector('#adminTable tbody');
            let no = 1;
            data.forEach(row => {
                const tr = document.createElement('tr');
                tr.innerHTML =
                    `
                    <td>${no++}</td>
                    <td>${row.username}</td>
                    <td>
                        <a class="btn btn-primary" href="edit_admin/${row.id}">Edit</a>
                        <a class="btn btn-danger" href="delete_admin/${row.id}">Hapus</a>
                    </td>
                `;
                tBody.appendChild(tr);
            });
        })
</script>
<?php
include_once __DIR__ . '/../includes/template/footer.php';

?>

