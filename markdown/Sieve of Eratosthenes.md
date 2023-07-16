# Sieve of Eratosthenes

## Task Link
[Rosetta Code - Sieve of Eratosthenes](https://rosettacode.org/wiki/Sieve_of_Eratosthenes)

## Java Code
### java_code_1.txt
```java
import java.util.LinkedList;

public class Sieve{
       public static LinkedList<Integer> sieve(int n){
               if(n < 2) return new LinkedList<Integer>();
               LinkedList<Integer> primes = new LinkedList<Integer>();
               LinkedList<Integer> nums = new LinkedList<Integer>();

               for(int i = 2;i <= n;i++){ //unoptimized
                       nums.add(i);
               }

               while(nums.size() > 0){
                       int nextPrime = nums.remove();
                       for(int i = nextPrime * nextPrime;i <= n;i += nextPrime){
                               nums.removeFirstOccurrence(i);
                       }
                       primes.add(nextPrime);
               }
               return primes;
       }
}

```

### java_code_2.txt
```java
nums.add(2);
for(int i = 3;i <= n;i += 2){
       nums.add(i);
}

```

### java_code_3.txt
```java
import java.util.ArrayList;
import java.util.List;
 
public class Eratosthenes {
    public List<Integer> sieve(Integer n) {
        List<Integer> primes = new ArrayList<Integer>(n);
        boolean[] isComposite = new boolean[n + 1];
        for(int i = 2; i <= n; i++) {
            if(!isComposite[i]) {
                primes.add(i);
                for(int j = i * i; j <= n; j += i) {
                    isComposite[j] = true;
                }
            }
        }
        return primes;
    }
}

```

### java_code_4.txt
```java
import java.util.LinkedList;
import java.util.BitSet;

public class Sieve{
    public static LinkedList<Integer> sieve(int n){
        LinkedList<Integer> primes = new LinkedList<Integer>();
        BitSet nonPrimes = new BitSet(n+1);
        
        for (int p = 2; p <= n ; p = nonPrimes.nextClearBit(p+1)) {
            for (int i = p * p; i <= n; i += p)
                nonPrimes.set(i);
            primes.add(p);
        }
        return primes;
    }
}

```

### java_code_5.txt
```java
import java.util.Set;
import java.util.TreeSet;

public class Sieve{
    public static Set<Integer> findPrimeNumbers(int limit) {
    int last = 2;
    TreeSet<Integer> nums = new TreeSet<>();

    if(limit < last) return nums;

    for(int i = last; i <= limit; i++){
      nums.add(i);
    }

    return filterList(nums, last, limit);
  }

  private static TreeSet<Integer> filterList(TreeSet<Integer> list, int last, int limit) {
    int squared = last*last;
    if(squared < limit) {
      for(int i=squared; i <= limit; i += last) {
        list.remove(i);
      }
      return filterList(list, list.higher(last), limit);
    } 
    return list; 
  }
}

```

### java_code_6.txt
```java
import java.util.Iterator;
import java.util.PriorityQueue;
import java.math.BigInteger;

// generates all prime numbers
public class InfiniteSieve implements Iterator<BigInteger> {

    private static class NonPrimeSequence implements Comparable<NonPrimeSequence> {
	BigInteger currentMultiple;
	BigInteger prime;

	public NonPrimeSequence(BigInteger p) {
	    prime = p;
	    currentMultiple = p.multiply(p); // start at square of prime
	}
	@Override public int compareTo(NonPrimeSequence other) {
	    // sorted by value of current multiple
	    return currentMultiple.compareTo(other.currentMultiple);
	}
    }

    private BigInteger i = BigInteger.valueOf(2);
    // priority queue of the sequences of non-primes
    // the priority queue allows us to get the "next" non-prime quickly
    final PriorityQueue<NonPrimeSequence> nonprimes = new PriorityQueue<NonPrimeSequence>();

    @Override public boolean hasNext() { return true; }
    @Override public BigInteger next() {
	// skip non-prime numbers
	for ( ; !nonprimes.isEmpty() && i.equals(nonprimes.peek().currentMultiple); i = i.add(BigInteger.ONE)) {
            // for each sequence that generates this number,
            // have it go to the next number (simply add the prime)
            // and re-position it in the priority queue
	    while (nonprimes.peek().currentMultiple.equals(i)) {
		NonPrimeSequence x = nonprimes.poll();
		x.currentMultiple = x.currentMultiple.add(x.prime);
		nonprimes.offer(x);
	    }
	}
	// prime
        // insert a NonPrimeSequence object into the priority queue
	nonprimes.offer(new NonPrimeSequence(i));
	BigInteger result = i;
	i = i.add(BigInteger.ONE);
	return result;
    }

    public static void main(String[] args) {
	Iterator<BigInteger> sieve = new InfiniteSieve();
	for (int i = 0; i < 25; i++) {
	    System.out.println(sieve.next());
	}
    }
}

```

### java_code_7.txt
```java
import java.util.Iterator;
import java.util.HashMap;
 
// generates all prime numbers up to about 10 ^ 19 if one can wait 1000's of years or so...
public class SoEInfHashMap implements Iterator<Long> {

  long candidate = 2;
  Iterator<Long> baseprimes = null;
  long basep = 3;
  long basepsqr = 9;
  // HashMap of the sequences of non-primes
  // the hash map allows us to get the "next" non-prime reasonably quickly
  // but further allows re-insertions to take amortized constant time
  final HashMap<Long,Long> nonprimes = new HashMap<>();

  @Override public boolean hasNext() { return true; }
  @Override public Long next() {
    // do the initial primes separately to initialize the base primes sequence
    if (this.candidate <= 5L) if (this.candidate++ == 2L) return 2L; else {
      this.candidate++; if (this.candidate == 5L) return 3L; else {
        this.baseprimes = new SoEInfHashMap();
        this.baseprimes.next(); this.baseprimes.next(); // throw away 2 and 3
        return 5L;
    } }
    // skip non-prime numbers including squares of next base prime
    for ( ; this.candidate >= this.basepsqr || //equals nextbase squared => not prime
              nonprimes.containsKey(this.candidate); candidate += 2) {
      // insert a square root prime sequence into hash map if to limit
      if (candidate >= basepsqr) { // if square of base prime, always equal
        long adv = this.basep << 1;
        nonprimes.put(this.basep * this.basep + adv, adv);
        this.basep = this.baseprimes.next();
        this.basepsqr = this.basep * this.basep;
      }
      // else for each sequence that generates this number,
      // have it go to the next number (simply add the advance)
      // and re-position it in the hash map at an emply slot
      else {
        long adv = nonprimes.remove(this.candidate);
        long nxt = this.candidate + adv;
        while (this.nonprimes.containsKey(nxt)) nxt += adv; //unique keys
        this.nonprimes.put(nxt, adv);
      }
    }
    // prime
    long tmp = candidate; this.candidate += 2; return tmp;
  }

  public static void main(String[] args) {    
    int n = 100000000;    
    long strt = System.currentTimeMillis();    
    SoEInfHashMap sieve = new SoEInfHashMap();
    int count = 0;
    while (sieve.next() <= n) count++;    
    long elpsd = System.currentTimeMillis() - strt;    
    System.out.println("Found " + count + " primes up to " + n + " in " + elpsd + " milliseconds.");
  }
  
}

```

### java_code_8.txt
```java
import java.util.Iterator;
import java.util.ArrayList;

// generates all prime numbers up to about 10 ^ 19 if one can wait 100's of years or so...
// practical range is about 10^14 in a week or so...
public class SoEPagedOdds implements Iterator<Long> {
  private final int BFSZ = 1 << 16;
  private final int BFBTS = BFSZ * 32;
  private final int BFRNG = BFBTS * 2;
  private long bi = -1;
  private long lowi = 0;
  private final ArrayList<Integer> bpa = new ArrayList<>();
  private Iterator<Long> bps;
  private final int[] buf = new int[BFSZ];
  
  @Override public boolean hasNext() { return true; }
  @Override public Long next() {
    if (this.bi < 1) {
      if (this.bi < 0) {
        this.bi = 0;
        return 2L;
      }
      //this.bi muxt be 0
      long nxt = 3 + (this.lowi << 1) + BFRNG;
      if (this.lowi <= 0) { // special culling for first page as no base primes yet:
          for (int i = 0, p = 3, sqr = 9; sqr < nxt; i++, p += 2, sqr = p * p)
              if ((this.buf[i >>> 5] & (1 << (i & 31))) == 0)
                  for (int j = (sqr - 3) >> 1; j < BFBTS; j += p)
                      this.buf[j >>> 5] |= 1 << (j & 31);
      }
      else { // after the first page:
        for (int i = 0; i < this.buf.length; i++)
          this.buf[i] = 0; // clear the sieve buffer
        if (this.bpa.isEmpty()) { // if this is the first page after the zero one:
            this.bps = new SoEPagedOdds(); // initialize separate base primes stream:
            this.bps.next(); // advance past the only even prime of two
            this.bpa.add(this.bps.next().intValue()); // get the next prime (3 in this case)
        }
        // get enough base primes for the page range...
        for (long p = this.bpa.get(this.bpa.size() - 1), sqr = p * p; sqr < nxt;
                p = this.bps.next(), this.bpa.add((int)p), sqr = p * p) ;
        for (int i = 0; i < this.bpa.size() - 1; i++) {
          long p = this.bpa.get(i);
          long s = (p * p - 3) >>> 1;
          if (s >= this.lowi) // adjust start index based on page lower limit...
            s -= this.lowi;
          else {
            long r = (this.lowi - s) % p;
            s = (r != 0) ? p - r : 0;
          }
          for (int j = (int)s; j < BFBTS; j += p)
            this.buf[j >>> 5] |= 1 << (j & 31);
        }
      }
    }
    while ((this.bi < BFBTS) &&
           ((this.buf[(int)this.bi >>> 5] & (1 << ((int)this.bi & 31))) != 0))
        this.bi++; // find next marker still with prime status
    if (this.bi < BFBTS) // within buffer: output computed prime
        return 3 + ((this.lowi + this.bi++) << 1);
    else { // beyond buffer range: advance buffer
        this.bi = 0;
        this.lowi += BFBTS;
        return this.next(); // and recursively loop
    }
  }

  public static void main(String[] args) {    
    long n = 1000000000;
    long strt = System.currentTimeMillis();
    Iterator<Long> gen = new SoEPagedOdds();
    int count = 0;
    while (gen.next() <= n) count++;
    long elpsd = System.currentTimeMillis() - strt;
    System.out.println("Found " + count + " primes up to " + n + " in " + elpsd + " milliseconds.");
  }
  
}

```

### java_code_9.txt
```java
int i=2;
int maxx;
int maxy;
int max;
boolean[] sieve;

void setup() {
  size(1000, 1000);
  // frameRate(2);
  maxx=width;
  maxy=height;
  max=width*height;
  sieve=new boolean[max+1];

  sieve[1]=false;
  plot(0, false);
  plot(1, false);
  for (int i=2; i<=max; i++) {
    sieve[i]=true;
    plot(i, true);
  }
}

void draw() {
  if (!sieve[i]) {
    while (i*i<max && !sieve[i]) {
      i++;
    }
  }
  if (sieve[i]) {
    print(i+" ");
    for (int j=i*i; j<=max; j+=i) {
      if (sieve[j]) {
        sieve[j]=false;
        plot(j, false);
      }
    }
  }
  if (i*i<max) {
    i++;
  } else {
    noLoop();
    println("finished");
  }
}

void plot(int pos, boolean active) {
  set(pos%maxx, pos/maxx, active?#000000:#ffffff);
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function

i = 2

def setup():
    size(1000, 1000)
    # frameRate(2)
    global maxx, maxy, max_num, sieve
    maxx = width
    maxy = height
    max_num = width * height
    sieve = [False] * (max_num + 1)

    sieve[1] = False
    plot(0, False)
    plot(1, False)
    for i in range(2, max_num + 1):
        sieve[i] = True
        plot(i, True)


def draw():
    global i
    if not sieve[i]:
        while (i * i < max_num and not sieve[i]):
            i += 1

    if sieve[i]:
        print("{} ".format(i), end = '')
        for j in range(i * i, max_num + 1, i):
            if sieve[j]:
                sieve[j] = False
                plot(j, False)

    if i * i < max_num:
        i += 1
    else:
        noLoop()
        println("finished")


def plot(pos, active):
    set(pos % maxx, pos / maxx, color(0) if active else color(255))

```

### python_code_10.txt
```python
from numpy import array, bool_, multiply, nonzero, ones, put, resize
#
def makepattern(smallprimes):
    pattern = ones(multiply.reduce(smallprimes), dtype=bool_)
    pattern[0] = 0
    for p in smallprimes:
        pattern[p::p] = 0
    return pattern
#
def primes_upto3(limit, smallprimes=(2,3,5,7,11)):    
    sp = array(smallprimes)
    if limit <= sp.max(): return sp[sp <= limit]
    #
    isprime = resize(makepattern(sp), limit + 1) 
    isprime[:2] = 0; put(isprime, sp, 1) 
    #
    for n in range(sp.max() + 2, int(limit**0.5 + 1.5), 2): 
        if isprime[n]:
            isprime[n*n::n] = 0 
    return nonzero(isprime)[0]

```

### python_code_11.txt
```python
>>> primes_upto3(10**6, smallprimes=(2,3)) # Wall time: 0.17
array([     2,      3,      5, ..., 999961, 999979, 999983])
>>> primes_upto3(10**7, smallprimes=(2,3))            # Wall time: '''2.13'''
array([      2,       3,       5, ..., 9999971, 9999973, 9999991])
>>> primes_upto3(15)
array([ 2,  3,  5,  7, 11, 13])
>>> primes_upto3(10**7, smallprimes=primes_upto3(15)) # Wall time: '''1.31'''
array([      2,       3,       5, ..., 9999971, 9999973, 9999991])
>>> primes_upto2(10**7)                               # Wall time: '''1.39''' <-- version ''without'' wheels
array([      2,       3,       5, ..., 9999971, 9999973, 9999991])
>>> primes_upto3(10**7)                               # Wall time: '''1.30'''
array([      2,       3,       5, ..., 9999971, 9999973, 9999991])

```

### python_code_12.txt
```python
import heapq

# generates all prime numbers
def sieve():
    # priority queue of the sequences of non-primes
    # the priority queue allows us to get the "next" non-prime quickly
    nonprimes = []
    
    i = 2
    while True:
        if nonprimes and i == nonprimes[0][0]: # non-prime
            while nonprimes[0][0] == i:
                # for each sequence that generates this number,
                # have it go to the next number (simply add the prime)
                # and re-position it in the priority queue
                x = nonprimes[0]
                x[0] += x[1]
                heapq.heapreplace(nonprimes, x)
        
        else: # prime
            # insert a 2-element list into the priority queue:
            # [current multiple, prime]
            # the first element allows sorting by value of current multiple
            # we start with i^2
            heapq.heappush(nonprimes, [i*i, i])
            yield i
        
        i += 1

```

### python_code_13.txt
```python
def primes():
    yield 2; yield 3; yield 5; yield 7;
    bps = (p for p in primes())             # separate supply of "base" primes (b.p.)
    p = next(bps) and next(bps)             # discard 2, then get 3
    q = p * p                               # 9 - square of next base prime to keep track of,
    sieve = {}                              #                       in the sieve dict
    n = 9                                   # n is the next candidate number
    while True:
        if n not in sieve:                  # n is not a multiple of any of base primes,
            if n < q:                       # below next base prime's square, so
                yield n                     # n is prime
            else:
                p2 = p + p                  # n == p * p: for prime p, add p * p + 2 * p
                sieve[q + p2] = p2          #   to the dict, with 2 * p as the increment step
                p = next(bps); q = p * p    # pull next base prime, and get its square
        else:
            s = sieve.pop(n); nxt = n + s   # n's a multiple of some b.p., find next multiple
            while nxt in sieve: nxt += s    # ensure each entry is unique
            sieve[nxt] = s                  # nxt is next non-marked multiple of this prime
        n += 2                              # work on odds only
 
import itertools
def primes_up_to(limit):
    return list(itertools.takewhile(lambda p: p <= limit, primes()))

```

### python_code_14.txt
```python
def primes():
    for p in [2,3,5,7]: yield p                 # base wheel primes
    gaps1 = [ 2,4,2,4,6,2,6,4,2,4,6,6,2,6,4,2,6,4,6,8,4,2,4,2,4,8 ]
    gaps = gaps1 + [ 6,4,6,2,4,6,2,6,6,4,2,4,6,2,6,4,2,4,2,10,2,10 ] # wheel2357
    def wheel_prime_pairs():
        yield (11,0); bps = wheel_prime_pairs() # additional primes supply
        p, pi = next(bps); q = p * p            # adv to get 11 sqr'd is 121 as next square to put
        sieve = {}; n = 13; ni = 1              #   into sieve dict; init cndidate, wheel ndx
        while True:
            if n not in sieve:                  # is not a multiple of previously recorded primes
                if n < q: yield (n, ni)         # n is prime with wheel modulo index
                else:
                    npi = pi + 1                # advance wheel index
                    if npi > 47: npi = 0
                    sieve[q + p * gaps[pi]] = (p, npi) # n == p * p: put next cull position on wheel
                    p, pi = next(bps); q = p * p  # advance next prime and prime square to put
            else:
                s, si = sieve.pop(n)
                nxt = n + s * gaps[si]          # move current cull position up the wheel
                si = si + 1                     # advance wheel index
                if si > 47: si = 0
                while nxt in sieve:             # ensure each entry is unique by wheel
                    nxt += s * gaps[si]
                    si = si + 1                 # advance wheel index
                    if si > 47: si = 0
                sieve[nxt] = (s, si)            # next non-marked multiple of a prime
            nni = ni + 1                        # advance wheel index
            if nni > 47: nni = 0
            n += gaps[ni]; ni = nni             # advance on the wheel
    for p, pi in wheel_prime_pairs(): yield p   # strip out indexes

```

### python_code_15.txt
```python
def primes():
    whlPrms = [2,3,5,7,11,13,17]                # base wheel primes
    for p in whlPrms: yield p
    def makeGaps():
        buf = [True] * (3 * 5 * 7 * 11 * 13 * 17 + 1) # all odds plus extra for o/f
        for p in whlPrms:
            if p < 3:
                continue              # no need to handle evens
            strt = (p * p - 19) >> 1            # start position (divided by 2 using shift)
            while strt < 0: strt += p
            buf[strt::p] = [False] * ((len(buf) - strt - 1) // p + 1) # cull for p
        whlPsns = [i + i for i,v in enumerate(buf) if v]
        return [whlPsns[i + 1] - whlPsns[i] for i in range(len(whlPsns) - 1)]
    gaps = makeGaps()                           # big wheel gaps
    def wheel_prime_pairs():
        yield (19,0); bps = wheel_prime_pairs() # additional primes supply
        p, pi = next(bps); q = p * p            # adv to get 11 sqr'd is 121 as next square to put
        sieve = {}; n = 23; ni = 1              #   into sieve dict; init cndidate, wheel ndx
        while True:
            if n not in sieve:                  # is not a multiple of previously recorded primes
                if n < q: yield (n, ni)         # n is prime with wheel modulo index
                else:
                    npi = pi + 1                # advance wheel index
                    if npi > 92159: npi = 0
                    sieve[q + p * gaps[pi]] = (p, npi) # n == p * p: put next cull position on wheel
                    p, pi = next(bps); q = p * p  # advance next prime and prime square to put
            else:
                s, si = sieve.pop(n)
                nxt = n + s * gaps[si]          # move current cull position up the wheel
                si = si + 1                     # advance wheel index
                if si > 92159: si = 0
                while nxt in sieve:             # ensure each entry is unique by wheel
                    nxt += s * gaps[si]
                    si = si + 1                 # advance wheel index
                    if si > 92159: si = 0
                sieve[nxt] = (s, si)            # next non-marked multiple of a prime
            nni = ni + 1                        # advance wheel index
            if nni > 92159: nni = 0
            n += gaps[ni]; ni = nni             # advance on the wheel
    for p, pi in wheel_prime_pairs(): yield p   # strip out indexes

```

### python_code_2.txt
```python
def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

print(list(eratosthenes2(100)))

```

### python_code_3.txt
```python
def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1) 
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

```

### python_code_4.txt
```python
def iprimes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in xrange(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n * n, limit + 1, n): # start at ``n`` squared
                is_prime[i] = False
    for i in xrange(limit + 1):
        if is_prime[i]: yield i

```

### python_code_5.txt
```python
>>> list(iprimes_upto(15))
[2, 3, 5, 7, 11, 13]

```

### python_code_6.txt
```python
def primes2(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]

```

### python_code_7.txt
```python
def iprimes2(limit):
    yield 2
    if limit < 3: return
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    for i in range(lmtbf + 1):
        if buf[i]: yield (i + i + 3)

```

### python_code_8.txt
```python
def primes235(limit):
    yield 2; yield 3; yield 5
    if limit < 7: return
    modPrms = [7,11,13,17,19,23,29,31]
    gaps = [4,2,4,2,4,6,2,6,4,2,4,2,4,6,2,6] # 2 loops for overflow
    ndxs = [0,0,0,0,1,1,2,2,2,2,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,7]
    lmtbf = (limit + 23) // 30 * 8 - 1 # integral number of wheels rounded up
    lmtsqrt = (int(limit ** 0.5) - 7)
    lmtsqrt = lmtsqrt // 30 * 8 + ndxs[lmtsqrt % 30] # round down on the wheel
    buf = [True] * (lmtbf + 1)
    for i in range(lmtsqrt + 1):
        if buf[i]:
            ci = i & 7; p = 30 * (i >> 3) + modPrms[ci]
            s = p * p - 7; p8 = p << 3
            for j in range(8):
                c = s // 30 * 8 + ndxs[s % 30]
                buf[c::p8] = [False] * ((lmtbf - c) // p8 + 1)
                s += p * gaps[ci]; ci += 1
    for i in range(lmtbf - 6 + (ndxs[(limit - 7) % 30])): # adjust for extras
        if buf[i]: yield (30 * (i >> 3) + modPrms[i & 7])

```

### python_code_9.txt
```python
import numpy
def primes_upto2(limit):
    is_prime = numpy.ones(limit + 1, dtype=numpy.bool)
    for n in xrange(2, int(limit**0.5 + 1.5)): 
        if is_prime[n]:
            is_prime[n*n::n] = 0
    return numpy.nonzero(is_prime)[0][2:]

```

