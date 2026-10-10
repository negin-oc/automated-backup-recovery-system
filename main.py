from backup import backup_files
from restore import restore_files

def main():
    while True:
        print("\n" + "="*30)
        print("  BACKUP & RESTORE PRO")
        print("="*30)
        print("1. Create Backup")
        print("2. Restore Backup")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ")
        
        if choice == "1":
            backup_files()
        elif choice == "2":
            restore_files()
        elif choice == "3":
            print("Thank you for using the system. Goodbye! 👋")
            break
        else:
            print("Invalid choice, please try again! ❌")

if __name__ == "__main__":
    main()
