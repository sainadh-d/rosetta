# Square-free integers

## Task Link
[Rosetta Code - Square-free integers](https://rosettacode.org/wiki/Square-free_integers)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public class SquareFree
{
    private static List<Long> sieve(long limit) {
        List<Long> primes = new ArrayList<Long>();
        primes.add(2L);
        boolean[] c = new boolean[(int)limit + 1]; // composite = true
        // no need to process even numbers > 2
        long p = 3;
        for (;;) {
            long p2 = p * p;
            if (p2 > limit) break;
            for (long i = p2; i <= limit; i += 2 * p) c[(int)i] = true;
            for (;;) {
                p += 2;
                if (!c[(int)p]) break;
            }
        }
        for (long i = 3; i <= limit; i += 2) {
            if (!c[(int)i]) primes.add(i);
        }
        return primes;
    }

    private static List<Long> squareFree(long from, long to) {
        long limit = (long)Math.sqrt((double)to);
        List<Long> primes = sieve(limit);
        List<Long> results = new ArrayList<Long>();

        outer: for (long i = from; i <= to; i++) {
            for (long p : primes) {
                long p2 = p * p;
                if (p2 > i) break;
                if (i % p2 == 0) continue outer;
            }
            results.add(i);
        }
        return results;
    }

    private final static long TRILLION = 1000000000000L;

    public static void main(String[] args) {
        System.out.println("Square-free integers from 1 to 145:");
        List<Long> sf = squareFree(1, 145);
        for (int i = 0; i < sf.size(); i++) {
            if (i > 0 && i % 20 == 0) {
                System.out.println();
            }
            System.out.printf("%4d", sf.get(i));
        }

        System.out.print("\n\nSquare-free integers");
        System.out.printf(" from %d to %d:\n", TRILLION, TRILLION + 145);
        sf = squareFree(TRILLION, TRILLION + 145);
        for (int i = 0; i < sf.size(); i++) {
            if (i > 0 && i % 5 == 0) System.out.println();
            System.out.printf("%14d", sf.get(i));
        }

        System.out.println("\n\nNumber of square-free integers:\n");
        long[] tos = {100, 1000, 10000, 100000, 1000000};
        for (long to : tos) {
            System.out.printf("  from %d to %d = %d\n", 1, to, squareFree(1, to).size());
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import math

def SquareFree ( _number ) :
	max = (int) (math.sqrt ( _number ))

	for root in range ( 2, max+1 ):					# Create a custom prime sieve
		if 0 == _number % ( root * root ):
			return False

	return True

def ListSquareFrees( _start, _end ):
	count = 0
	for i in range ( _start, _end+1 ):
		if True == SquareFree( i ):
			print ( "{}\t".format(i), end="" )
			count += 1

	print ( "\n\nTotal count of square-free numbers between {} and {}: {}".format(_start, _end, count))

ListSquareFrees( 1, 100 )
ListSquareFrees( 1000000000000, 1000000000145 )

```

