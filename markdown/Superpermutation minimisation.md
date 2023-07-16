# Superpermutation minimisation

## Task Link
[Rosetta Code - Superpermutation minimisation](https://rosettacode.org/wiki/Superpermutation_minimisation)

## Java Code
### java_code_1.txt
```java
import static java.util.stream.IntStream.rangeClosed;

public class Test {
    final static int nMax = 12;

    static char[] superperm;
    static int pos;
    static int[] count = new int[nMax];

    static int factSum(int n) {
        return rangeClosed(1, n)
                .map(m -> rangeClosed(1, m).reduce(1, (a, b) -> a * b)).sum();
    }

    static boolean r(int n) {
        if (n == 0)
            return false;

        char c = superperm[pos - n];
        if (--count[n] == 0) {
            count[n] = n;
            if (!r(n - 1))
                return false;
        }
        superperm[pos++] = c;
        return true;
    }

    static void superPerm(int n) {
        String chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        pos = n;
        superperm = new char[factSum(n)];

        for (int i = 0; i < n + 1; i++)
            count[i] = i;
        for (int i = 1; i < n + 1; i++)
            superperm[i - 1] = chars.charAt(i);

        while (r(n)) {
        }
    }

    public static void main(String[] args) {
        for (int n = 0; n < nMax; n++) {
            superPerm(n);
            System.out.printf("superPerm(%2d) len = %d", n, superperm.length);
            System.out.println();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
"Generate a short Superpermutation of n characters A... as a string using various algorithms."


from __future__ import print_function, division

from itertools import permutations
from math import factorial
import string
import datetime
import gc



MAXN = 7


def s_perm0(n):
    """
    Uses greedy algorithm of adding another char (or two, or three, ...)
    until an unseen perm is formed in the last n chars
    """
    allchars = string.ascii_uppercase[:n]
    allperms = [''.join(p) for p in permutations(allchars)]
    sp, tofind = allperms[0], set(allperms[1:])
    while tofind:
        for skip in range(1, n):
            for trial_add in (''.join(p) for p in permutations(sp[-n:][:skip])):
                #print(sp, skip, trial_add)
                trial_perm = (sp + trial_add)[-n:]
                if trial_perm in tofind:
                    #print(sp, skip, trial_add)
                    sp += trial_add
                    tofind.discard(trial_perm)
                    trial_add = None    # Sentinel
                    break
            if trial_add is None:
                break
    assert all(perm in sp for perm in allperms) # Check it is a superpermutation
    return sp

def s_perm1(n):
    """
    Uses algorithm of concatenating all perms in order if not already part
    of concatenation.
    """
    allchars = string.ascii_uppercase[:n]
    allperms = [''.join(p) for p in sorted(permutations(allchars))]
    perms, sp = allperms[::], ''
    while perms:
        nxt = perms.pop()
        if nxt not in sp:
            sp += nxt
    assert all(perm in sp for perm in allperms)
    return sp

def s_perm2(n):
    """
    Uses algorithm of concatenating all perms in order first-last-nextfirst-
    nextlast... if not already part of concatenation.
    """
    allchars = string.ascii_uppercase[:n]
    allperms = [''.join(p) for p in sorted(permutations(allchars))]
    perms, sp = allperms[::], ''
    while perms:
        nxt = perms.pop(0)
        if nxt not in sp:
            sp += nxt
        if perms:
            nxt = perms.pop(-1)
            if nxt not in sp:
                sp += nxt
    assert all(perm in sp for perm in allperms)
    return sp

def _s_perm3(n, cmp):
    """
    Uses algorithm of concatenating all perms in order first,
    next_with_LEASTorMOST_chars_in_same_position_as_last_n_chars, ...
    """
    allchars = string.ascii_uppercase[:n]
    allperms = [''.join(p) for p in sorted(permutations(allchars))]
    perms, sp = allperms[::], ''
    while perms:
        lastn = sp[-n:]
        nxt = cmp(perms,
                  key=lambda pm:
                    sum((ch1 == ch2) for ch1, ch2 in zip(pm, lastn)))
        perms.remove(nxt)
        if nxt not in sp:
            sp += nxt
    assert all(perm in sp for perm in allperms)
    return sp

def s_perm3_max(n):
    """
    Uses algorithm of concatenating all perms in order first,
    next_with_MOST_chars_in_same_position_as_last_n_chars, ...
    """
    return _s_perm3(n, max)

def s_perm3_min(n):
    """
    Uses algorithm of concatenating all perms in order first,
    next_with_LEAST_chars_in_same_position_as_last_n_chars, ...
    """
    return _s_perm3(n, min)


longest = [factorial(n) * n for n in range(MAXN + 1)]
weight, runtime = {}, {}
print(__doc__)
for algo in [s_perm0, s_perm1, s_perm2, s_perm3_max, s_perm3_min]:
    print('\n###\n### %s\n###' % algo.__name__)
    print(algo.__doc__)
    weight[algo.__name__], runtime[algo.__name__] = 1, datetime.timedelta(0)
    for n in range(1, MAXN + 1):
        gc.collect()
        gc.disable()
        t = datetime.datetime.now()
        sp = algo(n)
        t = datetime.datetime.now() - t
        gc.enable()
        runtime[algo.__name__] += t
        lensp = len(sp)
        wt = (lensp / longest[n]) ** 2
        print('  For N=%i: SP length %5i Max: %5i Weight: %5.2f'
              % (n, lensp, longest[n], wt))
        weight[algo.__name__] *= wt
    weight[algo.__name__] **= 1 / n  # Geometric mean
    weight[algo.__name__] = 1 / weight[algo.__name__]
    print('%*s Overall Weight: %5.2f in %.1f seconds.'
          % (29, '', weight[algo.__name__], runtime[algo.__name__].total_seconds()))

print('\n###\n### Algorithms ordered by shortest superpermutations first\n###')
print('\n'.join('%12s (%.3f)' % kv for kv in
                sorted(weight.items(), key=lambda keyvalue: -keyvalue[1])))
      
print('\n###\n### Algorithms ordered by shortest runtime first\n###')
print('\n'.join('%12s (%.3f)' % (k, v.total_seconds()) for k, v in
                sorted(runtime.items(), key=lambda keyvalue: keyvalue[1])))

```

### python_code_2.txt
```python
from array import array
from string import ascii_uppercase, digits
from operator import mul

try:
    import psyco
    psyco.full()
except:
    pass

N_MAX = 12

# fact_sum(n) = 1! + 2! + ... + n!
def fact_sum(n):
    return sum(reduce(mul, xrange(1, m + 1), 1) for m in xrange(1, n + 1))


def r(n, superperm, pos, count):
    if not n:
        return False

    c = superperm[pos - n]
    count[n] -= 1
    if not count[n]:
        count[n] = n
        if not r(n - 1, superperm, pos, count):
            return False

    superperm[pos] = c
    pos += 1
    return True


def super_perm(n, superperm, pos, count, chars = digits + ascii_uppercase):
    assert len(chars) >= N_MAX
    pos = n
    superperm += array("c", " ") * (fact_sum(n) - len(superperm))

    for i in xrange(n + 1):
        count[i] = i
    for i in xrange(1, n + 1):
        superperm[i - 1] = chars[i]

    while r(n, superperm, pos, count):
        pass


def main():
    superperm = array("c", "")
    pos = 0
    count = array("l", [0]) * N_MAX

    for n in xrange(N_MAX):
        super_perm(n, superperm, pos, count)
        print "Super perm(%2d) len = %d" % (n, len(superperm)),
        #print superperm.tostring(),
        print

main()

```

