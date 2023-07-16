# Factorial primes

## Task Link
[Rosetta Code - Factorial primes](https://rosettacode.org/wiki/Factorial_primes)

## Java Code
### java_code_1.txt
```java
public class MainApp {
    public static void main(String[] args) {
        int countOfPrimes = 0;
        final int targetCountOfPrimes = 10;
        long f = 1;
        while (countOfPrimes < targetCountOfPrimes) {
            long factorialNum = getFactorial(f);
            boolean primePlus = isPrime(factorialNum + 1);
            boolean primeMinus = isPrime(factorialNum - 1);
            if (primeMinus) {
                countOfPrimes++;
                System.out.println(countOfPrimes + ": " + factorialNum + "! - 1 = " + (factorialNum - 1));

            }
            if (primePlus  && f > 1) {
                countOfPrimes++;
                System.out.println(countOfPrimes + ": " + factorialNum + "! + 1 = " + (factorialNum + 1));
            }
            f++;
        }
    }

    private static long getFactorial(long f) {
        long factorial = 1;
        for (long i = 1; i < f; i++) {
            factorial *= i;
        }
        return factorial;
    }

    private static boolean isPrime(long num) {
        if (num < 2) {return false;}
        for (long i = 2; i < num; i++) {
            if (num % i == 0) {return false;}
        }
        return true;
    }
}

```

### java_code_2.txt
```java
import java.math.BigInteger;

public class MainApp {
    public static void main(String[] args) {
        //Used to measure total runtime of program.
        long starttime = System.nanoTime();
        //How many primes found, how many primes wanted, loop counter.
        int countOfPrimes = 0;
        final int targetCountOfPrimes = 30;
        long f = 1;
        //Starting BigInteger at 1.
        BigInteger biFactorial = BigInteger.ONE;
        while (countOfPrimes < targetCountOfPrimes) {
            //Each loop, multiply the number by the loop 
            //counter (f) to increase factorial much more quickly.
            biFactorial = biFactorial.multiply(BigInteger.valueOf(f)); 
            // one less than the factorial.
            BigInteger biMinusOne = biFactorial.subtract(BigInteger.ONE); 
            // one more than the factorial.
            BigInteger biPlusOne = biFactorial.add(BigInteger.ONE); 
            
            //Determine if the numbers are prime with a probability of 100
            boolean primeMinus = biMinusOne.isProbablePrime(100);
            boolean primePlus = biPlusOne.isProbablePrime(100);
            
            //Make the big number look like a pretty string for output.
            String biMinusOneString = convert(biMinusOne);
            String biPlusOneString = convert(biPlusOne);
            
            //If the number was prime, output and increment the primt counter.
            if (primeMinus) {
                countOfPrimes++;
                System.out.println(
                        countOfPrimes + ": " + f + "! - 1 = " + biMinusOneString);
            }
            if (primePlus) {
                countOfPrimes++;
                System.out.println(countOfPrimes + ": " + f + "! + 1 = " + biPlusOneString);
            }
            //Increment loop counter.
            f++;
        }
        //Calculate and display program runtime.
        long stoptime = System.nanoTime();
        long runtime = stoptime - starttime;
        System.out.println("Program runtime: " + runtime + " ns (~" + runtime/1_000_000_000 + " seconds)");
    }

    //Method to make output pretty
    private static String convert(BigInteger bi) {
        String s = bi.toString();
        int l = s.length();
        String s2 = "";
        if (l >= 40) {
            s2 = s.substring(0, 19);
            s2 += "..." + s.substring(s.length() - 20, s.length());
            s2 += " : " + l + " digits";
        } else {s2 = s;}
        return s2;
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import count
from itertools import islice
from typing import Iterable
from typing import Tuple

import gmpy2


def factorials() -> Iterable[int]:
    fact = 1
    for i in count(1):
        yield fact
        fact *= i


def factorial_primes() -> Iterable[Tuple[int, int, str]]:
    for n, fact in enumerate(factorials()):
        if gmpy2.is_prime(fact - 1):
            yield (n, fact - 1, "-")
        if gmpy2.is_prime(fact + 1):
            yield (n, fact + 1, "+")


def print_factorial_primes(limit=10) -> None:
    print(f"First {limit} factorial primes.")
    for n, fact_prime, op in islice(factorial_primes(), 1, limit + 1):
        s = str(fact_prime)
        if len(s) > 40:
            s = f"{s[:20]}...{s[-20:]} ({len(s)} digits)"
        print(f"{n}! {op} 1 = {s}")


if __name__ == "__main__":
    import sys
    print_factorial_primes(int(sys.argv[1]) if len(sys.argv) > 1 else 10)

```

