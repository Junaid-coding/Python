import time
def shutdown_system():
    print("\n System Shutdown Initiated...")
    for i in range(5, 0, -1):
        print(f"Shutting down in {i} seconds")
        time.sleep(1)
    print("System has been shut down successfully (simulation)")
def restart_system():
    print("\nSystem Restart Initiated...")
    for i in range(3, 0, -1):
        print(f"Restarting in {i} seconds")
        time.sleep(1)
    print("System restarted successfully (simulation).")
print("===== SYSTEM CONTROL PROGRAM ======  ")
print("1. Shutdown System")
print("2. Restart System")
choice = input("Enter your choice (1/2): ")
if choice == "1":
     shutdown_system()   
elif choice == "2":
    restart_system()
else:
        print("Invalid choice! Program ended.")