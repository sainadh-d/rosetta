# Greedy algorithm for Egyptian fractions

## Task Link
[Rosetta Code - Greedy algorithm for Egyptian fractions](https://rosettacode.org/wiki/Greedy_algorithm_for_Egyptian_fractions)

## Java Code
### java_code_1.txt
```java
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class EgyptianFractions {
    private static BigInteger gcd(BigInteger a, BigInteger b) {
        if (b.equals(BigInteger.ZERO)) {
            return a;
        }
        return gcd(b, a.mod(b));
    }

    private static class Frac implements Comparable<Frac> {
        private BigInteger num, denom;

        public Frac(BigInteger n, BigInteger d) {
            if (d.equals(BigInteger.ZERO)) {
                throw new IllegalArgumentException("Parameter d may not be zero.");
            }

            BigInteger nn = n;
            BigInteger dd = d;
            if (nn.equals(BigInteger.ZERO)) {
                dd = BigInteger.ONE;
            } else if (dd.compareTo(BigInteger.ZERO) < 0) {
                nn = nn.negate();
                dd = dd.negate();
            }
            BigInteger g = gcd(nn, dd).abs();
            if (g.compareTo(BigInteger.ZERO) > 0) {
                nn = nn.divide(g);
                dd = dd.divide(g);
            }
            num = nn;
            denom = dd;
        }

        public Frac(int n, int d) {
            this(BigInteger.valueOf(n), BigInteger.valueOf(d));
        }

        public Frac plus(Frac rhs) {
            return new Frac(
                num.multiply(rhs.denom).add(denom.multiply(rhs.num)),
                rhs.denom.multiply(denom)
            );
        }

        public Frac unaryMinus() {
            return new Frac(num.negate(), denom);
        }

        public Frac minus(Frac rhs) {
            return plus(rhs.unaryMinus());
        }

        @Override
        public int compareTo(Frac rhs) {
            BigDecimal diff = this.toBigDecimal().subtract(rhs.toBigDecimal());
            if (diff.compareTo(BigDecimal.ZERO) < 0) {
                return -1;
            }
            if (BigDecimal.ZERO.compareTo(diff) < 0) {
                return 1;
            }
            return 0;
        }

        @Override
        public boolean equals(Object obj) {
            if (null == obj || !(obj instanceof Frac)) {
                return false;
            }
            Frac rhs = (Frac) obj;
            return compareTo(rhs) == 0;
        }

        @Override
        public String toString() {
            if (denom.equals(BigInteger.ONE)) {
                return num.toString();
            }
            return String.format("%s/%s", num, denom);
        }

        public BigDecimal toBigDecimal() {
            BigDecimal bdn = new BigDecimal(num);
            BigDecimal bdd = new BigDecimal(denom);
            return bdn.divide(bdd, MathContext.DECIMAL128);
        }

        public List<Frac> toEgyptian() {
            if (num.equals(BigInteger.ZERO)) {
                return Collections.singletonList(this);
            }
            List<Frac> fracs = new ArrayList<>();
            if (num.abs().compareTo(denom.abs()) >= 0) {
                Frac div = new Frac(num.divide(denom), BigInteger.ONE);
                Frac rem = this.minus(div);
                fracs.add(div);
                toEgyptian(rem.num, rem.denom, fracs);
            } else {
                toEgyptian(num, denom, fracs);
            }
            return fracs;
        }

        public void toEgyptian(BigInteger n, BigInteger d, List<Frac> fracs) {
            if (n.equals(BigInteger.ZERO)) {
                return;
            }
            BigDecimal n2 = new BigDecimal(n);
            BigDecimal d2 = new BigDecimal(d);
            BigDecimal[] divRem = d2.divideAndRemainder(n2, MathContext.UNLIMITED);
            BigInteger div = divRem[0].toBigInteger();
            if (divRem[1].compareTo(BigDecimal.ZERO) > 0) {
                div = div.add(BigInteger.ONE);
            }
            fracs.add(new Frac(BigInteger.ONE, div));
            BigInteger n3 = d.negate().mod(n);
            if (n3.compareTo(BigInteger.ZERO) < 0) {
                n3 = n3.add(n);
            }
            BigInteger d3 = d.multiply(div);
            Frac f = new Frac(n3, d3);
            if (f.num.equals(BigInteger.ONE)) {
                fracs.add(f);
                return;
            }
            toEgyptian(f.num, f.denom, fracs);
        }
    }

    public static void main(String[] args) {
        List<Frac> fracs = List.of(
            new Frac(43, 48),
            new Frac(5, 121),
            new Frac(2014, 59)
        );
        for (Frac frac : fracs) {
            List<Frac> list = frac.toEgyptian();
            Frac first = list.get(0);
            if (first.denom.equals(BigInteger.ONE)) {
                System.out.printf("%s -> [%s] + ", frac, first);
            } else {
                System.out.printf("%s -> %s", frac, first);
            }
            for (int i = 1; i < list.size(); ++i) {
                System.out.printf(" + %s", list.get(i));
            }
            System.out.println();
        }

        for (Integer r : List.of(98, 998)) {
            if (r == 98) {
                System.out.println("\nFor proper fractions with 1 or 2 digits:");
            } else {
                System.out.println("\nFor proper fractions with 1, 2 or 3 digits:");
            }

            int maxSize = 0;
            List<Frac> maxSizeFracs = new ArrayList<>();
            BigInteger maxDen = BigInteger.ZERO;
            List<Frac> maxDenFracs = new ArrayList<>();
            boolean[][] sieve = new boolean[r + 1][];
            for (int i = 0; i < r + 1; ++i) {
                sieve[i] = new boolean[r + 2];
            }
            for (int i = 1; i < r; ++i) {
                for (int j = i + 1; j < r + 1; ++j) {
                    if (sieve[i][j]) continue;
                    Frac f = new Frac(i, j);
                    List<Frac> list = f.toEgyptian();
                    int listSize = list.size();
                    if (listSize > maxSize) {
                        maxSize = listSize;
                        maxSizeFracs.clear();
                        maxSizeFracs.add(f);
                    } else if (listSize == maxSize) {
                        maxSizeFracs.add(f);
                    }
                    BigInteger listDen = list.get(list.size() - 1).denom;
                    if (listDen.compareTo(maxDen) > 0) {
                        maxDen = listDen;
                        maxDenFracs.clear();
                        maxDenFracs.add(f);
                    } else if (listDen.equals(maxDen)) {
                        maxDenFracs.add(f);
                    }
                    if (i < r / 2) {
                        int k = 2;
                        while (true) {
                            if (j * k > r + 1) break;
                            sieve[i * k][j * k] = true;
                            k++;
                        }
                    }
                }
            }
            System.out.printf("  largest number of items = %s\n", maxSize);
            System.out.printf("fraction(s) with this number : %s\n", maxSizeFracs);
            String md = maxDen.toString();
            System.out.printf("  largest denominator = %s digits, ", md.length());
            System.out.printf("%s...%s\n", md.substring(0, 20), md.substring(md.length() - 20, md.length()));
            System.out.printf("fraction(s) with this denominator : %s\n", maxDenFracs);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from fractions import Fraction
from math import ceil

class Fr(Fraction):
    def __repr__(self):
        return '%s/%s' % (self.numerator, self.denominator)

def ef(fr):
    ans = []
    if fr >= 1:
        if fr.denominator == 1:
            return [[int(fr)], Fr(0, 1)]
        intfr = int(fr)
        ans, fr = [[intfr]], fr - intfr
    x, y = fr.numerator, fr.denominator
    while x != 1:
        ans.append(Fr(1, ceil(1/fr)))
        fr = Fr(-y % x, y* ceil(1/fr))
        x, y = fr.numerator, fr.denominator
    ans.append(fr)
    return ans

if __name__ == '__main__':
    for fr in [Fr(43, 48), Fr(5, 121), Fr(2014, 59)]:
        print('%r ─► %s' % (fr, ' '.join(str(x) for x in ef(fr))))
    lenmax = denommax = (0, None) 
    for fr in set(Fr(a, b) for a in range(1,100) for b in range(1, 100)):
        e = ef(fr)
        #assert sum((f[0] if type(f) is list else f) for f in e) == fr, 'Whoops!'
        elen, edenom = len(e), e[-1].denominator
        if elen > lenmax[0]:
            lenmax = (elen, fr, e)
        if edenom > denommax[0]:
            denommax = (edenom, fr, e)
    print('Term max is %r with %i terms' % (lenmax[1], lenmax[0]))
    dstr = str(denommax[0])
    print('Denominator max is %r with %i digits %s...%s' %
          (denommax[1], len(dstr), dstr[:5], dstr[-5:]))

```

### python_code_2.txt
```python
'''Egyptian fractions'''

from fractions import Fraction
from functools import reduce
from operator import neg


# eqyptianFraction :: Ratio Int -> Ratio Int
def eqyptianFraction(nd):
    '''The rational number nd as a sum
       of the series of unit fractions
       obtained by application of the
       greedy algorithm.'''
    def go(x):
        n, d = x.numerator, x.denominator
        r = 1 + d // n if n else None
        return Just((0, x) if 1 == n else (
            (fr(n % d, d), fr(n // d, 1)) if n > d else (
                fr(-d % n, d * r), fr(1, r)
            )
        )) if n else Nothing()
    fr = Fraction
    f = unfoldr(go)
    return list(map(neg, f(-nd))) if 0 > nd else f(nd)


# TESTS ---------------------------------------------------

# maxEqyptianFraction :: Int -> (Ratio Int -> a)
#                               -> (Ratio Int, a)
def maxEqyptianFraction(nDigits):
    '''An Egyptian Fraction, representing a
       proper fraction with numerators and
       denominators of up to n digits each,
       which returns a maximal value for the
       supplied function f.'''

    # maxVals :: ([Ratio Int], a) -> (Ratio Int, a)
    #                               -> ([Ratio Int], a)
    def maxima(xsv, ndfx):
        xs, v = xsv
        nd, fx = ndfx
        return ([nd], fx) if fx > v else (
            xs + [nd], v
        ) if fx == v and nd not in xs else xsv

    # go :: (Ratio Int -> a) -> ([Ratio Int], a)
    def go(f):
        iLast = int(nDigits * '9')
        fs, mx = reduce(
            maxima, [
                (nd, f(eqyptianFraction(nd))) for nd in [
                    Fraction(n, d)
                    for n in enumFromTo(1)(iLast)
                    for d in enumFromTo(1 + n)(iLast)
                ]
            ],
            ([], 0)
        )
        return f.__name__ + ' -> [' + ', '.join(
            map(str, fs)
        ) + '] -> ' + str(mx)
    return lambda f: go(f)


# main :: IO ()
def main():
    '''Tests'''

    ef = eqyptianFraction
    fr = Fraction

    print('Three values as Eqyptian fractions:')
    print('\n'.join([
        str(fr(*nd)) + ' -> ' + ' + '.join(map(str, ef(fr(*nd))))
        for nd in [(43, 48), (5, 121), (2014, 59)]
    ]))

    # maxDenominator :: [Ratio Int] -> Int
    def maxDenominator(ef):
        return max(map(lambda nd: nd.denominator, ef))

    # maxTermCount :: [Ratio Int] -> Int
    def maxTermCount(ef):
        return len(ef)

    for i in [1, 2, 3]:
        print(
            '\nMaxima for proper fractions with up to ' + (
                str(i) + ' digit(s):'
            )
        )
        for f in [maxTermCount, maxDenominator]:
            print(maxEqyptianFraction(i)(f))


# GENERIC -------------------------------------------------


# Just :: a -> Maybe a
def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.'''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}


# Nothing :: Maybe a
def Nothing():
    '''Constructor for an empty Maybe (option type) value.'''
    return {'type': 'Maybe', 'Nothing': True}


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# unfoldr :: (b -> Maybe (b, a)) -> b -> [a]
def unfoldr(f):
    '''Dual to reduce or foldr.
       Where catamorphism reduces a list to a summary value,
       the anamorphic unfoldr builds a list from a seed value.
       As long as f returns Just(a, b), a is prepended to the list,
       and the residual b is used as the argument for the next
       application of f.
       When f returns Nothing, the completed list is returned.'''
    def go(xr):
        mb = f(xr[0])
        if mb.get('Nothing'):
            return []
        else:
            y, r = mb.get('Just')
            return [r] + go((y, r))

    return lambda x: go((x, x))


# MAIN ---
if __name__ == '__main__':
    main()

```

