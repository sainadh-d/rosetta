# Hofstadter Figure-Figure sequences

## Task Link
[Rosetta Code - Hofstadter Figure-Figure sequences](https://rosettacode.org/wiki/Hofstadter_Figure-Figure_sequences)

## Java Code
### java_code_1.txt
```java
import java.util.*;

class Hofstadter
{
  private static List<Integer> getSequence(int rlistSize, int slistSize)
  {
    List<Integer> rlist = new ArrayList<Integer>();
    List<Integer> slist = new ArrayList<Integer>();
    Collections.addAll(rlist, 1, 3, 7);
    Collections.addAll(slist, 2, 4, 5, 6);
    List<Integer> list = (rlistSize > 0) ? rlist : slist;
    int targetSize = (rlistSize > 0) ? rlistSize : slistSize;
    while (list.size() > targetSize)
      list.remove(list.size() - 1);
    while (list.size() < targetSize)
    {
      int lastIndex = rlist.size() - 1;
      int lastr = rlist.get(lastIndex).intValue();
      int r = lastr + slist.get(lastIndex).intValue();
      rlist.add(Integer.valueOf(r));
      for (int s = lastr + 1; (s < r) && (list.size() < targetSize); s++)
        slist.add(Integer.valueOf(s));
    }
    return list;
  }
  
  public static int ffr(int n)
  {  return getSequence(n, 0).get(n - 1).intValue();  }
  
  public static int ffs(int n)
  {  return getSequence(0, n).get(n - 1).intValue();  }
  
  public static void main(String[] args)
  {
    System.out.print("R():");
    for (int n = 1; n <= 10; n++)
      System.out.print(" " + ffr(n));
    System.out.println();
    
    Set<Integer> first40R = new HashSet<Integer>();
    for (int n = 1; n <= 40; n++)
      first40R.add(Integer.valueOf(ffr(n)));
      
    Set<Integer> first960S = new HashSet<Integer>();
    for (int n = 1; n <= 960; n++)
      first960S.add(Integer.valueOf(ffs(n)));
    
    for (int i = 1; i <= 1000; i++)
    {
      Integer n = Integer.valueOf(i);
      if (first40R.contains(n) == first960S.contains(n))
        System.out.println("Integer " + i + " either in both or neither set");
    }
    System.out.println("Done");
  }
}

```

## Python Code
### python_code_1.txt
```python
def ffr(n):
    if n < 1 or type(n) != int: raise ValueError("n must be an int >= 1")
    try:
        return ffr.r[n]
    except IndexError:
        r, s = ffr.r, ffs.s
        ffr_n_1 = ffr(n-1)
        lastr = r[-1]
        # extend s up to, and one past, last r 
        s += list(range(s[-1] + 1, lastr))
        if s[-1] < lastr: s += [lastr + 1]
        # access s[n-1] temporarily extending s if necessary
        len_s = len(s)
        ffs_n_1 = s[n-1] if len_s > n else (n - len_s) + s[-1]
        ans = ffr_n_1 + ffs_n_1
        r.append(ans)
        return ans
ffr.r = [None, 1]

def ffs(n):
    if n < 1 or type(n) != int: raise ValueError("n must be an int >= 1")
    try:
        return ffs.s[n]
    except IndexError:
        r, s = ffr.r, ffs.s
        for i in range(len(r), n+2):
            ffr(i)
            if len(s) > n:
                return s[n]
        raise Exception("Whoops!")
ffs.s = [None, 2]

if __name__ == '__main__':
    first10 = [ffr(i) for i in range(1,11)]
    assert first10 == [1, 3, 7, 12, 18, 26, 35, 45, 56, 69], "ffr() value error(s)"
    print("ffr(n) for n = [1..10] is", first10)
    #
    bin = [None] + [0]*1000
    for i in range(40, 0, -1):
        bin[ffr(i)] += 1
    for i in range(960, 0, -1):
        bin[ffs(i)] += 1
    if all(b == 1 for b in bin[1:1000]):
        print("All Integers 1..1000 found OK")
    else:
        print("All Integers 1..1000 NOT found only once: ERROR")

```

### python_code_2.txt
```python
cR = [1]
cS = [2]

def extend_RS():
	x = cR[len(cR) - 1] + cS[len(cR) - 1]
	cR.append(x)
	cS += range(cS[-1] + 1, x)
	cS.append(x + 1)

def ff_R(n):
	assert(n > 0)
	while n > len(cR): extend_RS()
	return cR[n - 1]

def ff_S(n):
	assert(n > 0)
	while n > len(cS): extend_RS()
	return cS[n - 1]

# tests
print([ ff_R(i) for i in range(1, 11) ])

s = {}
for i in range(1, 1001): s[i] = 0
for i in range(1, 41):  del s[ff_R(i)]
for i in range(1, 961): del s[ff_S(i)]

# the fact that we got here without a key error
print("Ok")

```

### python_code_3.txt
```python
from itertools import islice

def R():
	n = 1
	yield n
	for s in S():
		n += s
		yield n;

def S():
	yield 2
	yield 4
	u = 5
	for r in R():
		if r <= u: continue;
		for x in range(u, r): yield x
		u = r + 1

def lst(s, n): return list(islice(s(), n))

print "R:", lst(R, 10)
print "S:", lst(S, 10)
print sorted(lst(R, 40) + lst(S, 960)) == list(range(1,1001))

# perf test case
# print sum(lst(R, 10000000))

```

