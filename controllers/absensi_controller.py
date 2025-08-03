import datetime
from telegram import Update
from telegram.ext import ContextTypes
from models.absensi_model import AbsensiModel
from views.absensi_view import AbsensiView


class AbsensiController:
    def __init__(self):
        self.model = AbsensiModel()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "Selamat datang di Absensi Bot! Gunakan /absensi untuk mulai."
        )

    async def isi_absensi(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        # Coba cari apakah telegram_id user ini sudah terdaftar di data employee
        karyawan = self.model.get_employees()
        karyawan_terdaftar = next(
            (k for k in karyawan if str(k[2]) == str(user_id)), None
        )

        if not karyawan_terdaftar:
            await update.message.reply_text(
                f"ID Telegram Anda belum terdaftar di sistem.\n\nID Anda: `{user_id}`",
                parse_mode="Markdown",
            )
            return
        await update.message.reply_text(
            "Pilih nama Anda:", reply_markup=AbsensiView.get_karyawan_keyboard(karyawan)
        )

    async def select_name(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        _, nama, emp_id, telegram_id = query.data.split(":")
        context.user_data.update(
            {"nama": nama, "employee_id": int(emp_id), "telegram_id": int(telegram_id)}
        )

        await query.edit_message_text(
            f"Halo {nama}, pilih shift:", reply_markup=AbsensiView.get_shift_keyboard()
        )

    async def select_shift(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        shift = query.data.split(":")[1]
        context.user_data["shift"] = shift

        await query.edit_message_text(
            "Pilih tipe absensi:", reply_markup=AbsensiView.get_tipe_keyboard()
        )

    async def confirm_absensi(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        tipe = query.data.split(":")[1]
        context.user_data["tipe"] = tipe

        nama = context.user_data["nama"]
        shift = context.user_data["shift"]
        text = AbsensiView.get_konfirmasi_text(nama, shift, tipe)
        await query.edit_message_text(
            text, reply_markup=AbsensiView.get_konfirmasi_keyboard()
        )

    async def simpan_absensi(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        emp_id = context.user_data["employee_id"]
        shift = context.user_data["shift"]
        tipe = context.user_data["tipe"]
        today = datetime.date.today().isoformat()

        absen = self.model.get_attendance(emp_id, today, shift)

        if tipe == "masuk":
            if absen and absen[1]:
                await query.edit_message_text("❌ Sudah absen masuk hari ini.")
                return
            if absen:
                self.model.update_masuk(absen[0])
            else:
                self.model.insert_absen_masuk(emp_id, shift, today)

            await query.edit_message_text(f"✅ Absensi masuk shift {shift} disimpan.")
        elif tipe == "pulang":
            if not absen or not absen[1]:
                await query.edit_message_text("❌ Belum absen masuk.")
                return
            if absen[2]:
                await query.edit_message_text("❌ Sudah absen pulang.")
                return
            self.model.update_pulang(absen[0])
            await query.edit_message_text(f"✅ Absensi pulang shift {shift} disimpan.")

    async def status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        status_data = self.model.get_status_by_telegram_id(user_id)

        if not status_data:
            await update.message.reply_text("❌ Kamu belum terdaftar di sistem.")
            return

        nama, tanggal, shift, masuk, pulang = status_data
        tanggal = tanggal or datetime.datetime.today().isoformat()
        shift = shift or "-"
        masuk = masuk or "belum absen"
        pulang = pulang or "belum absen"

        text = (
            f"📋 *Status Absensi Hari Ini*\n"
            f"📅 Tanggal: *{tanggal}*\n"
            "\n"
            f"👤 Nama: *{nama}*\n"
            f"🕘 Shift: *{shift}*\n"
            "\n"
            f"✅ Masuk: *{masuk}*\n"
            f"❌ Pulang: *{pulang}*"
        )

        await update.message.reply_text(text, parse_mode="MARKDOWN")
        # await update.message.reply_text(str(status_data))
