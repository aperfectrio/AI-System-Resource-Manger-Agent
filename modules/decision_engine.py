from modules.logger import write_log


def generate_recommendations(cpu, ram, disk):
    recommendations = []

    # CPU Rules
    if cpu >= 80:
        message = (
            "⚠ High CPU Usage Detected. Consider closing CPU-intensive applications."
        )

        recommendations.append(message)

        write_log(
            "WARNING: High CPU Usage Detected"
        )

    # RAM Rules
    if ram >= 80:
        message = (
            "⚠ High RAM Usage Detected. Consider closing unused applications or browser tabs."
        )

        recommendations.append(message)

        write_log(
            "WARNING: High RAM Usage Detected"
        )

    # Disk Rules
    if disk >= 80:
        message = (
            "⚠ Disk Usage Above 80%. Consider cleaning temporary or unnecessary files."
        )

        recommendations.append(message)

        write_log(
            "WARNING: Disk Usage Above 80%"
        )

    # Healthy System
    if not recommendations:
        recommendations.append(
            "✓ System Health Good. No action required."
        )

    return recommendations