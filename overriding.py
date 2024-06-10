class Server:
    def __init__(self, ipAddress, port, status, uptime, downtime):
        self.ipAddress = ipAddress
        self.port = port
        self.status = status
        self.uptime = uptime
        self.downtime = downtime

    def start(self):
        self.status = "online"
        print("Server has started on port number", self.port)

    def stop(self):
        if self.status == "online":
            self.status = "offline"
        else:
            print("Error: the server is already offline")

    def display_information(self):
        print(f"IP Address: {self.ipAddress}")
        print(f"Status: {self.status}")
        print(f"Uptime: {self.uptime}")
        print(f"Downtime: {self.downtime}")

class WebServer(Server):
    def __init__(self, ipAddress, port, status, uptime, downtime, domain):
        super().__init__(ipAddress, port, status, uptime, downtime)
        self.domain = domain

    def display_information(self):
        # Overriding the display_information method to include domain information
        super().display_information()  # Call the parent class method
        print(f"Domain: {self.domain}")

class DBServer(Server):
    def __init__(self, ipAddress, port, status, uptime, downtime, domain):
        super().__init__(ipAddress, port, status, uptime, downtime)
        self.domain = domain

    def display_information(self):
        # Overriding the display_information method to include domain information
        super().display_information()  # Call the parent class method
        print(f"Domain: {self.domain}")

testServer = Server("120.34.1.1", 3000, "offline", 8, 20)
testServer.start()
testServer.stop()
testServer.display_information()

print()

webServer = WebServer("130.45.2.2", 4000, "offline", 10, 25, "example.com")
webServer.start()
webServer.stop()
webServer.display_information()

dbserve = DBServer("130.45.2.2", 4000, "offline", 10, 25, "example1.com")
dbserve.start()
dbserve.stop()
dbserve.display_information()
