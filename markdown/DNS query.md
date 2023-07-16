# DNS query

## Task Link
[Rosetta Code - DNS query](https://rosettacode.org/wiki/DNS_query)

## Java Code
### java_code_1.txt
```java
import java.net.InetAddress;
import java.net.UnknownHostException;

```

### java_code_2.txt
```java
public static void main(String[] args) throws UnknownHostException {
    /* 'getAllByName' will use the system configured 'resolver' */
    for (InetAddress ip : InetAddress.getAllByName("www.kame.net"))
        System.out.println(ip.getHostAddress());
}

```

### java_code_3.txt
```java
import java.net.InetAddress;
import java.net.Inet4Address;
import java.net.Inet6Address;
import java.net.UnknownHostException;

class DnsQuery {
    public static void main(String[] args) {
        try {
            InetAddress[] ipAddr = InetAddress.getAllByName("www.kame.net");
            for(int i=0; i < ipAddr.length ; i++) {
                if (ipAddr[i] instanceof Inet4Address) {
                    System.out.println("IPv4 : " + ipAddr[i].getHostAddress());
                } else if (ipAddr[i] instanceof Inet6Address) {
                    System.out.println("IPv6 : " + ipAddr[i].getHostAddress());
                }
            }
        } catch (UnknownHostException uhe) {
            System.err.println("unknown host");
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> import socket
>>> ips = set(i[4][0] for i in socket.getaddrinfo('www.kame.net', 80))
>>> for ip in ips: print ip
...
2001:200:dff:fff1:216:3eff:feb1:44d7
203.178.141.194

```

