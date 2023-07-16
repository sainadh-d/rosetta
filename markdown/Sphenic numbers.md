# Sphenic numbers

## Task Link
[Rosetta Code - Sphenic numbers](https://rosettacode.org/wiki/Sphenic_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class SphenicNumbers {
    public static void main(String[] args) {
        final int limit = 1000000;
        final int imax = limit / 6;
        boolean[] sieve = primeSieve(imax + 1);
        boolean[] sphenic = new boolean[limit + 1];
        for (int i = 0; i <= imax; ++i) {
            if (!sieve[i])
                continue;
            int jmax = Math.min(imax, limit / (i * i));
            if (jmax <= i)
                break;
            for (int j = i + 1; j <= jmax; ++j) {
                if (!sieve[j])
                    continue;
                int p = i * j;
                int kmax = Math.min(imax, limit / p);
                if (kmax <= j)
                    break;
                for (int k = j + 1; k <= kmax; ++k) {
                    if (!sieve[k])
                        continue;
                    assert(p * k <= limit);
                    sphenic[p * k] = true;
                }
            }
        }
    
        System.out.println("Sphenic numbers < 1000:");
        for (int i = 0, n = 0; i < 1000; ++i) {
            if (!sphenic[i])
                continue;
            ++n;
            System.out.printf("%3d%c", i, n % 15 == 0 ? '\n' : ' ');
        }
    
        System.out.println("\nSphenic triplets < 10,000:");
        for (int i = 0, n = 0; i < 10000; ++i) {
            if (i > 1 && sphenic[i] && sphenic[i - 1] && sphenic[i - 2]) {
                ++n;
                System.out.printf("(%d, %d, %d)%c",
                                  i - 2, i - 1, i, n % 3 == 0 ? '\n' : ' ');
            }
        }
    
        int count = 0, triplets = 0, s200000 = 0, t5000 = 0;
        for (int i = 0; i < limit; ++i) {
            if (!sphenic[i])
                continue;
            ++count;
            if (count == 200000)
                s200000 = i;
            if (i > 1 && sphenic[i - 1] && sphenic[i - 2]) {
                ++triplets;
                if (triplets == 5000)
                    t5000 = i;
            }
        }
    
        System.out.printf("\nNumber of sphenic numbers < 1,000,000: %d\n", count);
        System.out.printf("Number of sphenic triplets < 1,000,000: %d\n", triplets);
    
        List<Integer> factors = primeFactors(s200000);
        assert(factors.size() == 3);
        System.out.printf("The 200,000th sphenic number: %d = %d * %d * %d\n",
                          s200000, factors.get(0), factors.get(1),
                          factors.get(2));
        System.out.printf("The 5,000th sphenic triplet: (%d, %d, %d)\n",
                          t5000 - 2, t5000 - 1, t5000);
    }

    private static boolean[] primeSieve(int limit) {
        boolean[] sieve = new boolean[limit];
        Arrays.fill(sieve, true);
        if (limit > 0)
            sieve[0] = false;
        if (limit > 1)
            sieve[1] = false;
        for (int i = 4; i < limit; i += 2)
            sieve[i] = false;
        for (int p = 3, sq = 9; sq < limit; p += 2) {
            if (sieve[p]) {
                for (int q = sq; q < limit; q += p << 1)
                    sieve[q] = false;
            }
            sq += (p + 1) << 2;
        }
        return sieve;
    }
    
    private static List<Integer> primeFactors(int n) {
        List<Integer> factors = new ArrayList<>();
        if (n > 1 && (n & 1) == 0) {
            factors.add(2);
            while ((n & 1) == 0)
                n >>= 1;
        }
        for (int p = 3; p * p <= n; p += 2) {
            if (n % p == 0) {
                factors.add(p);
                while (n % p == 0)
                    n /= p;
            }
        }
        if (n > 1)
            factors.add(n);
        return factors;
    }
}

```

## Python Code
### python_code_1.txt
```python
""" rosettacode.org task Sphenic_numbers """


from sympy import factorint

sphenics1m, sphenic_triplets1m = [], []

for i in range(3, 1_000_000):
    d = factorint(i)
    if len(d) == 3 and sum(d.values()) == 3:
        sphenics1m.append(i)
        if len(sphenics1m) > 2 and i - sphenics1m[-3] == 2 and i - sphenics1m[-2] == 1:
            sphenic_triplets1m.append(i)

print('Sphenic numbers less than 1000:')
for i, n in enumerate(sphenics1m):
    if n < 1000:
        print(f'{n : 5}', end='\n' if (i + 1) % 15 == 0 else '')
    else:
        break

print('\n\nSphenic triplets less than 10_000:')
for i, n in enumerate(sphenic_triplets1m):
    if n < 10_000:
        print(f'({n - 2} {n - 1} {n})', end='\n' if (i + 1) % 3 == 0 else '  ')
    else:
        break

print('\nThere are', len(sphenics1m), 'sphenic numbers and', len(sphenic_triplets1m),
      'sphenic triplets less than 1 million.')

S2HK = sphenics1m[200_000 - 1]
T5K = sphenic_triplets1m[5000 - 1]
print(f'The 200_000th sphenic number is {S2HK}, with prime factors {list(factorint(S2HK).keys())}.')
print(f'The 5000th sphenic triplet is ({T5K - 2} {T5K - 1} {T5K}).')

```

