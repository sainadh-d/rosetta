# Distributed programming

## Task Link
[Rosetta Code - Distributed programming](https://rosettacode.org/wiki/Distributed_programming)

## Java Code
## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SimpleXMLRPCServer

class MyHandlerInstance:
    def echo(self, data):
        '''Method for returning data got from client'''
        return 'Server responded: %s' % data

    def div(self, num1, num2):
        '''Method for divide 2 numbers'''
        return num1/num2

def foo_function():
    '''A function (not an instance method)'''
    return True

HOST = "localhost"
PORT = 8000

server = SimpleXMLRPCServer.SimpleXMLRPCServer((HOST, PORT))

# register built-in system.* functions.
server.register_introspection_functions()

# register our instance
server.register_instance(MyHandlerInstance())

# register our function as well
server.register_function(foo_function)

try:
    # serve forever
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting...'
    server.server_close()

```

### python_code_10.txt
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import spread

PORT = '4803'

conn = spread.connect(PORT)
conn.join('test')

conn.multicast(spread.RELIABLE_MESS, 'test', 'hello, this is message sent from python')
conn.disconnect()

```

### python_code_2.txt
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib

HOST = "localhost"
PORT = 8000

rpc = xmlrpclib.ServerProxy("http://%s:%d" % (HOST, PORT))

# print what functions does server support 
print 'Server supports these functions:',
print ' '.join(rpc.system.listMethods())

# echo something
rpc.echo("We sent this data to server")

# div numbers
print 'Server says: 8 / 4 is: %d' % rpc.div(8, 4)

# control if foo_function returns True
if rpc.foo_function():
    print 'Server says: foo_function returned True'

```

### python_code_3.txt
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import BaseHTTPServer

HOST = "localhost"
PORT = 8000

# we just want to write own class, we replace do_GET method. This could be extended, I just added basics
# see; http://docs.python.org/lib/module-BaseHTTPServer.html
class MyHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        # send 200 (OK) message
        self.send_response(200)
        # send header
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # send context
        self.wfile.write("<html><head><title>Our Web Title</title></head>")
        self.wfile.write("<body><p>This is our body. You wanted to visit <b>%s</b> page</p></body>" % self.path)
        self.wfile.write("</html>")

if __name__ == '__main__':
    server = BaseHTTPServer.HTTPServer((HOST, PORT), MyHTTPHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Exiting...'
        server.server_close()

```

### python_code_4.txt
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib

HOST = "localhost"
PORT = 8000

conn = httplib.HTTPConnection(HOST, PORT)
conn.request("GET", "/somefile")

response = conn.getresponse()
print 'Server Status: %d' % response.status

print 'Server Message: %s' % response.read()

```

### python_code_5.txt
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import SocketServer
import pickle
 
HOST = "localhost"
PORT = 8000

class RPCServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    # The object_to_proxy member should be set to the object we want
    # methods called on. Unfortunately, we can't do this in the constructor
    # because the constructor should not be overridden in TCPServer...

    daemon_threads = True

class RPCHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        in_channel = pickle.Unpickler(self.rfile)
        out_channel = pickle.Pickler(self.wfile, protocol=2)
        while True:
            try:
                name, args, kwargs = in_channel.load()
                print 'got %s %s %s' % (name, args, kwargs)
            except EOFError:
                # EOF means we're done with this request.
                # Catching this exception to detect EOF is a bit hackish,
                # but will work for a quick demo like this
                break
            try:
                method = getattr(self.server.object_to_proxy, name)
                result = method(*args, **kwargs)
            except Exception, e:
                out_channel.dump(('Error',e))
            else:
                out_channel.dump(('OK',result))

class MyHandlerInstance(object):
    def echo(self, data):
        '''Method for returning data got from client'''
        return 'Server responded: %s' % data
 
    def div(self, dividend, divisor):
        '''Method to divide 2 numbers'''
        return dividend/divisor
 
    def is_computer_on(self):
        return True
 
if __name__ == '__main__':
    rpcserver = RPCServer((HOST, PORT), RPCHandler)
    rpcserver.object_to_proxy = MyHandlerInstance()
    try:
        rpcserver.serve_forever()
    except KeyboardInterrupt:
        print 'Exiting...'
        rpcserver.server_close()

```

### python_code_6.txt
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import socket
import pickle
 
HOST = "localhost"
PORT = 8000

class RPCClient(object):
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.rfile = self.socket.makefile('rb')
        self.wfile = self.socket.makefile('wb')
        self.in_channel = pickle.Unpickler(self.rfile)
        self.out_channel = pickle.Pickler(self.wfile, protocol=2)

    def _close(self):
        self.socket.close()
        self.rfile.close()
        self.wfile.close()

    # Make calling remote methods easy by overriding attribute access.
    # Accessing any attribute on our instances will give a proxy method that
    # calls the method with the same name on the remote machine.
    def __getattr__(self, name):
        def proxy(*args, **kwargs):
            self.out_channel.dump((name, args, kwargs))
            self.wfile.flush() # to make sure the server won't wait forever
            status, result = self.in_channel.load()
            if status == 'OK':
                return result
            else:
                raise result

        return proxy
 
if __name__ == '__main__':
    # connect to server and send data
    rpcclient = RPCClient(HOST, PORT)

    print 'Testing the echo() method:'
    print rpcclient.echo('Hello world!')
    print
    print 'Calculating 42/2 on the remote machine:'
    print rpcclient.div(42, 2)
    print
    print 'is_computer_on on the remote machine returns:'
    print rpcclient.is_computer_on()
    print
    print 'Testing keyword args:'
    print '42/2 is:', rpcclient.div(divisor=2, dividend=42)
    rpcclient._close()
    del rpcclient

```

### python_code_7.txt
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import Pyro.core
import Pyro.naming

# create instance that will return upper case
class StringInstance(Pyro.core.ObjBase):
    def makeUpper(self, data):
        return data.upper()

class MathInstance(Pyro.core.ObjBase):
    def div(self, num1, num2):
        return num1/num2

if __name__ == '__main__':
    server = Pyro.core.Daemon()
    name_server = Pyro.naming.NameServerLocator().getNS()
    server.useNameServer(name_server)
    server.connect(StringInstance(), 'string')
    server.connect(MathInstance(), 'math')
    try:
        server.requestLoop()
    except KeyboardInterrupt:
        print 'Exiting...'
        server.shutdown()

```

### python_code_8.txt
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import Pyro.core

DATA = "my name is eren"
NUM1 = 10
NUM2 = 5

string = Pyro.core.getProxyForURI("PYRONAME://string")
math = Pyro.core.getProxyForURI("PYRONAME://math")

print 'We sent: %s' % DATA
print 'Server responded: %s\n' % string.makeUpper(DATA)

print 'We sent two numbers to divide: %d and %d' % (NUM1, NUM2)
print 'Server responded the result: %s' % math.div(NUM1, NUM2)

```

### python_code_9.txt
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import spread

PORT = '4803'

# connect spread daemon
conn = spread.connect(PORT)
# join the room
conn.join('test')

print 'Waiting for messages... If you want to stop this script, please stop spread daemon'
while True:
    recv = conn.receive()
    if hasattr(recv, 'sender') and hasattr(recv, 'message'):
        print 'Sender: %s' % recv.sender
        print 'Message: %s' % recv.message

```

