# Import
import os
from re import A

# OTU Variables
app_ver = str("0.1.0")

# Define Functions

# Check for a file that contains a directory path
# If file exists, return directory path
# If file does not exist, ask for directory path
# Ask for program directory
# Store program Directory in string
# Write directory path to file
# Return directory path
def Install_Dir():
    # Check if file exists
    if os.path.exists("Install_Dir.txt"):
        print("File Containing Directory Exists")
        # If file exists, return directory path
        with open("Install_Dir.txt", "r") as file:
            dir = file.read()
        return dir
    else:
        # If file does not exist, ask for directory path
        while True:
            dir = input("\nPlease Enter the Directory That ADB.exe is in: ")
            if os.path.exists(dir):
                break
        # Write directory path to file
        with open("Install_Dir.txt", "w") as file:
            file.write(dir)
        return dir


# Check if string ends in a \
# If not, add a \ to the end of the string
def Check_Slash(dir):
    # Check if string ends in a \
    if dir[-1] != "\\":
        # If not, add a \ to the end of the string
        dir = dir + "\\"
    # Return string
    return dir

# Test if directory exists
# If not, ask for directory
# Loop till valid directory is entered
# Return valid directory
def Check_Dir(dir):
    # Test if directory exists
    if os.path.exists(dir):
        #print("DEBUG: Directory Exists")
        return dir
    else:
        while True:
            # Ask for program directory
            dir = input("Directory Does Not Exist. Please Enter the Directory That ADB.exe is in: ")
            if os.path.exists(dir):
                print("Directory Exists")
                break
        return dir

# Run Program
# Print output of program
def Run_Program(dir):
    print("DEBUG: Output of ADB.exe")
    os.system(dir + "adb.exe")

# Check if device is connected to PC through ADB
# If not, wait for user input to check again
# Return True if device is connected
def Check_Device(dir):
    output = os.popen(dir + "adb.exe devices").read()
    if "device" in output:
        print(f"\nDevice Connected")
        return
    else:
        while True:
            print("\nDevice Not Connected")
            print("Please Connect Device to PC")
            input("\nPress Enter to Check Again")
            output = os.system(dir + "adb.exe devices").read()
            if "device" in output:
                return

# Scan device packages useing ADB
# Store output in string
# Split string into list
# Append incrementing number to list
# Return list
def Scan_Packages(dir):
    output = os.popen(dir + "adb.exe shell pm list packages").read()
    output = output.split("\n")
    output = output[1:]
    for i in range(len(output)):
        output[i] = str(i + 1) + ": " + output[i]
        #Replace package: with nothing
        output[i] = output[i].replace("package:", "")
    #Remove last entry in list
    output.pop()
    return output

# Print list of packages
def Print_Packages(packages):
    print("\nList of Packages")
    print("------------------------------------------------------\n")
    for i in range(len(packages)):
        print(packages[i])
    print("\n------------------------------------------------------\n")

# Ask user to select package number
# Store user input in string to be used in a later function
# Return package name
def Select_Package(packages):
    while True:
        # Ask user to select package number
        package = input("\nPlease Select Package Number: ")
        # Store user input in string to be used in a later function
        package_numb = str(package)
        # Check if input is a number
        if package.isdigit():
            # Check if input is in range of packages
            if int(package) in range(1, len(packages) + 1):
                break
            else:
                print("\nInvalid Number")
        else:
            print("\nInvalid Number")
    package = packages[int(package) - 1]
    # Remove package number from string useing package_numb variable
    package = package.replace(package_numb + ":", "")
    # Return package name
    return package

# Ask user if they want to uninstall, disable, or enable package
# if user selects uninstall, return uninstall
# if user selects disable, return disable
# if user selects enable, return enable
def Select_Action(package):
    while True:
        # Ask user if they want to uninstall, disable, or enable package
        action = input("\nPlease Select Action: 1=Uninstall, 2=Disable, 3=Enable: ")
        if action in [ '1', 'Uninstall', 'uninstall', 'UNINSTALL', 'U', 'u' ]:
            return "uninstall"
        if action in [ '2', 'Disable', 'disable', 'DISABLE', 'D', 'd' ]:
            return "disable"
        if action in [ '3', 'Enable', 'enable', 'ENABLE', 'E', 'e' ]:
            return "enable"

# Use the action varaible to call the correct ADB command
# If action is uninstall, call uninstall command
# If action is disable, call disable command
# If action is enable, call enable command
def Run_Action(dir, action, package):
    if action == "uninstall":
        os.system(dir + "adb.exe uninstall " + package)
    if action == "disable":
        os.system(dir + "adb.exe shell pm disable " + package)
    if action == "enable":
        os.system(dir + "adb.exe shell pm enable " + package)

# Ask if user wants to search for a package or input a package number
# If user selects search, return search
# If user selects input, return input
# If user selects quit, return quit
def Select_Search():
    while True:
        # Ask user if they want to search for a package or input a package number
        search = input("\nPlease Select an Option: 1=Search, 2=Input, 3=Quit: ")
        if search in [ '1', 'Search', 'search', 'SEARCH', 'S', 's' ]:
            return "search"
        if search in [ '2', 'Input', 'input', 'INPUT', 'I', 'i' ]:
            return "input"
        if search in [ '3', 'Quit', 'quit', 'QUIT', 'Q', 'q' ]:
            return "quit"

# Ask user for package name
# Search for package name in lists of output and print every match
# If no matches are found, print error message
def Search_Package(output):
    while True:
        # Ask user for package name
        package = input("\nPlease Enter Package Name: ")
        # Search for package name in lists of output and print every match
        for i in range(len(output)):
            if package in output[i]:
                print('\n' + output[i])
        # Ask user if they want to search for another package
        search = input("\nSearch for Another Package? 1=Yes, 2=No: ")
        if search in [ '1', 'Yes', 'yes', 'YES', 'Y', 'y' ]:
            continue
        else:
            break

# Main
print(f"ADB App Uninstaller\nVersion {app_ver}\nGRIMREAPER35487\n")
dir = Install_Dir()
dir = Check_Dir(dir)
dir = Check_Slash(dir)
print(f"\nSetting ADB Directory to {dir}")
#Run_Program(dir) | Only Usefull to test if you can run ADB.exe in this context. Otherwise leave commented out..
Check_Device(dir)
output = Scan_Packages(dir)
Print_Packages(output)
while True:
    search = Select_Search()
    if search == "search":
        Search_Package(output)
    if search == "input":
        package = Select_Package(output)
        action = Select_Action(package)
        Run_Action(dir, action, package)
    if search == "quit":
        break
print("Exting Program")
