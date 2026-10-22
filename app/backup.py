import tarfile
import logging
from datetime import datetime
from pathlib import Path

# Configure logging to save to a file
logging.basicConfig(
    filename="app.log", 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def backup_files():
    source_dir = Path("data/test_files")
    backup_dir = Path("backups")
    
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    if not source_dir.exists():
        error_msg = "Source directory 'data/test_files' not found!"
        print(f"Error: {error_msg} ❌")
        logging.error(error_msg)
        return None

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"backup_{timestamp}.tar.gz"
    backup_path = backup_dir / backup_filename
    
    try:
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add(source_dir, arcname="backup_data")
        
        success_msg = f"Backup created successfully: {backup_filename}"
        print(f"{success_msg} ✅")
        logging.info(success_msg)
        return backup_path
    except Exception as e:
        error_msg = f"Backup failed: {e}"
        print(f"{error_msg} ❌")
        logging.error(error_msg)
        return None

if __name__ == "__main__":
    backup_files()
