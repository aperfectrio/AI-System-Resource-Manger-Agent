def generate_recommendations(cpu, ram, disk):
    recommendations = []

    # CPU Rules
    if cpu >= 80:
        recommendations.append(
            "⚠ High CPU Usage Detected. Consider closing CPU-intensive applications."
        )

    # RAM Rules
    if ram >= 80:
        recommendations.append(
            "⚠ High RAM Usage Detected. Consider closing unused applications or browser tabs."
        )

    # Disk Rules
    if disk >= 80:
        recommendations.append(
            "⚠ Disk Usage Above 80%. Consider cleaning temporary or unnecessary files."
        )

    # Healthy System
    if not recommendations:
        recommendations.append(
            "✓ System Health Good. No action required."
        )

    return recommendations