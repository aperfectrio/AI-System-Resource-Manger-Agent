from modules.monitor import (
    get_cpu_usage,
    get_ram_usage,
    get_disk_usage
)

from modules.analyzer import (
    get_top_memory_processes,
    get_top_cpu_processes
)

from modules.decision_engine import (
    generate_recommendations
)

import os
import time


while True:
    os.system("cls")

    cpu = get_cpu_usage()
    ram = get_ram_usage()
    disk = get_disk_usage()

    print("=" * 50)
    print("AI System Resource Manager Agent")
    print("=" * 50)

    print(f"CPU Usage  : {cpu}%")
    print(f"RAM Usage  : {ram}%")
    print(f"Disk Usage : {disk}%")

    # RAM Processes
    print("\nTop RAM Processes")
    print("-" * 50)

    processes = get_top_memory_processes()

    for process in processes:
        print(
            f"{process['name']:<25}"
            f"{process['memory']:.2f} MB"
        )

    # CPU Processes
    print("\nTop CPU Processes")
    print("-" * 50)

    cpu_processes = get_top_cpu_processes()

    for process in cpu_processes:
        print(
            f"{process['name']:<25}"
            f"{process['cpu']:.2f}%"
        )

    # Recommendations
    print("\nRecommendations")
    print("-" * 50)

    recommendations = generate_recommendations(
        cpu,
        ram,
        disk
    )

    for recommendation in recommendations:
        print(recommendation)

    print("\nRefreshing every second...")

    time.sleep(1)from modules.monitor import (
    get_cpu_usage,
    get_ram_usage,
    get_disk_usage
)

from modules.analyzer import (
    get_top_memory_processes,
    get_top_cpu_processes
)

from modules.decision_engine import (
    generate_recommendations
)

import os
import time


while True:
    os.system("cls")

    cpu = get_cpu_usage()
    ram = get_ram_usage()
    disk = get_disk_usage()

    print("=" * 50)
    print("AI System Resource Manager Agent")
    print("=" * 50)

    print(f"CPU Usage  : {cpu}%")
    print(f"RAM Usage  : {ram}%")
    print(f"Disk Usage : {disk}%")

    # RAM Processes
    print("\nTop RAM Processes")
    print("-" * 50)

    processes = get_top_memory_processes()

    for process in processes:
        print(
            f"{process['name']:<25}"
            f"{process['memory']:.2f} MB"
        )

    # CPU Processes
    print("\nTop CPU Processes")
    print("-" * 50)

    cpu_processes = get_top_cpu_processes()

    for process in cpu_processes:
        print(
            f"{process['name']:<25}"
            f"{process['cpu']:.2f}%"
        )

    # Recommendations
    print("\nRecommendations")
    print("-" * 50)

    recommendations = generate_recommendations(
        cpu,
        ram,
        disk
    )

    for recommendation in recommendations:
        print(recommendation)

    print("\nRefreshing every second...")

    time.sleep(1)