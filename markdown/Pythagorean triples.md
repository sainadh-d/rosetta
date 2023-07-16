# Pythagorean triples

## Task Link
[Rosetta Code - Pythagorean triples](https://rosettacode.org/wiki/Pythagorean_triples)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import static java.math.BigInteger.ONE;

public class PythTrip{

    public static void main(String[] args){
        long tripCount = 0, primCount = 0;

        //change this to whatever perimeter limit you want;the RAM's the limit
        BigInteger periLimit = BigInteger.valueOf(100),
                peri2 = periLimit.divide(BigInteger.valueOf(2)),
                peri3 = periLimit.divide(BigInteger.valueOf(3));

        for(BigInteger a = ONE; a.compareTo(peri3) < 0; a = a.add(ONE)){
            BigInteger aa = a.multiply(a);
            
            for(BigInteger b = a.add(ONE);
                    b.compareTo(peri2) < 0; b = b.add(ONE)){
                BigInteger bb = b.multiply(b);
                BigInteger ab = a.add(b);
                BigInteger aabb = aa.add(bb);
                
                for(BigInteger c = b.add(ONE);
                        c.compareTo(peri2) < 0; c = c.add(ONE)){

                    int compare = aabb.compareTo(c.multiply(c));
                    //if a+b+c > periLimit
                    if(ab.add(c).compareTo(periLimit) > 0){
                        break;
                    }
                    //if a^2 + b^2 != c^2
                    if(compare < 0){
                        break;
                    }else if (compare == 0){
                        tripCount++;
                        System.out.print(a + ", " + b + ", " + c);

                        //does binary GCD under the hood
                        if(a.gcd(b).equals(ONE)){
                            System.out.print(" primitive");
                            primCount++;
                        }
                        System.out.println();
                    }
                }
            }
        }
        System.out.println("Up to a perimeter of " + periLimit + ", there are "
                + tripCount + " triples, of which " + primCount + " are primitive.");
    }
}

```

### java_code_2.txt
```java
import java.math.BigInteger;

public class Triples{
    public static BigInteger LIMIT;
    public static final BigInteger TWO = BigInteger.valueOf(2);
    public static final BigInteger THREE = BigInteger.valueOf(3);
    public static final BigInteger FOUR = BigInteger.valueOf(4);
    public static final BigInteger FIVE = BigInteger.valueOf(5);
    public static long primCount = 0;
    public static long tripCount = 0;

    //I don't know Japanese :p
    public static void parChild(BigInteger a, BigInteger b, BigInteger c){
        BigInteger perim = a.add(b).add(c);
        if(perim.compareTo(LIMIT) > 0) return;
        primCount++; tripCount += LIMIT.divide(perim).longValue();
        BigInteger a2 = TWO.multiply(a), b2 = TWO.multiply(b), c2 = TWO.multiply(c),
                   c3 = THREE.multiply(c);
        parChild(a.subtract(b2).add(c2),
                 a2.subtract(b).add(c2),
                 a2.subtract(b2).add(c3));
        parChild(a.add(b2).add(c2),
                 a2.add(b).add(c2),
                 a2.add(b2).add(c3));
        parChild(a.negate().add(b2).add(c2),
                 a2.negate().add(b).add(c2),
                 a2.negate().add(b2).add(c3));
    }

    public static void main(String[] args){
        for(long i = 100; i <= 10000000; i*=10){
            LIMIT = BigInteger.valueOf(i);
            primCount = tripCount = 0;
            parChild(THREE, FOUR, FIVE);
            System.out.println(LIMIT + ": " + tripCount + " triples, " + primCount + " primitive.");
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from fractions import gcd


def pt1(maxperimeter=100):
    '''
# Naive method
    '''
    trips = []
    for a in range(1, maxperimeter):
        aa = a*a
        for b in range(a, maxperimeter-a+1):
            bb = b*b
            for c in range(b, maxperimeter-b-a+1):
                cc = c*c
                if a+b+c > maxperimeter or cc > aa + bb: break
                if aa + bb == cc:
                    trips.append((a,b,c, gcd(a, b) == 1))
    return trips

def pytrip(trip=(3,4,5),perim=100, prim=1):
    a0, b0, c0 = a, b, c = sorted(trip)
    t, firstprim = set(), prim>0
    while a + b + c <= perim:
        t.add((a, b, c, firstprim>0))
        a, b, c, firstprim = a+a0, b+b0, c+c0, False
    #
    t2 = set()
    for a, b, c, firstprim in t:
        a2, a5, b2, b5, c2, c3, c7 = a*2, a*5, b*2, b*5, c*2, c*3, c*7
        if  a5 - b5 + c7 <= perim:
            t2 |= pytrip(( a - b2 + c2,  a2 - b + c2,  a2 - b2 + c3), perim, firstprim)
        if  a5 + b5 + c7 <= perim:
            t2 |= pytrip(( a + b2 + c2,  a2 + b + c2,  a2 + b2 + c3), perim, firstprim)
        if -a5 + b5 + c7 <= perim:
            t2 |= pytrip((-a + b2 + c2, -a2 + b + c2, -a2 + b2 + c3), perim, firstprim)
    return t | t2

def pt2(maxperimeter=100):
    '''
# Parent/child relationship method:
# http://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#XI.
    '''
    trips = pytrip((3,4,5), maxperimeter, 1)
    return trips

def printit(maxperimeter=100, pt=pt1):
    trips = pt(maxperimeter)
    print("  Up to a perimeter of %i there are %i triples, of which %i are primitive"
          % (maxperimeter,
             len(trips),
             len([prim for a,b,c,prim in trips if prim])))
  
for algo, mn, mx in ((pt1, 250, 2500), (pt2, 500, 20000)):
    print(algo.__doc__)
    for maxperimeter in range(mn, mx+1, mn):
        printit(maxperimeter, algo)

```

### python_code_2.txt
```python
from sys import setrecursionlimit
setrecursionlimit(2000) # 2000 ought to be big enough for everybody

def triples(lim, a = 3, b = 4, c = 5):
    l = a + b + c
    if l > lim: return (0, 0)
    return reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), [
        (1, lim / l),
        triples(lim,  a - 2*b + 2*c,  2*a - b + 2*c,  2*a - 2*b + 3*c),
        triples(lim,  a + 2*b + 2*c,  2*a + b + 2*c,  2*a + 2*b + 3*c),
        triples(lim, -a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c) ])

for peri in [10 ** e for e in range(1, 8)]:
    print peri, triples(peri)

```

