# Negative base numbers

## Task Link
[Rosetta Code - Negative base numbers](https://rosettacode.org/wiki/Negative_base_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.List;
import java.util.Map;
import java.util.Objects;

public class NegativeBaseNumbers {
    private static final String DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    private static String encodeNegBase(long n, int b) {
        if (b < -62 || b > -1) throw new IllegalArgumentException("Parameter b is out of bounds");
        if (n == 0) return "0";
        StringBuilder out = new StringBuilder();
        long nn = n;
        while (nn != 0) {
            int rem = (int) (nn % b);
            nn /= b;
            if (rem < 0) {
                nn++;
                rem -= b;
            }
            out.append(DIGITS.charAt(rem));
        }
        out.reverse();
        return out.toString();
    }

    private static long decodeNegBase(String ns, int b) {
        if (b < -62 || b > -1) throw new IllegalArgumentException("Parameter b is out of bounds");
        if (Objects.equals(ns, "0")) return 0;
        long total = 0;
        long bb = 1;
        for (int i = ns.length() - 1; i >= 0; i--) {
            char c = ns.charAt(i);
            total += DIGITS.indexOf(c) * bb;
            bb *= b;
        }
        return total;
    }

    public static void main(String[] args) {
        List<Map.Entry<Long, Integer>> nbl = List.of(
                Map.entry(10L, -2),
                Map.entry(146L, -3),
                Map.entry(15L, -10),
                Map.entry(-4393346L, -62)
        );
        for (Map.Entry<Long, Integer> p : nbl) {
            String ns = encodeNegBase(p.getKey(), p.getValue());
            System.out.printf("%12d encoded in base %-3d = %s\n", p.getKey(), p.getValue(), ns);
            long n = decodeNegBase(ns, p.getValue());
            System.out.printf("%12s decoded in base %-3d = %d\n\n", ns, p.getValue(), n);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/bin/python
from __future__ import print_function

def EncodeNegBase(n, b): #Converts from decimal
	if n == 0:
		return "0"
	out = []
	while n != 0:
		n, rem = divmod(n, b)
		if rem < 0:
			n += 1
			rem -= b
		out.append(rem)
	return "".join(map(str, out[::-1]))

def DecodeNegBase(nstr, b): #Converts to decimal
	if nstr == "0":
		return 0
	
	total = 0
	for i, ch in enumerate(nstr[::-1]):
		total += int(ch) * b**i
	return total

if __name__=="__main__":
	
	print ("Encode 10 as negabinary (expect 11110)")
	result = EncodeNegBase(10, -2)
	print (result)
	if DecodeNegBase(result, -2) == 10: print ("Converted back to decimal")
	else: print ("Error converting back to decimal")

	print ("Encode 146 as negaternary (expect 21102)")
	result = EncodeNegBase(146, -3)
	print (result)
	if DecodeNegBase(result, -3) == 146: print ("Converted back to decimal")
	else: print ("Error converting back to decimal")

	print ("Encode 15 as negadecimal (expect 195)")
	result = EncodeNegBase(15, -10)
	print (result)
	if DecodeNegBase(result, -10) == 15: print ("Converted back to decimal")
	else: print ("Error converting back to decimal")

```

