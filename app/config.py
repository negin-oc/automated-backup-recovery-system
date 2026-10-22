from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BACKUP_DIR = BASE_DIR / "backups"
SOURCE_DIR = BASE_DIR / "data"
RESTORE_DIR = BASE_DIR / "restored_files"
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "app.log"

for directory in (BACKUP_DIR, SOURCE_DIR, RESTORE_DIR, LOG_DIR):
    directory.mkdir(parents=True, exist_ok=True)
