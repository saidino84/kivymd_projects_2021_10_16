import socket


port = 5001
host = ""
buffersize = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
print("LIstenning in port ", port)
sock.listen(5)

quit = "again"
while "x" not in quit:
    conn, addr = sock.accept()
    print("Connection estabished from ", addr)
    dada = conn.recv(buffersize)
    print("[received] :", dada.decode("utf8"))
    conn.send(bytes(input("[send]>>"), "utf8"))

    quit = input("[again ?]")
sock.close()
