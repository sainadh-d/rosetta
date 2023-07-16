# Zeckendorf number representation

## Task Link
[Rosetta Code - Zeckendorf number representation](https://rosettacode.org/wiki/Zeckendorf_number_representation)

## Java Code
### java_code_1.txt
```java
import java.util.*;

class Zeckendorf
{
  public static String getZeckendorf(int n)
  {
    if (n == 0)
      return "0";
    List<Integer> fibNumbers = new ArrayList<Integer>();
    fibNumbers.add(1);
    int nextFib = 2;
    while (nextFib <= n)
    {
      fibNumbers.add(nextFib);
      nextFib += fibNumbers.get(fibNumbers.size() - 2);
    }
    StringBuilder sb = new StringBuilder();
    for (int i = fibNumbers.size() - 1; i >= 0; i--)
    {
      int fibNumber = fibNumbers.get(i);
      sb.append((fibNumber <= n) ? "1" : "0");
      if (fibNumber <= n)
        n -= fibNumber;
    }
    return sb.toString();
  }
  
  public static void main(String[] args)
  {
    for (int i = 0; i <= 20; i++)
      System.out.println("Z(" + i + ")=" + getZeckendorf(i));
  }
}

```

### java_code_2.txt
```java
import java.util.ArrayList;
import java.util.List;

public class Zeckendorf {

    private List<Integer> getFibList(final int maxNum, final int n1, final int n2, final List<Integer> fibs){
        if(n2 > maxNum) return fibs;

        fibs.add(n2);

        return getFibList(maxNum, n2, n1 + n2, fibs);
    }

    public String getZeckendorf(final int num) {
        if (num <= 0) return "0";

        final List<Integer> fibs = getFibList(num, 1, 2, new ArrayList<Integer>(){{ add(1); }});

        return getZeckString("", num, fibs.size() - 1, fibs);
    }

    private String getZeckString(final String zeck, final int num, final int index, final List<Integer> fibs){
        final int curFib = fibs.get(index);
        final boolean placeZeck = num >= curFib;

        final String outString = placeZeck ? zeck + "1" : zeck + "0";
        final int outNum = placeZeck ? num - curFib : num;

        if(index == 0) return outString;

        return  getZeckString(outString, outNum, index - 1, fibs);
    }
    
    public static void main(final String[] args) {
        final Zeckendorf zeckendorf = new Zeckendorf();

        for(int i =0; i <= 20; i++){
            System.out.println("Z("+ i +"):\t" + zeckendorf.getZeckendorf(i));
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def fib():
    memo = [1, 2]
    while True:
        memo.append(sum(memo))
        yield memo.pop(0)

def sequence_down_from_n(n, seq_generator):
    seq = []
    for s in seq_generator():
        seq.append(s)
        if s >= n: break
    return seq[::-1]

def zeckendorf(n):
    if n == 0: return [0]
    seq = sequence_down_from_n(n, fib)
    digits, nleft = [], n
    for s in seq:
        if s <= nleft:
            digits.append(1)
            nleft -= s
        else:
            digits.append(0)
    assert nleft == 0, 'Check all of n is accounted for'
    assert sum(x*y for x,y in zip(digits, seq)) == n, 'Assert digits are correct'
    while digits[0] == 0:
        # Remove any zeroes padding L.H.S.
        digits.pop(0)
    return digits

n = 20
print('Fibonacci digit multipliers: %r' % sequence_down_from_n(n, fib))
for i in range(n + 1):
    print('%3i: %8s' % (i, ''.join(str(d) for d in zeckendorf(i))))

```

### python_code_2.txt
```python
n = 20
def z(n):
    if n == 0 : return [0]
    fib = [2,1]
    while fib[0] < n: fib[0:0] = [sum(fib[:2])]
    dig = []
    for f in fib:
        if f <= n:
            dig, n = dig + [1], n - f
        else:
            dig += [0]
    return dig if dig[0] else dig[1:]

for i in range(n + 1):
    print('%3i: %8s' % (i, ''.join(str(d) for d in z(i))))

```

