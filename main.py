from cloudlink import cloudlink
if __name__ == "__main__":
    cl = cloudlink()
    server = cl.server(logs=False)
    server.run(
        ip = "0.0.0.0",
        port = 8080
    )
