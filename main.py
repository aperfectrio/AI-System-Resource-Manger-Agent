from modules.monitor import (
    get_cpu_usage,
    get_ram_usage,
    get_disk_usage
)

import os
import time


while True:
    os.system("cls")  # clear terminal (Windows)

    print("=" * 50)
    print("AI System Resource Manager Agent")
    print("=" * 50)

    cpu = get_cpu_usage()
    ram = get_ram_usage()
    disk = get_disk_usage()

    print(f"CPU Usage  : {cpu}%")
    print(f"RAM Usage  : {ram}%")
    print(f"Disk Usage : {disk}%")

    print("\nRefreshing every second...")

    time.sleep(1)