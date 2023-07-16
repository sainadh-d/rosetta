# Eban numbers

## Task Link
[Rosetta Code - Eban numbers](https://rosettacode.org/wiki/Eban_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.List;

public class Main {
    private static class Range {
        int start;
        int end;
        boolean print;

        public Range(int s, int e, boolean p) {
            start = s;
            end = e;
            print = p;
        }
    }

    public static void main(String[] args) {
        List<Range> rgs = List.of(
            new Range(2, 1000, true),
            new Range(1000, 4000, true),
            new Range(2, 10_000, false),
            new Range(2, 100_000, false),
            new Range(2, 1_000_000, false),
            new Range(2, 10_000_000, false),
            new Range(2, 100_000_000, false),
            new Range(2, 1_000_000_000, false)
        );
        for (Range rg : rgs) {
            if (rg.start == 2) {
                System.out.printf("eban numbers up to and including %d\n", rg.end);
            } else {
                System.out.printf("eban numbers between %d and %d\n", rg.start, rg.end);
            }
            int count = 0;
            for (int i = rg.start; i <= rg.end; ++i) {
                int b = i / 1_000_000_000;
                int r = i % 1_000_000_000;
                int m = r / 1_000_000;
                r = i % 1_000_000;
                int t = r / 1_000;
                r %= 1_000;
                if (m >= 30 && m <= 66) m %= 10;
                if (t >= 30 && t <= 66) t %= 10;
                if (r >= 30 && r <= 66) r %= 10;
                if (b == 0 || b == 2 || b == 4 || b == 6) {
                    if (m == 0 || m == 2 || m == 4 || m == 6) {
                        if (t == 0 || t == 2 || t == 4 || t == 6) {
                            if (r == 0 || r == 2 || r == 4 || r == 6) {
                                if (rg.print) System.out.printf("%d ", i);
                                count++;
                            }
                        }
                    }
                }
            }
            if (rg.print) {
                System.out.println();
            }
            System.out.printf("count = %d\n\n", count);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
# Use inflect

"""

  show all eban numbers <= 1,000 (in a horizontal format), and a count
  show all eban numbers between 1,000 and 4,000 (inclusive), and a count
  show a count of all eban numbers up and including 10,000
  show a count of all eban numbers up and including 100,000
  show a count of all eban numbers up and including 1,000,000
  show a count of all eban numbers up and including 10,000,000
  
"""

import inflect
import time

before = time.perf_counter()

p = inflect.engine()

# eban numbers <= 1000

print(' ')
print('eban numbers up to and including 1000:')
print(' ')

count = 0

for i in range(1,1001):
    if not 'e' in p.number_to_words(i):
        print(str(i)+' ',end='')
        count += 1
        
print(' ')
print(' ')
print('count = '+str(count))
print(' ')

# eban numbers 1000 to 4000

print(' ')
print('eban numbers between 1000 and 4000 (inclusive):')
print(' ')

count = 0

for i in range(1000,4001):
    if not 'e' in p.number_to_words(i):
        print(str(i)+' ',end='')
        count += 1
        
print(' ')
print(' ')
print('count = '+str(count))
print(' ')

# eban numbers up to 10000

print(' ')
print('eban numbers up to and including 10000:')
print(' ')

count = 0

for i in range(1,10001):
    if not 'e' in p.number_to_words(i):
        count += 1
        
print(' ')
print('count = '+str(count))
print(' ')

# eban numbers up to 100000

print(' ')
print('eban numbers up to and including 100000:')
print(' ')

count = 0

for i in range(1,100001):
    if not 'e' in p.number_to_words(i):
        count += 1
        
print(' ')
print('count = '+str(count))
print(' ')

# eban numbers up to 1000000

print(' ')
print('eban numbers up to and including 1000000:')
print(' ')

count = 0

for i in range(1,1000001):
    if not 'e' in p.number_to_words(i):
        count += 1
        
print(' ')
print('count = '+str(count))
print(' ')

# eban numbers up to 10000000

print(' ')
print('eban numbers up to and including 10000000:')
print(' ')

count = 0

for i in range(1,10000001):
    if not 'e' in p.number_to_words(i):
        count += 1
        
print(' ')
print('count = '+str(count))
print(' ')

after = time.perf_counter()

print(" ")
print("Run time in seconds: "+str(after - before))

```

