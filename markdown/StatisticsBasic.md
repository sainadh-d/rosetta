# Statistics/Basic

## Task Link
[Rosetta Code - Statistics/Basic](https://rosettacode.org/wiki/Statistics/Basic)

## Java Code
### java_code_1.txt
```java
import static java.lang.Math.pow;
import static java.util.Arrays.stream;
import static java.util.stream.Collectors.joining;
import static java.util.stream.IntStream.range;

public class Test {
    static double[] meanStdDev(double[] numbers) {
        if (numbers.length == 0)
            return new double[]{0.0, 0.0};

        double sx = 0.0, sxx = 0.0;
        long n = 0;
        for (double x : numbers) {
            sx += x;
            sxx += pow(x, 2);
            n++;
        }
        return new double[]{sx / n, pow((n * sxx - pow(sx, 2)), 0.5) / n};
    }

    static String replicate(int n, String s) {
        return range(0, n + 1).mapToObj(i -> s).collect(joining());
    }

    static void showHistogram01(double[] numbers) {
        final int maxWidth = 50;
        long[] bins = new long[10];

        for (double x : numbers)
            bins[(int) (x * bins.length)]++;

        double maxFreq = stream(bins).max().getAsLong();

        for (int i = 0; i < bins.length; i++)
            System.out.printf(" %3.1f: %s%n", i / (double) bins.length,
                    replicate((int) (bins[i] / maxFreq * maxWidth), "*"));
        System.out.println();
    }

    public static void main(String[] a) {
        Locale.setDefault(Locale.US);
        for (int p = 1; p < 7; p++) {
            double[] n = range(0, (int) pow(10, p))
                    .mapToDouble(i -> Math.random()).toArray();

            System.out.println((int)pow(10, p) + " numbers:");
            double[] res = meanStdDev(n);
            System.out.printf(" Mean: %8.6f, SD: %8.6f%n", res[0], res[1]);
            showHistogram01(n);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def sd1(numbers):
    if numbers:
        mean = sum(numbers) / len(numbers)
        sd = (sum((n - mean)**2 for n in numbers) / len(numbers))**0.5
        return sd, mean
    else:
        return 0, 0

def sd2(numbers):
    if numbers:
        sx = sxx = n = 0
        for x in numbers:
            sx += x
            sxx += x*x
            n += 1
        sd = (n * sxx - sx*sx)**0.5 / n
        return sd, sx / n
    else:
        return 0, 0

def histogram(numbers):
    h = [0] * 10
    maxwidth = 50 # characters
    for n in numbers:
        h[int(n*10)] += 1
    mx = max(h)
    print()
    for n, i in enumerate(h):
        print('%3.1f: %s' % (n / 10, '+' * int(i / mx * maxwidth)))
    print()

if __name__ == '__main__':
    import random
    for i in range(1, 6):
        n = [random.random() for j in range(10**i)]
        print("\n##\n## %i numbers\n##" % 10**i)
        print('  Naive  method: sd: %8.6f, mean: %8.6f' % sd1(n))
        print('  Second method: sd: %8.6f, mean: %8.6f' % sd2(n))
        histogram(n)

```

