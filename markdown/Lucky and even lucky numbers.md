# Lucky and even lucky numbers

## Task Link
[Rosetta Code - Lucky and even lucky numbers](https://rosettacode.org/wiki/Lucky_and_even_lucky_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class LuckyNumbers {

    private static int MAX = 200000;
    private static List<Integer> luckyEven = luckyNumbers(MAX, true);
    private static List<Integer> luckyOdd = luckyNumbers(MAX, false);
    
    public static void main(String[] args) {
        //  Case 1 and 2
        if ( args.length == 1 || ( args.length == 2 && args[1].compareTo("lucky") == 0 ) ) {
            int n = Integer.parseInt(args[0]);
            System.out.printf("LuckyNumber(%d) = %d%n", n, luckyOdd.get(n-1));
        }
        //  Case 3
        else if ( args.length == 2 && args[1].compareTo("evenLucky") == 0 ) {
            int n = Integer.parseInt(args[0]);
            System.out.printf("EvenLuckyNumber(%d) = %d%n", n, luckyEven.get(n-1));            
        }
        //  Case 4 through 9
        else if ( args.length == 2 || args.length == 3 ) {
            int j = Integer.parseInt(args[0]);
            int k = Integer.parseInt(args[1]);
            //  Case 4 and 5
            if ( ( args.length == 2 && k > 0 ) || (args.length == 3 && k > 0 && args[2].compareTo("lucky") == 0 ) ) {
                System.out.printf("LuckyNumber(%d) through LuckyNumber(%d) = %s%n", j, k, luckyOdd.subList(j-1, k));
            }
            //  Case 6
            else if ( args.length == 3 && k > 0 && args[2].compareTo("evenLucky") == 0 ) {
                System.out.printf("EvenLuckyNumber(%d) through EvenLuckyNumber(%d) = %s%n", j, k, luckyEven.subList(j-1, k));
            }
            //  Case 7 and 8
            else if ( ( args.length == 2 && k < 0 ) || (args.length == 3 && k < 0 && args[2].compareTo("lucky") == 0 ) ) {
                int n = Collections.binarySearch(luckyOdd, j);
                int m = Collections.binarySearch(luckyOdd, -k);
                System.out.printf("Lucky Numbers in the range %d to %d inclusive = %s%n", j, -k, luckyOdd.subList(n < 0 ? -n-1 : n, m < 0 ? -m-1 : m+1));
            }
            //  Case 9
            else if ( args.length == 3 && k < 0 && args[2].compareTo("evenLucky") == 0 ) {
                int n = Collections.binarySearch(luckyEven, j);
                int m = Collections.binarySearch(luckyEven, -k);
                System.out.printf("Even Lucky Numbers in the range %d to %d inclusive = %s%n", j, -k, luckyEven.subList(n < 0 ? -n-1 : n, m < 0 ? -m-1 : m+1));
            }
        }
    }
    
    private static List<Integer> luckyNumbers(int max, boolean even) {
        List<Integer> luckyList = new ArrayList<>();
        for ( int i = even ? 2 : 1 ; i <= max ; i += 2 ) {
            luckyList.add(i);
        }
        int start = 1;
        boolean removed = true;
        while ( removed ) {
            removed = false;
            int increment = luckyList.get(start);
            List<Integer> remove = new ArrayList<>();
            for ( int i = increment-1 ; i < luckyList.size() ; i += increment ) {
                remove.add(0, i);
                removed = true;
            }
            for ( int i : remove ) {
                luckyList.remove(i);
            }
            start++;
        }
        return luckyList;
    }

}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function

def lgen(even=False, nmax=1000000):
    start = 2 if even else 1
    n, lst = 1, list(range(start, nmax + 1, 2))
    lenlst = len(lst)
    yield lst[0]
    while n < lenlst and lst[n] < lenlst:
        yield lst[n]
        n, lst = n + 1, [j for i,j in enumerate(lst, 1) if i % lst[n]]
        lenlst = len(lst)
    # drain
    for i in lst[n:]:
        yield i

```

### python_code_2.txt
```python
from itertools import islice
import sys, re

class ArgumentError(Exception):
    pass
def arghandler(argstring):
    match_obj = re.match( r"""(?mx)
    (?:
      (?P<SINGLE>
         (?: ^ (?P<SINGLEL> \d+ ) (?:  | \s , \s lucky ) \s* $ )
        |(?: ^ (?P<SINGLEE> \d+ ) (?:  | \s , \s evenLucky ) \s* $ )
      )
     |(?P<KTH>
         (?: ^ (?P<KTHL> \d+ \s \d+ ) (?:  | \s lucky ) \s* $ )
        |(?: ^ (?P<KTHE> \d+ \s \d+ ) (?:  | \s evenLucky ) \s* $ )
      )
     |(?P<RANGE>
         (?: ^ (?P<RANGEL> \d+ \s -\d+ ) (?:  | \s lucky ) \s* $ )
        |(?: ^ (?P<RANGEE> \d+ \s -\d+ ) (?:  | \s evenLucky ) \s* $ )
      )
    )""", argstring)
    
    if match_obj:
        # Retrieve group(s) by name
        SINGLEL = match_obj.group('SINGLEL')
        SINGLEE = match_obj.group('SINGLEE')
        KTHL = match_obj.group('KTHL')
        KTHE = match_obj.group('KTHE')
        RANGEL = match_obj.group('RANGEL')
        RANGEE = match_obj.group('RANGEE')
        if SINGLEL: 
            j = int(SINGLEL)
            assert 0 < j < 10001, "Argument out of range"
            print("Single %i'th lucky number:" % j, end=' ')
            print( list(islice(lgen(), j-1, j))[0] )
        elif SINGLEE: 
            j = int(SINGLEE)
            assert 0 < j < 10001, "Argument out of range"
            print("Single %i'th even lucky number:" % j, end=' ')
            print( list(islice(lgen(even=True), j-1, j))[0] )
        elif KTHL: 
            j, k = [int(num) for num in KTHL.split()]
            assert 0 < j < 10001, "first argument out of range"
            assert 0 < k < 10001 and k > j, "second argument out of range"
            print("List of %i ... %i lucky numbers:" % (j, k), end=' ')
            for n, luck in enumerate(lgen(), 1):
                if n > k: break
                if n >=j: print(luck, end = ', ')
            print('')
        elif KTHE: 
            j, k = [int(num) for num in KTHE.split()]
            assert 0 < j < 10001, "first argument out of range"
            assert 0 < k < 10001 and k > j, "second argument out of range"
            print("List of %i ... %i even lucky numbers:" % (j, k), end=' ')
            for n, luck in enumerate(lgen(even=True), 1):
                if n > k: break
                if n >=j: print(luck, end = ', ')
            print('')
        elif RANGEL: 
            j, k = [int(num) for num in RANGEL.split()]
            assert 0 < j < 10001, "first argument out of range"
            assert 0 < -k < 10001 and -k > j, "second argument out of range"
            k = -k
            print("List of lucky numbers in the range %i ... %i :" % (j, k), end=' ')
            for n in lgen():
                if n > k: break
                if n >=j: print(n, end = ', ')
            print('')
        elif RANGEE: 
            j, k = [int(num) for num in RANGEE.split()]
            assert 0 < j < 10001, "first argument out of range"
            assert 0 < -k < 10001 and -k > j, "second argument out of range"
            k = -k
            print("List of even lucky numbers in the range %i ... %i :" % (j, k), end=' ')
            for n in lgen(even=True):
                if n > k: break
                if n >=j: print(n, end = ', ')
            print('')
    else:
        raise ArgumentError('''
        
  Error Parsing Arguments!
  
  Expected Arguments of the form (where j and k are integers):
      
      j                #  Jth       lucky number
      j  ,      lucky  #  Jth       lucky number
      j  ,  evenLucky  #  Jth  even lucky number
                       #
      j  k             #  Jth  through  Kth (inclusive)       lucky numbers
      j  k      lucky  #  Jth  through  Kth (inclusive)       lucky numbers
      j  k  evenLucky  #  Jth  through  Kth (inclusive)  even lucky numbers
                       #
      j -k             #  all       lucky numbers in the range  j --? |k|
      j -k      lucky  #  all       lucky numbers in the range  j --? |k|
      j -k  evenLucky  #  all  even lucky numbers in the range  j --? |k|
        ''')

if __name__ == '__main__':
    arghandler(' '.join(sys.argv[1:]))

```

### python_code_3.txt
```python
from itertools import count
def lgen(even=False):
    lucky = []
    if not even:
        yield 1
    for k in count(1):
        for l in reversed(lucky):
            k = (k*l)//(l-1)
        lucky.append(2*k+1 + even)
        yield 2*k+1 + even

```

