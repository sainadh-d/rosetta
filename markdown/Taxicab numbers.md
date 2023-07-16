# Taxicab numbers

## Task Link
[Rosetta Code - Taxicab numbers](https://rosettacode.org/wiki/Taxicab_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.PriorityQueue;
import java.util.ArrayList;
import java.util.List;
import java.util.Iterator;

class CubeSum implements Comparable<CubeSum> {
	public long x, y, value;

	public CubeSum(long x, long y) {
		this.x = x;
		this.y = y;
		this.value = x*x*x + y*y*y;
	}

	public String toString() {
		return String.format("%4d^3 + %4d^3", x, y);
	}

	public int compareTo(CubeSum that) {
		return value < that.value ? -1 : value > that.value ? 1 : 0;
	}
}

class SumIterator implements Iterator<CubeSum> {
	PriorityQueue<CubeSum> pq = new PriorityQueue<CubeSum>();
	long n = 0;

	public boolean hasNext() { return true; }
	public CubeSum next() {
		while (pq.size() == 0 || pq.peek().value >= n*n*n)
			pq.add(new CubeSum(++n, 1));

		CubeSum s = pq.remove();
		if (s.x > s.y + 1) pq.add(new CubeSum(s.x, s.y+1));

		return s;
	}
}

class TaxiIterator implements Iterator<List<CubeSum>> {
	Iterator<CubeSum> sumIterator = new SumIterator();
	CubeSum last = sumIterator.next();

	public boolean hasNext() { return true; }
	public List<CubeSum> next() {
		CubeSum s;
		List<CubeSum> train = new ArrayList<CubeSum>();

		while ((s = sumIterator.next()).value != last.value)
			last = s;

		train.add(last);

		do { train.add(s); } while ((s = sumIterator.next()).value == last.value);
		last = s;

		return train;
	}
}
	
public class Taxi {
	public static final void main(String[] args) {
		Iterator<List<CubeSum>> taxi = new TaxiIterator();

		for (int i = 1; i <= 2006; i++) {
			List<CubeSum> t = taxi.next();
			if (i > 25 && i < 2000) continue;

			System.out.printf("%4d: %10d", i, t.get(0).value);
			for (CubeSum s: t)
				System.out.print(" = " + s);
			System.out.println();
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
from collections import defaultdict
from itertools import product
from pprint import pprint as pp

cube2n = {x**3:x for x in range(1, 1201)}
sum2cubes = defaultdict(set)
for c1, c2 in product(cube2n, cube2n):
	if c1 >= c2: sum2cubes[c1 + c2].add((cube2n[c1], cube2n[c2]))
	
taxied = sorted((k, v) for k,v in sum2cubes.items() if len(v) >= 2)

#pp(len(taxied))  # 2068
for t in enumerate(taxied[:25], 1):
    pp(t)
print('...')    
for t in enumerate(taxied[2000-1:2000+6], 2000):
    pp(t)

```

### python_code_2.txt
```python
cubes, crev = [x**3 for x in range(1,1200)], {}
# for cube root lookup
for x,x3 in enumerate(cubes): crev[x3] = x + 1

sums = sorted(x+y for x in cubes for y in cubes if y < x)

idx = 0
for i in range(1, len(sums)-1):
    if sums[i-1] != sums[i] and sums[i] == sums[i+1]:
        idx += 1
        if idx > 25 and idx < 2000 or idx > 2006: continue

        n,p = sums[i],[]
        for x in cubes:
            if n-x < x: break
            if n-x in crev:
                p.append((crev[x], crev[n-x]))
        print "%4d: %10d"%(idx,n),
        for x in p: print " = %4d^3 + %4d^3"%x,
        print

```

### python_code_3.txt
```python
from heapq import heappush, heappop

def cubesum():
    h,n = [],1
    while True:
        while not h or h[0][0] > n**3: # could also pre-calculate cubes
            heappush(h, (n**3 + 1, n, 1))
            n += 1

        (s, x, y) = heappop(h)
        yield((s, x, y))
        y += 1
        if y < x:    # should be y <= x?
            heappush(h, (x**3 + y**3, x, y))

def taxis():
    out = [(0,0,0)]
    for s in cubesum():
        if s[0] == out[-1][0]:
            out.append(s)
        else:
            if len(out) > 1: yield(out)
            out = [s]

n = 0
for x in taxis():
    n += 1
    if n >= 2006: break
    if n <= 25 or n >= 2000:
        print(n, x)

```

