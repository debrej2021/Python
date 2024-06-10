class Server:
    def __init__(self, ipAddress, port, status, uptime, downtime):
        self.ipAddress = ipAddress
        self.port = port
        self.status = status
        self.uptime = uptime
        self.downtime = downtime

    def displayServerInformation(self):
        print("ipAddrss:", self.ipAddress)
        print("Status:", self.status)

    def start(self):
        self.status = "online"
        print("Server has started in port number", self.port)

    def stop(self):
        if (self.status == "online"):
            self.status = "offline"
        else:
            print("Error: othe server is already offline")


testServer = Server("120.34.0.1", 3000, "Offline", 8, 20)
testServer.start()
testServer.stop()

# inheritance


class Webserver(Server):
    def __init__(self, ipAddress, port, status, uptime, downtime, domain):
        # calling the init function of the server class
        super.__init__(ipAddress, port, status, uptime, downtime)
        self.domain = domain

    def displayServerInformation(self):
        print("ipAddrss:", self.ipAddress)
        print("Status:", self.status)
        print("Domain", self.domain)


class Databaseserver(Server):
    def __init__(self, ipAddress, port, status, uptime, downtime, databaseURL):
        # calling the init function of the server class
        super.__init__(ipAddress, port, status, uptime, downtime)
        self.databaseURL = databaseURL

    def displayServerInformation(self):
        print("ipAddrss:", self.ipAddress)
        print("Status:", self.status)
        print("Domain", self.databaseURL)


# same function can have multiple implementation in a parent child relationship

webserver1 = Webserver("localhost", 5000, "Offline", 8, 20, "Google.com")
