# Hofstadter-Conway $10,000 sequence

## Task Link
[Rosetta Code - Hofstadter-Conway $10,000 sequence](https://rosettacode.org/wiki/Hofstadter-Conway_$10,000_sequence)

## Java Code
### java_code_1.txt
```java
//  Title:  Hofstadter-Conway $10,000 sequence

public class HofstadterConwaySequence {

    private static int MAX = (int) Math.pow(2, 20) + 1;
    private static int[] HCS = new int[MAX];
    static {
        HCS[1] = 1;
        HCS[2] = 1;
        for ( int n = 3 ; n < MAX ; n++ ) {
            int nm1 = HCS[n - 1];
            HCS[n] = HCS[nm1] + HCS[n - nm1];
        }
    }
    
    public static void main(String[] args) {
        int mNum = 0;
        for ( int m = 1 ; m < 20 ; m++ ) {
            int min = (int) Math.pow(2, m);
            int max = min * 2;
            double maxRatio = 0.0;
            int nVal = 0;
            for ( int n = min ; n <= max ; n ++ ) {
                double ratio = (double) HCS[n] / n;
                if ( ratio > maxRatio ) {
                    maxRatio = Math.max(ratio,  maxRatio);
                    nVal = n;
                }
                if ( ratio >= 0.55 ) {
                    mNum = n;
                }
            }
            System.out.printf("Max ratio between 2^%d and 2^%d is %f at n = %,d%n", m, m+1, maxRatio, nVal);
        }
        System.out.printf("Mallow's number is %d.%n", mNum);
    }

}

```

## Python Code
### python_code_1.txt
```python
from __future__ import division

def maxandmallows(nmaxpower2):
    nmax = 2**nmaxpower2
    mx = (0.5, 2)
    mxpow2 = []
    mallows = None

    # Hofstadter-Conway sequence starts at hc[1],
    # hc[0] is not part of the series.
    hc = [None, 1, 1]

    for n in range(2, nmax + 1):
        ratio = hc[n] / n
        if ratio > mx[0]:
            mx = (ratio, n)
        if ratio >= 0.55:
            mallows = n
        if ratio == 0.5:
            print("In the region %7i < n <= %7i: max a(n)/n = %6.4f at  n = %i" %
		  (n//2, n, mx[0], mx[1]))
            mxpow2.append(mx[0])
            mx = (ratio, n)
        hc.append(hc[hc[n]] + hc[-hc[n]])

    return hc, mallows if mxpow2 and mxpow2[-1] < 0.55 and n > 4 else None

if __name__ == '__main__':
    hc, mallows = maxandmallows(20)
    if mallows:
        print("\nYou too might have won $1000 with the mallows number of %i" % mallows)

```

