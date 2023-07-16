# Earliest difference between prime gaps

## Task Link
[Rosetta Code - Earliest difference between prime gaps](https://rosettacode.org/wiki/Earliest_difference_between_prime_gaps)

## Java Code
### java_code_1.txt
```java
import java.util.HashMap;
import java.util.Map;

public class PrimeGaps {
    private Map<Integer, Integer> gapStarts = new HashMap<>();
    private int lastPrime;
    private PrimeGenerator primeGenerator = new PrimeGenerator(1000, 500000);

    public static void main(String[] args) {
        final int limit = 100000000;
        PrimeGaps pg = new PrimeGaps();
        for (int pm = 10, gap1 = 2;;) {
            int start1 = pg.findGapStart(gap1);
            int gap2 = gap1 + 2;
            int start2 = pg.findGapStart(gap2);
            int diff = start2 > start1 ? start2 - start1 : start1 - start2;
            if (diff > pm) {
                System.out.printf(
                    "Earliest difference > %,d between adjacent prime gap starting primes:\n"
                    + "Gap %,d starts at %,d, gap %,d starts at %,d, difference is %,d.\n\n",
                    pm, gap1, start1, gap2, start2, diff);
                if (pm == limit)
                    break;
                pm *= 10;
            } else {
                gap1 = gap2;
            }
        }
    }

    private int findGapStart(int gap) {
        Integer start = gapStarts.get(gap);
        if (start != null)
            return start;
        for (;;) {
            int prev = lastPrime;
            lastPrime = primeGenerator.nextPrime();
            int diff = lastPrime - prev;
            gapStarts.putIfAbsent(diff, prev);
            if (diff == gap)
                return prev;
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
""" https://rosettacode.org/wiki/Earliest_difference_between_prime_gaps """

from primesieve import primes

LIMIT = 10**9
pri = primes(LIMIT * 5)
gapstarts = {}
for i in range(1, len(pri)):
    if pri[i] - pri[i - 1] not in gapstarts:
        gapstarts[pri[i] - pri[i - 1]] = pri[i - 1]

PM, GAP1, = 10, 2
while True:
    while GAP1 not in gapstarts:
        GAP1 += 2
    start1 = gapstarts[GAP1]
    GAP2 = GAP1 + 2
    if GAP2 not in gapstarts:
        GAP1 = GAP2 + 2
        continue
    start2 = gapstarts[GAP2]
    diff = abs(start2 - start1)
    if diff > PM:
        print(f"Earliest difference >{PM: ,} between adjacent prime gap starting primes:")
        print(f"Gap {GAP1} starts at{start1: ,}, gap {GAP2} starts at{start2: ,}, difference is{diff: ,}.\n")
        if PM == LIMIT:
            break
        PM *= 10
    else:
        GAP1 = GAP2

```

