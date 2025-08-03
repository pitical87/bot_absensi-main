from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class AbsensiView:
    @staticmethod
    def get_karyawan_keyboard(karyawan):
        return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, callback_data=f"absen:{name}:{emp_id}:{telegram_id}"
                    )
                ]
                for emp_id, name, telegram_id in karyawan
            ]
        )

    @staticmethod
    def get_shift_keyboard():
        return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Pagi (08.00-14.00)", callback_data="shift:pagi"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Sore (14.00-20.00)", callback_data="shift:sore"
                    )
                ],
            ]
        )

    @staticmethod
    def get_tipe_keyboard():
        return InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Masuk", callback_data="tipe:masuk")],
                [InlineKeyboardButton("Pulang", callback_data="tipe:pulang")],
            ]
        )

    @staticmethod
    def get_konfirmasi_keyboard():
        return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💾 Simpan Absensi", callback_data="simpan_absensi"
                    )
                ]
            ]
        )

    @staticmethod
    def get_konfirmasi_text(nama, shift, tipe):
        return (
            f"📝 Konfirmasi Absensi:\n"
            f"Nama: {nama}\nShift: {shift.title()}\nTipe: {tipe.title()}\n\n"
            f"Tekan tombol di bawah untuk menyimpan."
        )
