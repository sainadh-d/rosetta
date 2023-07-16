# Brazilian numbers

## Task Link
[Rosetta Code - Brazilian numbers](https://rosettacode.org/wiki/Brazilian_numbers)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.List;

public class Brazilian {
    private static final List<Integer> primeList = List.of(
        2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
        97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 169, 173, 179, 181,
        191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 247, 251, 257, 263, 269, 271, 277, 281,
        283, 293, 299, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 377, 379, 383, 389,
        397, 401, 403, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 481, 487, 491,
        499, 503, 509, 521, 523, 533, 541, 547, 557, 559, 563, 569, 571, 577, 587, 593, 599, 601, 607,
        611, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 689, 691, 701, 709, 719,
        727, 733, 739, 743, 751, 757, 761, 767, 769, 773, 787, 793, 797, 809, 811, 821, 823, 827, 829,
        839, 853, 857, 859, 863, 871, 877, 881, 883, 887, 907, 911, 919, 923, 929, 937, 941, 947, 949,
        953, 967, 971, 977, 983, 991, 997
    );

    public static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }

        for (Integer prime : primeList) {
            if (n == prime) {
                return true;
            }
            if (n % prime == 0) {
                return false;
            }
            if (prime * prime > n) {
                return true;
            }
        }

        BigInteger bi = BigInteger.valueOf(n);
        return bi.isProbablePrime(10);
    }

    private static boolean sameDigits(int n, int b) {
        int f = n % b;
        while ((n /= b) > 0) {
            if (n % b != f) {
                return false;
            }
        }
        return true;
    }

    private static boolean isBrazilian(int n) {
        if (n < 7) return false;
        if (n % 2 == 0) return true;
        for (int b = 2; b < n - 1; ++b) {
            if (sameDigits(n, b)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        for (String kind : List.of("", "odd ", "prime ")) {
            boolean quiet = false;
            int bigLim = 99_999;
            int limit = 20;
            System.out.printf("First %d %sBrazilian numbers:\n", limit, kind);
            int c = 0;
            int n = 7;
            while (c < bigLim) {
                if (isBrazilian(n)) {
                    if (!quiet) System.out.printf("%d ", n);
                    if (++c == limit) {
                        System.out.println("\n");
                        quiet = true;
                    }
                }
                if (quiet && !"".equals(kind)) continue;
                switch (kind) {
                    case "":
                        n++;
                        break;
                    case "odd ":
                        n += 2;
                        break;
                    case "prime ":
                        do {
                            n += 2;
                        } while (!isPrime(n));
                        break;
                    default:
                        throw new AssertionError("Oops");
                }
            }
            if ("".equals(kind)) {
                System.out.printf("The %dth Brazilian number is: %d\n\n", bigLim + 1, n);
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
'''Brazilian numbers'''

from itertools import count, islice


# isBrazil :: Int -> Bool
def isBrazil(n):
    '''True if n is a Brazilian number,
       in the sense of OEIS:A125134.
    '''
    return 7 <= n and (
        0 == n % 2 or any(
            map(monoDigit(n), range(2, n - 1))
        )
    )


# monoDigit :: Int -> Int -> Bool
def monoDigit(n):
    '''True if all the digits of n,
       in the given base, are the same.
    '''
    def go(base):
        def g(b, n):
            (q, d) = divmod(n, b)

            def p(qr):
                return d != qr[1] or 0 == qr[0]

            def f(qr):
                return divmod(qr[0], b)
            return d == until(p)(f)(
                (q, d)
            )[1]
        return g(base, n)
    return go


# -------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''First 20 members each of:
        OEIS:A125134
        OEIS:A257521
        OEIS:A085104
    '''
    for kxs in ([
            (' ', count(1)),
            (' odd ', count(1, 2)),
            (' prime ', primes())
    ]):
        print(
            'First 20' + kxs[0] + 'Brazilians:\n' +
            showList(take(20)(filter(isBrazil, kxs[1]))) + '\n'
        )


# ------------------- GENERIC FUNCTIONS --------------------

# primes :: [Int]
def primes():
    ''' Non finite sequence of prime numbers.
    '''
    n = 2
    dct = {}
    while True:
        if n in dct:
            for p in dct[n]:
                dct.setdefault(n + p, []).append(p)
            del dct[n]
        else:
            yield n
            dct[n * n] = [n]
        n = 1 + n


# showList :: [a] -> String
def showList(xs):
    '''Stringification of a list.'''
    return '[' + ','.join(str(x) for x in xs) + ']'


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    def go(xs):
        return (
            xs[0:n]
            if isinstance(xs, (list, tuple))
            else list(islice(xs, n))
        )
    return go


# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    '''The result of repeatedly applying f until p holds.
       The initial seed value is x.
    '''
    def go(f):
        def g(x):
            v = x
            while not p(v):
                v = f(v)
            return v
        return g
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

