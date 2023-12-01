import socket
import os
import threading
import subprocess
import sys
def is_authorized(client_address, operation, device_name):
    # just "admin" can write and execute
    if device_name.lower() == "admin":
        return True
    elif operation == "read":
        return True  # Të Read-Only users 
    elif operation in ["write", "execute"]:
        return False  
    else:
        return False

def handle_received_message(message, client_address, client_socket, device_name):
    print(f"Received message from {client_address}: {message}")

    if message.startswith("read:") or message.startswith("write:") or message.startswith("execute:"):
        parts = message.split(":")
        operation = parts[0].strip().lower()
        file_name = parts[1].strip()

        if not is_authorized(client_address, operation, device_name):
            response = "Permission denied. You are not authorized to perform this operation."
            client_socket.send(response.encode())
            return

        if message.startswith("read:"):
            content = read_file(file_name)
            client_socket.send(content.encode())
        elif message.startswith("write:") and len(parts) == 3:
            content = parts[2].strip()
            write_file(file_name, content)
            response = "File written successfully."
            client_socket.send(response.encode())
        elif message.startswith("execute:"):
            # Run the command and get the output
            command_output = execute_command(parts[1:])
            client_socket.send(command_output.encode())
            def read_file(file_name):
                try:
                    script_dir =
                    os.path.dirname(os.path.realpath(__file__))
                    file_path = os.path.join(script_dir file_name)
                    with open(file_path, "r") as file:
                        content = file.read()
                        return content
                except FileNotFoundError:
                    return "File not found."

             def write_file(file_name, content):
                 try:
                     script_dir = 
                     os.path.dirname(or.path.realpath(__file__))
                     file_path = os.path.join(script_dir, file_name)
                    with open(file_path, "w") as file:
                        file.write(content)
                        return "File written successfully."
                    except Exception as e:
                 return "Error:{}".format(e)
                 
