import winreg as reg
from pathlib import Path
from getpass import getuser

email = input("Enter email : ")
key = reg.OpenKey(reg.HKEY_CURRENT_USER,
                  "Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_ALL_ACCESS)
reg.SetValueEx(key, "new", 0, reg.REG_SZ, f"{Path().absolute()}\main.exe")
user = getuser()
file_path = f"C:\\Users\\{user}\\Downloads\\email.txt"
with open(file_path, "w") as FILE:
        FILE.write(email)
        FILE.close()