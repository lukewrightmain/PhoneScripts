import subprocess
import requests
import threading
import time
import os

# Define the path to the adb and fastboot executables
adb_path = r"C:\Users\Lukio-4090\OneDrive\Desktop\platform-tools\adb.exe"
fastboot_path = r"C:\Users\Lukio-4090\OneDrive\Desktop\platform-tools\fastboot.exe"

# Function to get a list of connected devices
def get_connected_devices():
    result = subprocess.run([adb_path, 'devices'], capture_output=True, text=True)
    devices = result.stdout.splitlines()
    device_list = [device.split('\t')[0] for device in devices if '\tdevice' in device]
    return device_list

# Function to simulate a tap on the screen
def tap_screen(device_id, x, y):
    subprocess.run([adb_path, '-s', device_id, 'shell', 'input', 'tap', str(x), str(y)])

# Function to type text
def type_text(device_id, text):
    subprocess.run([adb_path, '-s', device_id, 'shell', 'input', 'text', text])

def long_press(device_id, x, y, duration):
    subprocess.run([adb_path, '-s', device_id, 'shell', 'input', 'swipe', str(x), str(y), str(x), str(y), str(duration)])

def run_in_userland(device_id, command):
    # Replace spaces with '%s' and escape special characters
    formatted_command = command.replace(' ', '%s').replace('&', '\&').replace('|', '\|')
    # Enter the command in the terminal
    subprocess.run([adb_path, '-s', device_id, 'shell', 'input', 'text', formatted_command])
    # Send the Enter key event
    subprocess.run([adb_path, '-s', device_id, 'shell', 'input', 'keyevent', '66'])
    time.sleep(10)

def setup_userland(device_id):
    # Launch Userland
    subprocess.run([adb_path, '-s', device_id, 'shell', 'am start -n tech.ula/.MainActivity'])
    time.sleep(10)  # Wait for Userland to launch

    # Interact with the UserLAnd App
    # Tap on "Ubuntu" option
    tap_screen(device_id, 328, 1036)  # Replace with actual coordinates
    time.sleep(2)

    # Tap on "OK" and "ALLOW"
    tap_screen(device_id, 557, 919)  # Replace with coordinates for "OK"
    time.sleep(1)
    tap_screen(device_id, 346, 863)  # Replace with coordinates for "ALLOW"
    time.sleep(1)

    # Enter username, password, and VNC password
    tap_screen(device_id, 240, 667)
    time.sleep(2) 
    type_text(device_id, 'x')  # Enter username
    time.sleep(2)
    tap_screen(device_id, 171, 590)  # Move to next field
    time.sleep(2)
    type_text(device_id, 'password')  # Enter password
    time.sleep(2)
    tap_screen(device_id, 198.6, 737.5)  # Move to VNC password field
    time.sleep(2)
    type_text(device_id, 'password')  # Enter VNC password
    time.sleep(2)

    # Tap on "CONTINUE"
    tap_screen(device_id, 526, 828)  # First "CONTINUE"
    time.sleep(2)
    tap_screen(device_id, 505, 991)  # Second "CONTINUE"
    time.sleep(1800)  # Wait for 5 minutes.

    # Close Userland (force stop)
    subprocess.run([adb_path, '-s', device_id, 'shell', 'am force-stop tech.ula'])
    time.sleep(5)

    # Re-launch Userland to open terminal
    subprocess.run([adb_path, '-s', device_id, 'shell', 'am start -n tech.ula/.MainActivity'])
    time.sleep(10)

    # Tap to setup AutoSTART TERMINAL
    tap_screen(device_id, 345.5, 128)  # Tap Top incase of messages.
    time.sleep(1)
    long_press(device_id, 344.5, 1042.3, 2000)
    tap_screen(device_id, 433.3, 1104.3) #Tap App INFO
    time.sleep(1)
    tap_screen(device_id, 167.8, 316.7)
    time.sleep(1)
    tap_screen(device_id, 167.8, 316.7)
    time.sleep(1)
    tap_screen(device_id, 229.6, 1216.1)
    time.sleep(1)

    # Close Userland (force stop)
    subprocess.run([adb_path, '-s', device_id, 'shell', 'am force-stop tech.ula'])
    time.sleep(5)

    # Re-launch Userland to open terminal
    subprocess.run([adb_path, '-s', device_id, 'shell', 'am start -n tech.ula/.MainActivity'])
    time.sleep(10)

    # Run the setup commands in the terminal
    ul_setup_commands = [
        'password',
    ]

        # Run the setup commands in the terminal
    ul_setup_commands2 = [
        'curl -o- -k https://raw.githubusercontent.com/lukewrightmain/VerusCliMining/main/install.sh | bash',
    ]

    for command in ul_setup_commands:
        run_in_userland(device_id, command)
        time.sleep(10)  # Adjust this based on your command execution time

    for command in ul_setup_commands2:
        run_in_userland2(device_id, command)
        time.sleep(10)  # Adjust this based on your command execution time

def run_in_userland(device_id, command):
    # No need to escape '&' and '|'
    formatted_command = command.replace(' ', '%s')
    # Enter the command in the terminal
    subprocess.run([adb_path, '-s', device_id, 'shell', 'input', 'text', formatted_command])
    # Send the Enter key event
    subprocess.run([adb_path, '-s', device_id, 'shell', 'input', 'keyevent', '66'])
    time.sleep(10)

def run_in_userland2(device_id, command):
    # Escape special characters
    escaped_command = command.replace(' ', '%s').replace('&', '\\&').replace('|', '\\|')

    # Enter the command in the terminal
    subprocess.run([adb_path, '-s', device_id, 'shell', 'input', 'text', escaped_command])
    # Send the Enter key event
    subprocess.run([adb_path, '-s', device_id, 'shell', 'input', 'keyevent', '66'])
    time.sleep(1800)


def reboot_into_fastboot(device_id):
    subprocess.run([adb_path, '-s', device_id, 'reboot', 'bootloader'])
    print(f"Rebooting {device_id} into fastboot mode...")
    time.sleep(10)

def run_fastboot_command(device_id, command):
    subprocess.run([fastboot_path, '-s', device_id] + command.split())
    print(f"Fastboot command executed on {device_id}.")

def reboot_phone(device_id):
    subprocess.run([fastboot_path, '-s', device_id, 'reboot'])
    print(f"Rebooting {device_id}...")


def device_setup(device_id, apk_file_path):
    print(f"Setting up device: {device_id}")

    # Install the APK on the current device
    subprocess.run([adb_path, '-s', device_id, 'install', apk_file_path])
    print(f"APK installed on {device_id}.")

    setup_userland(device_id)

    reboot_into_fastboot(device_id)
    time.sleep(5)
    run_fastboot_command(device_id, r'oem off-mode-charge 0')
    time.sleep(3)
    reboot_phone(device_id)

    print(f'Device {device_id} setup complete.')

def main():
    devices = get_connected_devices()

    # Define the APK URL and download it
    apk_url = 'https://github.com/CypherpunkArmory/UserLAnd/releases/download/v2.8.3/app-release.apk'
    apk_file_name = apk_url.split('/')[-1]
    apk_file_path = os.path.join(os.getcwd(), apk_file_name)

    response = requests.get(apk_url)
    if response.status_code == 200:
        with open(apk_file_path, 'wb') as f:
            f.write(response.content)
        print("APK downloaded successfully.")
    else:
        print(f"Failed to download APK: {response.status_code}")
        return  # Exit if download fails

    threads = []
    for device_id in devices:
        thread = threading.Thread(target=device_setup, args=(device_id, apk_file_path))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

print('Userland setup and ccminer installation complete on all connected devices.')