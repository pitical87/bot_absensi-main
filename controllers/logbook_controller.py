import datetime
from telegram import Update, ForceReply
from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, filters
from models.absensi_model import AbsensiModel

ISI_LOGBOOK = 0


class LogbookController:
    def __init__(self):
        self.model = AbsensiModel()

    async def isi_logbook(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        emp_id = self.model.get_employee_id(update.effective_user.id)
        if not emp_id:
            await update.message.reply_text("❌ Kamu belum terdaftar di sistem.")
            return ConversationHandler.END

        today = datetime.date.today().isoformat()
        shift = self.model.get_latest_shift(emp_id, today)

        if not shift:
            await update.message.reply_text("❌ Kamu belum absen masuk hari ini.")
            return ConversationHandler.END

        if self.model.is_logbook_filled(emp_id, today, shift):
            await update.message.reply_text("❌ Logbook untuk hari ini sudah diisi.")
            return ConversationHandler.END

        context.user_data["employee_id"] = emp_id
        context.user_data["tanggal"] = today
        context.user_data["shift"] = shift

        await update.message.reply_text(
            "📝 Silakan tuliskan logbook kamu untuk hari ini:",
            reply_markup=ForceReply(selective=True),
        )
        return ISI_LOGBOOK

    async def simpan_logbook(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        logbook_text = update.message.text.strip()
        emp_id = context.user_data.get("employee_id")
        tanggal = context.user_data.get("tanggal")
        shift = context.user_data.get("shift")

        if not (emp_id and tanggal and shift):
            await update.message.reply_text("❌ Data tidak lengkap.")
            return ConversationHandler.END

        self.model.update_logbook(emp_id, tanggal, logbook_text, shift)
        await update.message.reply_text("✅ Logbook berhasil disimpan. Terima kasih!")
        return ConversationHandler.END

    async def batal_logbook(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("❌ Pengisian logbook dibatalkan.")
        return ConversationHandler.END
