# Hamming numbers

## Task Link
[Rosetta Code - Hamming numbers](https://rosettacode.org/wiki/Hamming_numbers)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.PriorityQueue;

final class Hamming {
    private static BigInteger THREE = BigInteger.valueOf(3);
    private static BigInteger FIVE = BigInteger.valueOf(5);

    private static void updateFrontier(BigInteger x,
                                       PriorityQueue<BigInteger> pq) {
        pq.offer(x.shiftLeft(1));
        pq.offer(x.multiply(THREE));
        pq.offer(x.multiply(FIVE));
    }

    public static BigInteger hamming(int n) {
        if (n <= 0)
            throw new IllegalArgumentException("Invalid parameter");
        PriorityQueue<BigInteger> frontier = new PriorityQueue<BigInteger>();
        updateFrontier(BigInteger.ONE, frontier);
        BigInteger lowest = BigInteger.ONE;
        for (int i = 1; i < n; i++) {
            lowest = frontier.poll();
            while (frontier.peek().equals(lowest))
                frontier.poll();
            updateFrontier(lowest, frontier);
        }
        return lowest;
    }

    public static void main(String[] args) {
        System.out.print("Hamming(1 .. 20) =");
        for (int i = 1; i < 21; i++)
             System.out.print(" " + hamming(i));
        System.out.println("\nHamming(1691) = " + hamming(1691));
        System.out.println("Hamming(1000000) = " + hamming(1000000));
    }
}

```

### java_code_2.txt
```java
import java.math.BigInteger;
import java.util.*;


public class HammingTriple implements Comparable<HammingTriple> {

    // Precompute a couple of constants that we need all the time
    private static final BigInteger two = BigInteger.valueOf(2);
    private static final BigInteger three = BigInteger.valueOf(3);
    private static final BigInteger five = BigInteger.valueOf(5);
    private static final double logOf2 = Math.log(2);
    private static final double logOf3 = Math.log(3);
    private static final double logOf5 = Math.log(5);
        
    // The powers of this triple
    private int a, b, c;
      
    public HammingTriple(int a, int b, int c) {
        this.a = a; this.b = b; this.c = c;
    }
    
    public String toString() {
        return "[" + a + ", " + b + ", " + c + "]";
    }
    
    public BigInteger getValue() {
        return two.pow(a).multiply(three.pow(b)).multiply(five.pow(c));
    }
    
    public boolean equals(Object other) {
        if(other instanceof HammingTriple) {
            HammingTriple h = (HammingTriple) other;
            return this.a == h.a && this.b == h.b && this.c == h.c;
        }
        else { return false; }
    }
    
    // Return 0 if this == other, +1 if this > other, and -1 if this < other
    public int compareTo(HammingTriple other) {
        // equality
        if(this.a == other.a && this.b == other.b && this.c == other.c) {
            return 0;
        }
        // this dominates
        if(this.a >= other.a && this.b >= other.b && this.c >= other.c) {
            return +1;
        }
        // other dominates
        if(this.a <= other.a && this.b <= other.b && this.c <= other.c) {
            return -1;
        }
       
        // take the logarithms for comparison
        double log1 = this.a * logOf2 + this.b * logOf3 + this.c * logOf5;
        double log2 = other.a * logOf2 + other.b * logOf3 + other.c * logOf5;
        
        // are these different enough to be reliable?
        if(Math.abs(log1 - log2) > 0.0000001) {
            return (log1 < log2) ? -1: +1;
        }
        
        // oh well, looks like we have to do this the hard way
        return this.getValue().compareTo(other.getValue());
        // (getting this far should be pretty rare, though)
    }
    
    public static BigInteger computeHamming(int n, boolean verbose) {
        if(verbose) {
            System.out.println("Hamming number #" + n);
        }
        long startTime = System.currentTimeMillis();
        
        // The elements of the search frontier
        PriorityQueue<HammingTriple> frontierQ = new PriorityQueue<HammingTriple>();
        int maxFrontierSize = 1;
        
        // Initialize the frontier
        frontierQ.offer(new HammingTriple(0, 0, 0)); // 1
        
        while(true) {
            if(frontierQ.size() > maxFrontierSize) {
                maxFrontierSize = frontierQ.size();
            }
            // Pop out the next Hamming number from the frontier
            HammingTriple curr = frontierQ.poll();
            
            if(--n == 0) {
                if(verbose) {
                    System.out.println("Time: " + (System.currentTimeMillis() - startTime) + " ms");
                    System.out.println("Frontier max size: " + maxFrontierSize);
                    System.out.println("As powers: " + curr.toString());
                    System.out.println("As value: " + curr.getValue());
                }
                return curr.getValue();
            }
            
            // Current times five, if at origin in (a,b) plane
            if(curr.a == 0 && curr.b == 0) {
                frontierQ.offer(new HammingTriple(curr.a, curr.b, curr.c + 1));
            }
            // Current times three, if at line a == 0
            if(curr.a == 0) {
                frontierQ.offer(new HammingTriple(curr.a, curr.b + 1, curr.c));
            }
            // Current times two, unconditionally
            curr.a++;
            frontierQ.offer(curr); // reuse the current HammingTriple object
        }
    }
}

```

### java_code_3.txt
```java
import java.math.BigInteger;

public class Hamming
{
    public static void main(String args[])
    {
        Stream hamming = makeHamming();
        System.out.print("H[1..20] ");
        for (int i=0; i<20; i++) {
            System.out.print(hamming.value());
            System.out.print(" ");
            hamming = hamming.advance();
        }
        System.out.println();

        System.out.print("H[1691] ");
        hamming = makeHamming();
        for (int i=1; i<1691; i++) {
            hamming = hamming.advance();
        }
        System.out.println(hamming.value());

        hamming = makeHamming();
        System.out.print("H[10^6] ");
        for (int i=1; i<1000000; i++) {
            hamming = hamming.advance();
        }
        System.out.println(hamming.value());
    }

    public interface Stream
    {
        BigInteger value();
        Stream advance();
    }

    public static class MultStream implements Stream
    {
        MultStream(int mult)
        { m_mult = BigInteger.valueOf(mult); }
        MultStream setBase(Stream s)
        { m_base = s; return this; }
        public BigInteger value()
        { return m_mult.multiply(m_base.value()); }
        public Stream advance()
        { return setBase(m_base.advance()); }

        private final BigInteger m_mult;
        private Stream m_base;
    }

    private final static class RegularStream implements Stream
    {
        RegularStream(Stream[] streams, BigInteger val)
        {
            m_streams = streams;
            m_val = val;
        }
        public BigInteger value()
        { return m_val; }

        public Stream advance()
        {
            // memoized value for the next stream instance.
            if (m_advance != null) { return m_advance; }

            int minidx = 0 ;
            BigInteger next = nextStreamValue(0);
            for (int i=1; i<m_streams.length; i++) {
                BigInteger v = nextStreamValue(i);
                if (v.compareTo(next) < 0) {
                    next = v;
                    minidx = i;
                }
            }
            RegularStream ret = new RegularStream(m_streams, next);
            // memoize the value!
            m_advance = ret;
            m_streams[minidx].advance();
            return ret;
        }
        private BigInteger nextStreamValue(int streamidx)
        {
            // skip past duplicates in the streams we're merging.
            BigInteger ret = m_streams[streamidx].value();
            while (ret.equals(m_val)) {
                m_streams[streamidx] = m_streams[streamidx].advance();
                ret = m_streams[streamidx].value();
            }
            return ret;
        }
        private final Stream[] m_streams;
        private final BigInteger m_val;
        private RegularStream m_advance = null;
    }

    private final static Stream makeHamming()
    {
        MultStream nums[] = new MultStream[] {
            new MultStream(2),
            new MultStream(3),
            new MultStream(5)
        };
        Stream ret = new RegularStream(nums, BigInteger.ONE);
        for (int i=0; i<nums.length; i++) {
            nums[i].setBase(ret);
        }
        return ret;
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import islice

def hamming2():
    '''\
    This version is based on a snippet from:
        https://web.archive.org/web/20081219014725/http://dobbscodetalk.com:80
                         /index.php?option=com_content&task=view&id=913&Itemid=85
        http://www.drdobbs.com/architecture-and-design/hamming-problem/228700538
        Hamming problem
        Written by Will Ness
        December 07, 2008

        When expressed in some imaginary pseudo-C with automatic
        unlimited storage allocation and BIGNUM arithmetics, it can be
        expressed as:
            hamming = h where
              array h;
              n=0; h[0]=1; i=0; j=0; k=0;
              x2=2*h[ i ]; x3=3*h[j]; x5=5*h[k];
              repeat:
                h[++n] = min(x2,x3,x5);
                if (x2==h[n]) { x2=2*h[++i]; }
                if (x3==h[n]) { x3=3*h[++j]; }
                if (x5==h[n]) { x5=5*h[++k]; } 
    '''
    h = 1
    _h=[h]    # memoized
    multipliers  = (2, 3, 5)
    multindeces  = [0 for i in multipliers] # index into _h for multipliers
    multvalues   = [x * _h[i] for x,i in zip(multipliers, multindeces)]
    yield h
    while True:
        h = min(multvalues)
        _h.append(h)
        for (n,(v,x,i)) in enumerate(zip(multvalues, multipliers, multindeces)):
            if v == h:
                i += 1
                multindeces[n] = i
                multvalues[n]  = x * _h[i]
        # cap the memoization
        mini = min(multindeces)
        if mini >= 1000:
            del _h[:mini]
            multindeces = [i - mini for i in multindeces]
        #
        yield h

```

### python_code_2.txt
```python
import psyco

def hamming(limit):
    h = [1] * limit
    x2, x3, x5 = 2, 3, 5
    i = j = k = 0

    for n in xrange(1, limit):
        h[n] = min(x2, x3, x5)
        if x2 == h[n]:
            i += 1
            x2 = 2 * h[i]
        if x3 == h[n]:
            j += 1
            x3 = 3 * h[j]
        if x5 == h[n]:
            k += 1
            x5 = 5 * h[k]

    return h[-1]

psyco.bind(hamming)
print [hamming(i) for i in xrange(1, 21)]
print hamming(1691)
print hamming(1000000)

```

### python_code_3.txt
```python
from heapq import heappush, heappop
from itertools import islice

def h():
    heap = [1]
    while True:
        h = heappop(heap)
        while heap and h==heap[0]:
            heappop(heap)
        for m in [2,3,5]:
            heappush(heap, m*h)
        yield h

print list(islice(h(), 20))
print list(islice(h(), 1690, 1691))
print list(islice(h(), 999999, 1000000)) # runtime 9.5 sec on i5-3570S

```

### python_code_4.txt
```python
from itertools import tee, chain, groupby, islice
from heapq import merge

def raymonds_hamming():
    # Generate "5-smooth" numbers, also called "Hamming numbers"
    # or "Regular numbers".  See: http://en.wikipedia.org/wiki/Regular_number
    # Finds solutions to 2**i * 3**j * 5**k  for some integers i, j, and k.

    def deferred_output():
        for i in output:
            yield i

    result, p2, p3, p5 = tee(deferred_output(), 4)
    m2 = (2*x for x in p2)                          # multiples of 2
    m3 = (3*x for x in p3)                          # multiples of 3
    m5 = (5*x for x in p5)                          # multiples of 5
    merged = merge(m2, m3, m5)
    combined = chain([1], merged)                   # prepend a starting point
    output = (k for k,g in groupby(combined))       # eliminate duplicates

    return result

print list(islice(raymonds_hamming(), 20))
print islice(raymonds_hamming(), 1689, 1690).next()
print islice(raymonds_hamming(), 999999, 1000000).next()

```

### python_code_5.txt
```python
from heapq import merge
from itertools import tee

def hamming_numbers():
    last = 1
    yield last

    a,b,c = tee(hamming_numbers(), 3)

    for n in merge((2*i for i in a), (3*i for i in b), (5*i for i in c)):
        if n != last:
            yield n
            last = n

```

### python_code_6.txt
```python
from itertools import islice, chain, tee

def merge(r, s):
    # This is faster than heapq.merge.
    rr = r.next()
    ss = s.next()
    while True:
        if rr < ss:
            yield rr
            rr = r.next()
        else:
            yield ss
            ss = s.next()

def p(n):
    def gen():
        x = n
        while True:
            yield x
            x *= n
    return gen()

def pp(n, s):
    def gen():
        for x in (merge(s, chain([n], (n * y for y in fb)))):
            yield x
    r, fb = tee(gen())
    return r

def hamming(a, b = None):
    if not b:
        b = a + 1
    seq = (chain([1], pp(5, pp(3, p(2)))))
    return list(islice(seq, a - 1, b - 1))

print hamming(1, 21)
print hamming(1691)[0]
print hamming(1000000)[0]

```

