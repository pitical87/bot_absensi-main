from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, ConversationHandler
import datetime
from models.absensi_model import AbsensiModel  # gunakan model yang sama
from utils.pdf_generator import generate_pdf_rekap

REKAP_JENIS, REKAP_BULAN, REKAP_TAHUN = range(3)


class RekapController:
    def __init__(self):
        self.model = AbsensiModel()

    async def pilih_jenis(self, update=Update, context=ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [InlineKeyboardButton("Absensi", callback_data="jenis:absensi")],
            [InlineKeyboardButton("Logbook", callback_data="jenis:logbook")],
        ]
        await update.message.reply_text(
            "Pilih jenis rekap:", reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return REKAP_JENIS

    async def pilih_bulan(self, update=Update, context=ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        jenis = query.data.split(":")[1]
        context.user_data["jenis_rekap"] = jenis

        keyboard = []
        for i in range(1, 13, 3):
            row = [
                InlineKeyboardButton(
                    datetime.date(1900, j, 1).strftime("%B"), callback_data=f"bulan:{j}"
                )
                for j in range(i, i + 3)
            ]
            keyboard.append(row)
        await query.edit_message_text(
            "Pilih bulan:", reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return REKAP_BULAN

    async def pilih_tahun(self, update=Update, context=ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        bulan = query.data.split(":")[1]
        context.user_data["bulan_rekap"] = int(bulan)

        tahun_sekarang = datetime.date.today().year
        keyboard = [
            [InlineKeyboardButton(str(t), callback_data=f"tahun:{t}")]
            for t in range(tahun_sekarang - 2, tahun_sekarang + 1)
        ]
        await query.edit_message_text(
            "pilih tahun:", reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return REKAP_TAHUN

    async def hasil_rekap(self, update: Update, context=ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        tahun = int(query.data.split(":")[1])
        bulan = context.user_data["bulan_rekap"]
        jenis = context.user_data["jenis_rekap"]

        user_id = update.effective_user.id
        nama = self.model.get_employee_name_by_telegram_id(user_id)

        data = self.model.get_rekap_data(jenis, bulan, tahun, user_id)
        pdf_file = generate_pdf_rekap(data, nama, bulan, tahun, jenis)

        await query.edit_message_text("✅ Berikut hasil rekap dalam bentuk pdf: ")
        await query.message.reply_document(
            document=pdf_file, filename=f"rekap-{jenis}.pdf"
        )
        return ConversationHandler.END

    async def batal(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("❌ Rekap dibatalkan.")
        return ConversationHandler.END
