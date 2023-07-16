# Sockets

## Task Link
[Rosetta Code - Sockets](https://rosettacode.org/wiki/Sockets)

## Java Code
### java_code_1.txt
```java
import java.io.IOException;
import java.net.*;
public class SocketSend {
  public static void main(String args[]) throws IOException {
    sendData("localhost", "hello socket world");
  }

  public static void sendData(String host, String msg) throws IOException {
    Socket sock = new Socket( host, 256 );
    sock.getOutputStream().write(msg.getBytes());
    sock.getOutputStream().flush();
    sock.close();
  }
}

```

## Python Code
### python_code_1.txt
```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 256))
sock.sendall("hello socket world") 
sock.close()

```

