# Determine if only one instance is running

## Task Link
[Rosetta Code - Determine if only one instance is running](https://rosettacode.org/wiki/Determine_if_only_one_instance_is_running)

## Java Code
### java_code_1.txt
```java
import java.io.IOException;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.UnknownHostException;
 
public class SingletonApp
{
    private static final int PORT = 65000;  // random large port number
    private static ServerSocket s;

    // static initializer
    static {
        try {
            s = new ServerSocket(PORT, 10, InetAddress.getLocalHost());
        } catch (UnknownHostException e) {
            // shouldn't happen for localhost
        } catch (IOException e) {
            // port taken, so app is already running
            System.out.print("Application is already running,");
            System.out.println(" so terminating this instance.");
            System.exit(0);
        }
    }

    public static void main(String[] args) {
        System.out.print("OK, only this instance is running");
        System.out.println(" but will terminate in 10 seconds.");
        try {
            Thread.sleep(10000);
            if (s != null && !s.isClosed()) s.close();
        } catch (Exception e) {
            System.err.println(e);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import __main__, os

def isOnlyInstance():
    # Determine if there are more than the current instance of the application
    # running at the current time.
    return os.system("(( $(ps -ef | grep python | grep '[" +
                     __main__.__file__[0] + "]" + __main__.__file__[1:] +
                     "' | wc -l) > 1 ))") != 0

```

