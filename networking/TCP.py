



# In most servers connections are accepted in one thread and a new thread or process is created to handle each connection. To keep things simple the example here describes an iterative server where each request is handled one at a time.



class TCP:
    def __init__(self):
        self.ip = None
        self.port = None
        self.listening = False

    def socket(self, ip, port):
        self.ip = ip
        self.port = port

    def bind(self):
        pass

    def listen(self):
        self.listening = True

    def accept(self):
        pass
    

    def read(self):
        
       # finish connection by sending 0 
       return 0


class TCPConnector:
    """
     Encapsulates the socket mechanisms to actively connect to a server. This is a factory class which produces TCPStream objects when client applications establish connections with servers.
    """
    def __init__(self):
        pass

class TCPAcceptor:
    """
    Encapsulates the socket mechanisms to passively accept connections from a client. This is also a factory class which produces TCPStream objects when server applications establish connections with clients
    """
    def __init__(self):
        pass

class TCPStream:
    """
    Provides network I/O mechanisms and returns IP address and TCP port of peer applications.
    """
    def __init__(self, sd, address):
        self.sd = sd
        self.address = address

    def send(self, buffer, length):
        pass
    def receive(self, buffer, length):


