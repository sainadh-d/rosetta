# Jensen's Device

## Task Link
[Rosetta Code - Jensen's Device](https://rosettacode.org/wiki/Jensen%27s_Device)

## Java Code
### java_code_1.txt
```java
import java.util.function.*;
import java.util.stream.*;

public class Jensen {
    static double sum(int lo, int hi, IntToDoubleFunction f) {
        return IntStream.rangeClosed(lo, hi).mapToDouble(f).sum();
    }
        
    public static void main(String args[]) {
        System.out.println(sum(1, 100, (i -> 1.0/i)));
    }
}

```

### java_code_2.txt
```java
public class Jensen2 {

    interface IntToDoubleFunction {
        double apply(int n);
    }

    static double sum(int lo, int hi, IntToDoubleFunction f) {
        double res = 0;
        for (int i = lo; i <= hi; i++)
            res += f.apply(i);
        return res;

    }
    public static void main(String args[]) {
        System.out.println(
            sum(1, 100,
                new IntToDoubleFunction() {
                    public double apply(int i) { return 1.0/i;}
                }));
    }
}

```

## Python Code
### python_code_1.txt
```python
class Ref(object):
    def __init__(self, value=None):
        self.value = value

def harmonic_sum(i, lo, hi, term):
    # term is passed by-name, and so is i
    temp = 0
    i.value = lo
    while i.value <= hi:  # Python "for" loop creates a distinct which
        temp += term() # would not be shared with the passed "i"
        i.value += 1   # Here the actual passed "i" is incremented.
    return temp

i = Ref()

# note the correspondence between the mathematical notation and the
# call to sum it's almost as good as sum(1/i for i in range(1,101))
print harmonic_sum(i, 1, 100, lambda: 1.0/i.value)

```

### python_code_2.txt
```python
def harmonic_sum(i, lo, hi, term):
    return sum(term() for i[0] in range(lo, hi + 1))
 
i = [0]
print(harmonic_sum(i, 1, 100, lambda: 1.0 / i[0]))

```

### python_code_3.txt
```python
def harmonic_sum(i, lo, hi, term):
    return sum(eval(term) for i[0] in range(lo, hi + 1))
 
i = [0]
print(harmonic_sum(i, 1, 100, "1.0 / i[0]"))

```

