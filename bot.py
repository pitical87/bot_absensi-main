from database.setup import setup_database
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)
from controllers.absensi_controller import AbsensiController
from controllers.logbook_controller import LogbookController, ISI_LOGBOOK
from controllers.rekap_controller import RekapController
from telegram import BotCommand
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

REKAP_JENIS, REKAP_BULAN, REKAP_TAHUN = range(3)


# Fungsi set command menu Telegram
async def set_commands(app):
    await app.bot.set_my_commands(
        [
            BotCommand("start", "Mulai bot"),
            BotCommand("absensi", "Isi absensi harian"),
            BotCommand("logbook", "Isi logbook harian"),
            BotCommand("status", "Status absensi harian"),
            BotCommand("rekap", "Rekap dokumen"),
        ]
    )


def main():
    # Setup database
    setup_database()

    # Buat aplikasi
    app = Application.builder().token(TOKEN).build()

    # Inisialisasi controller
    absensi_controller = AbsensiController()
    logbook_controller = LogbookController()
    rekap_controller = RekapController()

    # 📌 Handler Absensi
    app.add_handler(CommandHandler("start", absensi_controller.start))
    app.add_handler(CommandHandler("absensi", absensi_controller.isi_absensi))
    app.add_handler(
        CallbackQueryHandler(absensi_controller.select_name, pattern="^absen:")
    )
    app.add_handler(
        CallbackQueryHandler(absensi_controller.select_shift, pattern="^shift:")
    )
    app.add_handler(
        CallbackQueryHandler(absensi_controller.confirm_absensi, pattern="^tipe:")
    )
    app.add_handler(
        CallbackQueryHandler(
            absensi_controller.simpan_absensi, pattern="^simpan_absensi$"
        )
    )
    app.add_handler(CommandHandler("status", absensi_controller.status))

    # 📌 Handler Logbook (pakai ConversationHandler)
    logbook_conv = ConversationHandler(
        entry_points=[CommandHandler("logbook", logbook_controller.isi_logbook)],
        states={
            ISI_LOGBOOK: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND, logbook_controller.simpan_logbook
                )
            ],
        },
        fallbacks=[CommandHandler("batal", logbook_controller.batal_logbook)],
        per_message=True
    )
    app.add_handler(logbook_conv)

    rekap_conv = ConversationHandler(
        entry_points=[CommandHandler("rekap", rekap_controller.pilih_jenis)],
        states={
            REKAP_JENIS: [
                CallbackQueryHandler(rekap_controller.pilih_bulan, pattern="^jenis:")
            ],
            REKAP_BULAN: [
                CallbackQueryHandler(rekap_controller.pilih_tahun, pattern="^bulan:")
            ],
            REKAP_TAHUN: [
                CallbackQueryHandler(rekap_controller.hasil_rekap, pattern="^tahun:")
            ],
        },
        fallbacks=[CommandHandler("batal", rekap_controller.batal)],
        
    )
    app.add_handler(rekap_conv)

    # Set command menu
    async def after_startup(app):
        await set_commands(app)

    app.post_init = after_startup

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
