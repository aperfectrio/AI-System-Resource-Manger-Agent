from modules.actions import terminate_process


process_name = input(
    "Enter process name to terminate: "
)

success, message = terminate_process(
    process_name
)

print(message)