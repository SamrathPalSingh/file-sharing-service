from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", 'C:/Users/Tintin/Documents/python_socket_programming', perm="elradfmw")
authorizer.add_anonymous('C:/Users/Tintin/Documents/python_socket_programming', perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler)
server.serve_forever()
