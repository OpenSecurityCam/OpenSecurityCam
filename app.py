from WebPortal import create_WebPortal, SocketIOClient

app = create_WebPortal()

if __name__ == "__main__":
    SocketIOClient.run(app)