# Arbitrary-precision integers (included)

## Task Link
[Rosetta Code - Arbitrary-precision integers (included)](https://rosettacode.org/wiki/Arbitrary-precision_integers_(included))

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

class IntegerPower {
    public static void main(String[] args) {
        BigInteger power = BigInteger.valueOf(5).pow(BigInteger.valueOf(4).pow(BigInteger.valueOf(3).pow(2).intValueExact()).intValueExact());
        String str = power.toString();
        int len = str.length();
        System.out.printf("5**4**3**2 = %s...%s and has %d digits%n",
                str.substring(0, 20), str.substring(len - 20), len);
    }
}

```

### java_code_2.txt
```java
import java.math.BigInteger;

// Variable definitions
BigInteger _5, _4, powResult;
_5 = BigInteger.valueOf(5);
_4 = BigInteger.valueOf(4);

//calculations
powResult          = _5.pow(_4.pow(9).intValueExact());
String powStr      = powResult.toString();
int    powLen      = powStr.length();
String powStrStart = powStr.substring(0, 20);
String powStrEnd   = powStr.substring(powLen - 20);

//output
System.out.printf("5**4**3**2 = %s...%s and has %d digits%n", powStrStart, powStrEnd, powLen);

```

## Python Code
### python_code_1.txt
```python
>>> y = str( 5**4**3**2 )
>>> print ("5**4**3**2 = %s...%s and has %i digits" % (y[:20], y[-20:], len(y)))
5**4**3**2 = 62060698786608744707...92256259918212890625 and has 183231 digits

```

