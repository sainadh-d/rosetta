# Abundant odd numbers

## Task Link
[Rosetta Code - Abundant odd numbers](https://rosettacode.org/wiki/Abundant_odd_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public class AbundantOddNumbers {
    private static List<Integer> list = new ArrayList<>();
    private static List<Integer> result = new ArrayList<>();

    public static void main(String[] args) {
        System.out.println("First 25: ");
        abundantOdd(1,100000, 25, false);

        System.out.println("\n\nThousandth: ");
        abundantOdd(1,2500000, 1000, true);

        System.out.println("\n\nFirst over 1bn:"); 
        abundantOdd(1000000001, 2147483647, 1, false);
    }
    private static void abundantOdd(int start, int finish, int listSize, boolean printOne) {
        for (int oddNum = start; oddNum < finish; oddNum += 2) {
            list.clear();
            for (int toDivide = 1; toDivide < oddNum; toDivide+=2) {
                if (oddNum % toDivide == 0)
                    list.add(toDivide);
            }
            if (sumList(list) > oddNum) {
                if(!printOne)
                    System.out.printf("%5d <= %5d \n",oddNum, sumList(list) );
                result.add(oddNum);
            }
            if(printOne && result.size() >= listSize)
                System.out.printf("%5d <= %5d \n",oddNum, sumList(list) );

            if(result.size() >= listSize) break;
        }
    }
    private static int sumList(List list) {
        int sum = 0;
        for (int i = 0; i < list.size(); i++) {
            String temp = list.get(i).toString();
            sum += Integer.parseInt(temp);
        }
        return sum;
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/python
# Abundant odd numbers - Python

oddNumber  = 1
aCount  = 0
dSum  = 0
 
from math import sqrt
 
def divisorSum(n):
    sum = 1
    i = int(sqrt(n)+1)
 
    for d in range (2, i):
        if n % d == 0:
            sum += d
            otherD = n // d
            if otherD != d:
                sum += otherD
    return sum
 
print ("The first 25 abundant odd numbers:")
while aCount  < 25:
    dSum  = divisorSum(oddNumber )
    if dSum  > oddNumber :
        aCount  += 1
        print("{0:5} proper divisor sum: {1}". format(oddNumber ,dSum ))
    oddNumber  += 2
 
while aCount  < 1000:
    dSum  = divisorSum(oddNumber )
    if dSum  > oddNumber :
        aCount  += 1
    oddNumber  += 2
print ("\n1000th abundant odd number:")
print ("    ",(oddNumber - 2)," proper divisor sum: ",dSum)
 
oddNumber  = 1000000001
found  = False
while not found :
    dSum  = divisorSum(oddNumber )
    if dSum  > oddNumber :
        found  = True
        print ("\nFirst abundant odd number > 1 000 000 000:")
        print ("    ",oddNumber," proper divisor sum: ",dSum)
    oddNumber  += 2

```

### python_code_2.txt
```python
'''Odd abundant numbers'''

from math import sqrt
from itertools import chain, count, islice


# abundantTuple :: Int -> [(Int, Int)]
def abundantTuple(n):
    '''A list containing the tuple of N and its divisor
       sum, if n is abundant, or an empty list.
    '''
    x = divisorSum(n)
    return [(n, x)] if n < x else []


#  divisorSum :: Int -> Int
def divisorSum(n):
    '''Sum of the divisors of n.'''
    floatRoot = sqrt(n)
    intRoot = int(floatRoot)
    blnSquare = intRoot == floatRoot
    lows = [x for x in range(1, 1 + intRoot) if 0 == n % x]
    return sum(lows + [
        n // x for x in (
            lows[1:-1] if blnSquare else lows[1:]
        )
    ])


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Subsets of abundant odd numbers.'''

    # First 25.
    print('First 25 abundant odd numbers with their divisor sums:')
    for x in take(25)(
            concatMap(abundantTuple)(
                enumFromThen(1)(3)
            )
    ):
        print(x)

    # The 1000th.
    print('\n1000th odd abundant number with its divisor sum:')
    print(
        take(1000)(
            concatMap(abundantTuple)(
                enumFromThen(1)(3)
            )
        )[-1]
    )

    # First over 10^9.
    print('\nFirst odd abundant number over 10^9, with its divisor sum:')
    billion = (10 ** 9)
    print(
        take(1)(
            concatMap(abundantTuple)(
                enumFromThen(1 + billion)(3 + billion)
            )
        )[0]
    )


# GENERAL FUNCTIONS ---------------------------------------

# enumFromThen :: Int -> Int -> [Int]
def enumFromThen(m):
    '''A non-finite stream of integers
       starting at m, and continuing
       at the interval between m and n.
    '''
    return lambda n: count(m, n - m)


# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function f
       has been mapped.
       The list monad can be derived by using an (a -> [b])
       function which wraps its output in a list (using an
       empty list to represent computational failure).
    '''
    return lambda xs: (
        chain.from_iterable(map(f, xs))
    )


# take :: Int -> [a] -> [a]
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    return lambda xs: (
        list(islice(xs, n))
    )


if __name__ == '__main__':
    main()

```

