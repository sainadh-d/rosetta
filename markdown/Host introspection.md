# Host introspection

## Task Link
[Rosetta Code - Host introspection](https://rosettacode.org/wiki/Host_introspection)

## Java Code
### java_code_1.txt
```java
import java.nio.ByteOrder;

public class ShowByteOrder {
    public static void main(String[] args) {
        // Print "BIG_ENDIAN" or "LITTLE_ENDIAN".
        System.out.println(ByteOrder.nativeOrder());
    }
}

```

### java_code_2.txt
```java
System.out.println("word size: "+System.getProperty("sun.arch.data.model"));
System.out.println("endianness: "+System.getProperty("sun.cpu.endian"));

```

## Python Code
### python_code_1.txt
```python
>>> import platform, sys, socket
>>> platform.architecture()
('64bit', 'ELF')
>>> platform.machine()
'x86_64'
>>> platform.node()
'yourhostname'
>>> platform.system()
'Linux'
>>> sys.byteorder
little
>>> socket.gethostname()
'yourhostname'
>>>

```

