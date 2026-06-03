import customtkinter as ctk

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

from modules.notifier import (
    get_system_status
)

from modules.actions import (
    terminate_process
)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("AI System Resource Manager Agent")
app.geometry("900x800")


# ==========================
# Title
# ==========================

title_label = ctk.CTkLabel(
    app,
    text="AI System Resource Manager Agent",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=15)


# ==========================
# System Statistics
# ==========================

stats_label = ctk.CTkLabel(
    app,
    text="Loading...",
    font=("Arial", 16)
)

stats_label.pack(pady=10)


# ==========================
# Notification Status
# ==========================

status_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 16, "bold")
)

status_label.pack(pady=10)


# ==========================
# Recommendations Box
# ==========================

recommendation_box = ctk.CTkTextbox(
    app,
    width=800,
    height=120
)

recommendation_box.pack(pady=10)


# ==========================
# RAM Processes Box
# ==========================

ram_process_box = ctk.CTkTextbox(
    app,
    width=800,
    height=140
)

ram_process_box.pack(pady=10)


# ==========================
# CPU Processes Box
# ==========================

cpu_process_box = ctk.CTkTextbox(
    app,
    width=800,
    height=140
)

cpu_process_box.pack(pady=10)


# ==========================
# Action Executor
# ==========================

def terminate_spotify():

    success, message = terminate_process(
        "Spotify.exe"
    )

    recommendation_box.insert(
        "end",
        f"\n\n[ACTION] {message}"
    )

spotify_button = ctk.CTkButton(
    app,
    text="Terminate Spotify",
    command=terminate_spotify
)

spotify_button.pack(pady=10)


# ==========================
# Dashboard Refresh Function
# ==========================

def update_dashboard():

    cpu = get_cpu_usage()
    ram = get_ram_usage()
    disk = get_disk_usage()

    recommendations = generate_recommendations(
        cpu,
        ram,
        disk
    )

    status, message = get_system_status(
        recommendations
    )

    ram_processes = get_top_memory_processes()

    cpu_processes = get_top_cpu_processes()

    # --------------------------
    # Statistics
    # --------------------------

    stats_label.configure(
        text=(
            f"CPU Usage : {cpu}%\n"
            f"RAM Usage : {ram}%\n"
            f"Disk Usage: {disk}%"
        )
    )

    # --------------------------
    # Notification Status
    # --------------------------

    status_label.configure(
        text=f"{status} | {message}"
    )

    # --------------------------
    # Recommendations
    # --------------------------

    recommendation_box.delete(
        "1.0",
        "end"
    )

    recommendation_box.insert(
        "end",
        "Recommendations\n\n"
    )

    for recommendation in recommendations:
        recommendation_box.insert(
            "end",
            recommendation + "\n"
        )

    # --------------------------
    # RAM Processes
    # --------------------------

    ram_process_box.delete(
        "1.0",
        "end"
    )

    ram_process_box.insert(
        "end",
        "Top RAM Processes\n\n"
    )

    for process in ram_processes:
        ram_process_box.insert(
            "end",
            f"{process['name']} - "
            f"{process['memory']:.2f} MB\n"
        )

    # --------------------------
    # CPU Processes
    # --------------------------

    cpu_process_box.delete(
        "1.0",
        "end"
    )

    cpu_process_box.insert(
        "end",
        "Top CPU Processes\n\n"
    )

    for process in cpu_processes:
        cpu_process_box.insert(
            "end",
            f"{process['name']} - "
            f"{process['cpu']:.2f}%\n"
        )

    app.after(
        1000,
        update_dashboard
    )


update_dashboard()

app.mainloop()