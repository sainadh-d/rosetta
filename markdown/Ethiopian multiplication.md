# Ethiopian multiplication

## Task Link
[Rosetta Code - Ethiopian multiplication](https://rosettacode.org/wiki/Ethiopian_multiplication)

## Java Code
### java_code_1.txt
```java
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
public class Mult{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int first = sc.nextInt();
    int second = sc.nextInt();

    if(first < 0){
        first = -first;
        second = -second;
    }

    Map<Integer, Integer> columns = new HashMap<Integer, Integer>();
        columns.put(first, second);
    int sum = isEven(first)? 0 : second;
    do{
      first = halveInt(first);
      second = doubleInt(second);
      columns.put(first, second);
      if(!isEven(first)){
          sum += second;
      }
    }while(first > 1);
 
    System.out.println(sum);
  }

  public static int doubleInt(int doubleMe){
    return doubleMe << 1; //shift left
  }

  public static int halveInt(int halveMe){
    return halveMe >>> 1; //shift right
  }

  public static boolean isEven(int num){
    return (num & 1) == 0;
  }
}

```

### java_code_2.txt
```java
/**
 * This method will use ethiopian styled multiplication.
 * @param a Any non-negative integer.
 * @param b Any integer.
 * @result a multiplied by b
 */
public static int ethiopianMultiply(int a, int b) {
  if(a==0 || b==0) {
    return 0;
  }
  int result = 0;
  while(a>=1) {
    if(!isEven(a)) {
      result+=b;
    }
    b = doubleInt(b);
    a = halveInt(a);
  }
  return result;
}

/**
 * This method is an improved version that will use
 * ethiopian styled multiplication, and also
 * supports negative parameters.
 * @param a Any integer.
 * @param b Any integer.
 * @result a multiplied by b
 */
public static int ethiopianMultiplyWithImprovement(int a, int b) {
  if(a==0 || b==0) {
    return 0;
  }
  if(a<0) {
    a=-a;
    b=-b;
  } else if(b>0 && a>b) {
    int tmp = a;
    a = b;
    b = tmp;
  }
  int result = 0;
  while(a>=1) {
    if(!isEven(a)) {
      result+=b;
    }
    b = doubleInt(b);
    a = halveInt(a);
  }
  return result;
}

```

## Python Code
### python_code_1.txt
```python
tutor = True

def halve(x):
    return x // 2

def double(x):
    return x * 2

def even(x):
    return not x % 2

def ethiopian(multiplier, multiplicand):
    if tutor:
        print("Ethiopian multiplication of %i and %i" %
              (multiplier, multiplicand))
    result = 0
    while multiplier >= 1:
        if even(multiplier):
            if tutor:
                print("%4i %6i STRUCK" %
                      (multiplier, multiplicand))
        else:
            if tutor:
                print("%4i %6i KEPT" %
                      (multiplier, multiplicand))
            result += multiplicand
        multiplier   = halve(multiplier)
        multiplicand = double(multiplicand)
    if tutor:
        print()
    return result

```

### python_code_2.txt
```python
halve  = lambda x: x // 2
double = lambda x: x*2
even   = lambda x: not x % 2
 
def ethiopian(multiplier, multiplicand):
    result = 0

    while multiplier >= 1:
        if not even(multiplier):
            result += multiplicand
        multiplier   = halve(multiplier)
        multiplicand = double(multiplicand)

    return result

```

### python_code_3.txt
```python
tutor = True

from itertools import izip, takewhile

def iterate(function, arg):
    while 1:
        yield arg
        arg = function(arg)

def halve(x): return x // 2
def double(x): return x * 2
def even(x): return x % 2 == 0

def show_heading(multiplier, multiplicand):
    print "Multiplying %d by %d" % (multiplier, multiplicand),
    print "using Ethiopian multiplication:"
    print

TABLE_FORMAT = "%8s %8s %8s %8s %8s"

def show_table(table):
    for p, q in table:
        print TABLE_FORMAT % (p, q, "->",
                              p, q if not even(p) else "-" * len(str(q)))

def show_result(result):
    print TABLE_FORMAT % ('', '', '', '', "=" * (len(str(result)) + 1))
    print TABLE_FORMAT % ('', '', '', '', result)

def ethiopian(multiplier, multiplicand):
    def column1(x): return takewhile(lambda v: v >= 1, iterate(halve, x))
    def column2(x): return iterate(double, x)
    def rows(x, y): return izip(column1(x), column2(y))
    table = rows(multiplier, multiplicand)
    if tutor: 
        table = list(table)
        show_heading(multiplier, multiplicand)
        show_table(table)
    result = sum(q for p, q in table if not even(p))
    if tutor: 
        show_result(result)
    return result

```

### python_code_4.txt
```python
'''Ethiopian multiplication'''

from functools import reduce


# ethMult :: Int -> Int -> Int
def ethMult(n):
    '''Ethiopian multiplication of n by m.'''

    def doubled(x):
        return x + x

    def halved(h):
        qr = divmod(h, 2)
        if 0 < h:
            print('halve:', str(qr).rjust(8, ' '))
        return qr if 0 < h else None

    def addedWhereOdd(a, remx):
        odd, x = remx
        if odd:
            print(
                str(a).rjust(2, ' '), '+',
                str(x).rjust(3, ' '), '->',
                str(a + x).rjust(3, ' ')
            )
            return a + x
        else:
            print(str(x).rjust(8, ' '))
            return a

    return lambda m: reduce(
        addedWhereOdd,
        zip(
            unfoldr(halved)(n),
            iterate(doubled)(m)
        ),
        0
    )


# ------------------------- TEST -------------------------
def main():
    '''Tests of multiplication.'''

    print(
        '\nProduct:    ' + str(
            ethMult(17)(34)
        ),
        '\n_______________\n'
    )
    print(
        '\nProduct:    ' + str(
            ethMult(34)(17)
        )
    )


# ----------------------- GENERIC ------------------------

# iterate :: (a -> a) -> a -> Gen [a]
def iterate(f):
    '''An infinite list of repeated
       applications of f to x.
    '''
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return go


# showLog :: a -> IO String
def showLog(*s):
    '''Arguments printed with
       intercalated arrows.'''
    print(
        ' -> '.join(map(str, s))
    )


# unfoldr :: (b -> Maybe (a, b)) -> b -> [a]
def unfoldr(f):
    '''Dual to reduce or foldr.
       Where catamorphism reduces a list to a summary value,
       the anamorphic unfoldr builds a list from a seed value.
       As long as f returns Just(a, b), a is prepended to the list,
       and the residual b is used as the argument for the next
       application of f.
       When f returns Nothing, the completed list is returned.'''
    def go(v):
        xr = v, v
        xs = []
        while True:
            xr = f(xr[0])
            if xr:
                xs.append(xr[1])
            else:
                return xs
        return xs
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

