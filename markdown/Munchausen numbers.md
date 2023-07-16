# Munchausen numbers

## Task Link
[Rosetta Code - Munchausen numbers](https://rosettacode.org/wiki/Munchausen_numbers)

## Java Code
### java_code_1.txt
```java
public class Main {
    public static void main(String[] args) {
        for(int i = 0 ; i <= 5000 ; i++ ){
            int val = String.valueOf(i).chars().map(x -> (int) Math.pow( x-48 ,x-48)).sum();
            if( i == val){
                System.out.println( i + " (munchausen)");
            }
        }
    }
}

```

### java_code_2.txt
```java
public class Munchhausen {

    static final long[] cache = new long[10];

    public static void main(String[] args) {
        // Allowing 0 ^ 0 to be 0
        for (int i = 1; i < 10; i++) {
            cache[i] = (long) Math.pow(i, i);
        }
        for (long i = 0L; i <= 500_000_000L; i++) {
            if (isMunchhausen(i)) {
                System.out.println(i);
            }
        }
    }

    private static boolean isMunchhausen(long n) {
        long sum = 0, nn = n;
        do {
            sum += cache[(int)(nn % 10)];
            if (sum > n) {
                return false;
            }
            nn /= 10;
        } while (nn > 0);

        return sum == n;
    }
}

```

## Python Code
### python_code_1.txt
```python
for i in range(5000):
    if i == sum(int(x) ** int(x) for x in str(i)):
        print(i)

```

### python_code_2.txt
```python
'''Munchausen numbers'''

from functools import (reduce)


# isMunchausen :: Int -> Bool
def isMunchausen(n):
    '''True if n equals the sum of
       each of its digits raised to
       the power of itself.'''
    def powerOfSelf(d):
        i = digitToInt(d)
        return i**i
    return n == reduce(
        lambda n, c: n + powerOfSelf(c),
        str(n), 0
    )


# main :: IO ()
def main():
    '''Test'''
    print(list(filter(
        isMunchausen,
        enumFromTo(1)(5000)
    )))


# GENERIC -------------------------------------------------

# digitToInt :: Char -> Int
def digitToInt(c):
    '''The integer value of any digit character
       drawn from the 0-9, A-F or a-f ranges.'''
    oc = ord(c)
    if 48 > oc or 102 < oc:
        return None
    else:
        dec = oc - 48   # ord('0')
        hexu = oc - 65  # ord('A')
        hexl = oc - 97  # ord('a')
    return dec if 9 >= dec else (
        10 + hexu if 0 <= hexu <= 5 else (
            10 + hexl if 0 <= hexl <= 5 else None
        )
    )


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


if __name__ == '__main__':
    main()

```

