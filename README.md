# ADB-App-Manager

## What is it?
ADB-App-Manager is a tool to manage your Android applications. The goal of this tool is to make useing adb to manage your applications easier.

## How to use it?
Before you can use this tool you have to install the Android SDK, and conect your device to your PC. (Check the Requried Software section)

When you run the tool, you will be asked to enter the path to your Android SDK or the folder that "adb.exe" resides in. This will create a file that will automatically be used by the tool to complete this step on future runs.

Next the tool will scan your phones memory for applications, and prompt you to select if you want to search for a package name or direcly enter an index number.

If you select search you can enter a package name, or a partial name. The tool will then search for all applications that match the name you entered.

Package names will be displayed with an leading index number, that index number is the number you will input when you want to manage that application.

Once a index has been entered, the tool will then prompt you to select if you want to Uninstall, Dissable, or Enable the application.

Select an option and thats it :)

## Required Software
- Android SDK | [Download](https://developer.android.com/studio)
- Python 3.10+ | [Download](https://www.python.org/downloads/)

## Whats Next?
- Add ability to select a package using the packages name instead of only the index number
- Shizuku support for on Android applications
- Make a Rust version to enable the tool to be used without the need for Python
- Make a GUI version to make the tool more user friendly

## License
This tool is licensed under GNU General Public License v3.0.
