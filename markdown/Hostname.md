# Hostname

## Task Link
[Rosetta Code - Hostname](https://rosettacode.org/wiki/Hostname)

## Java Code
### java_code_1.txt
```java
import java.net.InetAddress;
import java.net.UnknownHostException;

```

### java_code_2.txt
```java
void printHostname() throws UnknownHostException {
    InetAddress localhost = InetAddress.getLocalHost();
    System.out.println(localhost.getHostName());
}

```

## Python Code
### python_code_1.txt
```python
import socket
host = socket.gethostname()

```

