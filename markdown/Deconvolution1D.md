# Deconvolution/1D

## Task Link
[Rosetta Code - Deconvolution/1D](https://rosettacode.org/wiki/Deconvolution/1D)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class Deconvolution1D {
    public static int[] deconv(int[] g, int[] f) {
        int[] h = new int[g.length - f.length + 1];
        for (int n = 0; n < h.length; n++) {
            h[n] = g[n];
            int lower = Math.max(n - f.length + 1, 0);
            for (int i = lower; i < n; i++)
                h[n] -= h[i] * f[n - i];
            h[n] /= f[0];
        }
        return h;
    }

    public static void main(String[] args) {
        int[] h = { -8, -9, -3, -1, -6, 7 };
        int[] f = { -3, -6, -1, 8, -6, 3, -1, -9, -9, 3, -2, 5, 2, -2, -7, -1 };
        int[] g = { 24, 75, 71, -34, 3, 22, -45, 23, 245, 25, 52, 25, -67, -96,
                96, 31, 55, 36, 29, -43, -7 };

        StringBuilder sb = new StringBuilder();
        sb.append("h = " + Arrays.toString(h) + "\n");
        sb.append("deconv(g, f) = " + Arrays.toString(deconv(g, f)) + "\n");
        sb.append("f = " + Arrays.toString(f) + "\n");
        sb.append("deconv(g, h) = " + Arrays.toString(deconv(g, h)) + "\n");
        System.out.println(sb.toString());
    }
}

```

## Python Code
### python_code_1.txt
```python
def ToReducedRowEchelonForm( M ):
    if not M: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        M[r] = [ mrx / lv for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1
    return M
 
def pmtx(mtx):
    print ('\n'.join(''.join(' %4s' % col for col in row) for row in mtx))
 
def convolve(f, h):
    g = [0] * (len(f) + len(h) - 1)
    for hindex, hval in enumerate(h):
        for findex, fval in enumerate(f):
            g[hindex + findex] += fval * hval
    return g

def deconvolve(g, f):
    lenh = len(g) - len(f) + 1
    mtx = [[0 for x in range(lenh+1)] for y in g]
    for hindex in range(lenh):
        for findex, fval in enumerate(f):
            gindex = hindex + findex
            mtx[gindex][hindex] = fval
    for gindex, gval in enumerate(g):        
        mtx[gindex][lenh] = gval
    ToReducedRowEchelonForm( mtx )
    return [mtx[i][lenh] for i in range(lenh)]  # h

if __name__ == '__main__':
    h = [-8,-9,-3,-1,-6,7]
    f = [-3,-6,-1,8,-6,3,-1,-9,-9,3,-2,5,2,-2,-7,-1]
    g = [24,75,71,-34,3,22,-45,23,245,25,52,25,-67,-96,96,31,55,36,29,-43,-7]
    assert convolve(f,h) == g
    assert deconvolve(g, f) == h

```

### python_code_2.txt
```python
import numpy

h = [-8,-9,-3,-1,-6,7]
f = [-3,-6,-1,8,-6,3,-1,-9,-9,3,-2,5,2,-2,-7,-1]
g = [24,75,71,-34,3,22,-45,23,245,25,52,25,-67,-96,96,31,55,36,29,-43,-7]

# https://stackoverflow.com/questions/14267555/find-the-smallest-power-of-2-greater-than-n-in-python

def shift_bit_length(x):
    return 1<<(x-1).bit_length()

def conv(a, b):
    p = len(a)
    q = len(b)
    n = p + q - 1
    r = shift_bit_length(n)
    y = numpy.fft.ifft(numpy.fft.fft(a,r) * numpy.fft.fft(b,r),r)
    return numpy.trim_zeros(numpy.around(numpy.real(y),decimals=6))

def deconv(a, b):
    p = len(a)
    q = len(b)
    n = p - q + 1
    r = shift_bit_length(max(p, q))
    y = numpy.fft.ifft(numpy.fft.fft(a,r) / numpy.fft.fft(b,r), r)
    return numpy.trim_zeros(numpy.around(numpy.real(y),decimals=6))
    
# should return g
   
print(conv(h,f))

# should return h

print(deconv(g,f))

# should return f

print(deconv(g,h))

```

