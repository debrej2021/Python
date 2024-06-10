class Server:

    def __init__(self, ipAddress, port, status, uptime, downtime):

        self.ipAddress = ipAddress

        self.port = port

        self.status = status

        self.uptime = uptime

        self.downtime = downtime

    def start(self):

        self.status = "online"

        print("Server has started in port number", self.port)

    def stop(self):

        if (self.status == "online"):

            self.status = "offline"

        else:

            print("Error: othe server is already offline")

 

testServer = Server("120.34.1.1",3000, "Offline", 08, 20)

testServer.start()

testServer.stop()