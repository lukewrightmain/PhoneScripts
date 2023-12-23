import subprocess
import time

adb_path = "C:\\Users\\Lukio-4090\\OneDrive\\Desktop\\platform-tools\\adb.exe"
fastboot_path = "C:\\Users\\Lukio-4090\\OneDrive\\Desktop\\platform-tools\\fastboot.exe"

def run_adb_command(device, command):
    subprocess.run([adb_path, "-s", device, "shell", command])

def run_fastboot_command(command):
    subprocess.run([fastboot_path, "-s", device, command])

def get_connected_devices():
    output = subprocess.getoutput(f"{adb_path} devices")
    lines = output.strip().split("\n")[1:]
    devices = [line.split()[0] for line in lines]
    return devices

if __name__ == "__main__":
    devices = get_connected_devices()
    for device in devices:
        print(f"Executing commands on device {device}")
        
        run_adb_command(device, "settings put global wifi_sleep_policy 2"),
        run_adb_command(device, "settings put global system_capabilities 100"),
        run_adb_command(device, "settings put global sem_enhanced_cpu_responsiveness 1")
        run_adb_command(device, "settings put global adaptive_battery_management_enable 0"),
        run_adb_command(device, "settings put global adaptive_power_saving_setting 0"),
        run_adb_command(device, "dumpsys deviceidle whitelist +tech.ula"),
        run_adb_command(device, "dumpsys battery set level 100"),  # Removed extra "shell"
        run_adb_command(device, "settings put global window_animation_scale 0"),
        run_adb_command(device, "settings put global transition_animation_scale 0"),
        run_adb_command(device, "settings put global animator_duration_scale 0"),
        run_adb_command(device, "su -c echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"),
        run_adb_command(device, "settings put global background_limit 4")
        run_adb_command(device,"pm uninstall --user 0 com.verizon.dmclientupdate")
        run_adb_command(device,"pm uninstall --user 0 com.verizon.mips.services")
        run_adb_command(device,"pm uninstall --user 0 com.verizon.obdm_permissions")
        run_adb_command(device,"pm uninstall --user 0 com.verizon.obdm")
        run_adb_command(device,"pm uninstall --user 0 com.verizon.messaging.vzmsgs")
        run_adb_command(device,"pm uninstall --user 0 com.verizon.llkagent")
        run_adb_command(device,"pm uninstall --user 0 com.vcast.mediamanager")
        run_adb_command(device,"pm uninstall --user 0 com.vzw.hss.myverizon")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.youtube")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.apps.docs")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.apps.maps")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.calculator")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.apps.photos")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.calendar")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.apps.chromecast.app")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.apps.youtube.music")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.gms.location.history")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.videos")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.setupwizard")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.deskclock")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.apps.tachyon")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.apps.messaging")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.googlequicksearchbox")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.apps.googleassistant")
        run_adb_command(device,"pm uninstall --user 0 com.android.soundrecorder")
        run_adb_command(device,"pm uninstall --user 0 org.codeaurora.dialer")
        run_adb_command(device,"pm uninstall --user 0 com.android.contacts")
        run_adb_command(device,"pm uninstall --user 0 org.codeaurora.snapcam")
        run_adb_command(device,"pm uninstall --user 0 com.android.vending")
        run_adb_command(device,"pm uninstall --user 0 com.google.android.gm")
        run_adb_command(device,"pm uninstall --user 0 com.dreamgames.royalmatch")
        run_adb_command(device,"pm uninstall --user 0 net.supertreat.solitaire")
        run_adb_command(device,"pm uninstall --user 0 com.disney.disneyplus")
        run_adb_command(device,"pm uninstall --user 0 air.com.playtika.slotomania")
        run_adb_command(device,"pm uninstall --user 0 com.tripledot.solitaire")
        run_adb_command(device,"pm uninstall --user 0 com.facebook.appmanager")
        run_adb_command(device,"pm uninstall --user 0 tv.pluto.android")
        run_adb_command(device,"pm uninstall --user 0 com.einnovation.temu")
        run_adb_command(device,"pm uninstall --user 0 com.weather.Weather")
        run_adb_command(device,"pm uninstall --user 0 com.tripledot.woodoku")
        run_adb_command(device,"pm uninstall --user 0 com.king.candycrushsaga")
        run_adb_command(device,"pm uninstall --user 0 com.tubitv")
        run_adb_command(device,"pm uninstall --user 0 in.playsimple.wordtrip")
        run_adb_command(device,"pm uninstall --user 0 com.onedebit.chime")
        run_adb_command(device,"pm uninstall --user 0 me.lyft.android")
        run_adb_command(device,"pm uninstall --user 0 de.wetteronline.wetterapp")
        run_adb_command(device,"pm uninstall --user 0 com.dti.folderlauncher")
        run_adb_command(device,"pm uninstall --user 0 com.huub.viper")
        run_adb_command(device,"pm uninstall --user 0 com.odm.batterypreservation")
        run_adb_command(device,"pm uninstall --user 0 com.fiberlink.maas360.android.control")
        run_adb_command(device,"pm uninstall --user 0 com.facebook.katana")
        run_adb_command(device,"pm uninstall --user 0 com.moonactive.coinmaster")
        run_adb_command(device,"pm uninstall --user 0 air.com.buffalo_studios.newflashbingo")
        run_adb_command(device,"pm uninstall --user 0 in.playsimple.tripcross")
        run_adb_command(device,"pm uninstall --user 0 com.staplegames.dice")
        run_adb_command(device,"pm uninstall --user 0 com.gotv.nflgamecenter.us.lite")
        run_adb_command(device,"pm uninstall --user 0 com.apple.android.music")
        #run_adb_command(device,"pm uninstall --user 0 ")
        time.sleep(3)
        
        # Put the device into fastboot mode
        run_adb_command(device, "reboot bootloader")
        time.sleep(1)

        
    print("Done executing commands on all devices.")
