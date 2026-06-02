import psutil
import time


def get_top_memory_processes(limit=5):
    processes = []

    for process in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            memory_mb = process.info['memory_info'].rss / (1024 * 1024)

            processes.append({
                "name": process.info['name'],
                "memory": memory_mb
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    processes.sort(
        key=lambda p: p["memory"],
        reverse=True
    )

    return processes[:limit]


def get_top_cpu_processes(limit=5):
    processes = []

    ignored_processes = [
        "System Idle Process",
        "System",
        "python.exe"
    ]

    # Initialize CPU measurements
    for process in psutil.process_iter():
        try:
            process.cpu_percent(None)
        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    # Wait briefly to calculate CPU usage
    time.sleep(0.5)

    for process in psutil.process_iter(['name']):
        try:
            process_name = process.info['name']

            if process_name in ignored_processes:
                continue

            cpu_usage = process.cpu_percent(None)

            if cpu_usage > 0:
                processes.append({
                    "name": process_name,
                    "cpu": cpu_usage
                })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    processes.sort(
        key=lambda p: p["cpu"],
        reverse=True
    )

    return processes[:limit]