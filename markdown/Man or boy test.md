# Man or boy test

## Task Link
[Rosetta Code - Man or boy test](https://rosettacode.org/wiki/Man_or_boy_test)

## Java Code
### java_code_1.txt
```java
import java.util.function.DoubleSupplier;

public class ManOrBoy {
    
    static double A(int k, DoubleSupplier x1, DoubleSupplier x2,
                 DoubleSupplier x3, DoubleSupplier x4, DoubleSupplier x5) {
        
        DoubleSupplier B = new DoubleSupplier() {
            int m = k;
            public double getAsDouble() {
                return A(--m, this, x1, x2, x3, x4);
            }
        };
                
        return k <= 0 ? x4.getAsDouble() + x5.getAsDouble() : B.getAsDouble();
    }
    
    public static void main(String[] args) {
        System.out.println(A(10, () -> 1.0, () -> -1.0, () -> -1.0, () -> 1.0, () -> 0.0));
    }
}

```

### java_code_2.txt
```java
public class ManOrBoy {
    interface Arg {
        public int run();
    }

    public static int A(final int k, final Arg x1, final Arg x2,
                          final Arg x3, final Arg x4, final Arg x5) {
        if (k <= 0)
            return x4.run() + x5.run();
        return new Arg() {
            int m = k;
            public int run() {
                m--;
                return A(m, this, x1, x2, x3, x4);
            }
        }.run();
    }
    public static Arg C(final int i) {
        return new Arg() {
            public int run() { return i; }
        };
    }

    public static void main(String[] args) {
        System.out.println(A(10, C(1), C(-1), C(-1), C(1), C(0)));
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python
import sys
sys.setrecursionlimit(1025)

def a(in_k, x1, x2, x3, x4, x5):
    k = [in_k]
    def b():
        k[0] -= 1
        return a(k[0], b, x1, x2, x3, x4)
    return x4() + x5() if k[0] <= 0 else b()

x = lambda i: lambda: i
print(a(10, x(1), x(-1), x(-1), x(1), x(0)))

```

### python_code_2.txt
```python
#!/usr/bin/env python
import sys
sys.setrecursionlimit(1025)

def a(k, x1, x2, x3, x4, x5):
    def b():
        b.k -= 1
        return a(b.k, b, x1, x2, x3, x4)
    b.k = k
    return x4() + x5() if b.k <= 0 else b()

x = lambda i: lambda: i
print(a(10, x(1), x(-1), x(-1), x(1), x(0)))

```

### python_code_3.txt
```python
#!/usr/bin/env python
import sys
sys.setrecursionlimit(1025)

def A(k, x1, x2, x3, x4, x5):
    def B():
        nonlocal k
        k -= 1
        return A(k, B, x1, x2, x3, x4)
    return x4() + x5() if k <= 0 else B()

print(A(10, lambda: 1, lambda: -1, lambda: -1, lambda: 1, lambda: 0))

```

