# Stirling numbers of the first kind

## Task Link
[Rosetta Code - Stirling numbers of the first kind](https://rosettacode.org/wiki/Stirling_numbers_of_the_first_kind)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;

public class SterlingNumbersFirstKind {

    public static void main(String[] args) {
        System.out.println("Unsigned Stirling numbers of the first kind:");
        int max = 12;
        System.out.printf("n/k");
        for ( int n = 0 ; n <= max ; n++ ) {
            System.out.printf("%10d", n);
        }
        System.out.printf("%n");
        for ( int n = 0 ; n <= max ; n++ ) {
            System.out.printf("%-3d", n);
            for ( int k = 0 ; k <= n ; k++ ) {
                System.out.printf("%10s", sterling1(n, k));
            }
            System.out.printf("%n");
        }
        System.out.println("The maximum value of S1(100, k) = ");
        BigInteger previous = BigInteger.ZERO;
        for ( int k = 1 ; k <= 100 ; k++ ) {
            BigInteger current = sterling1(100, k);
            if ( current.compareTo(previous) > 0 ) {
                previous = current;
            }
            else {
                System.out.printf("%s%n(%d digits, k = %d)%n", previous, previous.toString().length(), k-1);
                break;
            }
        }
    }
    
    private static Map<String,BigInteger> COMPUTED = new HashMap<>();
    
    private static final BigInteger sterling1(int n, int k) {
        String key = n + "," + k;
        if ( COMPUTED.containsKey(key) ) {
            return COMPUTED.get(key);
        }
        if ( n == 0 && k == 0 ) {
            return BigInteger.valueOf(1);
        }
        if ( n > 0 && k == 0 ) {
            return BigInteger.ZERO; 
        }
        if ( k > n ) {
            return BigInteger.ZERO;
        }
        BigInteger result = sterling1(n-1, k-1).add(BigInteger.valueOf(n-1).multiply(sterling1(n-1, k)));
        COMPUTED.put(key, result);
        return result;
    }

}

```

## Python Code
### python_code_1.txt
```python
computed = {}

def sterling1(n, k):
	key = str(n) + "," + str(k)

	if key in computed.keys():
		return computed[key]
	if n == k == 0:
		return 1
	if n > 0 and k == 0:
		return 0
	if k > n:
		return 0
	result = sterling1(n - 1, k - 1) + (n - 1) * sterling1(n - 1, k)
	computed[key] = result
	return result

print("Unsigned Stirling numbers of the first kind:")
MAX = 12
print("n/k".ljust(10), end="")
for n in range(MAX + 1):
	print(str(n).rjust(10), end="")
print()
for n in range(MAX + 1):
	print(str(n).ljust(10), end="")
	for k in range(n + 1):
		print(str(sterling1(n, k)).rjust(10), end="")
	print()
print("The maximum value of S1(100, k) = ")
previous = 0
for k in range(1, 100 + 1):
	current = sterling1(100, k)
	if current > previous:
		previous = current
	else:
		print("{0}\n({1} digits, k = {2})\n".format(previous, len(str(previous)), k - 1))
		break

```

