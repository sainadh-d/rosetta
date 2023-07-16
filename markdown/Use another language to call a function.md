# Use another language to call a function

## Task Link
[Rosetta Code - Use another language to call a function](https://rosettacode.org/wiki/Use_another_language_to_call_a_function)

## Java Code
### java_code_1.txt
```java
/* Query.java */
public class Query {
    public static boolean call(byte[] data, int[] length)
	throws java.io.UnsupportedEncodingException
    {
	String message = "Here am I";
	byte[] mb = message.getBytes("utf-8");
	if (length[0] < mb.length)
	    return false;
	length[0] = mb.length;
	System.arraycopy(mb, 0, data, 0, mb.length);
	return true;
    }
}

```

## Python Code
### python_code_1.txt
```python
# store this in file rc_embed.py
# store this in file rc_embed.py
def query(buffer_length):
    message = b'Here am I'
    L = len(message)
    return message[0:L*(L <= buffer_length)]

```

