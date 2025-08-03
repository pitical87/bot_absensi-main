<?php
include_once __DIR__ . '/../includes/template/header.php';
?>
<h2 class="mb-3">Pilih Data Rekap</h2>

<div class="row">
    <div class="col-md-6">
        <div class="card shadow-sm">
            <div class="card-body">
                <h5 class="card-title">Rekap Absensi</h5>
                <a href="rekap_absensi" class="btn btn-primary">Lihat</a>
            </div>
        </div>
    </div>
    <div class="col-md-6">
        <div class="card shadow-sm">
            <div class="card-body">
                <h5 class="card-title">Rekap Logbook</h5>
                <a href="rekap_logbook" class="btn btn-primary">Lihat</a>
            </div>
        </div>
    </div>
</div>

<?php
include_once __DIR__ . '/../includes/template/footer.php';
?>

