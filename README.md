# macos-change-kbdlayout

Python wrapper to change the keyboard layout using [keyboardSwitcher](https://github.com/Lutzifer/keyboardSwitcher) under MacOs 
depending on if an external bluetooth keyboard is connected or not.

## Possible usage

In my scenario i have a Macbook with a german keyboard built-in as well as an external one that has a us-english styled layout.
Depending on if the external keyboard is connected or not i need to set the right keyboard layout/language.

![Change keyboard layout](bluetooth.gif)

## Installation

Clone the repository

```
git@github.com:ktklin/macos-change-kbdlayout.git
```

copy the python script to the directory of your choice (in my case below ~/.local/scripts)
and make it executable. In addition the script needs to be adjusted to reflect the 
name of your keyboard

```
cp macos-change-kbdlayout/kbd.py ~/.local/scripts
chmod 755 ~/.local/scripts/kbd.py
```

Copy the LaunchAgent definition below ~/Library/LaunchAgents and adjust the ProgramArguments string to point 
the kbd.py file (fully qualified path)

```
cp com.apple.bluetoothkbd.plist ~/Library/LaunchAgents/
```

Finally activate the LaunchAgent via
```
launchctl load ~/Library/LaunchAgents/com.apple.bluetoothkbd.plist 
```




