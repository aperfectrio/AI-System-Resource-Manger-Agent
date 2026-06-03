def get_system_status(recommendations):

    if not recommendations:
        return (
            "✓ HEALTHY",
            "System Operating Normally"
        )

    return (
        "⚠ WARNING",
        f"{len(recommendations)} issue(s) detected"
    )