# Extensible prime generator

## Task Link
[Rosetta Code - Extensible prime generator](https://rosettacode.org/wiki/Extensible_prime_generator)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class PrimeGenerator {
    private int limit_;
    private int index_ = 0;
    private int increment_;
    private int count_ = 0;
    private List<Integer> primes_ = new ArrayList<>();
    private BitSet sieve_ = new BitSet();
    private int sieveLimit_ = 0;

    public PrimeGenerator(int initialLimit, int increment) {
        limit_ = nextOddNumber(initialLimit);
        increment_ = increment;
        primes_.add(2);
        findPrimes(3);
    }

    public int nextPrime() {
        if (index_ == primes_.size()) {
            if (Integer.MAX_VALUE - increment_ < limit_)
                return 0;
            int start = limit_ + 2;
            limit_ = nextOddNumber(limit_ + increment_);
            primes_.clear();
            findPrimes(start);
        }
        ++count_;
        return primes_.get(index_++);
    }

    public int count() {
        return count_;
    }

    private void findPrimes(int start) {
        index_ = 0;
        int newLimit = sqrt(limit_);
        for (int p = 3; p * p <= newLimit; p += 2) {
            if (sieve_.get(p/2 - 1))
                continue;
            int q = p * Math.max(p, nextOddNumber((sieveLimit_ + p - 1)/p));
            for (; q <= newLimit; q += 2*p)
                sieve_.set(q/2 - 1, true);
        }
        sieveLimit_ = newLimit;
        int count = (limit_ - start)/2 + 1;
        BitSet composite = new BitSet(count);
        for (int p = 3; p <= newLimit; p += 2) {
            if (sieve_.get(p/2 - 1))
                continue;
            int q = p * Math.max(p, nextOddNumber((start + p - 1)/p)) - start;
            q /= 2;
            for (; q >= 0 && q < count; q += p)
                composite.set(q, true);
        }
        for (int p = 0; p < count; ++p) {
            if (!composite.get(p))
                primes_.add(p * 2 + start);
        }
    }

    private static int sqrt(int n) {
        return nextOddNumber((int)Math.sqrt(n));
    }

    private static int nextOddNumber(int n) {
        return 1 + 2 * (n/2);
    }

    public static void main(String[] args) {
        PrimeGenerator pgen = new PrimeGenerator(20, 200000);
        System.out.println("First 20 primes:");
        for (int i = 0; i < 20; ++i) {
            if (i > 0)
                System.out.print(", ");
            System.out.print(pgen.nextPrime());
        }
        System.out.println();
        System.out.println("Primes between 100 and 150:");
        for (int i = 0; ; ) {
            int prime = pgen.nextPrime();
            if (prime > 150)
                break;
            if (prime >= 100) {
                if (i++ != 0)
                    System.out.print(", ");
                System.out.print(prime);
            }
        }
        System.out.println();
        int count = 0;
        for (;;) {
            int prime = pgen.nextPrime();
            if (prime > 8000)
                break;
            if (prime >= 7700)
                ++count;
        }
        System.out.println("Number of primes between 7700 and 8000: " + count);
        int n = 10000;
        for (;;) {
            int prime = pgen.nextPrime();
            if (prime == 0) {
                System.out.println("Can't generate any more primes.");
                break;
            }
            if (pgen.count() == n) {
                System.out.println(n + "th prime: " + prime);
                n *= 10;
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
islice(count(7), 0, None, 2)

```

### python_code_2.txt
```python
from __future__ import print_function
from prime_decomposition import primes
from itertools import islice


def p_range(lower_inclusive, upper_exclusive):
    'Primes in the range'
    for p in primes():
        if p >= upper_exclusive: break
        if p >= lower_inclusive: yield p

if __name__ == '__main__':
    print('The first twenty primes:\n  ', list(islice(primes(),20)))
    print('The primes between 100 and 150:\n  ', list(p_range(100, 150)))
    print('The ''number'' of primes between 7,700 and 8,000:\n  ', len(list(p_range(7700, 8000))))
    print('The 10,000th prime:\n  ', next(islice(primes(),10000-1, 10000)))

```

### python_code_3.txt
```python
def wsieve():       # ideone.com/mqO25A
    wh11 = [ 2,4,2,4,6,2,6,4,2,4,6,6, 2,6,4,2,6,4,6,8,4,2,4,2,
             4,8,6,4,6,2,4,6,2,6,6,4, 2,4,6,2,6,4,2,4,2,10,2,10 ]
    cs = accumulate(chain([11], cycle(wh11)))
    yield next(cs)     # cf. ideone.com/WFv4f
    ps = wsieve()      #     codereview.stackexchange.com/q/92365/9064
    p = next(ps)       # 11         stackoverflow.com/q/30553925/849891
    psq = p*p          # 121
    D = dict(zip( accumulate(chain([0], wh11)), count(0) ))   # start from
    mults = {}
    for c in cs:
        if c in mults:
            wheel = mults.pop(c)
        elif c < psq:
            yield c
            continue
        else:          # c==psq:  map (p*) (roll wh from p) = roll (wh*p) from (p*p)
            x = [p*d for d in wh11]
            i = D[(p-11) % 210]
            wheel = accumulate(chain([psq+x[i]], cycle(x[i+1:] + x[:i+1])))
            p = next(ps)
            psq = p*p
        for m in wheel:
            if not m in mults:
                break
        mults[m] = wheel

def primes():
    yield from (2, 3, 5, 7)
    yield from wsieve()

print( list( islice( primes(), 0, 20)))
print( list( takewhile( lambda x: x<150,
                   dropwhile( lambda x: x<100, primes()))))
print( len( list( takewhile( lambda x: x<8000,
                   dropwhile( lambda x: x<7700, primes())))))
print( next( islice( primes(), 10000-1, 10000)))

```

### python_code_4.txt
```python
from itertools import count, takewhile, islice

def prime_sieve():
    sieved = count(2)
    prime = next(sieved)
    yield prime
    primes = [prime]
    for x in sieved:
        possible_prime_divs = takewhile(lambda p: p <= x**0.5, primes)
        if any(x % prime == 0 for prime in possible_prime_divs):
            continue
        yield x
        primes.append(x)

if __name__ == '__main__':
    def leq_150(x): return x <= 150
    def leq_8000(x): return x <= 8000
    
    print("Show the first twenty primes.\n   =",
        list(islice(prime_sieve(), 20)))
    print("Show the primes between 100 and 150\n   =",
        [x for x in takewhile(leq_150, prime_sieve()) if x >= 100])
    print("Show the number of primes between 7,700 and 8,000.\n   =",
        sum(1 for x in takewhile(leq_8000, prime_sieve()) if x >= 7700))
    print("Show the 10,000th prime.\n   =",
        next(islice(prime_sieve(), 10000-1, 10000)))

```

