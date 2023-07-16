# Index finite lists of positive integers

## Task Link
[Rosetta Code - Index finite lists of positive integers](https://rosettacode.org/wiki/Index_finite_lists_of_positive_integers)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import static java.util.Arrays.stream;
import java.util.*;
import static java.util.stream.Collectors.*;

public class Test3 {
    static BigInteger rank(int[] x) {
        String s = stream(x).mapToObj(String::valueOf).collect(joining("F"));
        return new BigInteger(s, 16);
    }

    static List<BigInteger> unrank(BigInteger n) {
        BigInteger sixteen = BigInteger.valueOf(16);
        String s = "";
        while (!n.equals(BigInteger.ZERO)) {
            s = "0123456789ABCDEF".charAt(n.mod(sixteen).intValue()) + s;
            n = n.divide(sixteen);
        }
        return stream(s.split("F")).map(x -> new BigInteger(x)).collect(toList());
    }

    public static void main(String[] args) {
        int[] s = {1, 2, 3, 10, 100, 987654321};
        System.out.println(Arrays.toString(s));
        System.out.println(rank(s));
        System.out.println(unrank(rank(s)));
    }
}

```

## Python Code
### python_code_1.txt
```python
def rank(x): return int('a'.join(map(str, [1] + x)), 11)

def unrank(n):
	s = ''
	while n: s,n = "0123456789a"[n%11] + s, n//11
	return map(int, s.split('a'))[1:]

l = [1, 2, 3, 10, 100, 987654321]
print l
n = rank(l)
print n
l = unrank(n)
print l

```

### python_code_2.txt
```python
def unrank(n):
        return map(len, bin(n)[3:].split("0")) if n else []

def rank(x):
        return int('1' + '0'.join('1'*a for a in x), 2) if x else 0

for x in range(11):
        print x, unrank(x), rank(unrank(x))

print
x = [1, 2, 3, 5, 8];
print x, rank(x), unrank(rank(x))

```

