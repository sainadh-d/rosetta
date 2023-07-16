# Happy numbers

## Task Link
[Rosetta Code - Happy numbers](https://rosettacode.org/wiki/Happy_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.HashSet;
public class Happy{
   public static boolean happy(long number){
       long m = 0;
       int digit = 0;
       HashSet<Long> cycle = new HashSet<Long>();
       while(number != 1 && cycle.add(number)){
           m = 0;
           while(number > 0){
               digit = (int)(number % 10);
               m += digit*digit;
               number /= 10;
           }
           number = m;
       }
       return number == 1;
   }

   public static void main(String[] args){
       for(long num = 1,count = 0;count<8;num++){
           if(happy(num)){
               System.out.println(num);
               count++;
           }
       }
   }
}

```

### java_code_2.txt
```java
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class HappyNumbers {


    public static void main(String[] args) {

        for (int current = 1, total = 0; total < 8; current++)
            if (isHappy(current)) {
                System.out.println(current);
                total++;
            }
    }


    public static boolean isHappy(int number) {
        HashSet<Integer> cycle = new HashSet<>();
        while (number != 1 && cycle.add(number)) {
            List<String> numStrList = Arrays.asList(String.valueOf(number).split(""));
            number = numStrList.stream().map(i -> Math.pow(Integer.parseInt(i), 2)).mapToInt(i -> i.intValue()).sum();
        }
        return number == 1;
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def happy(n):
    past = set()			
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True

>>> [x for x in xrange(500) if happy(x)][:8]
[1, 7, 10, 13, 19, 23, 28, 31]

```

### python_code_2.txt
```python
'''Happy numbers'''

from itertools import islice


# main :: IO ()
def main():
    '''Test'''
    print(
        take(8)(
            happyNumbers()
        )
    )


# happyNumbers :: Gen [Int]
def happyNumbers():
    '''Generator :: non-finite stream of happy numbers.'''
    x = 1
    while True:
        x = until(isHappy)(succ)(x)
        yield x
        x = succ(x)


# isHappy :: Int -> Bool
def isHappy(n):
    '''Happy number sequence starting at n reaches 1 ?'''
    seen = set()

    # p :: Int -> Bool
    def p(x):
        if 1 == x or x in seen:
            return True
        else:
            seen.add(x)
            return False

    # f :: Int -> Int
    def f(x):
        return sum(int(d)**2 for d in str(x))

    return 1 == until(p)(f)(n)


# GENERIC -------------------------------------------------

# succ :: Int -> Int
def succ(x):
    '''The successor of an integer.'''
    return 1 + x


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.'''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(islice(xs, n))
    )


# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    '''The result of repeatedly applying f until p holds.
       The initial seed value is x.'''
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v
    return lambda f: lambda x: go(f, x)


if __name__ == '__main__':
    main()

```

