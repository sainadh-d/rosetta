# Successive prime differences

## Task Link
[Rosetta Code - Successive prime differences](https://rosettacode.org/wiki/Successive_prime_differences)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SuccessivePrimeDifferences {
    private static Integer[] sieve(int limit) {
        List<Integer> primes = new ArrayList<>();
        primes.add(2);
        boolean[] c = new boolean[limit + 1];// composite = true
        // no need to process even numbers > 2
        int p = 3;
        while (true) {
            int p2 = p * p;
            if (p2 > limit) {
                break;
            }
            for (int i = p2; i <= limit; i += 2 * p) {
                c[i] = true;
            }
            do {
                p += 2;
            } while (c[p]);
        }
        for (int i = 3; i <= limit; i += 2) {
            if (!c[i]) {
                primes.add(i);
            }
        }

        return primes.toArray(new Integer[0]);
    }

    private static List<List<Integer>> successivePrimes(Integer[] primes, Integer[] diffs) {
        List<List<Integer>> results = new ArrayList<>();
        int dl = diffs.length;
        outer:
        for (int i = 0; i < primes.length - dl; i++) {
            Integer[] group = new Integer[dl + 1];
            group[0] = primes[i];
            for (int j = i; j < i + dl; ++j) {
                if (primes[j + 1] - primes[j] != diffs[j - i]) {
                    continue outer;
                }
                group[j - i + 1] = primes[j + 1];
            }
            results.add(Arrays.asList(group));
        }
        return results;
    }

    public static void main(String[] args) {
        Integer[] primes = sieve(999999);
        Integer[][] diffsList = {{2}, {1}, {2, 2}, {2, 4}, {4, 2}, {6, 4, 2}};
        System.out.println("For primes less than 1,000,000:-\n");
        for (Integer[] diffs : diffsList) {
            System.out.printf("  For differences of %s ->\n", Arrays.toString(diffs));
            List<List<Integer>> sp = successivePrimes(primes, diffs);
            if (sp.isEmpty()) {
                System.out.println("    No groups found");
                continue;
            }
            System.out.printf("    First group   = %s\n", Arrays.toString(sp.get(0).toArray(new Integer[0])));
            System.out.printf("    Last group    = %s\n", Arrays.toString(sp.get(sp.size() - 1).toArray(new Integer[0])));
            System.out.printf("    Number found  = %d\n", sp.size());
            System.out.println();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
# https://docs.sympy.org/latest/index.html
from sympy import Sieve

def nsuccprimes(count, mx):
    "return tuple of <count> successive primes <= mx (generator)"
    sieve = Sieve()
    sieve.extend(mx)
    primes = sieve._list
    return zip(*(primes[n:] for n in range(count)))

def check_value_diffs(diffs, values):
    "Differences between successive values given by successive items in diffs?"
    return all(v[1] - v[0] == d 
               for d, v in zip(diffs, zip(values, values[1:])))

def successive_primes(offsets=(2, ), primes_max=1_000_000):
    return (sp for sp in nsuccprimes(len(offsets) + 1, primes_max) 
            if check_value_diffs(offsets, sp))

if __name__ == '__main__':
    for offsets, mx in [((2,),      1_000_000), 
                        ((1,),      1_000_000),
                        ((2, 2),    1_000_000),
                        ((2, 4),    1_000_000),
                        ((4, 2),    1_000_000),
                        ((6, 4, 2), 1_000_000),
                       ]:
        print(f"## SETS OF {len(offsets)+1} SUCCESSIVE PRIMES <={mx:_} WITH "
              f"SUCCESSIVE DIFFERENCES OF {str(list(offsets))[1:-1]}")
        for count, last in enumerate(successive_primes(offsets, mx), 1):
            if count == 1:
                first = last
        print("  First group:", str(first)[1:-1])
        print("   Last group:", str(last)[1:-1])
        print("        Count:", count)

```

