import tarfile
from datetime import datetime
from pathlib import Path

def backup_files():
    source_dir = Path("data/test_files")
    backup_dir = Path("backups")
    
    # Ensure backup directory exists
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    if not source_dir.exists():
        print("Error: Source directory 'data/test_files' not found! ❌")
        return None

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"backup_{timestamp}.tar.gz"
    backup_path = backup_dir / backup_filename
    
    try:
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add(source_dir, arcname="backup_data")
        print(f"Backup created successfully: {backup_filename} ✅")
        return backup_path
    except Exception as e:
        print(f"Backup failed: {e} ❌")
        return None

if __name__ == "__main__":
    backup_files()
