import tarfile
import logging
from pathlib import Path
import os

# Configure logging
logging.basicConfig(
    filename="app.log", 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message) s"
)

def restore_files():
    # Use absolute path based on where the script is located
    script_dir = Path(__file__).parent.absolute()
    backup_dir = script_dir / "backups"
    restore_dir = script_dir / "data" / "restored_files"

    if not backup_dir.exists():
        error_msg = f"No backups directory found at {backup_dir}"
        print(f"Error: {error_msg} ❌")
        logging.error(error_msg)
        return

    # Search for all .tar.gz files
    backups = sorted(backup_dir.glob("*.tar.gz"))

    if not backups:
        error_msg = f"No backup files available for recovery in {backup_dir}"
        print(f"Error: {error_msg} ❌")
        logging.error(error_msg)
        return

    print("\nAvailable backups:")
    for i, backup in enumerate(backups, 1):
        print(f"{i}. {backup.name}")

    try:
        choice = int(input("\nSelect backup number to restore: "))
        if 1 <= choice <= len(backups):
            selected_backup = backups[choice - 1]
            restore_dir.mkdir(parents=True, exist_ok=True)

            with tarfile.open(selected_backup, "r:gz") as tar:
                tar.extractall(path=restore_dir)

            success_msg = f"Successfully restored from {selected_backup.name}"
            print(f"{success_msg}! ✅")
            logging.info(success_msg)
        else:
            print("Invalid selection! ❌")
    except ValueError:
        print("Please enter a valid number! ❌")
    except Exception as e:
        error_msg = f"Restore failed: {e}"
        print(f"{error_msg} ❌")
        logging.error(error_msg)

if __name__ == "__main__":
    restore_files()
