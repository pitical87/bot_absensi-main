from database.connection import get_connection


class AbsensiModel:
    def __init__(self):
        self.conn = get_connection()
        if self.conn is None:
            raise Exception("Failed to connect to database")
        self.cursor = self.conn.cursor()

    def get_employees(self):
        if not self.cursor:
            return []
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        result = cursor.fetchall()
        conn.close()
        return result

    def get_employee_id(self, telegram_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM employees WHERE telegram_id = %s", (telegram_id,)
        )
        result = cursor.fetchone()
        return result[0] if result else None

    def get_employee_name_by_telegram_id(self, telegram_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM employees WHERE telegram_id = %s", (telegram_id,)
        )
        result = cursor.fetchone()
        return result[0] if result else None

    def get_attendance(self, emp_id, date, shift):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, masuk, pulang FROM attendance
            WHERE employee_id = %s AND tanggal = %s AND shift = %s
        """,
            (emp_id, date, shift),
        )
        return cursor.fetchone()

    def insert_absen_masuk(self, emp_id, shift, date):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO attendance (employee_id, shift, masuk, tanggal)
            VALUES (%s, %s, CURTIME(), %s)
        """,
            (emp_id, shift, date),
        )
        conn.commit()

    def update_masuk(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE attendance SET masuk = CURTIME() WHERE id = %s", (id,)
        )
        conn.commit()

    def update_pulang(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE attendance SET pulang = CURTIME() WHERE id = %s",
            (id,),
        )
        conn.commit()

    def update_logbook(self, emp_id, tanggal, logbook, shift):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE attendance set  
            logbook = %s
            WHERE employee_id = %s AND tanggal = %s AND shift = %s 
        """,
            (logbook, emp_id, tanggal, shift),
        )
        conn.commit()

    def get_latest_shift(self, emp_id, date):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT shift FROM attendance WHERE employee_id = %s AND tanggal = %s ORDER BY id DESC LIMIT 1",
            (emp_id, date),
        )
        result = cursor.fetchone()
        return result[0] if result else None

    def is_logbook_filled(self, emp_id, date, shift):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT logbook FROM attendance WHERE employee_id = %s AND tanggal = %s AND shift = %s",
            (emp_id, date, shift),
        )
        result = cursor.fetchone()

        logbook = result[0] if result else None
        return bool(logbook and str(logbook).strip())

    def get_rekap_data(self, jenis, bulan, tahun, telegram_id):
        if jenis == "absensi":
            query = """
                SELECT a.tanggal, a.shift, a.masuk, a.pulang
                FROM attendance a
                LEFT JOIN employees e ON e.id = a.employee_id
                WHERE MONTH(a.tanggal) = %s 
                AND YEAR(a.tanggal) = %s 
                AND e.telegram_id = %s
                ORDER BY a.tanggal
            """
        elif jenis == "logbook":
            query = """
                SELECT a.tanggal, a.shift, a.logbook
                FROM attendance a
                LEFT JOIN employees e ON e.id = a.employee_id
                WHERE MONTH(a.tanggal) = %s 
                AND YEAR(a.tanggal) = %s 
                AND e.telegram_id = %s
                  AND a.logbook IS NOT NULL AND a.logbook != '' 
                ORDER BY a.tanggal
            """
        else:
            return []
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query, (bulan, tahun, telegram_id))
        return cursor.fetchall()

    def get_status_by_telegram_id(self, telegram_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT e.name, a.tanggal, a.shift, a.masuk, a.pulang FROM employees e LEFT JOIN
            attendance a ON e.id = a.employee_id AND a.tanggal = CURDATE() WHERE e.telegram_id = %s
            """,
            (telegram_id,),
        )
        return cursor.fetchone()
