import psutil

from modules.logger import write_log


SAFE_PROCESSES = [
    "Spotify.exe",
    "Discord.exe",
    "notepad.exe",
    "WindowsCamera.exe"
]


def terminate_process(process_name):

    terminated_count = 0

    for process in psutil.process_iter(['pid', 'name']):
        try:
            if process.info['name'].lower() == process_name.lower():

                process.kill()

                terminated_count += 1

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    if terminated_count > 0:

        message = (
            f"Terminated {terminated_count} instance(s) of {process_name}."
        )

        write_log(
            f"ACTION: {message}"
        )

        return True, message

    return False, f"{process_name} not found."


def get_optimization_candidates():

    processes = []

    for process in psutil.process_iter(
        ['pid', 'name', 'memory_info']
    ):
        try:

            name = process.info['name']

            if name in SAFE_PROCESSES:

                memory_mb = (
                    process.info['memory_info'].rss
                    / (1024 * 1024)
                )

                processes.append({
                    "name": name,
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

    return processes[:3]


def optimize_system():

    candidates = get_optimization_candidates()

    results = []

    for process in candidates:

        success, message = terminate_process(
            process["name"]
        )

        results.append(message)

    return results