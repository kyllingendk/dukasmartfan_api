"""
Create a file called ".deviceid" in the current folder.
This file should contain  the duka one device id.
You can see the duka one device id in the duka one app.
"""
import sys
import time

from dukasmartfan_api.dukaclient import DukaClient
from dukasmartfan_api.device import Device, Mode


def onchange(device: Device):
    """Callback function when device changes"""
    print(
        f"ip: {device.ip_address}"
        f" speed: {device.speed},"
        f" manualspeed: {device.manualspeed},"
        f" fan1rpm: {device.fan1rpm},"
        f" mode: {device.mode},"
        f" schedulemode: {device._schedulemode},"
        f" humidity: {device.humidity},"
        f" filter alarm: {device.filter_alarm},"
        f" filter timer; {device.filter_timer} minutes"
    )


def newdevice_callback(deviceid: str):
    print("New device id: " + deviceid)


def main():
    """Main example """
    client: DukaClient = DukaClient()
    client.search_devices(newdevice_callback)
    time.sleep(5)

    # read the device id
    with open(".deviceid", "r") as file:
        device_id = file.readline().replace("\n", "")
        device_pass = file.readline().replace("\n", "")
        device_ip = file.readline().replace("\n", "")
    # initialize the DukaClient and add the device
    mydevice: Device = client.validate_device(device_id, password=device_pass, ip_address=device_ip)
    if mydevice is None:
        print("Device does not respond")
    else:
        mydevice = client.add_device(
            device_id, ip_address=mydevice.ip_address, password="0243", onchange=onchange
        )
        print("Device added")

        print(f"Firmware version: {mydevice.firmware_version}")
        print(f"Firmware date: {mydevice.firmware_date}")
        print(f"Unit type: {mydevice.unit_type}")
        while True:
            print(
                "Press one key and enter. "
                "1-3 for speed, 0=off, 9=on,b,n,m for mode,"
                " f for reset filter alarm, q for quit"
            )
            char = sys.stdin.read(2)[0]
            if char == "q":
                break
            if char >= "0" and char <= "3":
                client.set_speed(mydevice, ord(char) - ord("0"))
            if char >= "4" and char <= "8":
                manualspeed = ((ord(char) - ord("4")) * 50) + 50
                client.set_manual_speed(mydevice, manualspeed)
            if char == "9":
                client.turn_on(mydevice)
            if char == "b":
                client.set_mode(mydevice, Mode.ONEWAY)
            if char == "n":
                client.set_mode(mydevice, Mode.TWOWAY)
            if char == "m":
                client.set_mode(mydevice, Mode.IN)
            if char == "a":
                client.set_schedule_on(mydevice)
            if char == "s":
                client.set_schedule_off(mydevice)
            if char == "f":
                client.reset_filter_alarm(mydevice)

    print("Closing")
    client.close()
    print("Done")

    exit(0)


main()
