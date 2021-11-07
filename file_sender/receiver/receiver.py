import socket

host = "localhost"
port = 5001
addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect_to_server() -> bool:
    try:
        sock.connect((addr))
        print("connected")
    except:
        print("No server")
        return False
    return True


def send_message() -> None:
    quit = "again"
    while quit != "x":
        if connect_to_server():
            sock.send(bytes(input("[send] >>"), "utf-8"))
            dada = sock.recv(1024)
        quit = input("[again] ?")


if __name__ == "__main__":
    send_message()
