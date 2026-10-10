import tarfile
from pathlib import Path

def restore_files():
    backup_dir = Path("backups")
    restore_dir = Path("data/restored_files")

    if not backup_dir.exists():
        print("No backups directory found! ❌")
        return

    # Get list of all backup files
    backups = sorted(backup_dir.glob("*.tar.gz"))
    if not backups:
        print("No backup files available for recovery! ❌")
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
            print(f"Successfully restored from {selected_backup.name}! ✅")
        else:
            print("Invalid selection! ❌")
    except ValueError:
        print("Please enter a valid number! ❌")
    except Exception as e:
        print(f"Restore failed: {e} ❌")

if __name__ == "__main__":
    restore_files()
