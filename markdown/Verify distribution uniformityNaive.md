# Verify distribution uniformity/Naive

## Task Link
[Rosetta Code - Verify distribution uniformity/Naive](https://rosettacode.org/wiki/Verify_distribution_uniformity/Naive)

## Java Code
### java_code_1.txt
```java
import static java.lang.Math.abs;
import java.util.*;
import java.util.function.IntSupplier;

public class Test {

    static void distCheck(IntSupplier f, int nRepeats, double delta) {
        Map<Integer, Integer> counts = new HashMap<>();

        for (int i = 0; i < nRepeats; i++)
            counts.compute(f.getAsInt(), (k, v) -> v == null ? 1 : v + 1);

        double target = nRepeats / (double) counts.size();
        int deltaCount = (int) (delta / 100.0 * target);

        counts.forEach((k, v) -> {
            if (abs(target - v) >= deltaCount)
                System.out.printf("distribution potentially skewed "
                        + "for '%s': '%d'%n", k, v);
        });

        counts.keySet().stream().sorted().forEach(k
                -> System.out.printf("%d %d%n", k, counts.get(k)));
    }

    public static void main(String[] a) {
        distCheck(() -> (int) (Math.random() * 5) + 1, 1_000_000, 1);
    }
}

```

## Python Code
### python_code_1.txt
```python
from collections import Counter
from pprint import pprint as pp

def distcheck(fn, repeats, delta):
    '''\
    Bin the answers to fn() and check bin counts are within +/- delta %
    of repeats/bincount'''
    bin = Counter(fn() for i in range(repeats))
    target = repeats // len(bin)
    deltacount = int(delta / 100. * target)
    assert all( abs(target - count) < deltacount
                for count in bin.values() ), "Bin distribution skewed from %i +/- %i: %s" % (
                    target, deltacount, [ (key, target - count)
                                          for key, count in sorted(bin.items()) ]
                    )
    pp(dict(bin))

```

