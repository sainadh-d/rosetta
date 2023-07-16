# Truncate a file

## Task Link
[Rosetta Code - Truncate a file](https://rosettacode.org/wiki/Truncate_a_file)

## Java Code
### java_code_1.txt
```java
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.channels.FileChannel;

public class TruncFile {
	public static void main(String[] args) throws IOException{
		if(args.length < 2){
			System.out.println("Usage: java TruncFile fileName newSize");
			return;
		}
		//turn on "append" so it doesn't clear the file
		FileChannel outChan = new FileOutputStream(args[0], true).getChannel();
		long newSize = Long.parseLong(args[1]);
		outChan.truncate(newSize);
		outChan.close();
	}
}

```

## Python Code
### python_code_1.txt
```python
def truncate_file(name, length):
    if not os.path.isfile(name):
        return False
    if length >= os.path.getsize(name):
        return False
    with open(name, 'ab') as f:
        f.truncate(length)
    return True

```

