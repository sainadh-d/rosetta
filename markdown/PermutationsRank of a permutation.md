# Permutations/Rank of a permutation

## Task Link
[Rosetta Code - Permutations/Rank of a permutation](https://rosettacode.org/wiki/Permutations/Rank_of_a_permutation)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.*;

class RankPermutation
{
  public static BigInteger getRank(int[] permutation)
  {
    int n = permutation.length;
    BitSet usedDigits = new BitSet();
    BigInteger rank = BigInteger.ZERO;
    for (int i = 0; i < n; i++)
    {
      rank = rank.multiply(BigInteger.valueOf(n - i));
      int digit = 0;
      int v = -1;
      while ((v = usedDigits.nextClearBit(v + 1)) < permutation[i])
        digit++;
      usedDigits.set(v);
      rank = rank.add(BigInteger.valueOf(digit));
    }
    return rank;
  }
  
  public static int[] getPermutation(int n, BigInteger rank)
  {
    int[] digits = new int[n];
    for (int digit = 2; digit <= n; digit++)
    {
      BigInteger divisor = BigInteger.valueOf(digit);
      digits[n - digit] = rank.mod(divisor).intValue();
      if (digit < n)
        rank = rank.divide(divisor);
    }
    BitSet usedDigits = new BitSet();
    int[] permutation = new int[n];
    for (int i = 0; i < n; i++)
    {
      int v = usedDigits.nextClearBit(0);
      for (int j = 0; j < digits[i]; j++)
        v = usedDigits.nextClearBit(v + 1);
      permutation[i] = v;
      usedDigits.set(v);
    }
    return permutation;
  }
  
  public static void main(String[] args)
  {
    for (int i = 0; i < 6; i++)
    {
      int[] permutation = getPermutation(3, BigInteger.valueOf(i));
      System.out.println(String.valueOf(i) + " --> " + Arrays.toString(permutation) + " --> " + getRank(permutation));
    }
    Random rnd = new Random();
    for (int n : new int[] { 12, 144 })
    {
      BigInteger factorial = BigInteger.ONE;
      for (int i = 2; i <= n; i++)
        factorial = factorial.multiply(BigInteger.valueOf(i));
      // Create 5 random samples
      System.out.println("n = " + n);
      for (int i = 0; i < 5; i++)
      {
        BigInteger rank = new BigInteger((factorial.bitLength() + 1) << 1, rnd);
        rank = rank.mod(factorial);
        int[] permutation = getPermutation(n, rank);
        System.out.println("  " + rank + " --> " + Arrays.toString(permutation) + " --> " + getRank(permutation));
      }
    }
  }
  
}

```

## Python Code
### python_code_1.txt
```python
from math import factorial as fact
from random import randrange
from textwrap import wrap

def identity_perm(n): 
    return list(range(n))

def unranker1(n, r, pi):
    while n > 0:
        n1, (rdivn, rmodn) = n-1, divmod(r, n)
        pi[n1], pi[rmodn] = pi[rmodn], pi[n1]
        n = n1
        r = rdivn
    return pi

def init_pi1(n, pi): 
    pi1 = [-1] * n
    for i in range(n): 
        pi1[pi[i]] = i
    return pi1

def ranker1(n, pi, pi1):
    if n == 1: 
        return 0
    n1 = n-1
    s = pi[n1]
    pi[n1], pi[pi1[n1]] = pi[pi1[n1]], pi[n1]
    pi1[s], pi1[n1] = pi1[n1], pi1[s]
    return s + n * ranker1(n1, pi, pi1)

def unranker2(n, r, pi):
    while n > 0:
        n1 = n-1
        s, rmodf = divmod(r, fact(n1))
        pi[n1], pi[s] = pi[s], pi[n1]
        n = n1
        r = rmodf
    return pi

def ranker2(n, pi, pi1):
    if n == 1: 
        return 0
    n1 = n-1
    s = pi[n1]
    pi[n1], pi[pi1[n1]] = pi[pi1[n1]], pi[n1]
    pi1[s], pi1[n1] = pi1[n1], pi1[s]
    return s * fact(n1) + ranker2(n1, pi, pi1)

def get_random_ranks(permsize, samplesize):    
    perms = fact(permsize)
    ranks = set()
    while len(ranks) < samplesize:
        ranks |= set( randrange(perms) 
                      for r in range(samplesize - len(ranks)) )
    return ranks    

def test1(comment, unranker, ranker):    
    n, samplesize, n2 = 3, 4, 12
    print(comment)
    perms = []
    for r in range(fact(n)):
        pi = identity_perm(n)
        perm = unranker(n, r, pi)
        perms.append((r, perm))
    for r, pi in perms:
        pi1 = init_pi1(n, pi)
        print('  From rank %2i to %r back to %2i' % (r, pi, ranker(n, pi[:], pi1)))
    print('\n  %i random individual samples of %i items:' % (samplesize, n2))
    for r in get_random_ranks(n2, samplesize):
        pi = identity_perm(n2)
        print('    ' + ' '.join('%2i' % i for i in unranker(n2, r, pi)))
    print('')

def test2(comment, unranker):    
    samplesize, n2 = 4, 144
    print(comment)
    print('  %i random individual samples of %i items:' % (samplesize, n2))
    for r in get_random_ranks(n2, samplesize):
        pi = identity_perm(n2)
        print('    ' + '\n      '.join(wrap(repr(unranker(n2, r, pi)))))
    print('')

if __name__ == '__main__':
    test1('First ordering:', unranker1, ranker1)
    test1('Second ordering:', unranker2, ranker2)
    test2('First ordering, large number of perms:', unranker1)

```

### python_code_2.txt
```python
from random import randrange
from typing import List

Perm = List[int]

_fact = [1]     # factorials cache


def print_perm(T: Perm) -> None:
    print(T)

def tj_unrank(n: int, r: int) -> Perm:
    "Returns the r-ranked Trotter-Johnson permutation of integers 0..n-1"
    global _fact

    for i in range(len(_fact), n+2):    # Extend factorial cache if necessary.
        _fact.append(_fact[i - 1] * i)

    pi: Perm = [0] * (n+2)
    pi[1] = 1
    r2 = 0
    for j in range(2, n+1):
        r1 = (r * _fact[j]) // _fact[n]
        k = r1 - j*r2
        if ((r2 % 2) == 0):
            for i in range(j-1, j - k - 1, -1):
                pi[i+1] = pi[i]
            pi[j-k] = j
        else:
            for i in range(j - 1, k, -1):
                pi[i+1] = pi[i]
            pi[k + 1] = j
        r2 = r1

    return [i - 1 for i in pi[1:-1]]

def tj_rank(p: Perm) -> int:
    "Returns the ranking of the Trotter-Johnson permutation p, of integers 0..n-1"
    n = len(p)
    assert set(p) == set(range(n)), f"Perm {p} not a perm of 0..{n-1}."

    pi = [0] + [i+1 for i in p] + [0]
    r = 0
    for j in range(2, n + 1):
        i = k = 1
        while pi[i] != j:
            if (pi[i] < j):
                k += 1
            i += 1
        if ((r % 2) == 0 ):
            r = j*r+j-k
        else:
            r = j*r+k-1

    return r

def tj_parity(p: Perm) -> int:
    "Returns the 0/1 parity of the Trotter-Johnson permutation p, of integers 0..n-1"
    n = len(p)
    assert set(p) == set(range(n)), f"Perm {p} not a perm of 0..{n-1}."

    pi = [0] + [i+1 for i in p] + [0]
    a, c = [0] * (n + 1), 0
    for j in range(1, n+1):
        if a[j] == 0:
            c += 1
            a[j] = 1
            i = j
            while ( pi[i] != j ):
                i = pi[i]
                a[i] = 1

    return (n-c) % 2

def get_random_ranks(permsize, samplesize, fact):
    perms = fact[permsize]
    ranks = set()
    while len(ranks) < samplesize:
        ranks |= set( randrange(perms)
                      for r in range(samplesize - len(ranks)) )
    return ranks

if __name__ == '__main__':
    n = 3

    print(f"Testing rank/unrank n={n}.\n");

    for i in range(len(_fact), n+2):    # Extend factorial cache if necessary.
        _fact.append(_fact[i - 1] * i)
    for r in range(_fact[n]):
        p = tj_unrank(n, r)
        rank = tj_rank(p)
        parity = tj_parity(p)
        print(f"  Rank: {r:4} to perm: {p}, parity: {parity} back to rank: {rank}")

    for samplesize, n2 in [(4, 12), (3, 144)]:
        print('\n  %i random individual samples of %i items:' % (samplesize, n2))
        for i in range(len(_fact), max([n, n2])+2):    # Extend factorial cache if necessary.
            _fact.append(_fact[i - 1] * i)
        for r in get_random_ranks(n2, samplesize, _fact):
            p = tj_unrank(n2, r)
            rank = tj_rank(p)
            parity = tj_parity(p)
            print(f"  Rank: {r:10} to perm: {p}, parity: {parity} to rank: {rank:10}")

```

### python_code_3.txt
```python
def ranker1(n, pi, pi1):
    if n == 1: 
        return 0
    n1 = n-1
    s = pi[n1]
    pi[n1], pi[pi1[n1]] = pi[pi1[n1]], pi[n1]
    pi1[s], pi1[n1] = pi1[n1], pi1[s]
    return s + n * ranker1(n1, pi, pi1)

def ranker2(n, pi, pi1):
    result = 0
    for i in range(n-1, 0, -1):
        s = pi[i]
        pi[i], pi[pi1[i]] = pi[pi1[i]], pi[i]
        pi1[s], pi1[i] = pi1[i], pi1[s]
        result += s * fact(i)
    return result

```

