# Find largest left truncatable prime in a given base

## Task Link
[Rosetta Code - Find largest left truncatable prime in a given base](https://rosettacode.org/wiki/Find_largest_left_truncatable_prime_in_a_given_base)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.*;

class LeftTruncatablePrime
{
  private static List<BigInteger> getNextLeftTruncatablePrimes(BigInteger n, int radix, int millerRabinCertainty)
  {
    List<BigInteger> probablePrimes = new ArrayList<BigInteger>();
    String baseString = n.equals(BigInteger.ZERO) ? "" : n.toString(radix);
    for (int i = 1; i < radix; i++)
    {
      BigInteger p = new BigInteger(Integer.toString(i, radix) + baseString, radix);
      if (p.isProbablePrime(millerRabinCertainty))
        probablePrimes.add(p);
    }
    return probablePrimes;
  }
  
  public static BigInteger getLargestLeftTruncatablePrime(int radix, int millerRabinCertainty)
  {
    List<BigInteger> lastList = null;
    List<BigInteger> list = getNextLeftTruncatablePrimes(BigInteger.ZERO, radix, millerRabinCertainty);
    while (!list.isEmpty())
    {
      lastList = list;
      list = new ArrayList<BigInteger>();
      for (BigInteger n : lastList)
        list.addAll(getNextLeftTruncatablePrimes(n, radix, millerRabinCertainty));
    }
    if (lastList == null)
      return null;
    Collections.sort(lastList);
    return lastList.get(lastList.size() - 1);
  }
  
  public static void main(String[] args)
  {
    if (args.length != 2) {
      System.err.println("There must be exactly two command line arguments.");
      return;
    }
    int maxRadix;
    try {
      maxRadix = Integer.parseInt(args[0]);
      if (maxRadix < 3) throw new NumberFormatException(); 
    } catch (NumberFormatException e) {
      System.err.println("Radix must be an integer greater than 2.");
      return;
    }
    int millerRabinCertainty;
    try {
      millerRabinCertainty = Integer.parseInt(args[1]);
    } catch (NumberFormatException e) {
      System.err.println("Miiller-Rabin Certainty must be an integer.");
      return;
    }  
    for (int radix = 3; radix <= maxRadix; radix++)
    {
      BigInteger largest = getLargestLeftTruncatablePrime(radix, millerRabinCertainty);
      System.out.print("n=" + radix + ": ");
      if (largest == null)
        System.out.println("No left-truncatable prime");
      else
        System.out.println(largest + " (in base " + radix + "): " + largest.toString(radix));
    }
  }
  
}

```

## Python Code
### python_code_1.txt
```python
import random

def is_probable_prime(n,k):
    #this uses the miller-rabin primality test found from rosetta code
    if n==0 or n==1:
        return False
    if n==2:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n-1

    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient

    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(k):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite    
    
    
def largest_left_truncatable_prime(base):    
    radix = 0
    candidates = [0]
    while True:
        new_candidates=[]
        multiplier = base**radix
        for i in range(1,base):
            new_candidates += [x+i*multiplier for x in candidates if is_probable_prime(x+i*multiplier,30)]
        if len(new_candidates)==0:
            return max(candidates)
        candidates = new_candidates
        radix += 1

for b in range(3,24):
    print("%d:%d\n" % (b,largest_left_truncatable_prime(b)))

```

