#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Check if a bluetooth device is connected or not on macOS.
"""

import sys
import subprocess
from plistlib import loads as read_plist_from_string

def check_bluetooth_connection(device_identifier):
    """check if the specified device is connected/disconnected"""
    output = subprocess.check_output(["system_profiler",
                                      "-xml",
                                      "-detailLevel",
                                      "basic",
                                      "SPBluetoothDataType"], stderr=subprocess.DEVNULL)

    plist = read_plist_from_string(output)
    devices = plist[0]['_items'][0]['device_title']

    for device in devices:
        if device_identifier in device.keys():
            device_info = device[device_identifier]
            break
    else:
        msg = u"\"{}\" not found".format(device_identifier)
        raise ValueError(msg)

    if device_info['device_isconnected'] == "attrib_Yes":
        return True


device_name = "KEYBOARD NAME"

try:
    is_connected = check_bluetooth_connection(device_name)
except (OSError, subprocess.CalledProcessError) as error:
    print(error)
    print("Failed to run system_profiler")
    sys.exit(1)
except ValueError as error:
    print(error)
    sys.exit(1)

if is_connected:
    subprocess.run(["/usr/local/bin/keyboardSwitcher", "select", "ABC"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                    check=False)
else:
    subprocess.run(["/usr/local/bin/keyboardSwitcher", "select", "German"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                    check=False)
