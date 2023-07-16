# Almost prime

## Task Link
[Rosetta Code - Almost prime](https://rosettacode.org/wiki/Almost_prime)

## Java Code
### java_code_1.txt
```java
public class AlmostPrime {
    public static void main(String[] args) {
        for (int k = 1; k <= 5; k++) {
            System.out.print("k = " + k + ":");

            for (int i = 2, c = 0; c < 10; i++) {
                if (kprime(i, k)) {
                    System.out.print(" " + i);
                    c++;
                }
            }

            System.out.println("");
        }
    }

    public static boolean kprime(int n, int k) {
        int f = 0;
        for (int p = 2; f < k && p * p <= n; p++) {
            while (n % p == 0) {
                n /= p;
                f++;
            }
        }
        return f + ((n > 1) ? 1 : 0) == k;
    }
}

```

## Python Code
### python_code_1.txt
```python
from prime_decomposition import decompose
from itertools import islice, count
try: 
    from functools import reduce
except: 
    pass


def almostprime(n, k=2):
    d = decompose(n)
    try:
        terms = [next(d) for i in range(k)]
        return reduce(int.__mul__, terms, 1) == n
    except:
        return False

if __name__ == '__main__':
    for k in range(1,6):
        print('%i: %r' % (k, list(islice((n for n in count() if almostprime(n, k)), 10))))

```

### python_code_2.txt
```python
# k-Almost-primes
# Python 3.6.3
# no imports
# author: manuelcaeiro | https://github.com/manuelcaeiro 

def prime_factors(m=2):
    
    for i in range(2, m):
        r, q = divmod(m, i)
        if not q:
            return [i] + prime_factors(r)
    return [m]

def k_almost_primes(n, k=2):
    multiples = set()
    lists = list()
    for x in range(k+1):
        lists.append([])

    for i in range(2, n+1):
        if i not in multiples:
            if len(lists[1]) < 10:
                lists[1].append(i)
            multiples.update(range(i*i, n+1, i))
    print("k=1: {}".format(lists[1]))

    for j in range(2, k+1):
        for m in multiples:
            l = prime_factors(m)
            ll = len(l)
            if ll == j and len(lists[j]) < 10:
                lists[j].append(m)

        print("k={}: {}".format(j, lists[j]))

k_almost_primes(200, 5)
# try:
#k_almost_primes(6000, 10)

```

