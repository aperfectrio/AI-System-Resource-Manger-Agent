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
    optimize_system,
    get_optimization_candidates
)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("AI System Resource Manager Agent")
app.geometry("900x900")


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
# Recommendations
# ==========================

recommendation_box = ctk.CTkTextbox(
    app,
    width=800,
    height=120
)

recommendation_box.pack(pady=10)


# ==========================
# RAM Processes
# ==========================

ram_process_box = ctk.CTkTextbox(
    app,
    width=800,
    height=140
)

ram_process_box.pack(pady=10)


# ==========================
# CPU Processes
# ==========================

cpu_process_box = ctk.CTkTextbox(
    app,
    width=800,
    height=140
)

cpu_process_box.pack(pady=10)


# ==========================
# Optimization Candidates
# ==========================

candidate_box = ctk.CTkTextbox(
    app,
    width=800,
    height=120
)

candidate_box.pack(pady=10)


# ==========================
# Action Executor
# ==========================

def optimize_system_action():

    results = optimize_system()

    recommendation_box.insert(
        "end",
        "\n\n===== SYSTEM OPTIMIZATION =====\n"
    )

    for result in results:
        recommendation_box.insert(
            "end",
            f"{result}\n"
        )


optimize_button = ctk.CTkButton(
    app,
    text="Optimize System",
    command=optimize_system_action
)

optimize_button.pack(pady=10)


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

    candidates = get_optimization_candidates()

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
    # Notification
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

    # --------------------------
    # Optimization Candidates
    # --------------------------

    candidate_box.delete(
        "1.0",
        "end"
    )

    candidate_box.insert(
        "end",
        "Optimization Candidates\n\n"
    )

    if len(candidates) == 0:

        candidate_box.insert(
            "end",
            "No safe optimization candidates found."
        )

    else:

        for process in candidates:

            candidate_box.insert(
                "end",
                f"{process['name']} - "
                f"{process['memory']:.2f} MB\n"
            )

    app.after(
        1000,
        update_dashboard
    )


update_dashboard()

app.mainloop()