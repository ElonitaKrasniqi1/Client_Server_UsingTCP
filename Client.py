import socket

def tcp_client():
    server_ip = "127.0.0.1"
    server_port = 3304

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
    
        client_socket.connect((server_ip, server_port))
        print(f"Connected to server {server_ip}:{server_port}")


        device_name = input("Enter your device name: ")
        client_socket.send(device_name.encode())

        while True:
            
            command = input("Enter a command: ")

            
            client_socket.send(command.encode())

           
            response = client_socket.recv(1024).decode()
            print("Server response:", response)

    except Exception as e:
        print(f"Error: {e}")
    finally:
       
        client_socket.close()

if __name__ == "__main__":
    
    tcp_client()
