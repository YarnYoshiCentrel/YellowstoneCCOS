import os
import time
import webbrowser
from datetime import datetime

import winsound

def play_boot_sound():
    sound_file = os.path.join(os.path.dirname(__file__), "boot.wav")
    if os.path.exists(sound_file):
        try:
            winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
        except RuntimeError as e:
            print("[!] Could not play sound:", e)
    else:
        print("[!] Boot sound not found. Skipping...\n")


# ---- Logo ----
def show_logo():
    logo = """
     ╔═══════════════════════════════╗
     ║       CENTREL COMPUTING       ║
     ║       OPERATING SYSTEM        ║
     ╚═══════════════════════════════╝
    """
    print(logo)
    time.sleep(1)

# ---- Commands ----
def show_help():
    print("""
Available Commands:
  help         - Show this help menu
  time         - Display current time
  calc         - Open calculator
  read         - Read a .txt file
  browser      - Open a real web browser
  wifi         - Connect or disconnect from CentrelNet
  clear        - Clear the screen
  exit         - Shutdown CentrelOS
    """)

def show_time():
    print("Current time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def calc():
    try:
        expr = input("Enter math expression: ")
        result = eval(expr)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

def read_file():
    file_name = input("Enter text file name: ")
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            print("\n--- File Content ---")
            print(file.read())
            print("--------------------")
    else:
        print("File not found.")

wifi_connected = False
def wifi():
    global wifi_connected
    if wifi_connected:
        print("Wi-Fi disconnected.")
        wifi_connected = False
    else:
        print("Connecting to CentrelNet...")
        time.sleep(1)
        print("Connected to CentrelNet.")
        wifi_connected = True

def browser():
    if not wifi_connected:
        print("No Wi-Fi connection. Type 'wifi' to connect first.")
        return
    url = input("Enter website (example.com or full URL): ")
    if not url.startswith("http"):
        url = "https://" + url
    print("Opening browser...")
    webbrowser.open(url)

# ---- Main Terminal Loop ----
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    play_boot_sound()
    show_logo()
    print("Welcome to CentrelOS Beta\n")

    while True:
        command = input("CentrelOS> ").lower()
        if command == "help":
            show_help()
        elif command == "time":
            show_time()
        elif command == "calc":
            calc()
        elif command == "read":
            read_file()
        elif command == "browser":
            browser()
        elif command == "wifi":
            wifi()
        elif command == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif command == "exit":
            print("Shutting down CentrelOS...")
            time.sleep(1)
            break
        elif command == "":
            continue
        else:
            print("Unknown command. Type 'help' to see options.")

if __name__ == "__main__":
    main()
