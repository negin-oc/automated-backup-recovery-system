from backup import backup_files
from restore import restore_files

def main():
    while True:
        print("\n--- Backup and Restore System ---")
        print("1. Backup")
        print("2. Restore")
        print("3. Exit")
        
        choice = input("Please select an option (1-3): ")
        
        if choice == "1":
            backup_files()
        elif choice == "2":
            restore_files()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
