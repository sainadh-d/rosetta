# Matrix chain multiplication

## Task Link
[Rosetta Code - Matrix chain multiplication](https://rosettacode.org/wiki/Matrix_chain_multiplication)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class MatrixChainMultiplication {

    public static void main(String[] args) {
        runMatrixChainMultiplication(new int[] {5, 6, 3, 1});
        runMatrixChainMultiplication(new int[] {1, 5, 25, 30, 100, 70, 2, 1, 100, 250, 1, 1000, 2});
        runMatrixChainMultiplication(new int[] {1000, 1, 500, 12, 1, 700, 2500, 3, 2, 5, 14, 10});
    }
    
    private static void runMatrixChainMultiplication(int[] dims) {
        System.out.printf("Array Dimension  = %s%n", Arrays.toString(dims));
        System.out.printf("Cost             = %d%n", matrixChainOrder(dims));
        System.out.printf("Optimal Multiply = %s%n%n", getOptimalParenthesizations());
    }

    private static int[][]cost;
    private static int[][]order;
    
    public static int matrixChainOrder(int[] dims) {
        int n = dims.length - 1;
        cost = new int[n][n];
        order = new int[n][n];

        for (int lenMinusOne = 1 ; lenMinusOne < n ; lenMinusOne++) {
            for (int i = 0; i < n - lenMinusOne; i++) {
                int j = i + lenMinusOne;
                cost[i][j] = Integer.MAX_VALUE;
                for (int k = i; k < j; k++) {
                    int currentCost = cost[i][k] + cost[k+1][j] + dims[i]*dims[k+1]*dims[j+1];
                    if (currentCost < cost[i][j]) {
                        cost[i][j] = currentCost;
                        order[i][j] = k;
                    }
                }
            }
        }
        return cost[0][n-1];
    }

    private static String getOptimalParenthesizations() {
        return getOptimalParenthesizations(order, 0, order.length - 1);
    }
    
    private static String getOptimalParenthesizations(int[][]s, int i, int j) {
        if (i == j) {
            return String.format("%c", i+65);
        }
        else {
            StringBuilder sb = new StringBuilder();
            sb.append("(");
            sb.append(getOptimalParenthesizations(s, i, s[i][j]));
            sb.append(" * ");
            sb.append(getOptimalParenthesizations(s, s[i][j] + 1, j));
            sb.append(")");
            return sb.toString();
        }
    }

}

```

## Python Code
### python_code_1.txt
```python
def parens(n):
    def aux(n, k):
        if n == 1:
            yield k
        elif n == 2:
            yield [k, k + 1]
        else:
            a = []
            for i in range(1, n):
                for u in aux(i, k):
                    for v in aux(n - i, k + i):
                        yield [u, v]
    yield from aux(n, 0)

```

### python_code_2.txt
```python
for u in parens(4):
    print(u)

[0, [1, [2, 3]]]
[0, [[1, 2], 3]]
[[0, 1], [2, 3]]
[[0, [1, 2]], 3]
[[[0, 1], 2], 3]

```

### python_code_3.txt
```python
def optim1(a):
    def cost(k):
        if type(k) is int:
            return 0, a[k], a[k + 1]
        else:
            s1, p1, q1 = cost(k[0])
            s2, p2, q2 = cost(k[1])
            assert q1 == p2
            return s1 + s2 + p1 * q1 * q2, p1, q2
    cmin = None
    n = len(a) - 1
    for u in parens(n):
        c, p, q = cost(u)
        if cmin is None or c < cmin:
            cmin = c
            umin = u
    return cmin, umin

```

### python_code_4.txt
```python
def optim2(a):
    def aux(n, k):
        if n == 1:
            p, q = a[k:k + 2]
            return 0, p, q, k
        elif n == 2:
            p, q, r = a[k:k + 3]
            return p * q * r, p, r, [k, k + 1]
        else:
            m = None
            p = a[k]
            q = a[k + n]
            for i in range(1, n):
                s1, p1, q1, u1 = aux(i, k)
                s2, p2, q2, u2 = aux(n - i, k + i)
                assert q1 == p2
                s = s1 + s2 + p1 * q1 * q2
                if m is None or s < m:
                    m = s
                    u = [u1, u2]
            return m, p, q, u
    s, p, q, u = aux(len(a) - 1, 0)
    return s, u

```

### python_code_5.txt
```python
def memoize(f):
    h = {}
    def g(*u):
        if u in h:
            return h[u]
        else:
            r = f(*u)
            h[u] = r
            return r
    return g

def optim3(a):
    @memoize
    def aux(n, k):
        if n == 1:
            p, q = a[k:k + 2]
            return 0, p, q, k
        elif n == 2:
            p, q, r = a[k:k + 3]
            return p * q * r, p, r, [k, k + 1]
        else:
            m = None
            p = a[k]
            q = a[k + n]
            for i in range(1, n):
                s1, p1, q1, u1 = aux(i, k)
                s2, p2, q2, u2 = aux(n - i, k + i)
                assert q1 == p2
                s = s1 + s2 + p1 * q1 * q2
                if m is None or s < m:
                    m = s
                    u = [u1, u2]
            return m, p, q, u
    s, p, q, u = aux(len(a) - 1, 0)
    return s, u

```

### python_code_6.txt
```python
import time

u = [[1, 5, 25, 30, 100, 70, 2, 1, 100, 250, 1, 1000, 2],
     [1000, 1, 500, 12, 1, 700, 2500, 3, 2, 5, 14, 10]]

for a in u:
    print(a)
    print()
    print("function     time       cost   parens  ")
    print("-" * 90)
    for f in [optim1, optim2, optim3]:
        t1 = time.clock()
        s, u = f(a)
        t2 = time.clock()
        print("%s %10.3f %10d   %s" % (f.__name__, 1000 * (t2 - t1), s, u))
    print()

```

### python_code_7.txt
```python
def optim4(a):
    global u
    n = len(a) - 1
    u = [None] * n
    u[0] = [[None, 0]] * n
    for j in range(1, n):
        v = [None] * (n - j)
        for i in range(n - j):
            m = None
            for k in range(j):
                s1, c1 = u[k][i]
                s2, c2 = u[j - k - 1][i + k + 1]
                c = c1 + c2 + a[i] * a[i + k + 1] * a[i + j + 1]
                if m is None or c < m:
                    s = k
                    m = c
            v[i] = [s, m]
        u[j] = v
    def aux(i, j):
        s, c = u[j][i]
        if s is None:
            return i
        else:
            return [aux(i, s), aux(i + s + 1, j - s - 1)]
    return u[n - 1][0][1], aux(0, n - 1)


print(optim4([1, 5, 25, 30, 100, 70, 2, 1, 100, 250, 1, 1000, 2]))
print(optim4([1000, 1, 500, 12, 1, 700, 2500, 3, 2, 5, 14, 10]))

```

