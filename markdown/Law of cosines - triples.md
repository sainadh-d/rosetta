# Law of cosines - triples

## Task Link
[Rosetta Code - Law of cosines - triples](https://rosettacode.org/wiki/Law_of_cosines_-_triples)

## Java Code
### java_code_1.txt
```java
public class LawOfCosines {

    public static void main(String[] args) {
        generateTriples(13);
        generateTriples60(10000);
    }
    
    private static void generateTriples(int max) {
        for ( int coeff : new int[] {0, -1, 1} ) {
            int count = 0;
            System.out.printf("Max side length %d, formula:  a*a + b*b %s= c*c%n", max, coeff == 0 ? "" : (coeff<0 ? "-"  : "+") + " a*b ");
            for ( int a = 1 ; a <= max ; a++ ) {
                for ( int b = 1 ; b <= a ; b++ ) {
                    int val = a*a + b*b + coeff*a*b;
                    int c = (int) (Math.sqrt(val) + .5d);
                    if ( c > max ) {
                        break;
                    }
                    if ( c*c == val ) {
                        System.out.printf("  (%d, %d, %d)%n", a, b ,c);
                        count++;
                    }
                }
            }
            System.out.printf("%d triangles%n", count);
        }        
    }

    private static void generateTriples60(int max) {
        int count = 0;
        System.out.printf("%nExtra Credit.%nMax side length %d, sides different length, formula:  a*a + b*b - a*b = c*c%n", max);
        for ( int a = 1 ; a <= max ; a++ ) {
            for ( int b = 1 ; b < a ; b++ ) {
                int val = a*a + b*b - a*b;
                int c = (int) (Math.sqrt(val) + .5d);
                if ( c*c == val ) {
                    count++;
                }
            }
        }
        System.out.printf("%d triangles%n", count);
    }

}

```

## Python Code
### python_code_1.txt
```python
N = 13

def method1(N=N):
    squares = [x**2 for x in range(0, N+1)]
    sqrset = set(squares)
    tri90, tri60, tri120 = (set() for _ in range(3))
    for a in range(1, N+1):
        a2 = squares[a]
        for b in range(1, a + 1):
            b2 = squares[b]
            c2 = a2 + b2
            if c2 in sqrset:
                tri90.add(tuple(sorted((a, b, int(c2**0.5)))))
            ab = a * b
            c2 -= ab
            if c2 in sqrset:
                tri60.add(tuple(sorted((a, b, int(c2**0.5)))))
            c2 += 2 * ab
            if c2 in sqrset:
                tri120.add(tuple(sorted((a, b, int(c2**0.5)))))
    return  sorted(tri90), sorted(tri60), sorted(tri120)
#%%
if __name__ == '__main__':
    print(f'Integer triangular triples for sides 1..{N}:')
    for angle, triples in zip([90, 60, 120], method1(N)):
        print(f'  {angle:3}° has {len(triples)} solutions:\n    {triples}')
    _, t60, _ = method1(10_000)
    notsame = sum(1 for a, b, c in t60 if a != b or b != c)
    print('Extra credit:', notsame)

```

### python_code_2.txt
```python
from itertools import (starmap)


def f90(dct):
    return lambda x2, ab, a, b: dct.get(x2, None)


def f60(dct):
    return lambda x2, ab, a, b: dct.get(x2 - ab, None)


def f120(dct):
    return lambda x2, ab, a, b: dct.get(x2 + ab, None)


def f60unequal(dct):
    return lambda x2, ab, a, b: (
        dct.get(x2 - ab, None) if a != b else None
    )


# triangles :: Dict -> (Int -> Int -> Int -> Int -> Maybe Int)
#                   -> [String]
def triangles(f, n):
    upto = enumFromTo(1)
    xs = upto(n)
    dctSquares = dict(zip(xs, [x**2 for x in xs]))
    dctRoots = {v: k for k, v in dctSquares.items()}
    fr = f(dctRoots)
    dct = {}
    for a in xs:
        a2 = dctSquares[a]
        for b in upto(a):
            suma2b2 = a2 + dctSquares[b]
            c = fr(suma2b2, a * b, a, b)
            if (c is not None):
                dct[str(sorted([a, b, c]))] = 1
    return list(dct.keys())


def main():
    print(
        'Triangles of maximum side 13\n\n' +
        unlines(
            zipWith(
                lambda f, n: (
                    lambda ks=triangles(f, 13): (
                        str(len(ks)) + ' solutions for ' +
                        str(n) + ' degrees:\n' +
                        unlines(ks) + '\n'
                    )
                )()
            )([f120, f90, f60])
             ([120, 90, 60])
        ) + '\n\n' +
        '60 degrees - uneven triangles of maximum side 10000. Total:\n' +
        str(len(triangles(f60unequal, 10000)))
    )


# GENERIC --------------------------------------------------------------

# enumFromTo :: Int -> Int -> [Int]
def enumFromTo(m):
    return lambda n: list(range(m, 1 + n))


# unlines :: [String] -> String
def unlines(xs):
    return '\n'.join(xs)


# zipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
def zipWith(f):
    return lambda xs: lambda ys: (
        list(starmap(f, zip(xs, ys)))
    )


if __name__ == '__main__':
    main()

```

