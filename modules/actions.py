import psutil


ALLOWED_PROCESSES = [
    "Spotify.exe",
    "chrome.exe",
    "Code.exe",
    "Discord.exe",
    "notepad.exe"
]


def terminate_process(process_name):

    if process_name not in ALLOWED_PROCESSES:
        return (
            False,
            f"{process_name} is not allowed to be terminated."
        )

    terminated_count = 0

    for process in psutil.process_iter(['pid', 'name']):
        try:
            if process.info['name'].lower() == process_name.lower():

                process.kill()   # stronger than terminate()

                terminated_count += 1

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    if terminated_count > 0:
        return (
            True,
            f"Terminated {terminated_count} instance(s) of {process_name}."
        )

    return (
        False,
        f"{process_name} not found."
    )