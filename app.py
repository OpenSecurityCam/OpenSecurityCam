from WebPortal import create_WebPortal

app = create_WebPortal()

if __name__ == "__main__":
    SocketIOClient.run(app)