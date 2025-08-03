import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from textwrap import wrap
import datetime


def write_header(p, width, height, nama, bulan, tahun, jenis):
    p.setFont("Helvetica-Bold", 12)
    p.drawCentredString(width / 2, height - 2.8 * cm, "RUMAH SAKIT UMUM DAERAH MERAUKE")
    p.setLineWidth(0.5)  # Set border thickness to 2 points
    p.setStrokeColor(colors.black)  # Set border color to blue
    p.line(2 * cm, height - 3 * cm, width - 2 * cm, height - 3 * cm)

    p.setFont("Helvetica-Bold", 14)
    p.drawCentredString(
        width / 2,
        height - 2 * cm,
        f"Rekap {jenis.title()} Bulan {get_bulan_nama(bulan)} {tahun}",
    )

    p.drawCentredString(width / 2, height - 4.2 * cm, nama.upper())

    # Table header
    y = height - 5 * cm
    return y - 0.7 * cm


from reportlab.lib import colors


def write_table(p, data, y, height, jenis):
    p.setFont("Helvetica-Bold", 10)

    if jenis == "absensi":
        col_x = [2 * cm, 6 * cm, 10 * cm, 14 * cm, 19 * cm]
        headers = ["Tanggal", "Shift", "Jam Masuk", "Jam Pulang"]
    else:
        col_x = [2 * cm, 6 * cm, 8 * cm, 19 * cm]
        headers = ["Tanggal", "Shift", "Logbook"]

    p.setStrokeColor(colors.black)
    p.setLineWidth(0.5)

    header_height = 0.6 * cm
    col_y = y

    # Header atas
    p.line(col_x[0], col_y, col_x[-1], col_y)
    col_y -= header_height
    for i, header in enumerate(headers):
        p.drawString(col_x[i] + 0.2 * cm, y - 0.4 * cm, header)
    p.line(col_x[0], col_y, col_x[-1], col_y)

    y = col_y
    p.setFont("Helvetica", 10)

    row_height = 0.6 * cm

    for row in data:
        # Cek untuk pindah halaman
        if y < 3.5 * cm:
            p.showPage()
            y = height - 3 * cm
            p.setFont("Helvetica-Bold", 10)
            col_y = y
            p.line(col_x[0], col_y, col_x[-1], col_y)
            col_y -= header_height
            for i, header in enumerate(headers):
                p.drawString(col_x[i] + 0.2 * cm, y - 0.4 * cm, header)
            p.line(col_x[0], col_y, col_x[-1], col_y)
            p.setFont("Helvetica", 10)
            y = col_y

        if jenis == "absensi":
            tanggal, shift, masuk, pulang = row
            row_data = [
                (
                    tanggal.strftime("%d-%m-%Y")
                    if isinstance(tanggal, (datetime.date, datetime.datetime))
                    else str(tanggal)
                ),
                str(shift or "-"),
                str(masuk or "-"),
                str(pulang or "-"),
            ]
            for i, cell in enumerate(row_data):
                p.drawString(col_x[i] + 0.2 * cm, y - 0.4 * cm, cell)

            p.line(col_x[0], y - row_height, col_x[-1], y - row_height)
            y -= row_height
        else:
            tanggal, shift, logbook = row
            logbook = logbook or "-"
            p.drawString(
                col_x[0] + 0.2 * cm, y - 0.4 * cm, tanggal.strftime("%d %B %Y")
            )
            p.drawString(col_x[1] + 0.2 * cm, y - 0.4 * cm, shift or "-")
            y_end = draw_wrapped_string(
                p,
                logbook,
                col_x[2] + 0.2 * cm,
                y - 0.4 * cm,
                max_width=col_x[3] - col_x[2] - 0.4 * cm,
            )
            p.line(col_x[0], y_end, col_x[-1], y_end)
            y = y_end

    # Gambar garis vertikal
    for x in col_x:
        p.line(x, y, x, col_y + header_height)
    p.line(col_x[-1], y, col_x[-1], col_y + header_height)

    return y


def write_footer(p, y, jenis):
    width, _ = A4  # untuk mendapatkan lebar halaman

    y -= 1.2 * cm
    p.setFont("Helvetica-Oblique", 9)
    if jenis == "absensi":
        p.drawCentredString(
            width / 2, y, "Keterangan: Presensi dilakukan mandiri setelah fingerprint."
        )
    else:
        p.drawCentredString(
            width / 2,
            y,
            "Keterangan: Logbook mencatat kegiatan/aktivitas sesuai shift.",
        )

    y -= 1.5 * cm
    p.setFont("Helvetica", 10)
    p.drawCentredString(width / 2, y, "Telah diperiksa dan disetujui oleh:")

    y -= 2.5 * cm
    p.drawCentredString(width / 2, y, "........................................")

    y -= 1.5 * cm
    p.setFont("Helvetica-Oblique", 8)
    p.drawCentredString(
        width / 2,
        y,
        "Dokumen ini dihasilkan otomatis melalui Sistem Presensi & Logbook Bot Telegram.",
    )


def generate_pdf_rekap(data, nama, bulan, tahun, jenis):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = write_header(p, width, height, nama, bulan, tahun, jenis)
    y = write_table(p, data, y, height, jenis)
    write_footer(p, y, jenis)

    p.save()
    buffer.seek(0)
    return buffer


def get_bulan_nama(bulan: int) -> str:
    nama_bulan = [
        "",  # indeks 0 tidak digunakan
        "Januari",
        "Februari",
        "Maret",
        "April",
        "Mei",
        "Juni",
        "Juli",
        "Agustus",
        "September",
        "Oktober",
        "November",
        "Desember",
    ]
    return nama_bulan[bulan]


def draw_wrapped_string(p, text, x, y, max_width, font_size=10, line_height=12):
    char_per_line = int(
        max_width / (font_size * 0.45)
    )  # perkiraan jumlah karakter per baris
    lines = wrap(text, width=char_per_line)
    for i, line in enumerate(lines):
        p.drawString(x, y - i * line_height, line)
    return y - len(lines) * line_height
