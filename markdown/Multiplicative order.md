# Multiplicative order

## Task Link
[Rosetta Code - Multiplicative order](https://rosettacode.org/wiki/Multiplicative_order)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class MultiplicativeOrder {
    private static final BigInteger ONE = BigInteger.ONE;
    private static final BigInteger TWO = BigInteger.valueOf(2);
    private static final BigInteger THREE = BigInteger.valueOf(3);
    private static final BigInteger TEN = BigInteger.TEN;

    private static class PExp {
        BigInteger prime;
        long exp;

        PExp(BigInteger prime, long exp) {
            this.prime = prime;
            this.exp = exp;
        }
    }

    private static void moTest(BigInteger a, BigInteger n) {
        if (!n.isProbablePrime(20)) {
            System.out.println("Not computed. Modulus must be prime for this algorithm.");
            return;
        }
        if (a.bitLength() < 100) System.out.printf("ord(%s)", a);
        else System.out.print("ord([big])");
        if (n.bitLength() < 100) System.out.printf(" mod %s ", n);
        else System.out.print(" mod [big] ");
        BigInteger mob = moBachShallit58(a, n, factor(n.subtract(ONE)));
        System.out.println("= " + mob);
    }

    private static BigInteger moBachShallit58(BigInteger a, BigInteger n, List<PExp> pf) {
        BigInteger n1 = n.subtract(ONE);
        BigInteger mo = ONE;
        for (PExp pe : pf) {
            BigInteger y = n1.divide(pe.prime.pow((int) pe.exp));
            long o = 0;
            BigInteger x = a.modPow(y, n.abs());
            while (x.compareTo(ONE) > 0) {
                x = x.modPow(pe.prime, n.abs());
                o++;
            }
            BigInteger o1 = BigInteger.valueOf(o);
            o1 = pe.prime.pow(o1.intValue());
            o1 = o1.divide(mo.gcd(o1));
            mo = mo.multiply(o1);
        }
        return mo;
    }

    private static List<PExp> factor(BigInteger n) {
        List<PExp> pf = new ArrayList<>();
        BigInteger nn = n;
        Long e = 0L;
        while (!nn.testBit(e.intValue())) e++;
        if (e > 0L) {
            nn = nn.shiftRight(e.intValue());
            pf.add(new PExp(TWO, e));
        }
        BigInteger s = sqrt(nn);
        BigInteger d = THREE;
        while (nn.compareTo(ONE) > 0) {
            if (d.compareTo(s) > 0) d = nn;
            e = 0L;
            while (true) {
                BigInteger[] qr = nn.divideAndRemainder(d);
                if (qr[1].bitLength() > 0) break;
                nn = qr[0];
                e++;
            }
            if (e > 0L) {
                pf.add(new PExp(d, e));
                s = sqrt(nn);
            }
            d = d.add(TWO);
        }
        return pf;
    }

    private static BigInteger sqrt(BigInteger n) {
        BigInteger b = n;
        while (true) {
            BigInteger a = b;
            b = n.divide(a).add(a).shiftRight(1);
            if (b.compareTo(a) >= 0) return a;
        }
    }

    public static void main(String[] args) {
        moTest(BigInteger.valueOf(37), BigInteger.valueOf(3343));

        BigInteger b = TEN.pow(100).add(ONE);
        moTest(b, BigInteger.valueOf(7919));

        b = TEN.pow(1000).add(ONE);
        moTest(b, BigInteger.valueOf(15485863));

        b = TEN.pow(10000).subtract(ONE);
        moTest(b, BigInteger.valueOf(22801763489L));

        moTest(BigInteger.valueOf(1511678068), BigInteger.valueOf(7379191741L));
        moTest(BigInteger.valueOf(3047753288L), BigInteger.valueOf(2257683301L));
    }
}

```

## Python Code
### python_code_1.txt
```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
 
def lcm(a, b):
    return (a*b) / gcd(a, b)
 
def isPrime(p):
    return (p > 1) and all(f == p for f,e in factored(p))

primeList = [2,3,5,7]
def primes():
    for p in primeList:
        yield p
    while 1:
        p += 2
        while not isPrime(p):
            p += 2
        primeList.append(p)
        yield p

def factored( a):
    for p in primes():
        j = 0
        while a%p == 0:
            a /= p
            j += 1
        if j > 0:
            yield (p,j)
        if a < p*p: break
    if a > 1:
        yield (a,1)
        

def multOrdr1(a,(p,e) ):
    m = p**e
    t = (p-1)*(p**(e-1)) #  = Phi(p**e) where p prime
    qs = [1,]
    for f in factored(t):
        qs = [ q * f[0]**j for j in range(1+f[1]) for q in qs ]
    qs.sort()

    for q in qs:
        if pow( a, q, m )==1: break
    return q

     
def multOrder(a,m):
    assert gcd(a,m) == 1
    mofs = (multOrdr1(a,r) for r in factored(m))
    return reduce(lcm, mofs, 1)


if __name__ == "__main__":
    print multOrder(37, 1000)        # 100
    b = 10**20-1
    print multOrder(2, b) # 3748806900
    print multOrder(17,b) # 1499522760
    b = 100001
    print multOrder(54,b)
    print pow( 54, multOrder(54,b),b)
    if any( (1==pow(54,r, b)) for r in range(1,multOrder(54,b))):
        print 'Exists a power r < 9090 where pow(54,r,b)==1'
    else:
        print 'Everything checks.'

```

