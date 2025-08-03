import os
import subprocess
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class BotReloader(FileSystemEventHandler):
    def __init__(self, script_name):
        self.script_name = script_name
        self.process = None
        self.restart_pending = False
        self.start_bot()

    def start_bot(self):
        print("🔁 Menjalankan bot...")
        self.process = subprocess.Popen([sys.executable, self.script_name])

    def restart_bot(self):
        print("🔄 Me-restart bot...")
        if self.process:
            self.process.kill()
            self.process.wait()
        self.start_bot()

    def on_any_event(self, event):
        if event.is_directory or not event.src_path.endswith(".py"):
            return
        print(f"📂 Deteksi perubahan file: {event.src_path}")
        self.restart_pending = True
        self.restart_bot()

    def monitor_bot(self):
        while True:
            retcode = self.process.poll()
            if retcode is not None:
                print("❌ Bot crash, mencoba restart...")
                self.start_bot()
            time.sleep(2)

if __name__ == "__main__":
    script = "bot.py"  # ganti kalau nama file utamamu beda
    event_handler = BotReloader(script)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()
    try:
        event_handler.monitor_bot()
    except KeyboardInterrupt:
        print("⛔ Dihentikan oleh pengguna.")
        observer.stop()
        if event_handler.process:
            event_handler.process.kill()
    observer.join()
