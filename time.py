import time
import os

try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears the screen
        current_time = time.strftime("%H:%M:%S")
        print(f"🕒 Current Time: {current_time}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.")
