# Topswops

## Task Link
[Rosetta Code - Topswops](https://rosettacode.org/wiki/Topswops)

## Java Code
### java_code_1.txt
```java
public class Topswops {
    static final int maxBest = 32;
    static int[] best;

    static private void trySwaps(int[] deck, int f, int d, int n) {
        if (d > best[n])
            best[n] = d;

        for (int i = n - 1; i >= 0; i--) {
            if (deck[i] == -1 || deck[i] == i)
                break;
            if (d + best[i] <= best[n])
                return;
        }

        int[] deck2 = deck.clone();
        for (int i = 1; i < n; i++) {
            final int k = 1 << i;
            if (deck2[i] == -1) {
                if ((f & k) != 0)
                    continue;
            } else if (deck2[i] != i)
                continue;

            deck2[0] = i;
            for (int j = i - 1; j >= 0; j--)
                deck2[i - j] = deck[j]; // Reverse copy.
            trySwaps(deck2, f | k, d + 1, n);
        }
    }

    static int topswops(int n) {
        assert(n > 0 && n < maxBest);
        best[n] = 0;
        int[] deck0 = new int[n + 1];
        for (int i = 1; i < n; i++)
            deck0[i] = -1;
        trySwaps(deck0, 1, 0, n);
        return best[n];
    }

    public static void main(String[] args) {
        best = new int[maxBest];
        for (int i = 1; i < 11; i++)
            System.out.println(i + ": " + topswops(i));
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> from itertools import permutations
>>> def f1(p):
	i = 0
	while True:
		p0  = p[0]
		if p0 == 1: break
		p[:p0] = p[:p0][::-1]
		i  += 1
	return i

>>> def fannkuch(n):
	return max(f1(list(p)) for p in permutations(range(1, n+1)))

>>> for n in range(1, 11): print(n,fannkuch(n))

1 0
2 1
3 2
4 4
5 7
6 10
7 16
8 22
9 30
10 38
>>>

```

### python_code_2.txt
```python
try:
    import psyco
    psyco.full()
except ImportError:
    pass

best = [0] * 16

def try_swaps(deck, f, s, d, n):
    if d > best[n]:
        best[n] = d

    i = 0
    k = 1 << s
    while s:
        k >>= 1
        s -= 1
        if deck[s] == -1 or deck[s] == s:
            break
        i |= k
        if (i & f) == i and d + best[s] <= best[n]:
            return d
    s += 1

    deck2 = list(deck)
    k = 1
    for i2 in xrange(1, s):
        k <<= 1
        if deck2[i2] == -1:
            if f & k: continue
        elif deck2[i2] != i2:
            continue

        deck[i2] = i2
        deck2[:i2 + 1] = reversed(deck[:i2 + 1])
        try_swaps(deck2, f | k, s, 1 + d, n)

def topswops(n):
    best[n] = 0
    deck0 = [-1] * 16
    deck0[0] = 0
    try_swaps(deck0, 1, n, 0, n)
    return best[n]

for i in xrange(1, 13):
    print "%2d: %d" % (i, topswops(i))

```

