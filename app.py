from flask import (
    Flask,
    render_template,
    redirect,
    url_for
)

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
    get_optimization_candidates,
    optimize_system
)

app = Flask(__name__)


def get_logs():

    try:

        with open(
            "logs/history.log",
            "r"
        ) as file:

            logs = file.readlines()

        logs.reverse()

        return logs[:10]

    except:

        return ["No logs available."]


@app.route("/")
def home():

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

    logs = get_logs()

    return render_template(
        "index.html",

        cpu=cpu,
        ram=ram,
        disk=disk,

        status=status,
        message=message,

        recommendations=recommendations,

        ram_processes=ram_processes,
        cpu_processes=cpu_processes,

        candidates=candidates,

        logs=logs
    )


@app.route("/optimize")
def optimize():

    optimize_system()

    return redirect(
        url_for("home")
    )


if __name__ == "__main__":
    app.run(debug=True)