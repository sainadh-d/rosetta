# FizzBuzz

## Task Link
[Rosetta Code - FizzBuzz](https://rosettacode.org/wiki/FizzBuzz)

## Java Code
### java_code_2.txt
```java
public class FizzBuzz {
    public static void main(String[] args) {
        for (int number = 1; number <= 100; number++) {
            if (number % 15 == 0) {
                System.out.println("FizzBuzz");
            } else if (number % 3 == 0) {
                System.out.println("Fizz");
            } else if (number % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(number);
            }
        }
    }
}

```

### java_code_3.txt
```java
public class FizzBuzz {
    public static void main(String[] args) {
        int number = 1;
        while (number <= 100) {
            if (number % 15 == 0) {
                System.out.println("FizzBuzz");
            } else if (number % 3 == 0) {
                System.out.println("Fizz");
            } else if (number % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(number);
            }
            number++;
        }
    }
}

```

### java_code_4.txt
```java
public class FizzBuzz {
    public static void main(String[] args) {
        int number = 1;
        while (number <= 100) {
            System.out.println(number % 15 == 0 ? "FizzBuzz" : number % 3 == 0 ? "Fizz" : number % 5 == 0 ? "Buzz" : number);
            number++;
        }
    }
}

```

### java_code_5.txt
```java
import java.util.stream.IntStream;
class FizzBuzzJdk12 {
    public static void main(String[] args) {
        IntStream.range(1,101)
        .mapToObj(i->switch (i%15) {
            case 0 -> "FizzBuzz";
            case 3, 6, 9, 12 -> "Fizz";
            case 5, 10 -> "Buzz";
            default -> Integer.toString(i);
        })
        .forEach(System.out::println)
        ;
    }
}

```

### java_code_6.txt
```java
import java.util.stream.IntStream;

class FizzBuzzJdk12 {
    static final int FIZZ_FLAG = 0x8000_0000;
    static final int BUZZ_FLAG = 0x4000_0000;
    static final int FIZZ_BUZZ_FLAG = FIZZ_FLAG|BUZZ_FLAG;
    static final int[] FLAGS = new int[] {
        FIZZ_BUZZ_FLAG|0, 1, 2, FIZZ_FLAG|3, 4, 
        BUZZ_FLAG|5, FIZZ_FLAG|6, 7, 8, FIZZ_FLAG|9,
        BUZZ_FLAG|10, 11, FIZZ_FLAG|12, 13, 14
    };
    public static void main(String[] args) {
    IntStream.iterate(0,i->++i)
       .flatMap(i -> IntStream.range(0,15).map(j->FLAGS[j]+15*i))
       .mapToObj(
        // JDK12 switch expression ...
        n-> switch(n & FIZZ_BUZZ_FLAG) {
            case FIZZ_BUZZ_FLAG -> "fizzbuzz";
            case FIZZ_FLAG -> "fizz";
            case BUZZ_FLAG -> "buzz";
            default -> Integer.toString(~FIZZ_BUZZ_FLAG & n);
            }
       )
       .skip(1)
       .limit(100)
       .forEach(System.out::println)
       ;
    }
}

```

## Python Code
### python_code_1.txt
```python
for i in xrange(1, 101):
    if i % 15 == 0:
        print "FizzBuzz"
    elif i % 3 == 0:
        print "Fizz"
    elif i % 5 == 0:
        print "Buzz"
    else:
        print i

```

### python_code_10.txt
```python
'''Fizz buzz'''

from itertools import count, cycle, islice


# fizzBuzz :: () -> Generator [String]
def fizzBuzz():
    '''A non-finite stream of fizzbuzz terms.
    '''
    return map(
        lambda f, b, n: (f + b) or str(n),
        cycle([''] * 2 + ['Fizz']),
        cycle([''] * 4 + ['Buzz']),
        count(1)
    )


# ------------------------- TEST -------------------------
def main():
    '''Display of first 100 terms of the fizzbuzz series.
    '''
    print(
        '\n'.join(
            list(islice(
                fizzBuzz(),
                100
            ))
        )
    )


if __name__ == '__main__':
    main()

```

### python_code_11.txt
```python
print(*map(lambda n: 'Fizzbuzz '[(i):i+13] if (i := n**4%-15) > -14 else n, range(1,100)))

```

### python_code_12.txt
```python
def numsum(n):
	''' The recursive sum of all digits in a number 
        unit a single character is obtained'''
	res = sum([int(i) for i in str(n)])
	if res < 10: return res
	else : return numsum(res)
	
for n in range(1,101):
	response = 'Fizz'*(numsum(n) in [3,6,9]) + \
                   'Buzz'*(str(n)[-1] in ['5','0'])\
	            or n
	print(response)

```

### python_code_13.txt
```python
print(*((lambda x=x: ''.join(chr(c) for c in (102, 105)) + (2 * chr(122)) + ''.join(chr(c) for c in (98, 117)) + (2 * chr(122)) + '\n' if x % (30 >> 1) == 0 else ''.join(chr(c) for c in (102, 105)) + (2 * chr(122)) + '\n' if x % (6 >> 1) == 0 else ''.join(chr(c) for c in (98, 117)) + (2 * chr(122)) + '\n' if x % (10 >> 1) == 0 else str(x) + '\n')() for x in range(1, 101)))

```

### python_code_2.txt
```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

```

### python_code_3.txt
```python
for n in range(1,101):
    response = ''

    if not n%3:
        response += 'Fizz'
    if not n%5:
        response += 'Buzz'

    print(response or n)

```

### python_code_4.txt
```python
for i in range(1,101): print("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i)

```

### python_code_5.txt
```python
for i in range(100):print(i%3//2*'Fizz'+i%5//4*'Buzz'or i+1)

```

### python_code_6.txt
```python
for n in range(1, 100):
    fb = ''.join([ denom[1] if n % denom[0] == 0 else '' for denom in [(3,'fizz'),(5,'buzz')] ])
    print fb if fb else n

```

### python_code_7.txt
```python
print (', '.join([(x%3<1)*'Fizz'+(x%5<1)*'Buzz' or str(x) for x in range(1,101)]))

```

### python_code_8.txt
```python
[print("FizzBuzz") if i % 15 == 0 else print("Fizz") if i % 3 == 0 else print("Buzz") if i % 5 == 0 else print(i) for i in range(1,101)]

```

### python_code_9.txt
```python
from itertools import cycle, izip, count, islice

fizzes = cycle([""] * 2 + ["Fizz"])
buzzes = cycle([""] * 4 + ["Buzz"])
both = (f + b for f, b in izip(fizzes, buzzes))

# if the string is "", yield the number
# otherwise yield the string
fizzbuzz = (word or n for word, n in izip(both, count(1)))

# print the first 100
for i in islice(fizzbuzz, 100):
    print i

```

