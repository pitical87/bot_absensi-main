# Simple Telegram Bot for Attendance

A personal telegram bot for generating attendance reports and tracking employee attendance in my office.

## Telegram Bot

### Features

- Track employee attendance via Telegram
- Fill in daily logbook entries
- Generate PDF reports per employee (monthly)

### Requirements

- Python 3.8+
- Telegram Bot API token
- MYSQL (default), or adapt to another DB engine

### Installation

1. Step 1: Clone the repository

```bash
$git clone https://github.com/your-username/rekap-absensi-bot.git
```

2. Step 2: Create and activate virtual env

```bash
   python -m venv (your virtual env bname) //create virtual env
   (your virtual env bname)\Scripts\activate
```

3. Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

4. Step 4: Create your own telegram bot with @botfather and mysql database

5. Step 5: Create .env file that include bot token and db configurations (host name, user, password and db name).

6. Step 6: Set up database connection

```bash
python setup.py
```

7. Step 7: Start the bot

```bash
python bot.py
```

### Usage

**Use the following commands:**

- `/start` – Mulai bot
- `/absensi` – Isi absensi harian
- `/logbook` – Isi logbook
- `/status` – Lihat status absensi hari ini
- `/rekap` – Buat rekap PDF

## Web Admin

Simple web service for admin

### Features

- Basic CRUD for attendance, employee and admin
- Attendance & logbook recap for all employee (monthly)

### Requirements

- PHP, for this project i use version 8.3.8
- PHPDOTENV library to load variables from .env file

### Installation

1. Install phpdotenv library with composer (assuming you have installed composer)

```bash
$ composer require vlucas/phpdotenv
```

2. Run the project locally (im using laragon)
