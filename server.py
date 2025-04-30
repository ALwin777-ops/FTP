import socket

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080
    totalclients = int(input("Enter The Total Number Of Clients: "))
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(totalclients)
    
    connections = []
    print("Waiting for clients to connect...")
    
    for i in range(totalclients):
        conn, addr = sock.accept()
        connections.append(conn)
        print(f"Client {i + 1} connected from {addr}")
    
    for idx, conn in enumerate(connections):
        data = conn.recv(1024).decode()
        if not data:
            continue
        
        filename = f"output{idx}.txt"
        with open(filename, 'w') as fo:
            while data:
                fo.write(data)
                data = conn.recv(1024).decode()
        
        print(f"Received file from client {idx + 1} -> Saved as {filename}")
    
    # Close all connections
    for conn in connections:
        conn.close()
