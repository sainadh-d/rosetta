# Long primes

## Task Link
[Rosetta Code - Long primes](https://rosettacode.org/wiki/Long_primes)

## Java Code
### java_code_1.txt
```java
import java.util.LinkedList;
import java.util.List;

public class LongPrimes
{
    private static void sieve(int limit, List<Integer> primes)
    {
        boolean[] c = new boolean[limit];
        for (int i = 0; i < limit; i++)
            c[i] = false;
        // No need to process even numbers
        int p = 3, n = 0;
        int p2 = p * p;
        while (p2 <= limit)
        {
            for (int i = p2; i <= limit; i += 2 * p)
                c[i] = true;
            do
                p += 2;
            while (c[p]);
            p2 = p * p;
        }
        for (int i = 3; i <= limit; i += 2)
            if (!c[i])
                primes.add(i);
    }

    // Finds the period of the reciprocal of n
    private static int findPeriod(int n)
    {
        int r = 1, period = 0;
        for (int i = 1; i < n; i++)
            r = (10 * r) % n;
        int rr = r;
        do
        {
            r = (10 * r) % n;
            ++period;
        }
        while (r != rr);
        return period;
    }
    
    public static void main(String[] args)
    {
        int[] numbers = new int[]{500, 1000, 2000, 4000, 8000, 16000, 32000, 64000};
        int[] totals = new int[numbers.length]; 
        List<Integer> primes = new LinkedList<Integer>();
        List<Integer> longPrimes = new LinkedList<Integer>();
        sieve(64000, primes);
        for (int prime : primes)
            if (findPeriod(prime) == prime - 1)
                longPrimes.add(prime);
        int count = 0, index = 0;
        for (int longPrime : longPrimes)
        {
            if (longPrime > numbers[index])
                totals[index++] = count;
            ++count;
        }
        totals[numbers.length - 1] = count;
        System.out.println("The long primes up to " + numbers[0] + " are:");
        System.out.println(longPrimes.subList(0, totals[0]));
        System.out.println();
        System.out.println("The number of long primes up to:");
        for (int i = 0; i <= 7; i++)
            System.out.printf("  %5d is %d\n", numbers[i], totals[i]);
    }
}

```

## Python Code
### python_code_1.txt
```python
def sieve(limit):
    primes = []
    c = [False] * (limit + 1) # composite = true
    # no need to process even numbers
    p = 3
    while True:
        p2 = p * p
        if p2 > limit: break
        for i in range(p2, limit, 2 * p): c[i] = True
        while True:
            p += 2
            if not c[p]: break

    for i in range(3, limit, 2):
        if not c[i]: primes.append(i)
    return primes

# finds the period of the reciprocal of n
def findPeriod(n):
    r = 1
    for i in range(1, n): r = (10 * r) % n
    rr = r
    period = 0
    while True:
        r = (10 * r) % n
        period += 1
        if r == rr: break
    return period

primes = sieve(64000)
longPrimes = []
for prime in primes:
    if findPeriod(prime) == prime - 1:
        longPrimes.append(prime)
numbers = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000]
count = 0
index = 0
totals = [0] * len(numbers)
for longPrime in longPrimes:
    if longPrime > numbers[index]:
        totals[index] = count
        index += 1
    count += 1
totals[-1] = count
print('The long primes up to 500 are:')
print(str(longPrimes[:totals[0]]).replace(',', ''))
print('\nThe number of long primes up to:')
for (i, total) in enumerate(totals):
    print('  %5d is %d' % (numbers[i], total))

```

