# Narcissistic decimal number

## Task Link
[Rosetta Code - Narcissistic decimal number](https://rosettacode.org/wiki/Narcissistic_decimal_number)

## Java Code
### java_code_1.txt
```java
public class Narc{
	public static boolean isNarc(long x){
		if(x < 0) return false;
		
		String xStr = Long.toString(x);
		int m = xStr.length();
		long sum = 0;
		
		for(char c : xStr.toCharArray()){
			sum += Math.pow(Character.digit(c, 10), m);
		}
		return sum == x;
	}

	public static void main(String[] args){
		for(long x = 0, count = 0; count < 25; x++){
			if(isNarc(x)){
				System.out.print(x + " ");
				count++;
			}
		}
	}
}

```

### java_code_2.txt
```java
import java.util.stream.IntStream;
public class NarcissisticNumbers {
    static int numbersToCalculate = 25;
    static int numbersCalculated = 0;
    
    public static void main(String[] args) {
        IntStream.iterate(0, n -> n + 1).limit(Integer.MAX_VALUE).boxed().forEach(i -> {
            int length = i.toString().length();
            int addedDigits = 0;
            
            for (int count = 0; count < length; count++) {
                int value = Integer.parseInt(String.valueOf(i.toString().charAt(count)));
                addedDigits += Math.pow(value, length);
            }

            if (i == addedDigits) {
                numbersCalculated++;
                System.out.print(addedDigits + " ");
            }

            if (numbersCalculated == numbersToCalculate) {
                System.exit(0);
            }
        });
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function
from itertools import count, islice

def narcissists():
    for digits in count(0):
        digitpowers = [i**digits for i in range(10)]
        for n in range(int(10**(digits-1)), 10**digits):
            div, digitpsum = n, 0
            while div:
                div, mod = divmod(div, 10)
                digitpsum += digitpowers[mod]
            if n == digitpsum:
                yield n

for i, n in enumerate(islice(narcissists(), 25), 1):
    print(n, end=' ')
    if i % 5 == 0: print() 
print()

```

### python_code_2.txt
```python
try:
    import psyco
    psyco.full()
except:
    pass

class Narcissistics:
    def __init__(self, max_len):
        self.max_len = max_len
        self.power = [0] * 10
        self.dsum = [0] * (max_len + 1)
        self.count = [0] * 10
        self.len = 0
        self.ord0 = ord('0')

    def check_perm(self, out = [0] * 10):
        for i in xrange(10):
            out[i] = 0

        s = str(self.dsum[0])
        for d in s:
            c = ord(d) - self.ord0
            out[c] += 1
            if out[c] > self.count[c]:
                return

        if len(s) == self.len:
            print self.dsum[0],

    def narc2(self, pos, d):
        if not pos:
            self.check_perm()
            return

        while True:
            self.dsum[pos - 1] = self.dsum[pos] + self.power[d]
            self.count[d] += 1
            self.narc2(pos - 1, d)
            self.count[d] -= 1
            if d == 0:
                break
            d -= 1

    def show(self, n):
        self.len = n
        for i in xrange(len(self.power)):
            self.power[i] = i ** n
        self.dsum[n] = 0
        print "length %d:" % n,
        self.narc2(n, 9)
        print

def main():
    narc = Narcissistics(14)
    for i in xrange(1, narc.max_len + 1):
        narc.show(i)

main()

```

### python_code_3.txt
```python
'''Narcissistic decimal numbers'''

from itertools import chain
from functools import reduce


# main :: IO ()
def main():
    '''Narcissistic numbers of digit lengths 1 to 7'''
    print(
        fTable(main.__doc__ + ':\n')(str)(str)(
            narcissiOfLength
        )(enumFromTo(1)(7))
    )


# narcissiOfLength :: Int -> [Int]
def narcissiOfLength(n):
    '''List of Narcissistic numbers of
       (base 10) digit length n.
    '''
    return [
        x for x in digitPowerSums(n)
        if isDaffodil(n)(x)
    ]


# digitPowerSums :: Int -> [Int]
def digitPowerSums(e):
    '''The subset of integers of e digits that are potential narcissi.
       (Flattened leaves of a tree of unique digit combinations, in which
       order is not significant. The sum is independent of the sequence.)
    '''
    powers = [(x, x ** e) for x in enumFromTo(0)(9)]

    def go(n, parents):
        return go(
            n - 1,
            chain.from_iterable(map(
                lambda pDigitSum: (
                    map(
                        lambda lDigitSum: (
                            lDigitSum[0],
                            lDigitSum[1] + pDigitSum[1]
                        ),
                        powers[0: 1 + pDigitSum[0]]
                    )
                ),
                parents
            )) if parents else powers
        ) if 0 < n else parents

    return [xs for (_, xs) in go(e, [])]


# isDaffodil :: Int -> Int -> Bool
def isDaffodil(e):
    '''True if n is a narcissistic number
       of decimal digit length e.
    '''
    def go(n):
        ds = digitList(n)
        return e == len(ds) and n == powerSum(e)(ds)
    return lambda n: go(n)


# powerSum :: Int -> [Int] -> Int
def powerSum(e):
    '''The sum of a list obtained by raising
       each element of xs to the power of e.
    '''
    return lambda xs: reduce(
        lambda a, x: a + x ** e,
        xs, 0
    )


# -----------------------FORMATTING------------------------

# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
       f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# GENERIC -------------------------------------------------

# digitList :: Int -> [Int]
def digitList(n):
    '''A decomposition of n into a
       list of single-digit integers.
    '''
    def go(x):
        return go(x // 10) + [x % 10] if x else []
    return go(n) if n else [0]


# enumFromTo :: Int -> Int -> [Int]
def enumFromTo(m):
    '''Enumeration of integer values [m..n]'''
    def go(n):
        return list(range(m, 1 + n))
    return lambda n: go(n)


# MAIN ---
if __name__ == '__main__':
    main()

```

