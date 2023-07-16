# Factors of a Mersenne number

## Task Link
[Rosetta Code - Factors of a Mersenne number](https://rosettacode.org/wiki/Factors_of_a_Mersenne_number)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

class MersenneFactorCheck
{

  private final static BigInteger TWO = BigInteger.valueOf(2);
  
  public static boolean isPrime(long n)
  {
    if (n == 2)
      return true;
    if ((n < 2) || ((n & 1) == 0))
      return false;
    long maxFactor = (long)Math.sqrt((double)n);
    for (long possibleFactor = 3; possibleFactor <= maxFactor; possibleFactor += 2)
      if ((n % possibleFactor) == 0)
        return false;
    return true;
  }
  
  public static BigInteger findFactorMersenneNumber(int primeP)
  {
    if (primeP <= 0)
      throw new IllegalArgumentException();
    BigInteger bigP = BigInteger.valueOf(primeP);
    BigInteger m = BigInteger.ONE.shiftLeft(primeP).subtract(BigInteger.ONE);
    // There are more complicated ways of getting closer to sqrt(), but not that important here, so go with simple
    BigInteger maxFactor = BigInteger.ONE.shiftLeft((primeP + 1) >>> 1);
    BigInteger twoP = BigInteger.valueOf(primeP << 1);
    BigInteger possibleFactor = BigInteger.ONE;
    int possibleFactorBits12 = 0;
    int twoPBits12 = primeP & 3;
    
    while ((possibleFactor = possibleFactor.add(twoP)).compareTo(maxFactor) <= 0)
    {
      possibleFactorBits12 = (possibleFactorBits12 + twoPBits12) & 3;
      // "Furthermore, q must be 1 or 7 mod 8". We know it's odd due to the +1 done above, so bit 0 is set. Therefore, we only care about bits 1 and 2 equaling 00 or 11
      if ((possibleFactorBits12 == 0) || (possibleFactorBits12 == 3))
        if (TWO.modPow(bigP, possibleFactor).equals(BigInteger.ONE))
          return possibleFactor;
    }
    return null;
  }
  
  public static void checkMersenneNumber(int p)
  {
    if (!isPrime(p))
    {
      System.out.println("M" + p + " is not prime");
      return;
    }
    BigInteger factor = findFactorMersenneNumber(p);
    if (factor == null)
      System.out.println("M" + p + " is prime");
    else
      System.out.println("M" + p + " is not prime, has factor " + factor);
    return;
  }

  public static void main(String[] args)
  {
    for (int p = 1; p <= 50; p++)
      checkMersenneNumber(p);
    checkMersenneNumber(929);
    return;
  }
  
}

```

## Python Code
### python_code_1.txt
```python
def is_prime(number):
    return True # code omitted - see Primality by Trial Division

def m_factor(p):
    max_k = 16384 / p # arbitrary limit; since Python automatically uses long's, it doesn't overflow
    for k in xrange(max_k):
        q = 2*p*k + 1
        if not is_prime(q):
            continue
        elif q % 8 != 1 and q % 8 != 7:
            continue
        elif pow(2, p, q) == 1:
            return q
    return None

if __name__ == '__main__':
    exponent = int(raw_input("Enter exponent of Mersenne number: "))
    if not is_prime(exponent):
        print "Exponent is not prime: %d" % exponent
    else:
        factor = m_factor(exponent)
        if not factor:
            print "No factor found for M%d" % exponent
        else:
            print "M%d has a factor: %d" % (exponent, factor)

```

