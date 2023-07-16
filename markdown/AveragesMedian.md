# Averages/Median

## Task Link
[Rosetta Code - Averages/Median](https://rosettacode.org/wiki/Averages/Median)

## Java Code
### java_code_1.txt
```java
double median(List<Double> values) {
    /* copy, as to prevent modifying 'values' */
    List<Double> list = new ArrayList<>(values);
    Collections.sort(list);
    /* 'mid' will be truncated */
    int mid = list.size() / 2;
    return switch (list.size() % 2) {
        case 0 -> {
            double valueA = list.get(mid);
            double valueB = list.get(mid + 1);
            yield (valueA + valueB) / 2;
        }
        case 1 -> list.get(mid);
        default -> 0;
    };
}

```

### java_code_2.txt
```java
public static double median2(List<Double> list) {
    PriorityQueue<Double> pq = new PriorityQueue<Double>(list);
    int n = list.size();
    for (int i = 0; i < (n - 1) / 2; i++)
        pq.poll(); // discard first half
    if (n % 2 != 0) // odd length
        return pq.poll();
    else
        return (pq.poll() + pq.poll()) / 2.0;
}

```

## Python Code
### python_code_1.txt
```python
def median(aray):
    srtd = sorted(aray)
    alen = len(srtd)
    return 0.5*( srtd[(alen-1)//2] + srtd[alen//2])

a = (4.1, 5.6, 7.2, 1.7, 9.3, 4.4, 3.2)
print a, median(a)
a = (4.1, 7.2, 1.7, 9.3, 4.4, 3.2)
print a, median(a)

```

