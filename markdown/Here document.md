# Here document

## Task Link
[Rosetta Code - Here document](https://rosettacode.org/wiki/Here_document)

## Java Code
### java_code_1.txt
```java
package rosettacode.heredoc;
public class MainApp {
	public static void main(String[] args) {
		String hereDoc = """
				This is a multiline string.
				It includes all of this text,
				but on separate lines in the code.
				 """;
		System.out.println(hereDoc);
	}
}

```

## Python Code
### python_code_1.txt
```python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

```

