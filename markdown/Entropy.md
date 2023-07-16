# Entropy

## Task Link
[Rosetta Code - Entropy](https://rosettacode.org/wiki/Entropy)

## Java Code
### java_code_1.txt
```java
import java.lang.Math;
import java.util.Map;
import java.util.HashMap;

public class REntropy {

  @SuppressWarnings("boxing")
  public static double getShannonEntropy(String s) {
    int n = 0;
    Map<Character, Integer> occ = new HashMap<>();

    for (int c_ = 0; c_ < s.length(); ++c_) {
      char cx = s.charAt(c_);
      if (occ.containsKey(cx)) {
        occ.put(cx, occ.get(cx) + 1);
      } else {
        occ.put(cx, 1);
      }
      ++n;
    }

    double e = 0.0;
    for (Map.Entry<Character, Integer> entry : occ.entrySet()) {
      char cx = entry.getKey();
      double p = (double) entry.getValue() / n;
      e += p * log2(p);
    }
    return -e;
  }

  private static double log2(double a) {
    return Math.log(a) / Math.log(2);
  }
  public static void main(String[] args) {
    String[] sstr = {
      "1223334444",
      "1223334444555555555", 
      "122333", 
      "1227774444",
      "aaBBcccDDDD",
      "1234567890abcdefghijklmnopqrstuvwxyz",
      "Rosetta Code",
    };

    for (String ss : sstr) {
      double entropy = REntropy.getShannonEntropy(ss);
      System.out.printf("Shannon entropy of %40s: %.12f%n", "\"" + ss + "\"", entropy);
    }
    return;
  }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import division
import math

def hist(source):
    hist = {}; l = 0;
    for e in source:
        l += 1
        if e not in hist:
            hist[e] = 0
        hist[e] += 1
    return (l,hist)

def entropy(hist,l):
    elist = []
    for v in hist.values():
        c = v / l
        elist.append(-c * math.log(c ,2))
    return sum(elist)

def printHist(h):
    flip = lambda (k,v) : (v,k)
    h = sorted(h.iteritems(), key = flip)
    print 'Sym\thi\tfi\tInf'
    for (k,v) in h:
        print '%s\t%f\t%f\t%f'%(k,v,v/l,-math.log(v/l, 2))
    
    

source = "1223334444"
(l,h) = hist(source);
print '.[Results].'
print 'Length',l
print 'Entropy:', entropy(h, l)
printHist(h)

```

### python_code_2.txt
```python
from math import log2
from collections import Counter

def entropy(s):
    p, lns = Counter(s), float(len(s))
    return log2(lns) - sum(count * log2(count) for count in p.values()) / lns

print(entropy("1223334444"))

```

### python_code_3.txt
```python
def Entropy(text):
    import math
    log2=lambda x:math.log(x)/math.log(2)
    exr={}
    infoc=0
    for each in text:
        try:
            exr[each]+=1
        except:
            exr[each]=1
    textlen=len(text)
    for k,v in exr.items():
        freq  =  1.0*v/textlen
        infoc+=freq*log2(freq)
    infoc*=-1
    return infoc

while True:
    print Entropy(raw_input('>>>'))

```

