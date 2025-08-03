from database.connection import get_connection


def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100),
            telegram_id INT UNIQUE
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS attendance (
            id INT PRIMARY KEY AUTO_INCREMENT,
            employee_id INTEGER,
            shift VARCHAR(10),
            masuk TIME,
            pulang TIME,
            tanggal DATE DEFAULT (DATE('now')),
            logbook TEXT,
            FOREIGN KEY(employee_id) REFERENCES employees(id)
        )
    """
    )

    conn.commit()
    conn.close()
