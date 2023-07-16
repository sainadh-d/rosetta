# Bernoulli numbers

## Task Link
[Rosetta Code - Bernoulli numbers](https://rosettacode.org/wiki/Bernoulli_numbers)

## Java Code
### java_code_1.txt
```java
import org.apache.commons.math3.fraction.BigFraction;

public class BernoulliNumbers {

    public static void main(String[] args) {
        for (int n = 0; n <= 60; n++) {
            BigFraction b = bernouilli(n);
            if (!b.equals(BigFraction.ZERO))
                System.out.printf("B(%-2d) = %-1s%n", n , b);
        }
    }

    static BigFraction bernouilli(int n) {
        BigFraction[] A = new BigFraction[n + 1];
        for (int m = 0; m <= n; m++) {
            A[m] = new BigFraction(1, (m + 1));
            for (int j = m; j >= 1; j--)
                A[j - 1] = (A[j - 1].subtract(A[j])).multiply(new BigFraction(j));
        }
        return A[0];
    }
}

```

## Python Code
### python_code_1.txt
```python
from fractions import Fraction as Fr

def bernoulli(n):
    A = [0] * (n+1)
    for m in range(n+1):
        A[m] = Fr(1, m+1)
        for j in range(m, 0, -1):
          A[j-1] = j*(A[j-1] - A[j])
    return A[0] # (which is Bn)

bn = [(i, bernoulli(i)) for i in range(61)]
bn = [(i, b) for i,b in bn if b]
width = max(len(str(b.numerator)) for i,b in bn)
for i,b in bn:
    print('B(%2i) = %*i/%i' % (i, width, b.numerator, b.denominator))

```

### python_code_2.txt
```python
def bernoulli2():
    A, m = [], 0
    while True:
        A.append(Fr(1, m+1))
        for j in range(m, 0, -1):
          A[j-1] = j*(A[j-1] - A[j])
        yield A[0] # (which is Bm)
        m += 1

bn2 = [ix for ix in zip(range(61), bernoulli2())]
bn2 = [(i, b) for i,b in bn2 if b]
width = max(len(str(b.numerator)) for i,b in bn2)
for i,b in bn2:
    print('B(%2i) = %*i/%i' % (i, width, b.numerator, b.denominator))

```

