import tarfile
from datetime import datetime
from pathlib import Path

def backup_files():
    source_dir = "data/test_files"
    backup_dir = "backups"
    Path(backup_dir).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"backup_{timestamp}.tar.gz"
    backup_path = Path(backup_dir) / backup_filename
    with tarfile.open(backup_path, "w:gz") as tar:
        tar.add(source_dir, arcname="backup_data")
    print(f"Backup created successfully at: {backup_path} ✅")
    return backup_path

if __name__ == "__main__":
    backup_files()
