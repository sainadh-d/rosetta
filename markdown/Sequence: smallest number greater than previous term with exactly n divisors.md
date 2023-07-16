# Sequence: smallest number greater than previous term with exactly n divisors

## Task Link
[Rosetta Code - Sequence: smallest number greater than previous term with exactly n divisors](https://rosettacode.org/wiki/Sequence:_smallest_number_greater_than_previous_term_with_exactly_n_divisors)

## Java Code
### java_code_1.txt
```java
public class AntiPrimesPlus {

    static int count_divisors(int n) {
        int count = 0;
        for (int i = 1; i * i <= n; ++i) {
            if (n % i == 0) {
                if (i == n / i)
                    count++;
                else
                    count += 2;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        final int max = 15;
        System.out.printf("The first %d terms of the sequence are:\n", max);
        for (int i = 1, next = 1; next <= max; ++i) {
            if (next == count_divisors(i)) {           
                System.out.printf("%d ", i);
                next++;
            }
        }
        System.out.println();
    }
}

```

## Python Code
### python_code_1.txt
```python
def divisors(n):
    divs = [1]
    for ii in range(2, int(n ** 0.5) + 3):
        if n % ii == 0:
            divs.append(ii)
            divs.append(int(n / ii))
    divs.append(n)
    return list(set(divs))


def sequence(max_n=None):
    previous = 0
    n = 0
    while True:
        n += 1
        ii = previous
        if max_n is not None:
            if n > max_n:
                break
        while True:
            ii += 1
            if len(divisors(ii)) == n:
                yield ii
                previous = ii
                break


if __name__ == '__main__':
    for item in sequence(15):
        print(item)

```

### python_code_2.txt
```python
1
2
4
6
16
18
64
66
100
112
1024
1035
4096
4288
4624

```

