import subprocess
import time

adb_path = "C:\\Users\\Lukio-4090\\OneDrive\\Desktop\\platform-tools\\adb.exe"

def run_adb_command(device, command):
    subprocess.run([adb_path, "-s", device, "shell", command])

def get_connected_devices():
    output = subprocess.getoutput(f"{adb_path} devices")
    lines = output.strip().split("\n")[1:]
    devices = [line.split()[0] for line in lines]
    return devices

if __name__ == "__main__":
    devices = get_connected_devices()
    for device in devices:
        print(f"Executing commands on device {device}")
        
        run_adb_command(device, "svc power stayon true")
        time.sleep(1)
        run_adb_command(device, "input keyevent 26")
        
    print("Done executing commands on all devices.")
