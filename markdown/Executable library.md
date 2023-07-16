# Executable library

## Task Link
[Rosetta Code - Executable library](https://rosettacode.org/wiki/Executable_library)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

//  task 1
public class HailstoneSequence {

    public static void main(String[] args) {
        //  task 2
        int n = 27;
        List<Long> sequence27 = hailstoneSequence(n);
        System.out.printf("Hailstone sequence for %d has a length of %d:%nhailstone(%d) = %s%n", n, sequence27.size(), n, sequence27);
        
        //  task 3
        int maxN = 0;
        int maxLength = 0;
        for ( int i = 1 ; i < 100_000 ; i++ ) {
            int seqLength = hailstoneSequence(i).size();
            if ( seqLength > maxLength ) {
                maxLength = seqLength;
                maxN = i;
            }
        }
        System.out.printf("Longest hailstone sequence less than 100,000: hailstone(%d).length() = %d", maxN, maxLength);
    }
    
    public static List<Long> hailstoneSequence(long n) {
        if ( n <= 0 ) {
            throw new IllegalArgumentException("Must be grater than or equal to zero.");
        }
        List<Long> sequence = new ArrayList<>();
        sequence.add(n);
        while ( n > 1 ) {
            if ( (n & 1) == 0 ) {
                n /= 2;
            }
            else {
                n = 3 * n + 1;
            }
            sequence.add(n);
        }
        return sequence;
    }
    
}

```

### java_code_2.txt
```java
import java.util.HashMap;
import java.util.Map;
import java.util.stream.IntStream;

public class ExecutableLibrary {

    public static void main(String[] args) {
        Map<Integer,Integer> lengthMap = new HashMap<>();
        IntStream.range(1, 100_000)
                 .map(n -> HailstoneSequence.hailstoneSequence(n).size())
                 .forEach(len -> lengthMap.merge(len, 1, (v1, v2) -> v1 + v2));
        int mostOften = lengthMap.values()
                                 .stream()
                                 .mapToInt(x -> x)
                                 .max().orElse(-1);

        System.out.printf("The most frequent hailstone length for n < 100,000 is %d.%n", mostOften);
    }

}

```

## Python Code
### python_code_1.txt
```python
def hailstone(n):
    seq = [n]
    while n>1:
        n = 3*n + 1 if n & 1 else n//2
        seq.append(n)
    return seq

if __name__ == '__main__':
    h = hailstone(27)
    assert len(h)==112 and h[:4]==[27, 82, 41, 124] and h[-4:]==[8, 4, 2, 1]
    print("Maximum length %i was found for hailstone(%i) for numbers <100,000" %
          max((len(hailstone(i)), i) for i in range(1,100000)))

```

### python_code_2.txt
```python
from collections import Counter

def function_length_frequency(func, hrange):
    return Counter(len(func(n)) for n in hrange).most_common()

if __name__ == '__main__':
    from executable_hailstone_library import hailstone

    upto = 100000
    hlen, freq = function_length_frequency(hailstone, range(1, upto))[0]
    print("The length of hailstone sequence that is most common for\n"
          "hailstone(n) where 1<=n<%i, is %i. It occurs %i times."
          % (upto, hlen, freq))

```

