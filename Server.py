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
                    script_dir = os.path.dirname(os.path.realpath(__file__))
                    file_path = os.path.join(script_dir file_name)
                    with open(file_path, "r") as file:
                        content = file.read()
                        return content
                except FileNotFoundError:
                    return "File not found."

             def write_file(file_name, content):
                 try:
                     script_dir = os.path.dirname(or.path.realpath(__file__))
                     file_path = os.path.join(script_dir, file_name)
                    with open(file_path, "w") as file:
                        file.write(content)
                        return "File written successfully."
                    except Exception as e:
                 return "Error:{}".format(e)

def execute_command(command_parts):
    try:
        script_name = command_parts[0]

        script_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), script_name)

        result = subprocess.run([sys.executable, script_path] + command_parts[1:], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout if result.returncode == 0 else result.stderr
        return output
    except Exception as e:
        return f"Error executing script: {e}"


def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    try:
        device_name = client_socket.recv(1024).decode()
        print(f"Device '{device_name}' connected from {address}")

        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                print(f"Connection closed by {address}")
                break

            handle_received_message(data, address, client_socket, device_name)

    except Exception as e:
        print(f"Error handling connection from {address}: {e}")

    finally:
        client_socket.close()
        print(f"Connection with {address} closed.")

def tcp_server():
    server_ip = "127.0.0.1"
    server_port = 3304

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"TCP server listening on {server_ip}:{server_port}")

    while True:
        client_socket, address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    tcp_server()

