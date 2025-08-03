<!DOCTYPE html>
<html lang="id">

<head>
    <meta charset="UTF-8">
    <title>Rekap Absensi</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 40px;
        }

        h1,
        h2,
        h3 {
            text-align: center;
            margin: 0;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 30px;
        }

        table,
        th,
        td {
            border: 1px solid #000;
        }

        th,
        td {
            padding: 8px;
            text-align: center;
        }

        th {
            font-weight: bold;
        }

        .footer {
            margin-top: 40px;
            text-align: center;
        }

        .signature {
            margin-top: 80px;
            text-align: center;
        }

        .note {
            font-size: 12px;
            font-style: italic;
            margin-top: 20px;
        }
    </style>
</head>

<body>
    <h2>RUMAH SAKIT UMUM DAERAH MERAUKE</h2>
    <h3>Rekap Logbook PIT Bulan <span id="periode"></span></h3>

    <table>
        <thead>
            <tr>
                <th>Nama</th>
                <th>Tanggal</th>
                <th>Shift</th>
                <th>Logbook</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>

    <div class="note">Keterangan: Logbook mencatat kegiatan/aktivitas sesuai shift.</div>

    <div class="footer">
        Telah diperiksa dan disetujui oleh:
        <div class="signature">..........................................</div>
    </div>

    <div class="note" style="text-align:center; margin-top: 30px;">
        Dokumen ini dihasilkan otomatis melalui Sistem Presensi & Logbook Bot Telegram.
    </div>

    <script>
        fetch('/bot_absensi-main/admin_web/api/get_attendances_by_month.php')
            .then(response => response.json())
            .then(data => {
                const tanggal = data[0].tanggal;
                const dateObj = new Date(tanggal);
                const bulan = dateObj.toLocaleString('id-ID', {
                    month: 'long'
                });
                const tahun = dateObj.getFullYear();

                const periode = `${bulan} ${tahun}`;
                const tBody = document.querySelector('tbody');
                data.forEach(row => {
                    const tr = document.createElement('tr');
                    tr.innerHTML =
                        `
                    <td>${row.name}</td>
                    <td>${row.tanggal}</td>
                    <td>${row.shift}</td>
                    <td>${row.logbook}</td>
                    `
                    tBody.appendChild(tr);
                });
                document.getElementById('periode').textContent = periode;
                window.print();
            })
    </script>
</body>

</html>
