import ipaddress
import subprocess
import platform

def validate_ip():
    ip = input("Enter an IP address: ")

    try:
        ipaddress.ip_address(ip)
        print("✅ Valid IP address")
    except ValueError:
        print("❌ Invalid IP address")

def ping_host():
    host =  input("Enter Ip or domain to ping: ")

    param = "-n" if platform.system().lower() == "windows" else "-c"

    command = ["ping", param, "4", host]

    try:
        subprocess.run(command)
    except Exception as e:
        print("Error", e)

def menu():
    print("\n=== Network Troubleshooting Toolkit ===")
    print("1, Validate IP Address")
    print("2. Ping a Host")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        validate_ip()
    elif choice == "2":
        ping_host()
    elif choice == "3":
        print ("Goodbye")
    else:
        print("Invalid option")

while True:
    menu()
