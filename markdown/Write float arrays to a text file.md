# Write float arrays to a text file

## Task Link
[Rosetta Code - Write float arrays to a text file](https://rosettacode.org/wiki/Write_float_arrays_to_a_text_file)

## Java Code
### java_code_1.txt
```java
import java.io.*;

public class FloatArray {
    public static void writeDat(String filename, double[] x, double[] y,
                                int xprecision, int yprecision)
        throws IOException {
        assert x.length == y.length;
        PrintWriter out = new PrintWriter(filename);
        for (int i = 0; i < x.length; i++)
            out.printf("%."+xprecision+"g\t%."+yprecision+"g\n", x[i], y[i]);
        out.close();
    }

    public static void main(String[] args) {
        double[] x = {1, 2, 3, 1e11};
        double[] y = new double[x.length];
        for (int i = 0; i < x.length; i++)
            y[i] = Math.sqrt(x[i]);
        
        try {
            writeDat("sqrt.dat", x, y, 3, 5);
        } catch (IOException e) {
            System.err.println("writeDat: exception: "+e);
        }

        try {
            BufferedReader br = new BufferedReader(new FileReader("sqrt.dat"));
            String line;
            while ((line = br.readLine()) != null)
                System.out.println(line);
        } catch (IOException e) { }
    }
}

```

## Python Code
### python_code_1.txt
```python
import itertools
def writedat(filename, x, y, xprecision=3, yprecision=5):
    with open(filename,'w') as f:
        for a, b in itertools.izip(x, y):
            print >> f, "%.*g\t%.*g" % (xprecision, a, yprecision, b)

```

### python_code_2.txt
```python
>>> import math
>>> x = [1, 2, 3, 1e11]
>>> y = map(math.sqrt, x)
>>> y
[1.0, 1.4142135623730951, 1.7320508075688772, 316227.76601683791]
>>> writedat("sqrt.dat", x, y)
>>> # check 
...
>>> for line in open('sqrt.dat'):
...   print line,
...
1       1
2       1.4142
3       1.7321
1e+011  3.1623e+005

```

### python_code_3.txt
```python
def writedat(filename, x, y, xprecision=3, yprecision=5):
    with open(filename,'w') as f:
        for a, b in zip(x, y):
            print("%.*g\t%.*g" % (xprecision, a, yprecision, b), file=f)
            #or, using the new-style formatting:
            #print("{1:.{0}g}\t{3:.{2}g}".format(xprecision, a, yprecision, b), file=f)

```

