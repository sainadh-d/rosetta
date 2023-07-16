# Wagstaff primes

## Task Link
[Rosetta Code - Wagstaff primes](https://rosettacode.org/wiki/Wagstaff_primes)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger; 

public class Main {
  public static void main(String[] args) {
    BigInteger d = new BigInteger("3"), a;
    int lmt = 25, sl, c = 0;
    for (int i = 3; i < 5808; ) {
      a = BigInteger.ONE.shiftLeft(i).add(BigInteger.ONE).divide(d);
      if (a.isProbablePrime(1)) {
        System.out.printf("%2d %4d ", ++c, i);
        String s = a.toString(); sl = s.length();
        if (sl < lmt) System.out.println(a);
        else System.out.println(s.substring(0, 11) + ".." + s.substring(sl - 11, sl) + " " + sl + " digits");
      }
      i = BigInteger.valueOf(i).nextProbablePrime().intValue();
    }
  }
}

```

## Python Code
### python_code_1.txt
```python
""" Rosetta code Wagstaff_primes task """

from sympy import isprime

def wagstaff(N):
    """ find first N Wagstaff primes """
    pri, wcount = 1, 0
    while wcount < N:
        pri += 2
        if isprime(pri):
            wag = (2**pri + 1) // 3
            if isprime(wag):
                wcount += 1
                print(f'{wcount: 3}: {pri: 5} => ', 
                      f'{wag:,}' if wcount < 11 else f'[{len(str(wag))} digit number]')


wagstaff(24)

```

