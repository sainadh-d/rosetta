# Knuth's algorithm S

## Task Link
[Rosetta Code - Knuth's algorithm S](https://rosettacode.org/wiki/Knuth%27s_algorithm_S)

## Java Code
### java_code_1.txt
```java
import java.util.*;
 
class SOfN<T> {
    private static final Random rand = new Random();
 
    private List<T> sample;
    private int i = 0;
    private int n;

    public SOfN(int _n) {
        n = _n;
        sample = new ArrayList<T>(n);
    }

    public List<T> process(T item) {
        if (++i <= n) {
            sample.add(item);
        } else if (rand.nextInt(i) < n) {
            sample.set(rand.nextInt(n), item);
        }
        return sample;
    }
}
 
public class AlgorithmS {
    public static void main(String[] args) {
        int[] bin = new int[10];
        for (int trial = 0; trial < 100000; trial++) {
            SOfN<Integer> s_of_n = new SOfN<Integer>(3);
            for (int i = 0; i < 9; i++) s_of_n.process(i);
            for (int s : s_of_n.process(9)) bin[s]++;
        }
        System.out.println(Arrays.toString(bin));
    }
}

```

### java_code_2.txt
```java
import java.util.*;
 
interface Function<S, T> {
    public T call(S x);
}
 
public class AlgorithmS {
    private static final Random rand = new Random();
    public static <T> Function<T, List<T>> s_of_n_creator(final int n) {
        return new Function<T, List<T>>() {
            private List<T> sample = new ArrayList<T>(n);
            private int i = 0;
            public List<T> call(T item) {
                if (++i <= n) {
                    sample.add(item);
                } else if (rand.nextInt(i) < n) {
                    sample.set(rand.nextInt(n), item);
                }
                return sample;
            }
        };
    }
 
    public static void main(String[] args) {
        int[] bin = new int[10];
        for (int trial = 0; trial < 100000; trial++) {
            Function<Integer, List<Integer>> s_of_n = s_of_n_creator(3);
            for (int i = 0; i < 9; i++) s_of_n.call(i);
            for (int s : s_of_n.call(9)) bin[s]++;
        }
        System.out.println(Arrays.toString(bin));
    }
}

```

## Python Code
### python_code_1.txt
```python
from random import randrange

def s_of_n_creator(n):
    sample, i = [], 0
    def s_of_n(item):
        nonlocal i

        i += 1
        if i <= n:
            # Keep first n items
            sample.append(item)
        elif randrange(i) < n:
            # Keep item
            sample[randrange(n)] = item
        return sample
    return s_of_n

if __name__ == '__main__':
    bin = [0]* 10
    items = range(10)
    print("Single run samples for n = 3:")
    s_of_n = s_of_n_creator(3)
    for item in items:
        sample = s_of_n(item)
        print("  Item: %i -> sample: %s" % (item, sample))
    #
    for trial in range(100000):
        s_of_n = s_of_n_creator(3)
        for item in items:
            sample = s_of_n(item)
        for s in sample:
            bin[s] += 1
    print("\nTest item frequencies for 100000 runs:\n ",
          '\n  '.join("%i:%i" % x for x in enumerate(bin)))

```

### python_code_2.txt
```python
class S_of_n_creator():
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.sample = []
    
    def __call__(self, item):
        self.i += 1
        n, i, sample = self.n, self.i, self.sample
        if i <= n:
            # Keep first n items
            sample.append(item)
        elif randrange(i) < n:
            # Keep item
            sample[randrange(n)] = item
        return sample

```

### python_code_3.txt
```python
s_of_n = S_of_n_creator(3)

```

