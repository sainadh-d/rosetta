# Echo server

## Task Link
[Rosetta Code - Echo server](https://rosettacode.org/wiki/Echo_server)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

public class EchoServer {

    public static void main(String[] args) throws IOException {
        try (ServerSocket listener = new ServerSocket(12321)) {
            while (true) {
                Socket conn = listener.accept();
                Thread clientThread = new Thread(() -> handleClient(conn));
                clientThread.start();
            }
        }
    }

    private static void handleClient(Socket connArg) {
        Charset utf8 = StandardCharsets.UTF_8;

        try (Socket conn = connArg) {
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(conn.getInputStream(), utf8));

            PrintWriter out = new PrintWriter(
                    new OutputStreamWriter(conn.getOutputStream(), utf8),
                    true);

            String line;
            while ((line = in.readLine()) != null) {
                out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import SocketServer

HOST = "localhost"
PORT = 12321

# this server uses ThreadingMixIn - one thread per connection
# replace with ForkMixIn to spawn a new process per connection

class EchoServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    # no need to override anything - default behavior is just fine
    pass

class EchoRequestHandler(SocketServer.StreamRequestHandler):
    """
    Handles one connection to the client.
    """
    def handle(self):
        print "connection from %s" % self.client_address[0]
        while True:
            line = self.rfile.readline()
            if not line: break
            print "%s wrote: %s" % (self.client_address[0], line.rstrip())
            self.wfile.write(line)
        print "%s disconnected" % self.client_address[0]


# Create the server
server = EchoServer((HOST, PORT), EchoRequestHandler)

# Activate the server; this will keep running until you
# interrupt the program with Ctrl-C
print "server listening on %s:%s" % server.server_address
server.serve_forever()

```

### python_code_2.txt
```python
#!/usr/bin/env python
# $ printf 'echo\r\n' | nc localhost 12321
# echo
import asyncio
import logging
import os

logger = logging.getLogger('echoserver')

async def echo_handler(reader, writer):
  address = writer.get_extra_info('peername')
  logger.debug('accept: %s', address)
  message = await reader.readline()
  writer.write(message)
  await writer.drain()
  writer.close()

if __name__ == '__main__':
  logging.basicConfig()
  logger.setLevel(logging.DEBUG)
  loop = asyncio.get_event_loop()
  factory = asyncio.start_server(
    echo_handler,
    os.environ.get('HOST'),
    os.environ.get('PORT', 12321)
  )
  server = loop.run_until_complete(factory)
  try:
    loop.run_forever()
  except KeyboardInterrupt:
    pass
  server.close()
  loop.run_until_complete(server.wait_closed())
  loop.close()

```

### python_code_3.txt
```python
    #!usr/bin/env python
    import socket
    import threading

    HOST = 'localhost'
    PORT = 12321
    SOCKET_TIMEOUT = 30

    # This function handles reading data sent by a client, echoing it back
    # and closing the connection in case of timeout (30s) or "quit" command
    # This function is meant to be started in a separate thread
    # (one thread per client)
    def handle_echo(client_connection, client_address):
        client_connection.settimeout(SOCKET_TIMEOUT)
        try:
            while True:
                data = client_connection.recv(1024)
                # Close connection if "quit" received from client
                if data == b'quit\r\n' or data == b'quit\n':
                    print('{} disconnected'.format(client_address))
                    client_connection.shutdown(1)
                    client_connection.close()
                    break
                # Echo back to client
                elif data:
                    print('FROM {} : {}'.format(client_address,data))
                    client_connection.send(data)
        # Timeout and close connection after 30s of inactivity
        except socket.timeout:
            print('{} timed out'.format(client_address))
            client_connection.shutdown(1)
            client_connection.close()

    # This function opens a socket and listens on specified port. As soon as a
    # connection is received, it is transfered to another socket so that the main
    # socket is not blocked and can accept new clients.
    def listen(host, port):
        # Create the main socket (IPv4, TCP)
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        connection.bind((host, port))
        # Listen for clients (max 10 clients in waiting)
        connection.listen(10)
        # Every time a client connects, allow a dedicated socket and a dedicated
        # thread to handle communication with that client without blocking others.
        # Once the new thread has taken over, wait for the next client.
        while True:
            current_connection, client_address = connection.accept()
            print('{} connected'.format(client_address))
            handler_thread = threading.Thread( \
                target = handle_echo, \
                args = (current_connection,client_address) \
            )
            # daemon makes sure all threads are killed if the main server process
            # gets killed
            handler_thread.daemon = True
            handler_thread.start()

    if __name__ == "__main__":
        try:
            listen(HOST, PORT)
        except KeyboardInterrupt:
            print('exiting')
            pass

```

