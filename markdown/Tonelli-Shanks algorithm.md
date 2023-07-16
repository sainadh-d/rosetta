# Tonelli-Shanks algorithm

## Task Link
[Rosetta Code - Tonelli-Shanks algorithm](https://rosettacode.org/wiki/Tonelli-Shanks_algorithm)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.List;
import java.util.Map;
import java.util.function.BiFunction;
import java.util.function.Function;

public class TonelliShanks {
    private static final BigInteger ZERO = BigInteger.ZERO;
    private static final BigInteger ONE = BigInteger.ONE;
    private static final BigInteger TEN = BigInteger.TEN;
    private static final BigInteger TWO = BigInteger.valueOf(2);
    private static final BigInteger FOUR = BigInteger.valueOf(4);

    private static class Solution {
        private BigInteger root1;
        private BigInteger root2;
        private boolean exists;

        Solution(BigInteger root1, BigInteger root2, boolean exists) {
            this.root1 = root1;
            this.root2 = root2;
            this.exists = exists;
        }
    }

    private static Solution ts(Long n, Long p) {
        return ts(BigInteger.valueOf(n), BigInteger.valueOf(p));
    }

    private static Solution ts(BigInteger n, BigInteger p) {
        BiFunction<BigInteger, BigInteger, BigInteger> powModP = (BigInteger a, BigInteger e) -> a.modPow(e, p);
        Function<BigInteger, BigInteger> ls = (BigInteger a) -> powModP.apply(a, p.subtract(ONE).divide(TWO));

        if (!ls.apply(n).equals(ONE)) return new Solution(ZERO, ZERO, false);

        BigInteger q = p.subtract(ONE);
        BigInteger ss = ZERO;
        while (q.and(ONE).equals(ZERO)) {
            ss = ss.add(ONE);
            q = q.shiftRight(1);
        }

        if (ss.equals(ONE)) {
            BigInteger r1 = powModP.apply(n, p.add(ONE).divide(FOUR));
            return new Solution(r1, p.subtract(r1), true);
        }

        BigInteger z = TWO;
        while (!ls.apply(z).equals(p.subtract(ONE))) z = z.add(ONE);
        BigInteger c = powModP.apply(z, q);
        BigInteger r = powModP.apply(n, q.add(ONE).divide(TWO));
        BigInteger t = powModP.apply(n, q);
        BigInteger m = ss;

        while (true) {
            if (t.equals(ONE)) return new Solution(r, p.subtract(r), true);
            BigInteger i = ZERO;
            BigInteger zz = t;
            while (!zz.equals(BigInteger.ONE) && i.compareTo(m.subtract(ONE)) < 0) {
                zz = zz.multiply(zz).mod(p);
                i = i.add(ONE);
            }
            BigInteger b = c;
            BigInteger e = m.subtract(i).subtract(ONE);
            while (e.compareTo(ZERO) > 0) {
                b = b.multiply(b).mod(p);
                e = e.subtract(ONE);
            }
            r = r.multiply(b).mod(p);
            c = b.multiply(b).mod(p);
            t = t.multiply(c).mod(p);
            m = i;
        }
    }

    public static void main(String[] args) {
        List<Map.Entry<Long, Long>> pairs = List.of(
            Map.entry(10L, 13L),
            Map.entry(56L, 101L),
            Map.entry(1030L, 10009L),
            Map.entry(1032L, 10009L),
            Map.entry(44402L, 100049L),
            Map.entry(665820697L, 1000000009L),
            Map.entry(881398088036L, 1000000000039L)
        );

        for (Map.Entry<Long, Long> pair : pairs) {
            Solution sol = ts(pair.getKey(), pair.getValue());
            System.out.printf("n = %s\n", pair.getKey());
            System.out.printf("p = %s\n", pair.getValue());
            if (sol.exists) {
                System.out.printf("root1 = %s\n", sol.root1);
                System.out.printf("root2 = %s\n", sol.root2);
            } else {
                System.out.println("No solution exists");
            }
            System.out.println();
        }

        BigInteger bn = new BigInteger("41660815127637347468140745042827704103445750172002");
        BigInteger bp = TEN.pow(50).add(BigInteger.valueOf(577));
        Solution sol = ts(bn, bp);
        System.out.printf("n = %s\n", bn);
        System.out.printf("p = %s\n", bp);
        if (sol.exists) {
            System.out.printf("root1 = %s\n", sol.root1);
            System.out.printf("root2 = %s\n", sol.root2);
        } else {
            System.out.println("No solution exists");
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r

if __name__ == '__main__':
    ttest = [(10, 13), (56, 101), (1030, 10009), (44402, 100049),
	     (665820697, 1000000009), (881398088036, 1000000000039),
             (41660815127637347468140745042827704103445750172002, 10**50 + 577)]
    for n, p in ttest:
        r = tonelli(n, p)
        assert (r * r - n) % p == 0
        print("n = %d p = %d" % (n, p))
        print("\t  roots : %d %d" % (r, p - r))

```

