# Digital root

## Task Link
[Rosetta Code - Digital root](https://rosettacode.org/wiki/Digital_root)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

class DigitalRoot
{
  public static int[] calcDigitalRoot(String number, int base)
  {
    BigInteger bi = new BigInteger(number, base);
    int additivePersistence = 0;
    if (bi.signum() < 0)
      bi = bi.negate();
    BigInteger biBase = BigInteger.valueOf(base);
    while (bi.compareTo(biBase) >= 0)
    {
      number = bi.toString(base);
      bi = BigInteger.ZERO;
      for (int i = 0; i < number.length(); i++)
        bi = bi.add(new BigInteger(number.substring(i, i + 1), base));
      additivePersistence++;
    }
    return new int[] { additivePersistence, bi.intValue() };
  }

  public static void main(String[] args)
  {
    for (String arg : args)
    {
      int[] results = calcDigitalRoot(arg, 10);
      System.out.println(arg + " has additive persistence " + results[0] + " and digital root of " + results[1]);
    }
  }
}

```

## Python Code
### python_code_1.txt
```python
def digital_root (n):
    ap = 0
    n = abs(int(n))
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
        ap += 1
    return ap, n

if __name__ == '__main__':
    for n in [627615, 39390, 588225, 393900588225, 55]:
        persistance, root = digital_root(n)
        print("%12i has additive persistance %2i and digital root %i." 
              % (n, persistance, root))

```

### python_code_2.txt
```python
from functools import (reduce)


# main :: IO ()
def main():
    print (
        tabulated(digitalRoot)(
            'Integer -> (additive persistence, digital root):'
        )([627615, 39390, 588225, 393900588225, 55])
    )


# digitalRoot :: Int -> (Int, Int)
def digitalRoot(n):
    '''Integer -> (additive persistence, digital root)'''

    # f :: (Int, Int) -> (Int, Int)
    def f(pn):
        p, n = pn
        return (
            1 + p,
            reduce(lambda a, x: a + int(x), str(n), 0)
        )

    # p :: (Int , Int) -> Bool
    def p(pn):
        return 10 > pn[1]

    return until(p)(f)(
        (0, abs(int(n)))
    )


# GENERIC -------------------------------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    return lambda f: lambda x: g(f(x))


# tabulated :: (a -> b) -> String -> String
def tabulated(f):
    '''function -> heading -> input List -> tabulated output string'''
    def go(s, xs):
        fw = compose(len)(str)
        w = fw(max(xs, key=fw))
        return s + '\n' + '\n'.join(list(map(
            lambda x: str(x).rjust(w, ' ') + ' -> ' + str(f(x)), xs
        )))
    return lambda s: lambda xs: go(s, xs)


# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v
    return lambda f: lambda x: go(f, x)


if __name__ == '__main__':
    main()

```

