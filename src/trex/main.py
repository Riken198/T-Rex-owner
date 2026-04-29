def main():
    print("🔥 T-Rex Multi-Scanner v3.0")
    print("Credit: T-Rex Owner 🔥\n")
    print("It's my tool (T-Rex)\n")

    # === Paste your original ARMAN / scanner code here ===
    # For now, use this example menu. Replace with your real code:

    while True:
        print("\nSELECT OPTION")
        print("[1] Domain File Scanner")
        print("[2] Advanced TCP/HTTP Scanner")
        print("[3] Extract Domains by Word")
        print("[4] Clean & Filter Domains")
        print("[5] Exit")

        choice = input("Choose option: ").strip()

        if choice in ["5", "exit", "quit"]:
            print("Exiting T-Rex Scanner... Goodbye!")
            break
        elif choice == "1":
            print("Starting Domain File Scanner...")
            # Add your real code for option 1 here
        elif choice == "2":
            print("Starting Advanced TCP/HTTP Scanner...")
            # Add your real code here
        elif choice == "3":
            print("Extracting Domains by Word...")
        elif choice == "4":
            print("Cleaning & Filtering Domains...")
        else:
            print("Invalid option! Please choose 1-5.")

if __name__ == "__main__":
    main()
