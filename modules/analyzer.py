import psutil


def get_top_memory_processes(limit=5):
    processes = []

    for process in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            memory_mb = process.info['memory_info'].rss / (1024 * 1024)

            processes.append({
                "name": process.info['name'],
                "memory": memory_mb
            })

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    processes.sort(
        key=lambda p: p["memory"],
        reverse=True
    )

    return processes[:limit]