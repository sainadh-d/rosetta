# Hello world/Web server

## Task Link
[Rosetta Code - Hello world/Web server](https://rosettacode.org/wiki/Hello_world/Web_server)

## Java Code
### java_code_1.txt
```java
import java.io.IOException;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class HelloWorld{
  public static void main(String[] args) throws IOException{
    ServerSocket listener = new ServerSocket(8080);
    while(true){
      Socket sock = listener.accept();
      new PrintWriter(sock.getOutputStream(), true).
                println("Goodbye, World!");
      sock.close();
    }
  }
}

```

## Python Code
### python_code_1.txt
```python
from wsgiref.simple_server import make_server

def app(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    yield b"<h1>Goodbye, World!</h1>"

server = make_server('127.0.0.1', 8080, app)
server.serve_forever()

```

### python_code_2.txt
```python
import threading

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class HelloHTTPRequestHandler(BaseHTTPRequestHandler):

  message = 'Hello World! 今日は'

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html; charset=UTF-8')
    self.end_headers()
    self.wfile.write(self.message.encode('utf-8'))
    self.close_connection = True


def serve(addr, port):
  with ThreadingHTTPServer((addr, port), HelloHTTPRequestHandler) as server:
    server.serve_forever(poll_interval=None)


if __name__ == '__main__':

  addr, port = ('localhost', 80)

  threading.Thread(target=serve, args=(addr, port), daemon=True).start()

  try:
    while True:
      # handle Ctrl+C
      input()

  except KeyboardInterrupt:
    pass

```

### python_code_3.txt
```python
with server_socket socket :port 4000
  accepting client :from socket
    making stdout outfile+fd.client
      prn "HTTP/1.0 200 OK"
      prn "Content-type: text/plain"
      prn ""
      prn "Hello, world!"

```

