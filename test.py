import os
import requests
import time

# Get the base URL from environment variable
base_url = os.environ.get('BASE_URL')
if not base_url:
    base_url = input("Enter the base URL for LED control (e.g., https://your-ngrok-url.app): ")

# Function to toggle LED
def toggle_led(color, state):
    endpoint = f"/toggle_{color}"
    payload = {f"{color}Led": state}
    url = f"{base_url}{endpoint}"
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"{color.capitalize()} LED turned {'on' if state else 'off'} successfully.")
        else:
            print(f"Failed to toggle {color} LED. Status: {response.status_code}")
    except Exception as e:
        print(f"Error toggling {color} LED: {e}")

# Test sequence: Turn each on, wait 2 seconds, turn off
colors = ['yellow', 'green', 'red']

for color in colors:
    print(f"Testing {color} LED...")
    toggle_led(color, True)  # On
    time.sleep(2)
    toggle_led(color, False)  # Off
    time.sleep(1)

print("Testing complete.")
