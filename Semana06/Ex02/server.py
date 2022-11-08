# --- Importando os modulos necessarios ---
import socket       # modulo para sockets
import threading    # modulo para threads

HEADER = 64
PORT = 5050                 #P orta de acesso
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, PORT)    # Endereco para realizar o server bind (utilizando o Server IP e a Porta de Acesso)
FORMAT = 'utf-8'           # Formato de decodificacao
DISCONNECT_MESSAGE = "!DISCONNECT"

# declarando o servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) # utilizando o metodo bind com a Server IP e a Porta de Acesso

# envia mensagem para unica pessoa
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():
    server.listen() # com esse comando o socket 'ouve/escuta' as solicitacoes do cliente
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()  # aceita a chamada de um cliente e ao conectar salva a conexao e o endereco do cliente
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
