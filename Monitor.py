import subprocess
import time

adb_path = r"C:\Users\Lukio-4090\OneDrive\Desktop\platform-tools\adb.exe"

def get_adb_devices():
    command = f"{adb_path} devices"
    result = subprocess.check_output(command, shell=True).decode("utf-8").strip()
    lines = result.split("\n")[1:]
    return [line.split()[0] for line in lines]

def write_to_file(filename, device_ids):
    with open(filename, "w") as f:
        for device_id in device_ids:
            f.write(f"{device_id}\n")

def read_from_file(filename):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        open(filename, "w").close()  # Create the file
        return []

def main():
    while True:
        # Get connected devices
        connected_devices = get_adb_devices()

        # Read online, disconnected, and completed device lists from files
        online_devices = read_from_file("online_devices.txt")
        disconnected_devices = read_from_file("disconnected_devices.txt")
        completed_devices = read_from_file("completed_devices.txt")

        # Update online and disconnected device lists
        new_online_devices = [d for d in connected_devices if d not in online_devices]
        new_disconnected_devices = [d for d in online_devices if d not in connected_devices]

        online_devices = connected_devices
        disconnected_devices += new_disconnected_devices

        # Remove disconnected devices from the completed devices list
        for device_id in new_disconnected_devices:
            if device_id in completed_devices:
                completed_devices.remove(device_id)

        # Run adb commands on new online devices
        for device_id in new_online_devices:
            if device_id not in completed_devices:
                # Wait for 30 seconds if the device is still booting
                time.sleep(25)
                retries = 0
                while retries < 10:
                    retries += 1
                    try:
                        subprocess.run(f"{adb_path} -s {device_id} shell dumpsys battery set temp 150", shell=True)
                        subprocess.run(f"{adb_path} -s {device_id} shell dumpsys battery set level 100", shell=True)
                        subprocess.run(f"{adb_path} -s {device_id} shell input swipe 500 1200 500 100", shell=True)
                        time.sleep(3)
                        subprocess.run(f"{adb_path} -s {device_id} shell input keyevent 3", shell=True)
                        time.sleep(5)
                        subprocess.run(f"{adb_path} -s {device_id} shell input keyevent 3", shell=True)
                        subprocess.run(f"{adb_path} -s {device_id} shell input keyevent 3", shell=True)
                        subprocess.run(f"{adb_path} -s {device_id} shell input keyevent 66", shell=True)
                        time.sleep(1)
                        subprocess.run(f"{adb_path} -s {device_id} shell input keyevent 66", shell=True)
                        time.sleep(5)
                        subprocess.run(f"{adb_path} -s {device_id} shell am start -n tech.ula/.MainActivity", shell=True)
                        time.sleep(10)
                        subprocess.run(f"{adb_path} -s {device_id} shell input keyevent 66", shell=True)
                        time.sleep(3)
                        subprocess.run(f"{adb_path} -s {device_id} shell input keyevent 66", shell=True)
                        time.sleep(3)
                        subprocess.run(f"{adb_path} -s {device_id} shell input text \"password\"", shell=True)
                        time.sleep(3)
                        subprocess.run(f"{adb_path} -s {device_id} shell input keyevent 66", shell=True)
                        time.sleep(3)
                        subprocess.run(f"{adb_path} -s {device_id} shell input text \"cd%sccminer\"", shell=True)
                        subprocess.run(f"{adb_path} -s {device_id} shell input keyevent 66", shell=True)
                        subprocess.run(f"{adb_path} -s {device_id} shell input text \"./start.sh\"", shell=True)
                        subprocess.run(f"{adb_path} -s {device_id} shell input keyevent 66", shell=True)
                        subprocess.run(f"{adb_path} -s {device_id} shell input keyevent 4", shell=True)
                        subprocess.run(f"{adb_path} -s {device_id} shell svc power stayon true", shell=True)
                        subprocess.run(f"{adb_path} -s {device_id} shell input keyevent 26", shell=True)
                        completed_devices.append(device_id)
                        break
                    except subprocess.CalledProcessError:
                        pass

        # Save device IDs to files
        write_to_file("online_devices.txt", online_devices)
        write_to_file("disconnected_devices.txt", disconnected_devices)
        write_to_file("completed_devices.txt", completed_devices)

        # Sleep for 2 seconds before running again
        time.sleep(2)

if __name__ == "__main__":
    main()
