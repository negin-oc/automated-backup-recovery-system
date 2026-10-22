from backup import backup_files
import sys

if __name__ == "__main__":
    print("Starting automated backup...")
    try:
        backup_files()
        print("Automated backup completed successfully!")
    except Exception as e:
        print(f"Error during automated backup: {e}")
        sys.exit(1)
