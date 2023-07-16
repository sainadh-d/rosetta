# Subtractive generator

## Task Link
[Rosetta Code - Subtractive generator](https://rosettacode.org/wiki/Subtractive_generator)

## Java Code
### java_code_1.txt
```java
import java.util.function.IntSupplier;
import static java.util.stream.IntStream.generate;

public class SubtractiveGenerator implements IntSupplier {
    static final int MOD = 1_000_000_000;
    private int[] state = new int[55];
    private int si, sj;

    public SubtractiveGenerator(int p1) {
        subrandSeed(p1);
    }

    void subrandSeed(int p1) {
        int p2 = 1;

        state[0] = p1 % MOD;
        for (int i = 1, j = 21; i < 55; i++, j += 21) {
            if (j >= 55)
                j -= 55;
            state[j] = p2;
            if ((p2 = p1 - p2) < 0)
                p2 += MOD;
            p1 = state[j];
        }

        si = 0;
        sj = 24;
        for (int i = 0; i < 165; i++)
            getAsInt();
    }

    @Override
    public int getAsInt() {
        if (si == sj)
            subrandSeed(0);

        if (si-- == 0)
            si = 54;
        if (sj-- == 0)
            sj = 54;

        int x = state[si] - state[sj];
        if (x < 0)
            x += MOD;

        return state[si] = x;
    }

    public static void main(String[] args) {
        generate(new SubtractiveGenerator(292_929)).limit(10)
                .forEach(System.out::println);
    }
}

```

## Python Code
### python_code_1.txt
```python
import collections
s= collections.deque(maxlen=55)
#    Start with a single seed in range 0 to 10**9 - 1.
seed = 292929

#    Set s0 = seed and s1 = 1. 
#    The inclusion of s1 = 1 avoids some bad states 
#    (like all zeros, or all multiples of 10).
s.append(seed)
s.append(1)

#    Compute s2,s3,...,s54 using the subtractive formula 
#    sn = s(n - 2) - s(n - 1)(mod 10**9).
for n in xrange(2, 55):
    s.append((s[n-2] - s[n-1]) % 10**9)

#    Reorder these 55 values so r0 = s34, r1 = s13, r2 = s47, ..., 
#                               rn = s(34 * (n + 1)(mod 55)).

r = collections.deque(maxlen=55)
for n in xrange(55):
    i = (34 * (n+1)) % 55
    r.append(s[i])
#        This is the same order as s0 = r54, s1 = r33, s2 = r12, ..., 
#                                  sn = r((34 * n) - 1(mod 55)).
#        This rearrangement exploits how 34 and 55 are relatively prime. 
#    Compute the next 165 values r55 to r219. Store the last 55 values.


def getnextr():
    """get next random number"""
    r.append((r[0]-r[31])%10**9)
    return r[54]

# rn = r(n - 55) - r(n - 24)(mod 10**9) for n >= 55
for n in xrange(219 - 54):
    getnextr()

# now fully initilised
# print first five numbers
for i in xrange(5):
    print "result = ", getnextr()

```

### python_code_2.txt
```python
import collections

_ten2nine = 10**9

class Subtractive_generator():
    
    def __init__(self, seed=292929):
        self.r = collections.deque(maxlen=55)
        s = collections.deque(maxlen=55)
        s.extend([seed, 1])
        s.extend((s[n-2] - s[n-1]) % _ten2nine for n in range(2, 55))
        self.r.extend(s[(34 * (n+1)) % 55] for n in range(55)) 
        for n in range(219 - 54):
            self()
     
    def __call__(self):
        r = self.r
        r.append((r[0] - r[31]) % _ten2nine)
        return r[54]
     
if __name__ == '__main__':
    srand = Subtractive_generator()
    print([srand() for i in range(5)])

```

