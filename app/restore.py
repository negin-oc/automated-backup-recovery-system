import tarfile
from pathlib import Path
import os

def restore_files():
    # Use absolute path to avoid confusion
    backup_dir = Path("backups")
    restore_dir = Path("data/restored_files")

    try:
        # Find all .tar.gz files in the backups folder
        backups = sorted(backup_dir.glob("*.tar.gz"))
        if not backups:
            print("No backup files found for recovery! ❌")
            return

        latest_backup = backups[-1]
        restore_dir.mkdir(parents=True, exist_ok=True)

        with tarfile.open(latest_backup, "r:gz") as tar:
            tar.extractall(path=restore_dir)

        print(f"Files successfully restored from {latest_backup.name}! ✅")
    except Exception as e:
        print(f"Error during restoration: {e}")

if __name__ == "__main__":
    restore_files()
