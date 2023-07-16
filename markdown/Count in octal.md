# Count in octal

## Task Link
[Rosetta Code - Count in octal](https://rosettacode.org/wiki/Count_in_octal)

## Java Code
### java_code_1.txt
```java
void printCount() {
    for (int value = 0; value <= 20; value++) {
        /* the 'o' specifier will print the octal integer */
        System.out.printf("%o%n", value);
    }
}

```

### java_code_2.txt
```java
public class Count{
    public static void main(String[] args){
        for(int i = 0;i >= 0;i++){
            System.out.println(Integer.toOctalString(i)); //optionally use "Integer.toString(i, 8)"
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import sys
for n in xrange(sys.maxint):
    print oct(n)

```

