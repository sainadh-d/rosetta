# Pi

## Task Link
[Rosetta Code - Pi](https://rosettacode.org/wiki/Pi)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger ;

public class Pi {
  final BigInteger TWO = BigInteger.valueOf(2) ;
  final BigInteger THREE = BigInteger.valueOf(3) ;
  final BigInteger FOUR = BigInteger.valueOf(4) ;
  final BigInteger SEVEN = BigInteger.valueOf(7) ;

  BigInteger q = BigInteger.ONE ;
  BigInteger r = BigInteger.ZERO ;
  BigInteger t = BigInteger.ONE ;
  BigInteger k = BigInteger.ONE ;
  BigInteger n = BigInteger.valueOf(3) ;
  BigInteger l = BigInteger.valueOf(3) ;

  public void calcPiDigits(){
    BigInteger nn, nr ;
    boolean first = true ;
    while(true){
        if(FOUR.multiply(q).add(r).subtract(t).compareTo(n.multiply(t)) == -1){
          System.out.print(n) ;
          if(first){System.out.print(".") ; first = false ;}
          nr = BigInteger.TEN.multiply(r.subtract(n.multiply(t))) ;
          n = BigInteger.TEN.multiply(THREE.multiply(q).add(r)).divide(t).subtract(BigInteger.TEN.multiply(n)) ;
          q = q.multiply(BigInteger.TEN) ;
          r = nr ;
          System.out.flush() ;
        }else{
          nr = TWO.multiply(q).add(r).multiply(l) ;
          nn = q.multiply((SEVEN.multiply(k))).add(TWO).add(r.multiply(l)).divide(t.multiply(l)) ;
          q = q.multiply(k) ;
          t = t.multiply(l) ;
          l = l.add(TWO) ;
          k = k.add(BigInteger.ONE) ;
          n = nn ;
          r = nr ;
        }
    }
  }

  public static void main(String[] args) {
    Pi p = new Pi() ;
    p.calcPiDigits() ;
  }
}

```

## Python Code
### python_code_1.txt
```python
def calcPi():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4*q+r-t < n*t:
            yield n
            nr = 10*(r-n*t)
            n  = ((10*(3*q+r))//t)-10*n
            q  *= 10
            r  = nr
        else:
            nr = (2*q+r)*l
            nn = (q*(7*k)+2+(r*l))//(t*l)
            q  *= k
            t  *= l
            l  += 2
            k += 1
            n  = nn
            r  = nr

import sys
pi_digits = calcPi()
i = 0
for d in pi_digits:
    sys.stdout.write(str(d))
    i += 1
    if i == 40: print(""); i = 0

```

