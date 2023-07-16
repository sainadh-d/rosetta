# AKS test for primes

## Task Link
[Rosetta Code - AKS test for primes](https://rosettacode.org/wiki/AKS_test_for_primes)

## Java Code
### java_code_1.txt
```java
public class AksTest {
    private static final long[] c = new long[64];

    public static void main(String[] args) {
        for (int n = 0; n < 10; n++) {
            coeff(n);
            show(n);
        }

        System.out.print("Primes:");
        for (int n = 1; n < c.length; n++)
            if (isPrime(n))
                System.out.printf(" %d", n);

        System.out.println();
    }

    static void coeff(int n) {
        c[0] = 1;
        for (int i = 0; i < n; c[0] = -c[0], i++) {
            c[1 + i] = 1;
            for (int j = i; j > 0; j--)
                c[j] = c[j - 1] - c[j];
        }
    }

    static boolean isPrime(int n) {
        coeff(n);
        c[0]++;
        c[n]--;

        int i = n;
        while (i-- != 0 && c[i] % n == 0)
            continue;
        return i < 0;
    }

    static void show(int n) {
        System.out.print("(x-1)^" + n + " =");
        for (int i = n; i >= 0; i--) {
            System.out.print(" + " + c[i] + "x^" + i);
        }
        System.out.println();
    }
}

```

## Python Code
### python_code_1.txt
```python
def expand_x_1(n): 
# This version uses a generator and thus less computations
    c =1
    for i in range(n//2+1):
        c = c*(n-i)//(i+1)
        yield c
        
def aks(p):
    if p==2:
        return True

    for i in expand_x_1(p):
        if i % p:
# we stop without computing all possible solutions
            return False
    return True

```

### python_code_2.txt
```python
def aks(p):
    if p==2:return True
    c=1
    for i in range(p//2+1):
        c=c*(p-i)//(i+1)
        if c%p:return False
    return True

```

### python_code_3.txt
```python
def expand_x_1(p):
    ex = [1]
    for i in range(p):
        ex.append(ex[-1] * -(p-i) / (i+1))
    return ex[::-1]

def aks_test(p):
    if p < 2: return False
    ex = expand_x_1(p)
    ex[0] += 1
    return not any(mult % p for mult in ex[0:-1])
    
    
print('# p: (x-1)^p for small p')
for p in range(12):
    print('%3i: %s' % (p, ' '.join('%+i%s' % (e, ('x^%i' % n) if n else '')
                                   for n,e in enumerate(expand_x_1(p)))))

print('\n# small primes using the aks test')
print([p for p in range(101) if aks_test(p)])

```

### python_code_4.txt
```python
print('''
{| class="wikitable" style="text-align:left;"
|+ Polynomial Expansions and AKS prime test
|-
! <math>p</math>
! <math>(x-1)^p</math>
|-''')
for p in range(12):
    print('! <math>%i</math>\n| <math>%s</math>\n| %r\n|-'
          % (p,
             ' '.join('%s%s' % (('%+i' % e) if (e != 1 or not p or (p and not n) ) else '+',
                                (('x^{%i}' % n) if n > 1 else 'x') if n else '')
                      for n,e in enumerate(expand_x_1(p))),
             aks_test(p)))
print('|}')

```

